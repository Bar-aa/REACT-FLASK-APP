import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [apiData, setApiData] = useState(null);

  useEffect(() => {
    fetch('/api/page1')
      .then(response => response.json())
      .then(data => setApiData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Edit <code>src/App.js</code> and save to reload.</p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        {apiData && (
          <div>
            <h2>Data from API:</h2>
            <p>{apiData.message}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
