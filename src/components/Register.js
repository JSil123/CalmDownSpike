import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Register = () => {
const [username, setUsername] = useState('');
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
const navigate = useNavigate();

const handleSubmit = async (e) => {
    e.preventDefault();

    // Example of sending a register request
    const response = await fetch('/api/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, email, password })
    });

    if (response.ok) {
      // Redirect to dashboard or perform other actions on successful register
    navigate('/dashboard');
    } else {
      // Handle register failure
    alert('Register failed');
    }
};

return (
    <div className="row justify-content-center">
    <div className="col-md-6">
        <h2>Register</h2>
        <form onSubmit={handleSubmit}>
        <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
            type="text"
            className="form-control"
            id="username"
            name="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            />
        </div>
        <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
            type="email"
            className="form-control"
            id="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            />
        </div>
        <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
            type="password"
            className="form-control"
            id="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            />
        </div>
        <button type="submit" className="btn btn-primary">Register</button>
        </form>
    </div>
    </div>
);
};
export default Register;
