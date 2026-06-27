import heapq

def solve(nums, k, multiplier):
    if multiplier == 1:
        return [x % (10**9 + 7) for x in nums]
    
    MOD = 10**9 + 7
    n = len(nums)
    heap = [(nums[i], i) for i in range(n)]
    heapq.heapify(heap)
    
    max_val = max(nums)
    
    # Simulation phase: multiply until all elements are close to max_val
    while k > 0 and heap[0][0] * multiplier <= max_val:
        val, idx = heapq.heappop(heap)
        new_val = val * multiplier
        heapq.heappush(heap, (new_val, idx))
        k -= 1
        
    # Mathematical phase: distribute remaining k operations
    # Each element will be multiplied by multiplier^(k // n)
    # The first (k % n) elements will be multiplied by an additional multiplier
    full_rounds = k // n
    extra_ops = k % n
    
    multiplier_pow = pow(multiplier, full_rounds, MOD)
    
    final_res = [0] * n
    
    # Sort heap to process elements in order of their current values
    sorted_heap = sorted(heap)
    
    for i in range(n):
        val, idx = sorted_heap[i]
        # Apply extra multiplier to the first 'extra_ops' elements
        if i < extra_ops:
            final_res[idx] = (val % MOD * multiplier_pow % MOD * multiplier % MOD) % MOD
        else:
            final_res[idx] = (val % MOD * multiplier_pow % MOD) % MOD
            
    return final_res
