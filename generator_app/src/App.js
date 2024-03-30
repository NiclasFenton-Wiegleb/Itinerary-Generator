import './App.css';
import {
  BrowserRouter,
  Route,
  Routes,
 } from "react-router-dom";

 import React, { useEffect } from 'react';

// const AdsenseComponent = ({ adClient, adSlot, adFormat }) => {
//   useEffect(() => {
//     (window.adsbygoogle = window.adsbygoogle || []).push({});
//   }, []);

//   return (
//     <ins className="adsbygoogle"
//          style={{ display: 'block' }}
//          data-ad-client={adClient}
//          data-ad-slot={adSlot}
//          data-ad-format={adFormat}></ins>
//   );
// };

// export default AdsenseComponent;

function NotFoundPage() {
  return (
    <div>
      Page not found
    </div>
  );
 }
 
        

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <body>
      </body>
      <iframe
      allowfullscreen
      id="myiframe"
      src="https://itinerary-generator-hg7qp7yihprqdbjzvylk5u.streamlit.app/?embed=true&?embed_options=light_theme"
      height="800"
      width="1000"
      style={{border: "none" }}
      title="Itinerary Generator"></iframe>
      <Routes><Route path="/*" element={<NotFoundPage />}/></Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
