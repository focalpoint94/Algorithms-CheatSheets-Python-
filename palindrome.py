    def palindrome(self, word):
        n = len(word)
        table = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j+1):
                if word[j] == word[i] and (j - i <= 2 or table[i+1][j-1]):
                    table[i][j] = True
        return table
