

class Fenwick:
    """
    Python implementation of
    Fenwick Tree (or Binary Indexed Tree)
    # Useful in handling range queries
    # Update: O(logN)
    # query: O(logN)
    # buildTree: O(NlogN)
    """
    def __init__(self, nums):
        """
        Initialization
        """
        self.N = len(nums)
        self.tree = [0] * (self.N+1)
        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, i: int, diff: int):
        """
        Updates value at index i with diff
        # diff = new value - old value
        """
        i += 1
        while i <= self.N:
            self.tree[i] += diff
            i += i & (-i)

    def query(self, i, j):
        """
        returns sum of nums from i to j (both i & j are included)
        """
        ret = 0
        j = j + 1
        while j > 0:
            ret += self.tree[j]
            j -= j & (-j)
        while i > 0:
            ret -= self.tree[i]
            i -= i & (-i)
        return ret


nums = [2, 5, 1, -3, 2, 3, -4, 5, 56, 7, 8, -79]
tree = Fenwick(nums)
print(tree.query(1, 6))

