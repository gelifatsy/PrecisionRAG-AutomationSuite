import React, { useState } from 'react';
import 'semantic-ui-css/semantic.min.css';
import InputComponent from './Components/input';
import OutputComponent from './Components/output';

const App = () => {
  const [inputText, setInputText] = useState('');
  const [data, setData] = useState('');
  
  const handleSubmit = async (event) => {
    event.preventDefault();
    const requestData = { inputText: inputText };
  
    try {
      const response = await fetch('http://127.0.0.1:8000/apeg', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
      });
  
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
  
      const jsonResponse = await response.json();
      setData(jsonResponse);
    } catch (error) {
      console.error('There has been a problem with your fetch operation:', error);
    }
  };
  
  
  return (
    <div style={{
      background: 'linear-gradient(to bottom, #001f3f, #0074cc)',
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
    }}>
      <h1 style={{ color: 'white', fontFamily: 'Arial, sans-serif', marginBottom: '60px' }}>Promptly Tech</h1>
      <InputComponent
        inputText={inputText}
        setInputText={setInputText}
        handleSubmit={handleSubmit}
      />
      <br />
      <OutputComponent result={data} />
    </div>
  );
};

export default App;
