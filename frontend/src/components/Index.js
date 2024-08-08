import React from 'react';
import { Link } from 'react-router-dom';

const Index = () => {
    const backgroundImageStyle = {
        backgroundImage: "url('/logo.png')",
        backgroundSize: 'tile',
        backgroundPosition: 'center',
        height: '100vh',
        width: '100%',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        flexDirection: 'column',
        color: 'white',
        textShadow: '1px 1px 2px black'
    };

    return (
        <div style={backgroundImageStyle}>
            <div className="jumbotron" style={{background: 'rgba(0, 0, 0, 0.5)', padding: '20px', borderRadius: '10px'}}>
                <h1 className="display-4">Welcome to CalmDownSpike!</h1>
                <p className="lead">An innovative interactive dog blanket designed to offer comfort and alleviate anxiety in dogs.</p>
                <hr className="my-4" />
                <p>Sign up today to customize your dog's calming experience.</p>
                <Link className="btn btn-primary btn-lg" to="/register" role="button">Get Started</Link>
            </div>
        </div>
    );
};

export default Index;
