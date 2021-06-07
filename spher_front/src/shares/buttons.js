import React from 'react'
import { apiShareAction } from './lookup'


export function ActionBtn(props) {

    const { share, action, didPerformAction } = props
    const likes = share.likes ? share.likes : 0
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    const actionDisplay = action.display ? action.display : 'Action'
    const display = action.type === 'like' ? `${likes} ${action.display}` : actionDisplay
  
  
    const handleActionBackendEvent = (response, status) => {
      console.log(response, status)
      if ((status === 200 || status === 201) && didPerformAction) {
        didPerformAction(response, status)
      }
    }
  
    const handleClick = (event) => {
      event.preventDefault()
      apiShareAction(share.id, action.type, handleActionBackendEvent)
    }
  
    return <button className={className} onClick={handleClick}>{display}</button>
}