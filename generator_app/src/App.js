import './App.css';
import AdsenseComponent from './AdSenseComponent';
        

function App() {
  return (
  <div className="App">
    <div className="left-component">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6270659904604748"
     crossorigin="anonymous">
     </script>
     {/* <!-- left component --> */}
     <ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-6270659904604748"
     data-ad-slot="4698668960"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
     <script>
     (adsbygoogle = window.adsbygoogle || []).push({});</script>
    </div>
    <div className="iFrame">
    <iframe
      allowfullscreen
      id="myiframe"
      src="https://itinerary-generator-hg7qp7yihprqdbjzvylk5u.streamlit.app/?embed=true&?embed_options=light_theme"
      height="800"
      width="1000"
      style={{border: "none" }}
      title="Itinerary Generator"></iframe>
    </div>
  </div>
  );
}

export default App;
