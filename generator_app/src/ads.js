import React, { useEffect } from 'react';
import './App.css';


const AdsenseComponent = ({ adClient, adSlot, adFormat }) => {
    useEffect(() => {
    (window.adsbygoogle = window.adsbygoogle || []).push({});
  }, []);

  return (
    <ins className="adsbygoogle"
    height="800"
    width="300"
    style={{border: "none" }}
    data-ad-client={adClient}
    data-ad-slot={adSlot}
    data-ad-format={adFormat}></ins>
  );
};

export default AdsenseComponent;