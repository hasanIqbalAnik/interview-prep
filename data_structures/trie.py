"""
A tree data structure.
Applications of a trie:
1. instant searches
2. small alphabet with lots of redundancy in words, like stems.
3. efficient lookup and insertion
4. no collision like in hash

however, it does suffer from memory overhead. space complexity is O(n * k * l) where,
n is the number of keys, k is the maximum length of a key and l is the size of alphabet.

construction:
a node class, consisting of a boolean value, representing whether this is the terminal node of a
string or not, and a map for storing the children, who are essentially a collection of trie
nodes themselves.
"""


class TrieNode:
    def __init__(self, terminal=None, children=None):
        self.terminal = terminal if terminal else False  # signifying whether this is the final node for a string
        self.children = children if children else {}  # would be a collection of TrieNodes

    def __str__(self):
        return str(self.children)


class Trie:
    def __init__(self):
        """initialize the trie instance with an empty root"""
        self.root = TrieNode()

    def insert(self, word):
        word_length = len(word)
        current_root = self.root

        for i in range(len(word)):
            if word[i] in current_root.children:  # change the root, move down the tree
                current_root = current_root.children[word[i]]
            else:  # create a new node
                current_root.children[word[i]] = TrieNode(True, None) if i == (word_length - 1) else TrieNode()
                current_root = current_root.children[word[i]]

    def search(self, word):
        word_length = len(word)
        current_root = self.root

        for i in range(len(word)):
            if word[i] in current_root.children:  # change the root, move down the tree
                current_root = current_root.children[word[i]]
                if i == word_length -1 and not current_root.terminal: # if this is the last character and its
                    #  not the terminal node
                    return False
            else:
                return False
        return True


# todo deletion



trie = Trie()
trie.insert('act')
trie.insert('acid')
trie.insert('acid')
trie.insert('bell')
trie.insert('belt')
trie.insert('bed')
trie.insert('cat')
trie.insert('cap')

print trie


