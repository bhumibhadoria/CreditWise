import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import InputForm from './components/InputForm';
import ResultDisplay from './components/ResultDisplay';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<InputForm />} />
          <Route path="/result" element={<ResultDisplay />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
