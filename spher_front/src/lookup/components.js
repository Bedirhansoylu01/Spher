

export function loadShare(callback) {
    const xhr = new XMLHttpRequest();
    xhr.responseType = "json";
    const url_ls = "http://127.0.0.1:8000/api/share_ls"
    xhr.open("GET", url_ls);
  
    xhr.onload = function () {
      callback(xhr.response, xhr.status)
    };
    xhr.onerror = function (ms) {
      console.log(ms);
      callback({ "message": "The request was an error" }, 400);
    }
    xhr.send();
  }
