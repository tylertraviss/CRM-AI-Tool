// Customers.js
import React from 'react';

const CustomerCard = ({ customer }) => {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', border: '1px solid #ddd', borderRadius: '5px', margin: '10px', padding: '10px' }}>
        <div style={{ marginBottom: '10px' }}>
          <strong>Name:</strong> {customer.name}
        </div>
        <div style={{ marginBottom: '10px' }}>
          <strong>Company:</strong> {customer.company}
        </div>
        <div style={{ marginBottom: '10px' }}>
          <strong>Email:</strong> {customer.email}
        </div>
      </div>
    );
  };
  

const Customers = () => {
  const customers = [
    {
      name: 'John Doe',
      email: 'john.doe@apple.com',
      company: 'Apple',
    },
    {
      name: 'Jane Smith',
      email: 'js@google.com',
      company: 'Google',
    },
    {
      name: 'Bob Johnson',
      email: 'bj@cisco.com',
      company: 'Cisco',
    },
  ];

  return (
    <div>
        <p>

        </p>
      {customers.map((customer, index) => (
        <CustomerCard key={index} customer={customer} />
      ))}
    </div>
  );
};

export default Customers;
