import './App.css';

function App() {
  return (
    <div className="App">
      <iframe
      allowfullscreen
      id="myiframe"
      src="https://itinerary-generator-hg7qp7yihprqdbjzvylk5u.streamlit.app/?embed=true&?embed_options=light_theme"
      height="800"
      width="1000"
      style={{border: "none" }}
      title="Itinerary Generator"></iframe>
      <script>
        var iframe = document.getElementById("myiframe");
        iframe.width = iframe.contentWindow.document.body.scrollWidth;
        iframe.height = iframe.contentWindow.document.body.scrollHeight;
      </script>
    </div>
  );
}

export default App;
