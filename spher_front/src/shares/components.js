import React,{useState,useEffect} from 'react'
import {loadShare} from '../lookup'
  


export function ShareList(props){

    const [commits, setCommits] = useState([])
  
    useEffect(() => {
      const myCallback = (response, status) => {
        if (status === 200) {
          setCommits(response)
        } else {
          alert('There was an error')
        }
      }
      loadShare(myCallback)
    },[])

     return commits.map((item, index) => { 
        return <Share share={item} className='my-5 py-5 border bg-white text-dark' key={`${index}`} />
    }
    
    )}
  




    function ActionBtn(props) {

        const { share, action } = props
        const className = props.className ? props.className : 'btn btn-primary btn-sm'
        let likes = share.likes
        const handleClick = (event) =>{
            event.preventDefault()
            if (action.type === 'like'){
                likes = share.likes + 1
            }    
        }
        const actionDisplay = action.display ? action.display: 'Action'
        const display = action.type === 'like'? `${likes} ${action.display }`: actionDisplay 
        return <button className={className} onClick={handleClick}>{display}</button>

    }





        function Share(props) {

    const { share } = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'

    return <div className={className}>
        <p>{share.user}-{share.content}</p>
        <ActionBtn share={share} action={{ type: 'like' ,display:"Like"}} />
        <ActionBtn share={share} action={{ type: 'unlike' ,display:"Unlike"}} />
        <ActionBtn share={share} action={{ type: 'recommit',display:"Recommit" }} />
                
    </div>

}





