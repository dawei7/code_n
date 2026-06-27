from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    # Group the indices of each number
    pos_map = defaultdict(list)
    for i, num in enumerate(nums):
        pos_map[num].append(i)
    
    max_len = 0
    
    # For each number, find the longest window of indices
    # such that the number of gaps between them is <= k
    for val in pos_map:
        indices = pos_map[val]
        left = 0
        for right in range(len(indices)):
            # The number of elements to delete to make the subarray 
            # from indices[left] to indices[right] equal is:
            # (total distance between indices) - (number of elements in the window - 1)
            # which simplifies to: (indices[right] - indices[left]) - (right - left)
            while (indices[right] - indices[left]) - (right - left) > k:
                left += 1
            
            # The length of the equal subarray is the number of elements in the window
            max_len = max(max_len, right - left + 1)
            
    return max_len
