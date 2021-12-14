
class Transaction:
    def __init__(self, amount, tag, merchant, fecha, comments, id = None):
        self.amount = amount
        self.tag = tag
        self.merchant = merchant
        self.fecha = fecha
        self.comments = comments
        self.id = id