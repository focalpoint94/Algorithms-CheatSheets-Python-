from collections import deque


class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Parser:

    @staticmethod
    def expTree(expression):
        tokens = deque(list(expression))
        return Parser.parse_expression(tokens)

    @staticmethod
    def parse_expression(tokens):
        lhs = Parser.parse_term(tokens)
        while tokens and tokens[0] in ['+', '-']:
            op = tokens.popleft()
            rhs = Parser.parse_term(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    @staticmethod
    def parse_term(tokens):
        lhs = Parser.parse_factor(tokens)
        while tokens and tokens[0] in ['*', '/']:
            op = tokens.popleft()
            rhs = Parser.parse_factor(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    @staticmethod
    def parse_factor(tokens):
        # if integer
        if tokens[0].isnumeric():
            num = 0
            while tokens and tokens[0].isnumeric():
                num = num * 10 + int(tokens.popleft())
            return Node(val=num)

        elif tokens[0] == '(':
            # consume '('
            tokens.popleft()
            # if node is none: raise error
            node = Parser.parse_expression(tokens)
            # consume ')'
            # if token is not ')': raise error
            tokens.popleft()
            return node

        # if negate
        elif tokens[0] == '-':
            # consume '-'
            tokens.popleft()
            # if numNode is none: raise error
            numNode = Parser.parse_factor(tokens)
            return Node(val='-', left=None, right=numNode)

        # invalid token: raise error
        else:
            return None


    @staticmethod
    def print_tree(root):
        def _print_node(node):
            # leaf node with number value
            if node.left is None and node.right is None:
                print(node.val, end='')
                return
            # negate case: - (3 + 5)
            if node.left is None and node.right is not None:
                print('(', end='')
                # node.val should be '-' (negate)
                print(node.val, end='')
                _print_node(node.right)
                print(')', end='')
                return
            # operator case with both children
            # if node.left is None: raise error
            print('(', end='')
            _print_node(node.left)
            # node.val should be an operator
            print(node.val, end='')
            _print_node(node.right)
            print(')', end='')
        _print_node(root)
        print()

    @staticmethod
    def eval_tree(root):
        def _eval_node(node):
            # leaf node with number value
            if node.left is None and node.right is None:
                return node.val
            # negate case: - (3 + 5)
            if node.left is None and node.right is not None:
                # node.val should be '-' (negate)
                return -_eval_node(node.right)
            # operator case with both children
            # if node.left is None: raise error
            lhs, rhs = _eval_node(node.left), _eval_node(node.right)
            if node.val == '+':
                return lhs + rhs
            elif node.val == '-':
                return lhs - rhs
            elif node.val == '*':
                return lhs * rhs
            elif node.val == '/':
                return int(lhs/rhs)
            # invalid operator: raise error
            else:
                return None
        return _eval_node(root)




'''
Example
'''
root = Parser.expTree('22-3/(5*2)+1')
Parser.print_tree(root)
print(Parser.eval_tree(root))

