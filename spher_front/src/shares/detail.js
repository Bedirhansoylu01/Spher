import React, { useState } from 'react'
import {ActionBtn} from './buttons'




function ParentShare(props) {
    const { share } = props
    return share.parent ? <div className='row'>
      <div className='col-11 mx-auto p-3 border rounded'>
        <p className={'mb-0 text-muted small'}>Main</p>
        <Share hideActions className={''} share={share.parent} /></div></div> : null
  }
  
  
  
  
  export function Share(props) {
  
    const { share,didRecommit,hideActions } = props
    const [actionShare, setActionShare] = useState(share ? share : null)
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    
    const path = window.location.pathname
    const match= path.match(/(?<share_id>\d+)/)
    const urlShareId = match ? match.groups.share_id : -1    
    const isDetail = `${share.id}` === `${urlShareId}`
    const handleLink=(event)=>{
      event.preventDefault()
      window.location.href=`/${share.id}`
    }

  
    const handlePerfomAction = (newActionShare, status) => {
      if (status === 200) {
        setActionShare(newActionShare)
      } else if (status === 201) {
        if (didRecommit){
          didRecommit(newActionShare)
        }
      }
    }
  
  
  
    return <div className={className}>
      <div>
        <p><strong>{share.user}</strong><br></br>{share.content}</p>
        <ParentShare share={share} />
      </div>
      <div className='btn btn-group'>
      {(actionShare&& hideActions !== true ) && <React.Fragment>
        <ActionBtn share={actionShare} didPerformAction={handlePerfomAction} action={{ type: 'like', display: "Like" }} />
        <ActionBtn share={actionShare} didPerformAction={handlePerfomAction} action={{ type: 'unlike', display: "Unlike" }} />
        <ActionBtn share={actionShare} didPerformAction={handlePerfomAction} action={{ type: 'recommit', display: "Recommit" }} />
      </React.Fragment>}

        { isDetail=== true ? null : <button className='btn btn-outline-primary btn-sm' onClick={handleLink}>View</button>}  
      </div>
    </div>
  }