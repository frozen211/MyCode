# 208. Implement Trie (Prefix Tree)
# This is also an important data structure for string related Leetcode questions
# because it can effectively search for strings with a specific prefix

# Trie basically trade space for time, so it has a realtively high space complexity
# O(S), S is the total number of characters in all the strings that are inserted into the trie.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    # The runtime of insertion is O(L), where L is the length of the string.
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    # The runtime of search is O(L).
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    # still O(L)
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

## main
if __name__ =="__main__":
    T = Trie()
    T.insert("Hello")
    T.insert("world")
    print(T.search("apple"), T.search("Hello"))
    print(T.startsWith("app"), T.startsWith("Hell"))

