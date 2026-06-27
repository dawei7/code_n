from typing import List

def solve(nums: List[int]) -> None:
    """
    Rearranges the input list in-place to satisfy the wiggle sort condition:
    nums[0] < nums[1] > nums[2] < nums[3]...
    """
    # Create a sorted copy of the array
    sorted_nums = sorted(nums)
    n = len(nums)
    
    # We split the sorted array into two halves.
    # To avoid collisions of identical elements, we fill the odd indices
    # first with the larger half, then the even indices with the smaller half.
    # We fill both in reverse order to ensure the largest elements are 
    # separated by smaller elements.
    
    # Small half: 0 to (n-1)//2
    # Large half: (n-1)//2 + 1 to n-1
    
    # Pointer to the end of the sorted array
    mid = (n - 1) // 2
    
    # Fill odd indices (1, 3, 5...) with the largest elements
    # Fill even indices (0, 2, 4...) with the smallest elements
    nums[1::2] = sorted_nums[mid + 1:][::-1]
    nums[0::2] = sorted_nums[:mid + 1][::-1]
