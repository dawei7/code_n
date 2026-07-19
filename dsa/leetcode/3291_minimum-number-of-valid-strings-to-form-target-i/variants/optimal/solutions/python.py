class TrieNode:
    def __init__(self):
        self.children = {}

def solve(words: list[str], target: str) -> int:
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            
    n = len(target)
    # dp[i] is the min strings to form target[0:i]
    # Initialize with infinity
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(n):
        if dp[i] == float('inf'):
            continue
            
        # From index i, find all possible valid substrings starting at target[i]
        node = root
        for j in range(i, n):
            if target[j] in node.children:
                node = node.children[target[j]]
                dp[j + 1] = min(dp[j + 1], dp[i] + 1)
            else:
                break
                
    return dp[n] if dp[n] != float('inf') else -1
