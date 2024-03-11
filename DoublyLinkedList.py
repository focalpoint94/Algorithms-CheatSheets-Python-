class Node:
    def __init__(self, val, prv=None, nxt=None):
        self.val = val
        self.prv = prv
        self.nxt = nxt


class DLL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, prv=self.head)
        self.head.nxt = self.tail
        self.count = 0

    def append(self, value):
        node = Node(value)
        if self.count == 0:
            self.head.nxt = node
            node.prv = self.head
            node.nxt = self.tail
            self.tail.prv = node
        else:
            prv_tail = self.tail.prv
            prv_tail.nxt = node
            node.prv = prv_tail
            node.nxt = self.tail
            self.tail.prv = node
        self.count += 1
        return True

    def remove(self, value):
        cur = self.head.nxt
        while cur != self.tail and cur.val != value:
            cur = cur.nxt
        if cur == self.tail:
            return False
        prv = cur.prv
        nxt = cur.nxt
        prv.nxt = nxt
        nxt.prv = prv
        return True

    def print(self):
        cur = self.head.nxt
        while cur != self.tail:
            print(cur.val, end=" ")
            cur = cur.nxt
        print("")


arr = DLL()
arr.append(3)
arr.append(4)
arr.append(5)
arr.append(6)
arr.print()
arr.remove(5)
arr.print()
arr.remove(7)
arr.print()
