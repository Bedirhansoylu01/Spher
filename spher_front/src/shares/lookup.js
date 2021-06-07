import {backendLookup} from '../lookup'


export function apiShareCreate(newShare,callback){
    backendLookup('POST','/share',callback,{content:newShare})
  }
  


export function apiShareList(username,callback) {
    let endpoint = '/share_ls'
    if(username){
      endpoint= `/share_ls?username=${username}`
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
  
