class TrieNode:
    def __init__(self):
        self.children = {}
        self.endFlag = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endFlag = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.endFlag

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        return self._delete(self.root, word, 0)

    def _delete(self, node, word, i):
        if i == len(word):
            if not node.endFlag:
                return False
            node.endFlag = False
            return len(node.children) == 0
        if word[i] not in node.children:
            return False
        need_delete = self._delete(node.children[word[i]], word, i+1)
        if need_delete:
            node.children.pop(word[i])
            return len(node.children) == 0
        return False
        
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
