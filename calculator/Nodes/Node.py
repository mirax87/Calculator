class Node:
    def __init__(self):
        self.l = None
        self.r = None

    def evaluate(self):
        raise NotImplementedError("Subclass must implement abstract method")
