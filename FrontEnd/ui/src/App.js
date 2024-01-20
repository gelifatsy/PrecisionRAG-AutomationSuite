import React, { useState } from 'react';
import 'semantic-ui-css/semantic.min.css';

const App = () => {

  const [inputText, setInputText] = useState('');
  const [outputType, setOutputType] = useState('');
  const [result, setResult] = useState('');

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleOutputChange = (e) => {
    setOutputType(e.target.value);
  };

 

  const handleSubmit = async () => {
    // Send both inputText and outputType to the backend
    const response = await fetch("http://localhost:8000/process_input", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        input_text: inputText,
        output_type: outputType,
      }),
    });

    const data = await response.json();
    console.log('Response from backend:', data);

    // Process the data from the backend
    console.log('Data from backend:', data);
    setResult(data.input_text);
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
      <div className="ui action input">
        <input
          type="text"
          placeholder="Enter Input"
          value={inputText}
          onChange={handleInputChange}
        />
        <select
          className="ui selection dropdown"
          style={{ width: '200px' }}
          value={outputType}
          onChange={handleOutputChange}
        >
          <option value="" disabled selected hidden>
            Expected Output...
          </option>
          <option value="text">Text</option>
          <option value="code">Code</option>
          <option value="sql">SQL</option>
        </select>
        <div className="ui blue button" onClick={() => {  handleSubmit(); }}>
          Enter
        </div>
      </div>
      <br />
      <div className="ui form">
        <div className="field">
          <label style={{ color: 'white', textAlign: 'center', width: '100%' }}>Prompt Generated</label>
          <textarea cols="50" rows="8" value={result} readOnly></textarea>
        </div>
      </div>
    </div>
  );
};

export default App;
