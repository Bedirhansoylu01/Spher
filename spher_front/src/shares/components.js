import React, { useState, useEffect,useRef } from 'react'
import { loadShare } from '../lookup'
import '../App.css';


export function ShareComponents(props) {

  const textAreaRef = useRef()
  const [newShares, setNewShare] = useState([])

  const handleSubmit = (event) => {
    // Change this to a server side call
    event.preventDefault()
    const newVal = textAreaRef.current.value
    let tmpNewShare = [...newShares]
    tmpNewShare.unshift({
      user: "test",
      content: newVal,
      likes: 0,
      id: 101
    })
    setNewShare(tmpNewShare)
    textAreaRef.current.value = ''
  }

  return <div className={props.className}>
    <div className='col-12 mb-3'>
      <form onSubmit={handleSubmit}>

        <textarea ref={textAreaRef} required={true} className='form-control' name='share'>
        </textarea>

        <button type='submit' className='btn btn-primary my-3'>Share</button>
      </form>
    </div>
    <ShareList newShares={newShares} />
  </div>
}

function ShareList(props) {

  const [sharesInit, setSharesInit] = useState([])
  const [shares, setShares] = useState([])

  useEffect(() => {
    const final = [...props.newShares].concat(sharesInit)
    if (final.length !== shares.length) { // consistent loop  can`t sees likes
      setShares(final)
    }
  }, [props.newShares, shares, sharesInit])



  useEffect(() => {
    const myCallback = (response, status) => {
      if (status === 200) {
        setSharesInit(response)
      } else {
        alert('There was an error')
      }
    }
    loadShare(myCallback)
  }, [sharesInit])//if second argument is sharesInit consistent loop begin 


  return shares.map((item, index) => {
    return <Share share={item} className='my-5 py-5 border bg-white text-dark' key={`${index}`} />
  }

  )
}





function ActionBtn(props) {

  const { share, action } = props
  const [likes, setLikes] = useState(share.likes ? share.likes : 0)
  const [userLike, setUserLike] = useState(share.UserLike ? share.UserLike : false)
  const className = props.className ? props.className : 'btn btn-primary btn-sm'

  const handleClick = (event) => {
    event.preventDefault()
    if (action.type === 'like') {
      if (userLike === true) {
        setLikes(likes - 1)
        setUserLike(false)
      } else {
        setLikes(share.likes + 1)
        setUserLike(true)
      }
    }
  }
  const actionDisplay = action.display ? action.display : 'Action'
  const display = action.type === 'like' ? `${likes} ${action.display}` : actionDisplay
  return <button className={className} onClick={handleClick}>{display}</button>

}


function Share(props) {

  const { share } = props
  const className = props.className ? props.className : 'col-10 mx-auto col-md-6'

  return <div className={className}>
    <p>{share.user}-{share.content}</p>
    <ActionBtn share={share} action={{ type: 'like', display: "Like" }} />
    <ActionBtn share={share} action={{ type: 'unlike', display: "Unlike" }} />
    <ActionBtn share={share} action={{ type: 'recommit', display: "Recommit" }} />

  </div>

}





