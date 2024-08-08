import React, { useState, useEffect } from 'react';

const Settings = () => {
const [username, setUsername] = useState('');
const [soundSetting, setSoundSetting] = useState('');
const [temperatureSetting, setTemperatureSetting] = useState(22.0);
const [ledLightSetting, setLedLightSetting] = useState('');
const [voiceActivation, setVoiceActivation] = useState(false);

    async function handleSubmit(e) {
        e.preventDefault();

        const response = await fetch('/api/update_settings', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, sound_setting: soundSetting, temperature_setting: temperatureSetting, led_light_setting: ledLightSetting, voice_activation: voiceActivation }),
        });

        if (response.ok) {
            alert('Settings updated successfully');
        } else {
            alert('Failed to update settings');
        }
    }

return (
<div className="row justify-content-center">
<div className="col-md-6">
<h2>Update Settings</h2>
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
<label htmlFor="soundSetting">Sound Setting</label>
<input
type="text"
className="form-control"
id="soundSetting"
name="soundSetting"
value={soundSetting}
onChange={(e) => setSoundSetting(e.target.value)}
required
/>
</div>
<div className="form-group">
<label htmlFor="temperatureSetting">Temperature Setting</label>
<input
type="number"
className="form-control"
id="temperatureSetting"
name="temperatureSetting"
value={temperatureSetting}
onChange={(e) => setTemperatureSetting(parseFloat(e.target.value))}
required
/>
</div>
<div className="form-group">
<label htmlFor="ledLightSetting">LED Light Setting</label>
<input
type="text"
className="form-control"
id="ledLightSetting"
name="ledLightSetting"
value={ledLightSetting}
onChange={(e) => setLedLightSetting(e.target.value)}
required
/>
</div>
<div className="form-group">
<label htmlFor="voiceActivation">Voice Activation</label>
<input
type="checkbox"
className="form-control"
id="voiceActivation"
name="voiceActivation"
checked={voiceActivation}
onChange={(e) => setVoiceActivation(e.target.checked)}
/>
</div>
<button type="submit" className="btn btn-primary">Update Settings</button>
</form>
</div>
</div>
);
};

export default Settings;export const Dashboard = () => {
    const [devices, setDevices] = useState([]);

    useEffect(() => {
        // Fetch data with the native fetch API
        async function fetchData() {
            try {
                const response = await fetch('/api/devices');
                if (response.ok) {
                    const data = await response.json();
                    setDevices(data);
                } else {
                    console.error('Error fetching devices:', response.statusText);
                }
            } catch (error) {
                console.error('Error fetching devices:', error);
            }
        }

        fetchData();
    }, []);

    return (
        <div>
            <h2>Dashboard</h2>
            <ul>
                {devices.map((device) => (
                    <li key={device.id}>{device.name} - {device.status}</li>
                ))}
            </ul>
        </div>
    );
};

