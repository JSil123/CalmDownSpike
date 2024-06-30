// frontend/src/services/deviceService.js

export async function fetchDevices() {
    const response = await fetch('/api/v1/devices');
    if (!response.ok) {
        throw new Error('Failed to fetch devices');
    }
    return await response.json();
}
