from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    # Map to store how many subarrays of length k contain a specific number
    count_map = defaultdict(int)
    n = len(nums)
    
    # Iterate through all possible subarrays of length k
    for i in range(n - k + 1):
        subarray = nums[i : i + k]
        # Use a set to ensure we only count the number once per subarray
        unique_elements = set(subarray)
        for val in unique_elements:
            count_map[val] += 1
            
    # Find the largest number that appeared in exactly one subarray
    max_val = -1
    for val, count in count_map.items():
        if count == 1:
            if val > max_val:
                max_val = val
                
    return max_val
