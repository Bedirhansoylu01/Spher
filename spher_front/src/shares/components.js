import React, { useEffect,useState } from 'react'
import {apiShareDetail} from './lookup'
import { Share } from './detail'
import {ShareList} from './list'
import {ShareCreate} from './create'
import '../App.css';



export function ShareComponents(props) {


  const [newShares, setNewShares] = useState([])
  const validUser = props.validUser === 'true' ? true : false 
  const handleNewShare = (newShare) => {
    let tmpNewShares = [...newShares]
    tmpNewShares.unshift(newShare)
    setNewShares(tmpNewShares)
  }


  return <div className={props.className}>
    {validUser === true && <ShareCreate didShare={handleNewShare} className='col-12 mb-3'/>} 
    <ShareList {...props} newShares={newShares} />
  </div>
}


export function ShareDetailComponent(props){
  const {shareId} = props
  const [didLookup,setDidLookup] = useState(false)
  const [share,setShare]=useState(null)


  const handleBackendLookup=(response,status)=>{
    if(status === 200){
      setShare(response)
    }else{
      alert('There was an error finding your Commit.')
    }
  }
  
  useEffect(()=>{
    if(didLookup===false){   
      apiShareDetail(shareId,handleBackendLookup)
      setDidLookup(true)
    
    }
  },[shareId,didLookup,setDidLookup])


  return share === null ? null : <Share share={share} className={props.className}/>
}