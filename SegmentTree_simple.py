import math
class SegmentTree:

    def __init__(self, nums):
        self.tree = [0] * pow(2,math.ceil(math.log(len(nums),2))+1)
        self.nums = nums
        self._build(node=1, start=0, end=len(nums)-1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = self.nums[start]
            return self.tree[node]
        mid = (start + end) // 2
        self.tree[node] = self._build(node*2, start, mid) + self._build(node*2+1, mid+1, end)
        return self.tree[node]

    def query(self, ql, qr):
        return self._query(1, 0, len(self.nums)-1, ql, qr)

    def _query(self, node, start, end, ql, qr):
        if start == ql and end == qr:
            return self.tree[node]
        mid = (start + end) // 2
        if qr <= mid:
            return self._query(node*2, start, mid, ql, qr)
        if ql > mid:
            return self._query(node*2+1, mid+1, end, ql, qr)
        return self._query(node*2, start, mid, ql, mid) + self._query(node*2+1, mid+1, end, mid+1, qr)

    def update(self, idx, val):
        delta = val - self.nums[idx]
        self.nums[idx] = val
        self._update(1, 0, len(self.nums)-1, idx, delta)

    def _update(self, node, start, end, idx, delta):
        if start == end:
            self.tree[node] += delta
            return
        self.tree[node] += delta
        mid = (start + end) // 2
        if idx <= mid:
            self._update(node*2, start, mid, idx, delta)
        else:
            self._update(node*2+1, mid+1, end, idx, delta)
