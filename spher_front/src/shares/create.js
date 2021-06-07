import React, { useRef } from 'react'
import { apiShareCreate } from './lookup'


export function ShareCreate(props) {
    const textAreaRef = useRef()
    const {didShare} = props
    const handleBackendUpdate=(response,status) =>{
      if (status === 201){
        didShare(response)
      }else{
        console.log(response)
        alert("An error occured please try again")
      }  
    } 
    
    const handleSubmit=(event)=>{
      event.preventDefault()
      const newVal =textAreaRef.current.value
      apiShareCreate(newVal,handleBackendUpdate)
      textAreaRef.current.value = ' '
    }
  
  
    return <div className={props.className}>
        <form onSubmit={handleSubmit}>
          <textarea ref={textAreaRef} required={true} className='form-control' name='share'>
          </textarea>
          <button type='submit' className='btn btn-primary my-3'>Share</button>
        </form>
    </div>
  }
  