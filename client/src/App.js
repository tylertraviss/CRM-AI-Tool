// App.js
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState, useEffect } from 'react';
import Dashboard from './Dashboard';
import Customers from './Customers';
import Sales from './Sales';
import NavScrollExample from './NavScrollExample';
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

  function App() {
    // ... (rest of your App.js code)
  
    return (
      <div className="App">
        <header className="App-header">
          {/* Replace your existing navigation with the new Bootstrap navigation */}
          <NavScrollExample />
  
          {/* Render the selected page */}
          {renderPage()}
        </header>
      </div>
    );
  }
  

export default App;


