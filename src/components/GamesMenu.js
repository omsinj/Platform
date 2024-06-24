// src/components/GamesMenu.js
import React from 'react';
import { Link } from 'react-router-dom';

const GamesMenu = () => (
    <div className="container">
        <h2>Games Menu</h2>
        <div className="menu">
            <Link to="/games/system-generated" className="btn">System Generated</Link>
            <Link to="/games/user-generated" className="btn">User Generated</Link>
        </div>
    </div>
);

export default GamesMenu;
