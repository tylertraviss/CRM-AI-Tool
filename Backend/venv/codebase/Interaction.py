class Interaction:
    def __init__(self, interaction_id, timestamp, interaction_type, notes):
        self.interaction_id = interaction_id
        self.timestamp = timestamp
        self.interaction_type = interaction_type
        self.notes = notes

    def __str__(self):
        return f"Interaction ID: {self.interaction_id}, Type: {self.interaction_type}, Notes: {self.notes}"


    def get_interaction_id(self):
        return self.interaction_id

    def set_interaction_id(self, interaction_id):
        self.interaction_id = interaction_id

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def get_interaction_type(self):
        return self.interaction_type

    def set_interaction_type(self, interaction_type):
        self.interaction_type = interaction_type

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

    def __str__(self):
        return f"Interaction ID: {self.interaction_id}, Type: {self.interaction_type}, Notes: {self.notes}"