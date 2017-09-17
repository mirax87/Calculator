import re

from calculator.ShuntingYard.ShuntingYard import ShuntingYard

class Formular:
    def __init__(self, formular, skipStack = False):
        self.__operators = '\+\-\*\/\(\)'
        self.formular = ''.join(formular.split())
        self.translateToOperations()
        if not skipStack:
            self.evaluate()

    def translateToOperations(self):
        x = re.split('(['+self.__operators+'])', self.formular)
        self.operations = [ y for y in x if len(y) > 0]

    def evaluate(self):
        sh = ShuntingYard(self.operations)
        self.stack = sh.stack

    def toString(self):
        return("".join(self.formular))
