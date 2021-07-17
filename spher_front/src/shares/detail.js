import React, { useState } from 'react'
import {ActionBtn} from './buttons'
import {UserDisplay,UserPicture} from '../profiles'


function ParentShare(props) {
    const { share } = props
    return share.parent ? <Share isRecommit recommiter={props.recommiter} hideActions className={' '} share={share.parent}/>: null
  }
  
    
  export function Share(props) {
  
    const { share,didRecommit,hideActions,isRecommit,recommiter } = props
    const [actionShare, setActionShare] = useState(props.share ? props.share : null)
    let className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    className = isRecommit === true ? `${className} py-2 border rounded`: className
    const path = window.location.pathname
    const match= path.match(/(?<share_id>\d+)/)
    const urlShareId = match ? match.groups.share_id : -1 //?share_id  
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
      {isRecommit === true &&<div className='mb-2'>
        <span className='small text-muted'>Recommit via <UserDisplay user={recommiter}/></span>
        </div>}
      <div className='d-flex'>
       <div className=''>
        <UserPicture user={share.user}/>
      </div>
      <div className='col-11'>
      <div>
        <p>
          <UserDisplay includeFullName user={share.user}/>
        </p>
        <p>{share.content}</p>
   
        <ParentShare share={share} recommiter={share.user}/>
      </div>
      <div className='btn btn-group px-0'>
      {(actionShare&& hideActions !== true ) && <React.Fragment>
        <ActionBtn share={actionShare} didPerformAction={handlePerfomAction} action={{ type: 'like', display: "Like" }} />
        <ActionBtn share={actionShare} didPerformAction={handlePerfomAction} action={{ type: 'unlike', display: "Unlike" }} />
        <ActionBtn share={actionShare} didPerformAction={handlePerfomAction} action={{ type: 'recommit', display: "Recommit" }} />
      </React.Fragment>}

        { isDetail=== true ? null : <button className='btn btn-outline-primary btn-sm' onClick={handleLink}>View</button>}  
      </div>
      </div>
    </div>
    </div>
  }
  