import './App.css';
import {useMediaQuery} from '@react-hook/media-query'

function App() {
  const isMobile = useMediaQuery({ query: '(max-width: 1440px)' }, {noSsr: true});
  const className = isMobile ? "mobile-class" : "desktop-class";
  return (
      <iframe
      allowfullscreen
      className= {className}
      src="https://itinerary-generator-hg7qp7yihprqdbjzvylk5u.streamlit.app/?embed=true&?embed_options=light_theme"
      // height="800"
      // width="1000"
      // style={{border: "none" }}
      title="Itinerary Generator"
      disabled = {this.state.submitting}>
      </iframe>
  );
}

export default App;
