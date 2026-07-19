from typing import List

def solve(nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
    # Pair up nums1 and nums2 and sort them by nums1 descending
    pairs = sorted(zip(nums1, nums2), key=lambda x: x[0], reverse=True)
    
    # Sort queries by xi descending, keeping track of original indices
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][0], reverse=True)
    
    ans = [-1] * len(queries)
    stack = []  # Will store tuples of (y, x + y)
    pair_idx = 0
    n = len(pairs)
    
    for q_idx, (xi, yi) in sorted_queries:
        # Add all pairs with x >= xi to the monotonic stack
        while pair_idx < n and pairs[pair_idx][0] >= xi:
            x, y = pairs[pair_idx]
            val = x + y
            # Maintain monotonic stack: y ascending, val descending
            while stack and stack[-1][1] <= val:
                stack.pop()
            if not stack or stack[-1][0] < y:
                stack.append((y, val))
            pair_idx += 1
            
        # Binary search for the first element in stack with y >= yi
        low = 0
        high = len(stack) - 1
        best_val = -1
        while low <= high:
            mid = (low + high) // 2
            if stack[mid][0] >= yi:
                best_val = stack[mid][1]
                high = mid - 1
            else:
                low = mid + 1
        ans[q_idx] = best_val
        
    return ans
