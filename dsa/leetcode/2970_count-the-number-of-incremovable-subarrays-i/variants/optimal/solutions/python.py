def solve(nums: list[int]) -> int:
    """
    Counts the number of incremovable subarrays by checking every possible
    subarray [i, j] and verifying if the remaining elements are strictly increasing.
    """
    n = len(nums)
    count = 0
    
    def is_strictly_increasing(arr):
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True

    # Iterate over all possible start indices i
    for i in range(n):
        # Iterate over all possible end indices j (where j >= i)
        for j in range(i, n):
            # Construct the remaining array after removing nums[i...j]
            remaining = nums[:i] + nums[j + 1:]
            
            if is_strictly_increasing(remaining):
                count += 1
                
    return count
