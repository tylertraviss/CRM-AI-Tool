from Customer import Customer
from Sale import Sale

class CRMSystem:
    def __init__(self):
        self.customers = []
        self.sales = []

    def add_customer(self, name, email, phone, company=None, category=None):
        customer = Customer()
        customer.set_id(len(self.customers) + 1)  # Assign a unique ID to the customer
        customer.set_name(name)
        customer.set_email(email)
        customer.set_phone(phone)
        customer.set_company(company)
        customer.set_category(category)
        self.customers.append(customer)
        return customer

    def edit_customer(self, email, new_name=None, new_phone=None, new_company=None, new_category=None):
        for customer in self.customers:
            if customer.get_email() == email:
                if new_name:
                    customer.set_name(new_name)
                if new_phone:
                    customer.set_phone(new_phone)
                if new_company:
                    customer.set_company(new_company)
                if new_category:
                    customer.set_category(new_category)
                return True  # Customer edited successfully
        return False  # Customer not found

    def delete_customer(self, email):
        for customer in self.customers:
            if customer.get_email() == email:
                self.customers.remove(customer)
                return True  # Customer deleted successfully
        return False  # Customer not found

    def categorize_contacts(self, category):
        categorized_contacts = [customer for customer in self.customers if customer.get_category() == category]
        return categorized_contacts

    def add_sale(self, customer_id, stage, amount, notes=None):
        sale_id = len(self.sales) + 1
        sale = Sale(sale_id, customer_id, stage, amount, notes)
        self.sales.append(sale)
        return sale

    def search_customers(self, keyword):
        """Search for customers based on a keyword."""
        matching_customers = [customer for customer in self.customers
                                if keyword.lower() in customer.get_name().lower() or
                                keyword.lower() in customer.get_email().lower()]
        return matching_customers

    def filter_sales_by_stage(self, stage):
        """Filter sales by the specified stage."""
        filtered_sales = [sale for sale in self.sales if sale.get_stage().lower() == stage.lower()]
        return filtered_sales


