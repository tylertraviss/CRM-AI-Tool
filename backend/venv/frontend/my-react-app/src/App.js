import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
    const [name, setName] = useState(''); // State to store the name
    const [selectedOption, setSelectedOption] = useState(''); // State for selected option

    useEffect(() => {
        // Fetch user information from Flask when the component mounts
        fetch('/api/userinfo')
            .then(response => response.json())
            .then(data => setName(data.name))
            .catch(error => console.error('Error:', error));
    }, []);

    const handleOptionChange = (option) => {
        // Handle option changes
        setSelectedOption(option);
    };

    return (
        <div className="App">
            <header className="App-header">
                <div className="top-bar">
                    <div className="option" onClick={() => handleOptionChange('option1')}>Dashboard</div>
                    <div className="option" onClick={() => handleOptionChange('option2')}>Customers</div>
                    <div className="option" onClick={() => handleOptionChange('option3')}>Sales</div>
                </div>
                <h1>Welcome back, {name}!</h1>
                <p>This is a simple landing page with options.</p>
                <p>Selected Option: {selectedOption}</p>
            </header>
        </div>
    );
}

export default App;
