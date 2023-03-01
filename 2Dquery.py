class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.M, self.N = len(matrix), len(matrix[0])
        self.matrix = [[0] * (self.N) for _ in range(self.M)]
        self.tree = [[0] * (self.N+1) for _ in range(self.M+1)]
        for y in range(self.M):
            for x in range(self.N):
                self.update(y, x, matrix[y][x])

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= self.M:
            j = col + 1
            while j <= self.N:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def sum(self, row, col):
        res, i = 0, row+1
        while i:
            j = col+1
            while j:
                res += self.tree[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum(row2, col2) + self.sum(row1-1, col1-1) - self.sum(row1-1, col2) - self.sum(row2, col1-1)
