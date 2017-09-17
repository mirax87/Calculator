import sys

from calculator.Formular.Formular import Formular
from calculator.Nodes.ExpressionTree import ExpressionTree


class Calculator:
    def __init__(self, formular):
        self.formular = Formular(formular)
        self.operations = self.formular.stack

        self.__tree = ExpressionTree()
        self.__tree.create_expression_tree_from_postfix(self.operations)

    def toString(self):
        return(self.operations.toString())

    def result(self):
        return(self.__tree.evaluate())

    def __str__(self):
        return(" ".join(self.operations))

if __name__ == '__main__':
    # take user input (cmd line)
    # pass to Calculator
    calc = Calculator(sys.argv[1])
    # print results
    print(calc.result())
