
class Node:
    def __init__(self, key: str, val, prv=None, nxt=None):
        self.key = key
        self.val = val
        self.prv = prv
        self.nxt = nxt

class myList:
    def __init__(self):
        self.dic = {}
        self.head = None
        self.tail = None
        self.count = 0

    # append node
    def append(self, node):
        if node.key in self.dic:
            print('Key 중복')
            return False
        self.dic[node.key] = node
        if self.count == 0:
            self.head = self.tail = node
            node.prv = node.nxt = None
        else:
            self.tail.nxt = node
            old_tail = self.tail
            self.tail = node
            self.tail.prv = old_tail
            self.tail.nxt = None
        self.count += 1
        return True

    # pop node & return node
    def pop(self, key):
        if key not in self.dic:
            print('Key 없음')
            return False
        if key == self.head.key:
            return self.popleft()
        elif key == self.tail.key:
            return self.popright()
        else:
            node = self.dic.pop(key)
            prev_node = node.prv
            next_node = node.nxt
            prev_node.nxt = next_node
            next_node.prv = prev_node
            self.count -= 1
            return node

    def popleft(self):
        if self.count == 0:
            print('원소 없음')
            return False
        if self.count == 1:
            ret = self.dic.pop(next(iter(self.dic)))
            self.head = self.tail = None
        else:
            new_head = self.head.nxt
            ret = self.dic.pop(next(iter(self.dic)))
            self.head = new_head
            self.head.prv = None
        self.count -= 1
        return ret

    def popright(self):
        if self.count == 0:
            print('원소 없음')
            return False
        if self.count == 1:
            ret = self.dic.pop(next(iter(self.dic)))
            self.head = self.tail = None
        else:
            new_tail = self.tail.prv
            ret = self.dic.pop(self.tail.key)
            self.tail = new_tail
            self.tail.nxt = None
        self.count -= 1
        return ret

    def print(self):
        for key, val in self.dic.items():
            print('key: ' + key + '; val: ' + str(val.val))
        print('----')


mylist = myList()
n1 = Node(key='1', val=1)
n2 = Node(key='2', val=2)
n3 = Node(key='3', val=3)
n4 = Node(key='4', val=4)
n5 = Node(key='5', val=5)
n6 = Node(key='6', val=6)
mylist.append(n1)
mylist.append(n2)
mylist.append(n3)
mylist.append(n4)
mylist.append(n5)
mylist.append(n6)
mylist.print()

mylist.popleft()
mylist.print()

mylist.popright()
mylist.print()

mylist.pop(key='3')
mylist.pop(key='2')
mylist.print()
