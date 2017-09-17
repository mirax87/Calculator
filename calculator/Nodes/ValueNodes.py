from Node import Node

class ValueNode(Node):
    def isOperator(self):
        return(False)
    
    def evaluate(self):
        raise NotImplementedError("Subclass must implement abstract method")

class RealNode(ValueNode):
    def __init__(self, value):
        self.value = float(value)
        self.l = None
        self.r = None

    def evaluate(self):
        return(self.value)

    def __str__(self):
        return(str(self.value))

class complexNode(ValueNode):
    def __init__(self, value):
        self.value = complex(value)
        self.l = None
        self.r = None

    def evaluate(self):
        return(self.value)
    def __str__(self):
        return(str(self.value))
