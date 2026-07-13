def solve(nums: list[int], k: int, x: int) -> list[int]:
    # The range of values is [-50, 50]. 
    # We map these to indices [0, 100] by adding 50.
    freq = [0] * 101
    
    def get_xth_smallest(x):
        count = 0
        for i in range(50):  # Only consider negative numbers (indices 0 to 49)
            count += freq[i]
            if count >= x:
                return i - 50
        return 0

    res = []
    # Initialize the first window
    for i in range(k):
        freq[nums[i] + 50] += 1
        
    res.append(get_xth_smallest(x))
    
    # Slide the window
    for i in range(k, len(nums)):
        # Remove the element sliding out
        freq[nums[i - k] + 50] -= 1
        # Add the element sliding in
        freq[nums[i] + 50] += 1
        
        res.append(get_xth_smallest(x))
        
    return res
