import string

def rabinKarp(sentence: string, pattern:string, p:int, mod=10**9+7) -> int:
    '''
    sentence: string
    pattern: pattern
    p: power value for hash function
    mod: mod value (default: 10**9 + 7)

    returns the first index of the matching
    '''
    n, l = len(sentence), len(pattern)
    if n < l:
        return -1

    if sentence[:l] == pattern:
        return 0

    arr = [ord(c) - ord('a') for c in sentence]

    patternHash, h = 0, 0
    for i in range(l):
        patternHash = (patternHash * p + ord(pattern[i]) - ord('a')) % mod
        h = (h * p + arr[i]) % mod

    for i in range(1, n - l + 1):
        h = (h * p - arr[i-1] * pow(p, l, mod) + arr[i+l-1]) % mod
        if h == patternHash and sentence[i:i+l] == pattern:
            return i
    return -1


'''
Example
'''
string = 'dkjfapviovjqvjaaavl'
pattern = 'iovjqvj'
h = len(set(string))
print(rabinKarp(string, pattern, h))
