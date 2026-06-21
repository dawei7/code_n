"""Solution for nc_1: Concatenation of Array.

Given an integer array `nums` of length `n`, return the concatenation of `nums` with itself.

## Example
```
Input:  nums = [1, 2, 1]
Output: [1, 2, 1, 1, 2, 1]
```

## GeeksforGeeks Reference
[Python list concatenation](https://www.geeksforgeeks.org/python-list-operations/)

Inputs passed to solve():
    nums: List[int]

Goal:
    List[int] of length 2n

Samples:
Sample 1 input:  nums = [1,2,1]
Sample 1 output: [1,2,1,1,2,1]


"""

def solve(nums):
    # Write your code here.
    return nums+nums
