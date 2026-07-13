from collections import defaultdict

def solve(nums: list[int]) -> int:
    """
    Calculates the number of beautiful subarrays using the prefix XOR property.
    A subarray nums[i:j+1] has an XOR sum of 0 if prefix_xor[j] == prefix_xor[i-1].
    """
    count = 0
    current_xor = 0
    # Map to store the frequency of prefix XOR sums encountered.
    # Initialize with 0: 1 to handle subarrays starting from index 0.
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1
    
    for num in nums:
        current_xor ^= num
        # If this XOR sum has been seen before, every previous occurrence
        # marks the start of a beautiful subarray ending at the current index.
        count += prefix_counts[current_xor]
        prefix_counts[current_xor] += 1
        
    return count
