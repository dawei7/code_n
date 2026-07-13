from collections import defaultdict

def solve(nums: list[int]) -> int:
    """
    The condition XOR(nums[i...j-1]) == XOR(nums[j...k])
    Let P[x] be the prefix XOR sum: P[x] = nums[0] ^ ... ^ nums[x-1]
    The condition is: (P[j] ^ P[i]) == (P[k+1] ^ P[j])
    This simplifies to: P[i] == P[k+1]
    
    For a fixed pair (i, m) where m = k+1 and P[i] == P[m],
    any j such that i < j < m is a valid split point.
    The number of such j's is (m - i - 1).
    
    We need to sum (m - i - 1) for all pairs (i, m) with i < m and P[i] == P[m].
    Sum = sum(m - i - 1) = sum(m) - sum(i) - count
    """
    n = len(nums)
    prefix_xor = [0] * (n + 1)
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ nums[i]
    
    # Store indices for each prefix XOR value
    val_to_indices = defaultdict(list)
    for idx, val in enumerate(prefix_xor):
        val_to_indices[val].append(idx)
        
    total_triplets = 0
    for val in val_to_indices:
        indices = val_to_indices[val]
        # For a list of indices [i1, i2, ..., im] where P[ix] are equal:
        # We want sum_{a < b} (indices[b] - indices[a] - 1)
        # = sum_{a < b} (indices[b] - indices[a]) - (number of pairs)
        # Let count = k. Number of pairs is k*(k-1)/2.
        # sum_{a < b} (indices[b] - indices[a]) = sum_{b=0 to k-1} (b * indices[b] - (k-1-b) * indices[b])
        # = sum_{b=0 to k-1} (2*b - k + 1) * indices[b]
        
        k = len(indices)
        if k < 2:
            continue
            
        sum_diff = 0
        for b in range(k):
            sum_diff += (2 * b - k + 1) * indices[b]
            
        num_pairs = k * (k - 1) // 2
        total_triplets += (sum_diff - num_pairs)
        
    return total_triplets
