// Dashboard.js
import React from 'react';

// Individual Metric Component
const Metric = ({ label, value }) => (
  <div style={{ margin: '20px', padding: '20px', border: '1px solid #ddd', borderRadius: '5px', textAlign: 'center' }}>
    <h3>{label}</h3>
    <p>{value}</p>
  </div>
);


// Dashboard Component
const Dashboard = () => {
  return (
    <div>
    </div>
  );
};

export default Dashboard;
