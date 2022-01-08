class SegmentTreeNode:
    def __init__(self, val, start, end, left=None, right=None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        self.mid = (start + end) // 2


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.root = self._build(0, len(nums)-1)

    def _build(self, start, end):
        if start == end:
            return SegmentTreeNode(self.nums[start], start, end)
        mid = (start + end) // 2
        left = self._build(start, mid)
        right = self._build(mid+1, end)
        return SegmentTreeNode(left.val+right.val, start, end, left, right)

    """
    l, r each means the start and the end of the range
    """
    def query(self, node, l, r):
        if node.start == l and node.end == r:
            return node.val
        mid = node.mid
        if r <= mid:
            return self.query(node.left, l, r)
        elif l > mid:
            return self.query(node.right, l, r)
        else:
            return self.query(node.left, l, mid) + self.query(node.right, mid+1, r)

    """
    idx: the index that should be changed
    diff: new value - old value
    """
    def update(self, node, idx, diff):
        if node.start == node.end:
            node.val += diff
            self.nums[idx] += diff
            return
        mid = node.mid
        if idx <= mid:
            self.update(node.left, idx, diff)
        else:
            self.update(node.right, idx, diff)
        node.val += diff



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = SegmentTree(nums)
tree.update(tree.root, 0, 9)
print(tree.query(tree.root, 0, 5))
tree.update(tree.root, 3, 17)
print(tree.query(tree.root, 0, 5))
