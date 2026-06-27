import math

class TrieNode:
    def __init__(self):
        self.children = {}
        self.cost = math.inf

def solve(target: str, words: list[str], costs: list[int]) -> int:
    root = TrieNode()
    
    # Build Trie
    for word, cost in zip(words, costs):
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.cost = min(node.cost, cost)
        
    n = len(target)
    dp = [math.inf] * (n + 1)
    dp[0] = 0
    
    # DP with Trie traversal
    for i in range(n):
        if dp[i] == math.inf:
            continue
            
        node = root
        for j in range(i, n):
            char = target[j]
            if char not in node.children:
                break
            node = node.children[char]
            if node.cost != math.inf:
                if dp[i] + node.cost < dp[j + 1]:
                    dp[j + 1] = dp[i] + node.cost
                    
    return dp[n] if dp[n] != math.inf else -1
