class MutableInt:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

    def __str__(self):
        return f"{self.value}"
