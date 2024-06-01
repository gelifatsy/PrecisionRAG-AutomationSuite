// import logo from './logo.svg';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Navbar from './components/Navbar'; // Import the Navbar component
import Promptly from './components/promptly';

const App = () => {
  return (
    <Router>
      <Navbar /> {/* Render Navbar outside of Routes */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/promptly" element={<Promptly />} />

      </Routes>
    </Router>
  );
};

export default App;
