import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import AdSense from 'react-adsense';


const root_1 = ReactDOM.createRoot(document.getElementById('root_1'));

root_1.render(
  
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

const root_2 = ReactDOM.createRoot(document.getElementById('root_2'));
root_2.render(
  <React.StrictMode>
    <AdSense.Google
    className= "adsbygoogle"
    client="ca-pub-6270659904604748"
    slot="4526444425"
    style={{
      display: "block"
    }}
    // layout='in-article'
    format="auto"
    responsive="true"/>
  </React.StrictMode>
);

const root_3 = ReactDOM.createRoot(document.getElementById('root_3'));
root_3.render(
  <React.StrictMode>
    <AdSense.Google
    className= "adsbygoogle"
    client="ca-pub-6270659904604748"
    slot="4526444425"
    style={{
      display: "block"
    }}
    // layout='in-article'
    format="auto"
    responsive="true"/>
  </React.StrictMode>
);
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
