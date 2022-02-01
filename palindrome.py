class Solution:
    def build_palindrome(self, word):
        n = len(word)
        dp = [[False] * n for _ in range(n)]
        for end in range(n):
            for start in range(end+1):
                if s[end] == s[start] and (end - start <= 2 or dp[start+1][end-1]):
                    dp[start][end] = True
        return dp
        

    
