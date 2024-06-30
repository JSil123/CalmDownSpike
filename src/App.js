import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import BaseLayout from './components/BaseLayout';
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import Register from './components/Register';
import Index from './components/Index';

const App = () => (
<Router>
    <BaseLayout>
    <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/" element={<Index />} exact />
    </Routes>
    </BaseLayout>
</Router>
);

export default App;
