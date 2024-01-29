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
        <p>Major Metrics</p>
      {/* Three Number Metrics */}
      <div style={{ display: 'flex', justifyContent: 'space-around' }}>
        <Metric label="Total Sales" value="$10,000" />
        <Metric label="Customers" value="500" />
        <Metric label="Profit Margin" value="15%" />
      </div>

      {/* Additional Dashboard Content */}
      <p>Upcoming Meetings</p>
    </div>
  );
};

export default Dashboard;
