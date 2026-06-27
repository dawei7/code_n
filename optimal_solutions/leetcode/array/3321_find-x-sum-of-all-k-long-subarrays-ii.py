def solve(nums: list[int], k: int, x: int) -> list[int]:
    from sortedcontainers import SortedList
    # We maintain two sets:
    # top_x: stores (frequency, value) for the top x elements
    # others: stores (frequency, value) for the remaining elements
    # We also maintain the current sum of elements in top_x
    
    freq = {}
    top_x = SortedList()
    others = SortedList()
    current_x_sum = 0
    
    def add(val):
        nonlocal current_x_sum
        old_f = freq.get(val, 0)
        new_f = old_f + 1
        freq[val] = new_f
        
        # Remove from whichever set it was in
        if (old_f, val) in top_x:
            top_x.remove((old_f, val))
            current_x_sum -= old_f * val
        elif (old_f, val) in others:
            others.remove((old_f, val))
            
        # Add to top_x initially
        top_x.add((new_f, val))
        current_x_sum += new_f * val
        
        # Rebalance
        if len(top_x) > x:
            moved = top_x.pop(0)
            current_x_sum -= moved[0] * moved[1]
            others.add(moved)
            
    def remove(val):
        nonlocal current_x_sum
        old_f = freq[val]
        new_f = old_f - 1
        freq[val] = new_f
        
        if (old_f, val) in top_x:
            top_x.remove((old_f, val))
            current_x_sum -= old_f * val
        else:
            others.remove((old_f, val))
            
        if new_f > 0:
            others.add((new_f, val))
            
        # Rebalance: if top_x is now smaller than x and others has elements, move one
        if len(top_x) < x and others:
            moved = others.pop()
            top_x.add(moved)
            current_x_sum += moved[0] * moved[1]

    res = []
    for i in range(len(nums)):
        add(nums[i])
        if i >= k:
            remove(nums[i - k])
        if i >= k - 1:
            res.append(current_x_sum)
            
    return res
