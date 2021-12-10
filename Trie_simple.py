trie = {}
for word in words:
  t = trie
  for char in word:
    if char not in t:
      t[char] = {}
    t = t[char]
  t['#'] = '#'
