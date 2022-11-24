import React, {useRef} from "react";
import CodeEdit from "./CodeEdit";
import Problem from "./Problem"
import Result from "./Result"
import styled from 'styled-components';
import axios from 'axios'
import Home from "./icon/House.png"
const pro1 = "두 수를 입력받아 더한 결과를 나타내십시오."
const pro2 = "입력받는 값은 정수로 처리해야 합니다."
const testcase1 ={
  'input': '1 3',
  'output': '4'
}
const testcase2 ={
  'input': '4 4',
  'output': '8'
}
export default class App extends React.Component {
  
  state  = {
    submit: 0,
    case_correct:{
                  "테스트케이스-1":"통과",
                  "테스트케이스-2":"통과",
                  "히든 테스트케이스-3":"실패",
                  "히든 테스트케이스-4":"실패",
                  "히든 테스트케이스-5":"통과",
                  },
    efficency:{
                  "Line Of Codes": 60,
                  "Resevation Words": 100,
                  "Data Flow Compliexity": 80,
                  "control Flow Complexity": 30
    },
    readability: {
                  "mypy": 20,
                  "pylint": 90,
                  "eradicate" : 85,
                  "radon": 70,
                  "pycodestyle": 15
    },
    code_result:" "
  }
  api = async (data)=>{
    await axios.post(
      "http://127.0.0.1:8000/code_efficiency/",
      {code: data}
    )
    .then(response=>
        console.log(response)
      )
    /*
    .then(response=>
        this.setState(current=>({
          code_result:JSON.parse(response['data'])['result']
        }))
    )
    */
  }
  setCodeResult = (code)=>{
        console.log(code)
        this.setState(current=>({
          code_result:code}))
  }
  setSubmit = (tf)=>{
        this.setState(current=>({
          submit:tf}))

  }

  
  render(){
      return(
        <div
          style={{
            height:"1000px",
            width:"1200px",
            backgroundColor:"#D5D4D6",
          }}
        >
          <div
            style={{
              position:"relative",
              height:"5%",
              widht:"100%",
              backgroundColor:"#2E4E3F"
            }}
          >
            <img
              style={{
                position:"relative",
                left:"1%",
                height:"70%",
                width:"3%",
                top:"15%"

              }}
              src = {Home}
            >
            </img>
            <span
              style={{
                position:"relative",
                color:"white",
                fontSize:"25px",
                fontWeight:"bolder",
                top:"4%",
                width:"10%",
                left:"4%"
              }}
            >강의 1</span>
            <div
              style={{
                position:"relative",
                borderRadius:"10px",
                backgroundColor:"white",
                top:"-60%",
                left:"35%",
                height:"60%",
                width:"30%",
                textAlign:"center",
                fontWeight:"bolder",
                fontSize:"120%",
              }}
            >
                week 1 정수 덧셈 구현
            </div>
          </div>
          <div
            style={{
              height:"94.5%",
              width:"29.5%",
              
              float:"left"
            }}>
              <Problem data1 = {pro1} 
                  data2 = {pro2}
                  testcase1 = {testcase1}
                  testcase2 = {testcase2}
              />
          </div>

          <div
            style={{
              height:"94.5%",
              width:"70.1%",
              
              float:"left"
            }}>
              <CodeEdit api = {this.api} submit = {this.setSubmit} setCodeResult = {this.setCodeResult}/>
          </div>
          {
            /*
          <div
            style={{
              height:"80%",
              width:"40%",
              borderColor:"black",
              borderStyle:"solid",
              borderWidth:"1px",
              float:"left"
            }}>
              <Result result = {this.state}/>
          </div>
            */
          }
        </div>
      )
    }
}