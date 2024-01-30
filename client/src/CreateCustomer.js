// CreateCustomer.js
import React, { useState } from 'react';

const CreateCustomer = () => {
  // State to manage input values
  const [customerData, setCustomerData] = useState({
    name: '',
    email: '',
    phone: '',
    company: '',
    category: '',
  });

  // Handle input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCustomerData((prevData) => ({ ...prevData, [name]: value }));
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    // Add logic to handle the submission of customerData
    console.log('Customer Data:', customerData);
  };

  return (
    <div>
      <h2>Create Customer</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" name="name" value={customerData.name} onChange={handleInputChange} />
        </label>
        <br />
        <label>
          Email:
          <input type="text" name="email" value={customerData.email} onChange={handleInputChange} />
        </label>
        <br />
        <label>
          Phone:
          <input type="text" name="phone" value={customerData.phone} onChange={handleInputChange} />
        </label>
        <br />
        <label>
          Company:
          <input type="text" name="company" value={customerData.company} onChange={handleInputChange} />
        </label>
        <br />
        <label>
          Category:
          <input type="text" name="category" value={customerData.category} onChange={handleInputChange} />
        </label>
        <br />
        <button type="submit">Create Customer</button>
      </form>
    </div>
  );
};

export default CreateCustomer;
