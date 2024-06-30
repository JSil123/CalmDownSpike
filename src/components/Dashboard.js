import React, { useEffect, useState } from 'react';

const Dashboard = () => {
const [devices, setDevices] = useState([]);

useEffect(() => {
    // Fetch data with the native fetch API
    const fetchData = async () => {
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
    };

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

export default Dashboard;
