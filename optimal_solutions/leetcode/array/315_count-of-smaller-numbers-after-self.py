def solve(nums: list[int]) -> list[int]:
    # Coordinate compression to handle negative numbers and large ranges
    sorted_unique = sorted(list(set(nums)))
    ranks = {val: i + 1 for i, val in enumerate(sorted_unique)}
    
    n = len(nums)
    bit = [0] * (len(sorted_unique) + 1)
    
    def update(i, delta):
        while i < len(bit):
            bit[i] += delta
            i += i & (-i)
            
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s
    
    result = [0] * n
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        rank = ranks[nums[i]]
        # Count elements strictly smaller than current
        result[i] = query(rank - 1)
        # Add current element to BIT
        update(rank, 1)
        
    return result
