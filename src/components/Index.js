import React from 'react';
import { Link } from 'react-router-dom';

const Index = () => {
    return (
        <div className="jumbotron">
            <h1 className="display-4">Welcome to CalmDownSpike!</h1>
            <p className="lead">An innovative interactive dog blanket designed to offer comfort and alleviate anxiety in dogs.</p>
            <hr className="my-4" />
            <p>Sign up today to customize your dog's calming experience.</p>
            <Link className="btn btn-primary btn-lg" to="/register" role="button">Get Started</Link>
        </div>
        );
    };
    export default Index;
