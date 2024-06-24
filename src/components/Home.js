// src/components/Home.js
import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => (
    <div className="container">
        <h1>Welcome to the Trivia Platform</h1>
        <div className="menu">
            <Link to="/games" className="btn">Games</Link>
            <Link to="/resources" className="btn">Resources</Link>
        </div>
    </div>
);

export default Home;
