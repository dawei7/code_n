class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

def insert(root, num):
    node = root
    for i in range(19, -1, -1):
        bit = (num >> i) & 1
        if not node.children[bit]:
            node.children[bit] = TrieNode()
        node = node.children[bit]
        node.count += 1

def remove(root, num):
    node = root
    for i in range(19, -1, -1):
        bit = (num >> i) & 1
        node = node.children[bit]
        node.count -= 1

def get_max_xor(root, num):
    node = root
    res = 0
    for i in range(19, -1, -1):
        bit = (num >> i) & 1
        target = 1 - bit
        if node.children[target] and node.children[target].count > 0:
            res |= (1 << i)
            node = node.children[target]
        elif node.children[bit] and node.children[bit].count > 0:
            node = node.children[bit]
        else:
            return 0
    return res

def solve(nums):
    nums.sort()
    root = TrieNode()
    max_xor = 0
    left = 0
    
    for right in range(len(nums)):
        insert(root, nums[right])
        
        while nums[left] * 2 < nums[right]:
            remove(root, nums[left])
            left += 1
            
        max_xor = max(max_xor, get_max_xor(root, nums[right]))
        
    return max_xor
