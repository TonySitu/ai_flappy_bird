class MutableInt:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other_value):
        self.value += other_value

    def __iadd__(self, other_value):
        self.value += other_value

    def __str__(self):
        return f"{self.value}"
