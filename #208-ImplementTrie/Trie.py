class Trie:
    """
    A trie (pronounced as "try") or prefix tree is a tree data structure 
    used to efficiently store and retrieve keys in a dataset of strings. 
    There are various applications of this data structure, such as autocomplete and spellchecker.
    Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), 
    and false otherwise.
    boolean startsWith(String prefix) 
    Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

    Example 1:

    Input
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output
    [null, null, true, false, true, null, true]

    Explanation
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True
    """
    
    class Node:
        def __init__(self):
            self.is_end = False
            self.children = {}

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str) -> None:

        N = len(word)

        def helper(index, node):
            if index != N:
                if word[index] in node.children:
                    helper(index + 1, node.children[word[index]])
                else:
                    node.children[word[index]] = Trie.Node()
                    helper(index + 1, node.children[word[index]])
            else:
                node.is_end = True

        helper(0, self.root)

    def search(self, word: str) -> bool:

        N = len(word)

        def helper(index, node):
            if index == N:
                if node.is_end:
                    return True
                return False
            else:
                if word[index] in node.children:
                    return helper(index + 1, node.children[word[index]])
                else:
                    return False

        return helper(0, self.root)

    def startsWith(self, word):
        N = len(word)

        def helper(index, node):
            if index == N:
                return True
            else:
                if word[index] in node.children:
                    return helper(index + 1, node.children[word[index]])
                else:
                    return False

        return helper(0, self.root)