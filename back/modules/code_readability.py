import os

class Pylama:
    def act(class_id, assign_id, file_path):
        mypy = 20
        pylint = 20
        eradicate = 20
        radon = 20
        pycodestyle = 20
        os.system("pylama " + file_path + " > save.txt")
        #file 자리에 해당 파이썬 코드의 파일이름 입력
        f = open('./save.txt', mode = 'r', encoding='utf-8')
        f1 = open('./mypy.txt', mode = 'w')
        f2 = open('./pylint.txt', mode = 'w')
        f3 = open('./eradicate.txt', mode = 'w')
        f4 = open('./radon.txt', mode = 'w')
        f5 = open('./pycodestyle.txt', mode = 'w')

        lines= f.readlines()
        for line in lines:
            to_write = ""
            word_list = line.split()
            if(word_list[-1] == "[mypy]"):
                mypy -= 1
                for i in word_list[2:-1]:
                    to_write += (i + " ")
                to_write += "\n"
                f1.write(to_write)
            elif(word_list[-1] == "[pylint]"):
                pylint -= 1
                for i in word_list[2:-1]:
                    to_write += (i + " ")
                to_write += "\n"
                f2.write(to_write)
            elif(word_list[-1] == "[eradicate]"):
                eradicate -= 1
                for i in word_list[2:-1]:
                    to_write += (i + " ")
                to_write += "\n"
                f3.write(to_write)
            elif(word_list[-1] == "[radon]"):
                radon -= 1
                for i in word_list[2:-1]:
                    to_write += (i + " ")
                to_write += "\n"
                f4.write(to_write)
            elif(word_list[-1] == "[pycodestyle]"):
                pycodestyle -= 1
                for i in word_list[2:-1]:
                    to_write += (i + " ")
                to_write += "\n"
                f5.write(to_write)

        if(mypy < 0):
            mypy = 0
        if(pylint < 0):
            pylint = 0
        if(eradicate < 0):
            eradicate = 0
        if(radon < 0):
            radon = 0
        if(pycodestyle < 0):
            pycodestyle = 0

        f.close()
        os.remove("save.txt")
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        f1 = open('./mypy.txt', mode = 'r')
        f2 = open('./pylint.txt', mode = 'r')
        f3 = open('./eradicate.txt', mode = 'r')
        f4 = open('./radon.txt', mode = 'r')
        f5 = open('./pycodestyle.txt', mode = 'r')
        data1 = f1.read()
        data2 = f2.read()
        data3 = f3.read()
        data4 = f4.read()
        data5 = f5.read()
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        os.remove("mypy.txt")
        os.remove("pylint.txt")
        os.remove("eradicate.txt")
        os.remove("radon.txt")
        os.remove("pycodestyle.txt")
        '''
        return "mypy: {0}, pylint: {1}, eradicate: {2}, radon: {3}, pycodestyle: {4}".format(self.mypy, self.pylint, self.eradicate, self.radon, self.pycodestyle)
        '''
        total_score = mypy + pylint + eradicate + radon + pycodestyle
        return mypy, pylint, eradicate, radon, pycodestyle, data1, data2, data3, data4, data5
                
