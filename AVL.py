class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _find_successor_node(self, node):
        while node.left:
            node = node.left
        return node

    def _rotateR(self, node):
        y = node.left
        t2 = y.right
        y.right = node
        node.left = t2
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _rotateL(self, node):
        y = node.right
        t2 = y.left
        y.left = node
        node.right = t2
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        # Termination: Reaching Leaf
        if not node:
            return TreeNode(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._balance(node)
        # LL Case -> Right Rotation of node
        if balance > 1 and val < node.left.val:
            return self._rotateR(node)
        # RR Case -> Left Rotation of node
        if balance < -1 and val > node.right.val:
            return self._rotateL(node)
        # LR Case -> Left Rotation of node.left -> Right Rotation of node
        if balance > 1 and val > node.left.val:
            node.left = self._rotateL(node.left)
            return self._rotateR(node)
        # RL Case -> Right Rotation of node.right -> Left Rotation of node
        if balance < -1 and val < node.right.val:
            node.right = self._rotateR(node.right)
            return self._rotateL(node)
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        # Node Found
        else:
            # If node has only one child
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            # If node has two children
            successor_node = self._find_successor_node(node.right)
            node.val = successor_node.val
            node.right = self._delete(node.right, successor_node.val)
        # If only None is left
        if not node:
            return None

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._balance(node)
        # LL Case
        if balance > 1 and self._balance(node.left) >= 0:
            return self._rotateR(node)
        # RR Case
        if balance < -1 and self._balance(node.right) <= 0:
            return self._rotateL(node)
        # LR Case
        if balance > 1 and self._balance(node.left) < 0:
            node.left = self._rotateL(node.left)
            return self._rotateR(node)
        # RL Case
        if balance < -1 and self._balance(node.right) > 0:
            node.right = self._rotateR(node.right)
            return self._rotateL(node)
        return node

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if not node:
            return
        print(node.val, end=' ')
        print('down left: ', end=' ')
        self._preorder(node.left)
        print('returned;', end=' ')
        print('down right: ', end=' ')
        self._preorder(node.right)
        print('returned;', end=' ')




tree = AVL()
tree.insert(3)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(9)
tree.insert(17)
tree.insert(22)
tree.insert(-3)
tree.delete(3)
tree.preorder()
