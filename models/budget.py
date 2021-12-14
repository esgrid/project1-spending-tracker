
class Budget:

    def __init__(self, alloted, id = None):
        self.alloted = alloted
        self.id = id

class Tracking:

    def __init__(self, budget, spent):
        self.budget = budget
        self.spent = spent