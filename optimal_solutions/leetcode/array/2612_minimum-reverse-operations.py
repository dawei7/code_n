from collections import deque
from bisect import bisect_left

def solve(n, p, banned, k):
    banned_set = set(banned)
    # We maintain two sets of unvisited indices: one for even indices, one for odd.
    # This allows us to efficiently find indices reachable from a current position.
    from sortedcontainers import SortedList
    
    available = [SortedList(), SortedList()]
    for i in range(n):
        if i not in banned_set:
            available[i % 2].add(i)
            
    dist = [-1] * n
    dist[p] = 0
    available[p % 2].remove(p)
    
    queue = deque([p])
    
    while queue:
        curr = queue.popleft()
        
        # A reversal of length k starting at 'start' covers [start, start + k - 1].
        # The element at 'curr' moves to 'new_pos' = start + (start + k - 1) - curr
        # new_pos = 2 * start + k - 1 - curr
        # Therefore, 2 * start = new_pos + curr - k + 1
        # start = (new_pos + curr - k + 1) / 2
        
        # Bounds for start:
        # 1. start >= 0
        # 2. start <= n - k
        # 3. start <= curr
        # 4. start >= curr - k + 1
        
        l = max(0, curr - k + 1)
        r = min(n - k, curr)
        
        # The parity of new_pos is (k - 1 - curr) % 2
        target_parity = (k - 1 - curr) % 2
        
        # Find all indices in available[target_parity] that are reachable
        # new_pos = 2 * start + k - 1 - curr
        # Since l <= start <= r, then 2*l + k - 1 - curr <= new_pos <= 2*r + k - 1 - curr
        
        lower_bound = 2 * l + k - 1 - curr
        upper_bound = 2 * r + k - 1 - curr
        
        s = available[target_parity]
        idx = s.bisect_left(lower_bound)
        
        to_remove = []
        while idx < len(s) and s[idx] <= upper_bound:
            to_remove.append(s[idx])
            idx += 1
            
        for val in to_remove:
            dist[val] = dist[curr] + 1
            available[target_parity].remove(val)
            queue.append(val)
            
    return dist
