import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import Description from './components/Description';
import Download from './components/Download';
import Footer from './Footer';

function App() {
  return (
    <div className="App">
        <Header></Header>
        <Description></Description>
        <Download></Download>
        <Footer></Footer>
    </div>
  );
}

export default App;
