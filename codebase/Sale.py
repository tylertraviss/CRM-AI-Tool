class Sale:
    
    def __init__(self, sale_id, customer_id, stage, amount, notes=None):
        self.sale_id = sale_id
        self.customer_id = customer_id
        self.stage = stage
        self.amount = amount
        self.notes = notes

    def get_sale_id(self):
        return self.sale_id

    def set_sale_id(self, sale_id):
        self.sale_id = sale_id

    def get_sales(self):
        return self.sales

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_stage(self):
        return self.stage

    def set_stage(self, stage):
        self.stage = stage

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

    def __str__(self):
        return f"Sale ID: {self.sale_id}, Customer ID: {self.customer_id}, Stage: {self.stage}, Amount: {self.amount}, Notes: {self.notes}"
