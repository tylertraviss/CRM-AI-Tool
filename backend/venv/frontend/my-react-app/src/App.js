import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        // Fetch data from Flask backend
        fetch('/api/message')
            .then(response => response.json())
            .then(data => setMessage(data.message))
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div className="App">
            <h1>Hello from React!</h1>
            <p>Message from Flask: {message}</p>
        </div>
    );
}

export default App;
