import React, { useState } from 'react';

const ControlBlanket = () => {
const [command, setCommand] = useState('');

const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('/api/control_blanket', {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ command }),
    });

    if (response.ok) {
alert('Blanket control command sent');
    } else {
alert('Failed to send command');
    }
};

return (
    <div className="row justify-content-center">
    <div className="col-md-6">
        <h2>Control Blanket</h2>
        <form onSubmit={handleSubmit}>
        <div className="form-group">
            <label htmlFor="command">Command</label>
            <input
            type="text"
            className="form-control"
            id="command"
            name="command"
            value={command}
            onChange={(e) => setCommand(e.target.value)}
            required
            />
        </div>
        <button type="submit" className="btn btn-primary">Send Command</button>
        </form>
    </div>
    </div>
);
};

export default ControlBlanket;
