class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores (length_of_word, index_in_container)
        self.best = (float('inf'), float('inf'))

def solve(wordsContainer, wordsQuery):
    root = TrieNode()
    
    def insert(word, index):
        length = len(word)
        node = root
        # Update root if this word is better than current best
        if (length, index) < node.best:
            node.best = (length, index)
            
        # Insert reversed word
        for char in reversed(word):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if (length, index) < node.best:
                node.best = (length, index)

    # Build the Trie
    for i, word in enumerate(wordsContainer):
        insert(word, i)
        
    results = []
    for query in wordsQuery:
        node = root
        # Traverse Trie with reversed query
        for char in reversed(query):
            if char in node.children:
                node = node.children[char]
            else:
                break
        results.append(node.best[1])
        
    return results
