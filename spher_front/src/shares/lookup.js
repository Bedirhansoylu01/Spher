import {backendLookup} from '../lookup'


export function apiShareCreate(newShare,callback){
    backendLookup('POST','/share',callback,{content:newShare})
  }

  

export function apiShareFeed(callback,nextUrl) {
  let endpoint = '/feed'  
  if(nextUrl !== null && nextUrl !== undefined){
    endpoint = nextUrl.replace("http://localhost:8000/api","")
  }
  backendLookup('GET',endpoint, callback)
}



export function apiShareList(username,callback,nextUrl) {
    let endpoint = '/share_ls'
    if(username){
      endpoint= `/share_ls?username=${username}`
    }
    if(nextUrl !== null && nextUrl !== undefined){
      endpoint = nextUrl.replace("http://localhost:8000/api","")
    }
    backendLookup('GET',endpoint, callback)
  }


  export function apiShareDetail(shareId,callback) {
    backendLookup('GET',`/share/${shareId}`, callback)
  }


  
export function apiShareAction(shareId,action,callback) {
  const data = {id:shareId,action:action}
  backendLookup('POST','/share/action',callback,data)
  }
  
