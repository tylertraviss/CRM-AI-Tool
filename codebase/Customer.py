from .Interaction import Interaction

class Customer:
    def __init__(self):
        self.name = None
        self.email = None
        self.phone = None
        self.company = None
        self.category = None
        self.interactions = []
        self.sales = []
        self.tags = []

    def get_tags(self):
        return self.tags

    def add_tags(self, tag):
        self.tags.append(tag)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def add_sale(self, sale):
        self.sales.append(sale)

    def get_sales(self):
        return self.sales

    def get_id(self):
        return self.customer_id

    def set_id(self, customer_id):
        self.customer_id = customer_id

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_company(self):
        return self.company

    def set_company(self, company):
        self.company = company

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def add_interaction(self, interaction):
        self.interactions.append(interaction)

    def get_interactions(self):
        return self.interactions

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.phone}"
