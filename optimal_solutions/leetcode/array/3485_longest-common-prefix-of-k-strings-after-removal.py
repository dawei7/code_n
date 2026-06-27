def solve(strs: list[str], k: int) -> int:
    # The problem asks for the longest common prefix shared by at least k strings
    # allowing one deletion per string.
    # We can model this as a Trie where each node tracks:
    # count0: number of strings reaching this node without any deletions
    # count1: number of strings reaching this node with exactly one deletion
    
    trie = {}
    
    for s in strs:
        # State: (node, has_deleted)
        # We use a set to avoid double counting the same string at the same node
        visited = set()
        
        def insert(idx, node, deleted):
            if (id(node), deleted) in visited:
                return
            visited.add((id(node), deleted))
            
            # If we haven't deleted yet, we have two choices:
            # 1. Keep current char: move to child
            # 2. Delete current char: stay at current node, move to next index
            
            if not deleted:
                # Option: Delete current char
                if idx < len(s):
                    insert(idx + 1, node, True)
                
                # Option: Keep current char
                if idx < len(s):
                    char = s[idx]
                    if char not in node:
                        node[char] = {'count0': 0, 'count1': 0}
                    node[char]['count0'] += 1
                    insert(idx + 1, node[char], False)
            else:
                # Already deleted, must keep current char
                if idx < len(s):
                    char = s[idx]
                    if char not in node:
                        node[char] = {'count0': 0, 'count1': 0}
                    node[char]['count1'] += 1
                    insert(idx + 1, node[char], True)

        insert(0, trie, False)

    max_len = 0
    
    def find_max(node, depth):
        nonlocal max_len
        # Check if this node is valid for at least k strings
        # A string reaches here if it's in count0 or count1
        total = node.get('count0', 0) + node.get('count1', 0)
        if total >= k:
            max_len = max(max_len, depth)
            for char in node:
                if char not in ('count0', 'count1'):
                    find_max(node[char], depth + 1)
                    
    find_max(trie, 0)
    return max_len
