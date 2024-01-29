import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
    const [userInfo, setUserInfo] = useState({
        name: '',
        selectedOption: '',
        companyName: ''
    });

    useEffect(() => {
        // Fetch user information from Flask when the component mounts
        fetch('http://localhost:5000/api/userinfo')
            .then(response => response.json())
            .then(data => {
                setUserInfo(data);
            })
            .catch(error => console.error('Error:', error));
    }, []);

    const handleOptionChange = (option) => {
        // Handle option changes
        setUserInfo(prevInfo => ({ ...prevInfo, selectedOption: option }));
    };

    return (
        <div className="App">
            <header className="App-header">
                <div className="top-bar">
                    <div className="Dashboard" onClick={() => handleOptionChange('Dashboard')}>Dashboard</div>
                    <div className="Customers" onClick={() => handleOptionChange('Customers')}>Customers</div>
                    <div className="Sales" onClick={() => handleOptionChange('Sales')}>Sales</div>
                </div>
                <h1>Welcome back, {userInfo.name}!</h1>
                <p>This is a simple landing page with options.</p>
                <p>Selected Option: {userInfo.selectedOption}</p>
                <p>Company Name: {userInfo.companyName}</p>
            </header>
        </div>
    );
}

export default App;
