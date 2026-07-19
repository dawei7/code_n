from collections import Counter

def solve(nums: list[int], k: int, x: int) -> list[int]:
    """
    Calculates the X-sum for every contiguous subarray of length k.
    """
    n = len(nums)
    results = []
    
    # Iterate through every possible window of size k
    for i in range(n - k + 1):
        window = nums[i : i + k]
        counts = Counter(window)
        
        # Convert counts to a list of (frequency, value) tuples
        # We want to sort by frequency descending, then by value descending
        freq_list = [(freq, val) for val, freq in counts.items()]
        
        # Sort based on the problem criteria:
        # 1. Frequency (descending)
        # 2. Value (descending)
        freq_list.sort(key=lambda item: (item[0], item[1]), reverse=True)
        
        # Take the top x elements
        top_x = freq_list[:x]
        
        # Calculate the sum of these elements (frequency * value)
        current_x_sum = sum(freq * val for freq, val in top_x)
        results.append(current_x_sum)
        
    return results
