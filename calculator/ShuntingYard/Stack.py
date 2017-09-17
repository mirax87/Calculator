class Stack(list):
    def push(self, elements):
        self.append(elements)

    def toString(self):
        return(self)


class OperatorStack(Stack):
    def __init__(self, operatorSet):
        self.operatorSet = operatorSet

    def isEmpty(self):
        return(len(self) == 0)

    def isOperatorOnTop(self):
        if self.isEmpty():
            return(False)
        return(self[-1] in self.operatorSet)

class OutputStack(Stack):
    pass
