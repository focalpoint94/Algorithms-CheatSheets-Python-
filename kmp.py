def getPi(pattern):
    m, j = len(pattern), 0
    pi = [0] * m
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            pi[i] = ++j
    return pi


def kmp(string, pattern):
    ret = []
    pi = getPi(pattern)
    n, m, j = len(string), len(pattern), 0
    for i in range(n):
        while j > 0 and string[i] != pattern[j]:
            j = pi[j-1]
        if string[i] == pattern[j]:
            if j == m - 1:
                ret.append(i-m+1)
                j = pi[j]
            else:
                j += 1
    return ret
