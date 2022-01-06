class SegmentTreeNode:
    def __init__(self, val, start, end, left=None, right=None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right

    def _mid(self):
        return self.start + (self.end - self.start) // 2


class Tree:
    def __init__(self, nums):
        self.nums = nums
        self.root = None
        if self.nums:
            self.root = self._build(0, len(self.nums) - 1)

    def _build(self, start, end):
        if start == end:
            return SegmentTreeNode(self.nums[start], start, end)

        mid = (start + end) // 2
        left = self._build(start, mid)
        right = self._build(mid + 1, end)
        return SegmentTreeNode(left.val + right.val, start, end, left, right)

    def _update(self, node, idx, val):
        if node.start == node.end == idx:
            self.nums[idx] += val
            node.val += val
            return

        mid = node._mid()
        if idx <= mid:
            self._update(node.left, idx, val)
        else:
            self._update(node.right, idx, val)
        node.val = node.left.val + node.right.val

    def _query(self, node, l, r):
        if node.start == l and node.end == r:
            return node.val

        mid = node._mid()
        if r <= mid:
            return self._query(node.left, l, r)
        elif l > mid:
            return self._query(node.right, l, r)
        return self._query(node.left, l, mid) + self._query(node.right, mid + 1, r)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# tree = Tree(nums)
# print(tree._query(tree.root, 1, 4))

