class SegmentTreeNode:

    def __init__(self, start, end, val, left=None, right=None):
        self.start = start
        self.end = end
        self.mid = (start + end) // 2
        self.val = val
        self.left = left
        self.right = right


class SegmentTree:

    def __init__(self, nums):
        self.nums = nums
        self.root = self._build(0, len(nums)-1)

    def _build(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, self.nums[start])
        mid = (start + end) // 2
        left = self._build(start, mid)
        right = self._build(mid+1, end)
        return SegmentTreeNode(start, end, left.val+right.val, left, right)

    def query(self, ql, qr):
        return self._query(self.root, ql, qr)

    def _query(self, node, ql, qr):
        if node.start == ql and node.end == qr:
            return node.val
        mid = node.mid
        if qr <= mid:
            return self._query(node.left, ql, qr)
        if ql > mid:
            return self._query(node.right, ql, qr)
        return self._query(node.left, ql, mid) + self._query(node.right, mid+1, qr)

    def update(self, idx, val):
        delta = val - self.nums[idx]
        self.nums[idx] = val
        self._update(self.root, idx, delta)

    def _update(self, node, idx, delta):
        if node.start == node.end:
            node.val += delta
            return
        node.val += delta
        mid = node.mid
        if idx <= mid:
            self._update(node.left, idx, delta)
        else:
            self._update(node.right, idx, delta)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = SegmentTree(nums)
tree.update(0, 9)
print(tree.query(0, 5))
tree.update(3, 17)
print(tree.query(0, 5))
