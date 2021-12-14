

class Transaction:
    def __init__(self, amount, tag, merchant, when, comments, id = None):
        self.amount = amount
        self.tag = tag
        self.merchant = merchant
        self.when = when
        self.comments = comments
        self.id = id