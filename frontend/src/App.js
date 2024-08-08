import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Index from './components/Index';
import Navbar from './components/Navbar';
import Register from './components/Register';
import ControlBlanket from './components/ControlBlanket';

function App() {
    useEffect(() => {
        console.log('App component mounted');
    }, []);

    return (
        <Router>
            <div>
                <Navbar />
                <Routes>
                    <Route path="/" element={<Index />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/control-blanket" element={<ControlBlanket />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;