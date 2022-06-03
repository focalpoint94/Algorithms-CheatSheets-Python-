class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(nums)
        self.tree = [0] * pow(2,math.ceil(math.log(self.size,2))+1)
        self.build(node=1, left=0, right=self.size-1)
    
    def build(self, node, left, right):
        if left == right:
            self.tree[node] = self.nums[left]
            return self.tree[node]
        mid = (left + right) // 2
        self.tree[node] = self.build(node*2, left, mid) + self.build(node*2+1, mid+1, right)
        return self.tree[node]
    
    def update(self, index: int, val: int) -> None:
        self._update(index, val-self.nums[index], node=1, left=0, right=self.size-1)
        self.nums[index] = val
        
    def _update(self, index, diff, node, left, right):
        if left == right:
            self.tree[node] += diff
            return
        self.tree[node] += diff
        mid = (left + right) // 2
        if index <= mid:
            self._update(index, diff, node*2, left, mid)
        else:
            self._update(index, diff, node*2+1, mid+1, right)

    def sumRange(self, left: int, right: int) -> int:
        return self._query(left, right, node=1, left=0, right=self.size-1)
        
    def _query(self, ql, qr, node, left, right):
        if ql == left and qr == right:
            return self.tree[node]
        mid = (left + right) // 2
        if qr <= mid:
            return self._query(ql, qr, node*2, left, mid)
        elif ql >= mid + 1:
            return self._query(ql, qr, node*2+1, mid+1, right)
        return self._query(ql, mid, node*2, left, mid) + self._query(mid+1, qr, node*2+1, mid+1, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
