# CRM Analytics Application

## Overview
The CRMAnalytics application is a Python-based tool designed to analyze and provide insights into customer relationship management (CRM) data. It includes classes for managing customers, sales, interactions, and an analytics module (CRMAnalytics) for calculating various metrics.

## Files and Modules
### CRMAnalytics.py
CRMAnalytics class
The main analytics module that calculates various metrics based on CRM data.
Methods:
total_sales_amount: Calculate the total amount of all sales.
average_sale_amount: Calculate the average amount of all sales.
total_customers: Get the total number of customers.
sales_by_stage: Count the number of sales in each stage.
interactions_by_type: Count the number of interactions by type.
### CRMSystem.py
CRMSystem class
Manages customers and sales within the CRM system.
Methods:
add_customer: Add a new customer to the CRM system.
edit_customer: Edit customer details.
delete_customer: Delete a customer from the CRM system.
categorize_contacts: Categorize contacts based on a specified category.
add_sale: Add a new sale to the CRM system.
search_customers: Search for customers based on a keyword.
filter_sales_by_stage: Filter sales by the specified stage.
### Customer.py
Customer class
Represents a customer in the CRM system.
Methods:
Getters and setters for customer attributes.
add_interaction: Add an interaction to the customer.
add_sale: Add a sale to the customer.
get_tags: Get customer tags.
### Email.py
EmailSender class
Handles sending emails using SMTP.
Reads email configuration from config.json.
Methods:
send_email: Send an email with the specified subject and body to the specified email address.
### Interaction.py
Interaction class
Represents an interaction with a customer.
Getters and setters for interaction attributes.
### main.py
Example usage of the CRM system, creating customers, sales, and interactions.
Example usage of the CRMAnalytics module to calculate and print various metrics.
### Sale.py
Sale class
Represents a sale in the CRM system.
Getters and setters for sale attributes.
Getting Started
Ensure you have Python installed on your machine.
Clone the repository or download the files.
Run main.py to see the example usage of the CRM system and analytics module.
## Dependencies
Python 3.x

## Configuration
Edit config.json to set up your email configuration for the EmailSender class.

```json
{
    "OPENAI_KEY": "Key for LLM Tasks",
    "emailRecepient": "Test email recepient",
    "emailSender": "Email sent by",
    "emailPassword": "Email encryption"
}
```
## Usage
Follow the examples in main.py to understand how to use the CRM system and analytics module.

## Note
The application is designed for educational purposes and may require additional enhancements for production use.
Make sure to handle sensitive information securely, especially in the email configuration.
Feel free to explore and modify the code to meet your specific requirements. If you have any questions or issues, please refer to the documentation or contact the author.
