// InputComponent.js

import React, { useState } from 'react';


const InputComponent = ({ inputText, setInputText, handleSubmit }) => {

    const [outputType, setoutputType] = useState('');
    
    
    const handleInputChange = (event) => {
      setInputText(event.target.value);
    };
  
    const handleOutputChange = (event) => {
      setoutputType(event.target.value);
    };
  
   

  return (
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
      <div className="ui blue button" onClick={handleSubmit}>
        Enter
      </div>
    </div>
  );
};

export default InputComponent;
