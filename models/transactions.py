

class Transaction:
    def __init__(self, amount, tag, merchant, when, description, id = None):
        self.amount = amount
        self.tag = tag
        self.merchant = merchant
        self.when = when
        self.description = description
        self.id = id