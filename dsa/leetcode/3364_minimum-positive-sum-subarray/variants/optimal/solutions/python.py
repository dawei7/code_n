def solve(nums: list[int], l: int, r: int) -> int:
    n = len(nums)
    # Create prefix sums to calculate subarray sums in O(1)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]
    
    min_pos_sum = float('inf')
    found = False
    
    # Iterate through all possible starting positions
    for i in range(n):
        # Iterate through all valid lengths from l to r
        for length in range(l, r + 1):
            if i + length <= n:
                current_sum = prefix_sums[i + length] - prefix_sums[i]
                if current_sum > 0:
                    if current_sum < min_pos_sum:
                        min_pos_sum = current_sum
                        found = True
            else:
                break
                
    return int(min_pos_sum) if found else -1
