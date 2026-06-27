import math

def solve(queries):
    # The maximum coordinate is 50,000 as per problem constraints
    MAX_X = 50000
    
    # Segment tree nodes store:
    # max_gap: the longest gap in this range
    # pref: the gap starting from the left boundary of this range
    # suff: the gap ending at the right boundary of this range
    # size: the total length of the range
    tree_size = 1
    while tree_size <= MAX_X:
        tree_size *= 2
    
    max_gap = [0] * (2 * tree_size)
    pref = [0] * (2 * tree_size)
    suff = [0] * (2 * tree_size)
    
    def update(idx, val):
        idx += tree_size
        if val == 1: # Obstacle placed
            max_gap[idx] = pref[idx] = suff[idx] = 0
        else: # Empty space
            max_gap[idx] = pref[idx] = suff[idx] = 1
            
        idx //= 2
        while idx >= 1:
            left = 2 * idx
            right = 2 * idx + 1
            
            # Update pref
            pref[idx] = pref[left]
            if pref[left] == (tree_size >> (int(math.log2(left)))):
                pref[idx] = pref[left] + pref[right]
            
            # Update suff
            suff[idx] = suff[right]
            if suff[right] == (tree_size >> (int(math.log2(right)))):
                suff[idx] = suff[right] + suff[left]
            
            # Update max_gap
            max_gap[idx] = max(max_gap[left], max_gap[right], suff[left] + pref[right])
            idx //= 2

    def query(l, r):
        l += tree_size
        r += tree_size
        res_l, res_r = [], []
        while l <= r:
            if l % 2 == 1:
                res_l.append(l)
                l += 1
            if r % 2 == 0:
                res_r.append(r)
                r -= 1
            l //= 2
            r //= 2
        
        nodes = res_l + res_r[::-1]
        
        curr_max = 0
        curr_suff = 0
        
        for node in nodes:
            curr_max = max(curr_max, max_gap[node], curr_suff + pref[node])
            if pref[node] == (tree_size >> (int(math.log2(node)))):
                curr_suff += pref[node]
            else:
                curr_suff = suff[node]
        return curr_max

    # Initialize tree with 1s (all empty)
    for i in range(MAX_X + 1):
        update(i, 0)
        
    results = []
    for q in queries:
        if q[0] == 1:
            update(q[1], 1)
        else:
            x, sz = q[1], q[2]
            if query(0, x - 1) >= sz:
                results.append(True)
            else:
                results.append(False)
    return results
