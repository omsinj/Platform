// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';
import logo from './logo.svg'; // Check if logo.svg exists in the correct path
import Home from './components/Home'; // Verify the path to Home component
import Games from './components/Games'; // Verify the path to Games component
import Resources from './components/Resources'; // Verify the path to Resources component

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/games" component={Games} />
          <Route path="/resources" component={Resources} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
