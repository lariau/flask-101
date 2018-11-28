class Counter:
    def __init__(self):
        self.id = 12

    def next(self):
        self.id += 1
        return self.id
