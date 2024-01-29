// App.js
import React, { useState, useEffect } from 'react';
import Dashboard from './Dashboard';
import Customers from './Customers';
import Sales from './Sales';
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

  // Render different pages based on the selected option
  const renderPage = () => {
    switch (userInfo.selectedOption) {
      case 'Dashboard':
        return <Dashboard />;
      case 'Customers':
        return <Customers />;
      case 'Sales':
        return <Sales />;
      default:
        return null;
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="top-bar">
          <div className="Dashboard" onClick={() => handleOptionChange('Dashboard')}>Dashboard</div>
          <div className="Customers" onClick={() => handleOptionChange('Customers')}>Customers</div>
          <div className="Sales" onClick={() => handleOptionChange('Sales')}>Sales</div>
        </div>
{/*         <h1>Welcome back, {userInfo.name}!</h1>
        <p>This is a simple landing page with options.</p> 
        <p>Selected Option: {userInfo.selectedOption}</p> */}
        {/* Render the selected page */}
        {renderPage()}
      </header>
    </div>
  );
}

export default App;
