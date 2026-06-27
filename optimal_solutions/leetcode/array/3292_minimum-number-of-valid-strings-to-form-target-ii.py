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
    # max_match[i] stores the length of the longest prefix of any word 
    # that matches target starting at index i
    max_match = [0] * n
    for i in range(n):
        node = root
        length = 0
        for j in range(i, n):
            if target[j] in node.children:
                node = node.children[target[j]]
                length += 1
            else:
                break
        max_match[i] = length
        
    # dp[i] is the min strings to form target[i:]
    # We use a greedy approach: at each step, jump as far as possible
    # This is equivalent to the Jump Game II problem
    count = 0
    curr_end = 0
    farthest = 0
    
    i = 0
    while i < n:
        # Update farthest reach from current position
        # We can reach any index j where j <= i + max_match[i]
        for j in range(i, min(i + max_match[i] + 1, n + 1)):
            if j < n:
                farthest = max(farthest, j + max_match[j])
            else:
                farthest = max(farthest, j)
        
        if farthest <= i:
            return -1
            
        count += 1
        i = farthest
        if i >= n:
            return count
            
    return count if i >= n else -1
