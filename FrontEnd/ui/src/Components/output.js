// OutputComponent.js
import React from 'react';

const OutputComponent = ({ result }) => {
  return (
    <div className="ui form">
      <div className="field">
        <label style={{ color: 'white', textAlign: 'center', width: '100%', fontWeight: 'bold' }}>Prompt Generated</label>
        <div style={{ display: 'flex' }}>
          <div style={{ flex: 1, marginRight: '5px' }}>
            <label style={{color: 'white'}}>Prompt </label>
            <textarea style={{ width: '100%', height: '200px' }} value={result} readOnly></textarea>
          </div>
          <div style={{ flex: 1, marginLeft: '5px' }}>
            <label style={{color: 'white'}}>Prompt Score</label>
            <textarea style={{ width: '100%', height: '200px' }} value={result} readOnly></textarea>
          </div>
        </div>
      </div>
    </div>
  );
};

export default OutputComponent;




