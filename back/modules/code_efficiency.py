import argparse
import json
import os
import textwrap
import multiprocessing as mp

import chardet
from pygments import lexers

from multimetric.cls.importer.filtered import FilteredImporter
from multimetric.cls.importer.pick import importer_pick
from multimetric.cls.modules import get_additional_parser_args
from multimetric.cls.modules import get_modules_calculated
from multimetric.cls.modules import get_modules_metrics
from multimetric.cls.modules import get_modules_stats

"""
API를 따로 제공해주지 않아 소스코드를 복사하여 사용
Copyright 관련해서 확인해야 함
"""


class MultiMetrics:
    def ArgParser(f):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            prog="multimetric", description='Calculate code metrics in various languages',
            epilog=textwrap.dedent("""
            Currently you could import files of the following types for --warn_* or --coverage
    
            Following information can be read
    
                <file> = full path to file
                <content> = either a string
                <severity> = optional severity
    
                Note: you could also add a single line, then <content>
                    has to be a number reflecting to total number of findings
    
            File formats
    
            csv: CSV file of following line format
                 <file>,<content>,<severity>
    
            json: JSON file
                 <file>: {
                     "content": <content>,
                     "severity": <severity>
                 }
            """))
        parser.add_argument(
            "--warn_compiler",
            default=None,
            help="File(s) holding information about compiler warnings")
        parser.add_argument(
            "--warn_duplication",
            default=None,
            help="File(s) holding information about code duplications")
        parser.add_argument(
            "--warn_functional",
            default=None,
            help="File(s) holding information about static code analysis findings")
        parser.add_argument(
            "--warn_standard",
            default=None,
            help="File(s) holding information about language standard violations")
        parser.add_argument(
            "--warn_security",
            default=None,
            help="File(s) File(s) holding information about found security issue")
        parser.add_argument(
            "--coverage",
            default=None,
            help="File(s) with compiler warningsFile(s) holding information about testing coverage")
        parser.add_argument(
            "--dump",
            default=False,
            action="store_true",
            help="Just dump the token tree")
        parser.add_argument(
            "--jobs",
            type=int,
            default=1,
            help="Run x jobs in parallel")
        get_additional_parser_args(parser)
        parser.add_argument("files", nargs='+', help="Files to parse")
        RUNARGS = parser.parse_args([f])
        # Turn all paths to abs-paths right here
        RUNARGS.files = [os.path.abspath(x) for x in RUNARGS.files]
        return RUNARGS
    
    
    def file_process(_file, _args, _importer):
        res = {}
        store = {}
        _lexer = lexers.get_lexer_for_filename(_file)
        try:
            with open(_file, "rb") as i:
                _cnt = i.read()
                _enc = chardet.detect(_cnt)
                _cnt = _cnt.decode(_enc["encoding"]).encode("utf-8")
            _localImporter = {k: FilteredImporter(
                v, _file) for k, v in _importer.items()}
            tokens = list(_lexer.get_tokens(_cnt))
            if _args.dump:
                for x in tokens:
                    print("{}: {} -> {}".format(_file, x[0], str(x[1])))
            else:
                _localMetrics = get_modules_metrics(_args, **_localImporter)
                _localCalc = get_modules_calculated(_args, **_localImporter)
                for x in _localMetrics:
                    x.parse_tokens(_lexer.name, tokens)
                    res.update(x.get_results())
                    store.update(x.get_internal_store())
                for x in _localCalc:
                    res.update(x.get_results(res))
                    store.update(x.get_internal_store())
        except Exception:
            tokens = []
        return (res, _file, _lexer.name, tokens, store)
    
    
    """
    해당 모듈을 사용하려면 py파일이 필요하므로
    입력받은 문자열을 py파일로 작성 후 작업

    결과물은 JSON 형식으로 나옴

    LOC : loc
    Control flow 복잡도: Cyclomatic_complexity

    Halstead와 Data flow 복잡도, Reservation Words는 어떤 항목을 보고 판단해야하는지 문의 필요
    """




    def CalculMetrics(code):
        f=open("test.py",'w')
        f.write(code)
        f.close()
        
        _args =  MultiMetrics.ArgParser("test.py")
        _result = {"files": {}, "overall": {}}
        
    
        # Get importer
        _importer = {}
        _importer["import_compiler"] = importer_pick(_args, _args.warn_compiler)
        _importer["import_coverage"] = importer_pick(_args, _args.coverage)
        _importer["import_duplication"] = importer_pick(
            _args, _args.warn_duplication)
        _importer["import_functional"] = importer_pick(
            _args, _args.warn_functional)
        _importer["import_security"] = importer_pick(_args, _args.warn_standard)
        _importer["import_standard"] = importer_pick(_args, _args.warn_security)
        # sanity check
        _importer = {k: v for k, v in _importer.items() if v}
    
        # instance metric modules
        _overallMetrics = get_modules_metrics(_args, **_importer)
        _overallCalc = get_modules_calculated(_args, **_importer)
    
        results = [MultiMetrics.file_process(f, _args, _importer) for f in _args.files]
        for x in results:
            _result["files"][x[1]] = x[0]
    
        for y in _overallMetrics:
            _result["overall"].update(y.get_results_global([x[4] for x in results]))
        for y in _overallCalc:
            _result["overall"].update(y.get_results(_result["overall"]))
        for m in get_modules_stats(_args, **_importer):
            _result = m.get_results(_result, "files", "overall")
  
        os.remove("test.py")
        return(_result)

    
