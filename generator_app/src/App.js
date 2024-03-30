import './App.css';
// import AdsenseComponent from './AdSenseComponent';
        

function App() {
  return (
  <div className="App">
      <iframe
      allowfullscreen
      id="myiframe"
      src="https://itinerary-generator-hg7qp7yihprqdbjzvylk5u.streamlit.app/?embed=true&?embed_options=light_theme"
      // height="800"
      // width="1000"
      style={{border: "none" }}
      title="Itinerary Generator">
      </iframe>
  </div>
  );
}

export default App;
