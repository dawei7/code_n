class TrieNode:
    def __init__(self):
        self.children = {}

def insert(root, val):
    node = root
    for i in range(31, -1, -1):
        bit = (val >> i) & 1
        if bit not in node.children:
            node.children[bit] = TrieNode()
        node = node.children[bit]

def query(root, val):
    node = root
    res = 0
    for i in range(31, -1, -1):
        bit = (val >> i) & 1
        target = 1 - bit
        if target in node.children:
            res |= (1 << i)
            node = node.children[target]
        else:
            node = node.children.get(bit, node)
    return res

def solve(nums: list[int]) -> int:
    root = TrieNode()
    insert(root, 0)
    
    max_xor = 0
    current_prefix = 0
    
    for num in nums:
        current_prefix ^= num
        insert(root, current_prefix)
        max_xor = max(max_xor, query(root, current_prefix))
        
    return max_xor
