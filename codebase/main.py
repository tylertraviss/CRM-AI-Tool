from CRMSystem import CRMSystem
from Interaction import Interaction
from Sale import Sale
from CRMAnalytics import CRMAnalytics
import json

# Example Usage:
crm = CRMSystem()

# Add customers with sales and interactions
customer1 = crm.add_customer("John Doe", "john@example.com", "123-456-7890", "ABC Inc.", "Business")
sale1 = Sale(1, customer1.get_id(), "Pending", 5000, "Initial sale")
interaction1 = Interaction(1, "2024-01-24 10:00:00", "Meeting", "Discussion about the product")
customer1.add_interaction(interaction1)
customer1.add_sale(sale1)

customer2 = crm.add_customer("Jane Smith", "jane@example.com", "987-654-3210", "XYZ Corp.", "Personal")
sale2 = Sale(2, customer2.get_id(), "Negotiation", 8000, "Ongoing negotiation")
interaction2 = Interaction(2, "2024-01-25 15:30:00", "Call", "Follow-up call with the customer")
customer2.add_interaction(interaction2)
customer2.add_sale(sale2)


# Print customer information with associated sales and interactions
print("Customer Information:")
for customer in crm.customers:
    print(customer)
    print("Sales:")
    for sale in customer.get_sales():
        print(f"  - {sale}")
    print("Interactions:")
    for interaction in customer.get_interactions():
        print(f"  - {interaction}")
    print("")


# Example Usage:
analytics = CRMAnalytics(crm)

# Calculate and print metrics
print(f"Total Sales Amount: ${analytics.total_sales_amount()}")
print(f"Average Sale Amount: ${analytics.average_sale_amount():.2f}")
print(f"Total Customers: {analytics.total_customers()}")
print("Sales by Stage:")
for stage, count in analytics.sales_by_stage().items():
    print(f"  - {stage}: {count} sales")
print("Interactions by Type:")
for interaction_type, count in analytics.interactions_by_type().items():
    print(f"  - {interaction_type}: {count} interactions")



