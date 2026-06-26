from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def solve(words: List[str]) -> List[int]:
    root = TrieNode()
    
    # Build the Trie
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
            
    # Calculate scores
    results = []
    for word in words:
        score = 0
        node = root
        for char in word:
            node = node.children[char]
            score += node.count
        results.append(score)
        
    return results
