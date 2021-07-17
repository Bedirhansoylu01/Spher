import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { FeedComponents,ShareComponents,ShareDetailComponent } from './shares'
import reportWebVitals from './reportWebVitals';

const appHome = document.getElementById('root')

if (appHome) {
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>, appHome
  );
}

const Sharels = document.getElementById("Home_Share")
if (Sharels) {
  ReactDOM.render(
    React.createElement(ShareComponents, Sharels.dataset),
    Sharels)
}


const spherFeedEl = document.getElementById("spher-feed")
if (spherFeedEl) {
  ReactDOM.render(
    React.createElement(FeedComponents, spherFeedEl.dataset),spherFeedEl)
}





const shareDetailElements= document.querySelectorAll(".spher-detail")

shareDetailElements.forEach(container=>{
  ReactDOM.render(
    React.createElement(ShareDetailComponent, container.dataset),
    container);
})

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
