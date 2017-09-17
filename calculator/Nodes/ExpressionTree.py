from calculator.Nodes.NodeFactory import NodeFactory

## class Expression tree taken from
## https://abhirama.wordpress.com/2009/08/26/expression-tree/

class ExpressionTree:
    def __init__(self):
        self.__root = None

    def evaluate(self):
        return(self.__root.evaluate())

    def inorder(self):
        self.__inorder_helper(self.__root)

    def __inorder_helper(self, node):
        if node:
            self.__inorder_helper(node.l)
            print str(node)
            self.__inorder_helper(node.r)

    def preorder(self):
        self.__preorder_helper(self.__root)

    def __preorder_helper(self, node):
        if node:
            print str(node)
            self.__preorder_helper(node.l)
            self.__preorder_helper(node.r)

    def postorder(self):
        self.__postorder_helper(self.__root)

    def __postorder_helper(self, node):
        if node:
            self.__postorder_helper(node.l)
            self.__postorder_helper(node.r)
            print str(node)

    def create_expression_tree_from_postfix(self, postfix):
        stack = []
        nf = NodeFactory()
        for char in postfix:
            node = nf.generate(char)
            if not node.isOperator():
                stack.append(node)
            else:
                right = stack.pop()
                left = stack.pop()
                node.r = right
                node.l = left
                stack.append(node)

        self.__root = stack.pop()
