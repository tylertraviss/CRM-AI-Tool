import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
    const [name, setName] = useState(''); // State to store the name
    const [selectedOption, setSelectedOption] = useState(''); // State for selected option

    useEffect(() => {
        // Fetch user information from Flask when the component mounts
        fetch('http://localhost:5000/api/userinfo')
            .then(response => response.json())
            .then(data => {
                setName(data.name);
            })
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
                    <div className="Dashboard" onClick={() => handleOptionChange('Dashboard')}>Dashboard</div>
                    <div className="Customers" onClick={() => handleOptionChange('Customers')}>Customers</div>
                    <div className="Sales" onClick={() => handleOptionChange('Sales')}>Sales</div>
                </div>
                <h1>Welcome back, {name}!</h1>
                <p>This is a simple landing page with options.</p>
                <p>Selected Option: {selectedOption}</p>
            </header>
        </div>
    );
}

export default App;

// const ScrollableTable = () => {
//   return (
//     <div className="scrollable-table-container">
//       <table className="scrollable-table">
//         <thead>
//           <tr>
//             <th>ID</th>
//             <th>Name</th>
//             <th>Company</th>
//             <th>Category</th>
//           </tr>
//         </thead>
//         <tbody>
//           <tr>
//             <td>1</td>
//             <td>John Doe</td>
//             <td>john@example.com</td>
//             <td>Admin</td>
//           </tr>
//           <tr>
//             <td>2</td>
//             <td>Jane Smith</td>
//             <td>jane@example.com</td>
//             <td>User</td>
//           </tr>
//           {/* Add more rows as needed */}
//         </tbody>
//       </table>
//     </div>
//   );
// };

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <ScrollableTable />
//       </header>
//     </div>
//   );
// }

// export default App;
