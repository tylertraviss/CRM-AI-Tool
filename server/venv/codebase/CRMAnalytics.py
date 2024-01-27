class CRMAnalytics:
    def __init__(self, crm_system):
        self.crm_system = crm_system

    def total_sales_amount(self): # troubleshoot total sales amount
        """Calculate the total amount of all sales."""
        return sum(sale.get_amount() for sale in self.crm_system.sales)

    def average_sale_amount(self): # troubleshoot total sales amount
        """Calculate the average amount of all sales."""
        total_amount = self.total_sales_amount()
        total_sales = len(self.crm_system.sales)
        return total_amount / total_sales if total_sales > 0 else 0

    def total_customers(self):
        """Get the total number of customers."""
        return len(self.crm_system.customers)

    def sales_by_stage(self):
        """Count the number of sales in each stage."""
        sales_by_stage = {}
        for sale in self.crm_system.sales:
            stage = sale.get_stage()
            sales_by_stage[stage] = sales_by_stage.get(stage, 0) + 1
        return sales_by_stage

    def interactions_by_type(self):
        """Count the number of interactions by type."""
        interactions_by_type = {}
        for customer in self.crm_system.customers:
            for interaction in customer.get_interactions():
                interaction_type = interaction.get_interaction_type()
                interactions_by_type[interaction_type] = interactions_by_type.get(interaction_type, 0) + 1
        return interactions_by_type