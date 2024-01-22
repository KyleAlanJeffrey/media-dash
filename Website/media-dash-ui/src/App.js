import './App.css';
import React, { useEffect, useState } from 'react';

const PORT = 8080;

function App() {
  const [data, setData] = useState({});
  useEffect(() => {
    fetch("http://localhost:" + PORT + "/currently_playing").then(response => {
      response.json().then(data => {
        console.log(data);
        setData(data);
      })
    }
    );
  
  }, []);
  return (
    <div className="App">
      <header className="App-header">
       <h1>{data}</h1>
      </header>
    </div>
  );
}

export default App;
