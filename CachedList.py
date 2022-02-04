
class DLinkedNode():
    def __init__(self, key=None, val=None, prv=None, nxt=None):
        self.key = key
        self.val = val
        self.prv = prv
        self.nxt = nxt

class CachedList():
    def __init__(self):
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.nxt, self.tail.prv = self.tail, self.head
        self.address = dict()

    def insertHead(self, key, val=0):
        if key in self.address:
            return False
        node = DLinkedNode(key=key, val=val, prv=self.head, nxt=self.head.nxt)
        self.head.nxt.prv = node
        self.head.nxt = node
        self.address[key] = node
        return True

    def removeNode(self, key):
        if key not in self.address:
            return False
        node = self.address[key]
        node.nxt.prv = node.prv
        node.prv.nxt = node.nxt
        self.address.pop(key)
        return node

    def print(self):
        cur = self.head.nxt
        while cur != self.tail:
            print(cur.key, cur.val)
            cur = cur.nxt
        print()

arr = CachedList()
arr.insertHead(1, 1)
arr.insertHead(2, 2)
arr.insertHead(3, 3)
arr.insertHead(4, 4)
arr.print()
arr.removeNode(4)
arr.print()
