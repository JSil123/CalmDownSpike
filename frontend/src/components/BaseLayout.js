// src/components/BaseLayout.js
import React from 'react';
import { Link } from 'react-router-dom';
import 'C:/CalmDownSpike/frontend/src/App';

const BaseLayout = ({ children }) => {
    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <a className="navbar-brand" href="/">CalmDownSpike</a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ml-auto">
                <li className="nav-item">
                    <Link className="nav-link" to="/login">Login</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/register">Register</Link>
                </li>
            </ul>
        </div>
    </nav>
    <div className="container">
        {children}
    </div>
    </div>
    );
};

export default BaseLayout;
