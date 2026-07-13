# Minimum Index of a Valid Split

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2780 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-index-of-a-valid-split](https://leetcode.com/problems/minimum-index-of-a-valid-split/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-index-of-a-valid-split/).

### Goal
Given an array of integers `nums`, find the smallest index `i` (where `0 <= i < len(nums) - 1`) such that splitting the array into two non-empty subarrays, `nums[0...i]` and `nums[i+1...len(nums)-1]`, results in both subarrays having the same dominant element. A dominant element in an array is an integer that appears strictly more than half the time in that array. If no such split index exists, return -1.

### Function Contract
**Inputs**

- `nums`: `List[int]` - An array of integers.

**Return value**

- `int` - The minimum index `i` that forms a valid split, or -1 if no such index exists.

### Examples
**Example 1**

- Input: `nums = [2,1,3,1,1,1,7,1,2,1]`
- Output: `4`
- Explanation: The dominant element of the entire array is `1` (appears 7 times in an array of length 10).
  - For `i = 4`:
    - Left part: `[2,1,3,1,1]` (length 5). `1` appears 3 times, which is `3 > 5/2`. So `1` is dominant.
    - Right part: `[1,7,1,2,1]` (length 5). `1` appears 3 times, which is `3 > 5/2`. So `1` is dominant.
  - Since `1` is dominant in both parts, `i = 4` is a valid split. It's the smallest such index.

**Example 2**

- Input: `nums = [3,3,3,3,7,3,3]`
- Output: `0`
- Explanation: The dominant element of the entire array is `3` (appears 6 times in an array of length 7).
  - For `i = 0`:
    - Left part: `[3]` (length 1). `3` appears 1 time, which is `1 > 1/2`. So `3` is dominant.
    - Right part: `[3,3,3,7,3,3]` (length 6). `3` appears 5 times, which is `5 > 6/2`. So `3` is dominant.
  - Since `3` is dominant in both parts, `i = 0` is a valid split. It's the smallest such index.

**Example 3**

- Input: `nums = [1,2,3,4,5]`
- Output: `-1`
- Explanation: No element appears more than `len(nums)/2` times in the entire array. Therefore, no global dominant element exists, and no valid split can be formed.

---

## Solution
### Approach
The solution leverages the following concepts:

1.  **Boyer-Moore Voting Algorithm**: This algorithm is used to efficiently find a candidate for the majority element (an element that appears more than `N/2` times) in an array in O(N) time and O(1) space. It works by maintaining a `candidate` and a `count`. When iterating through the array, if the current element matches the `candidate`, the `count` is incremented; otherwise, it's decremented. If `count` drops to 0, a new `candidate` is chosen.
2.  **Prefix Sum / Running Count**: After identifying a potential global dominant element, we need to verify if it is indeed dominant in the entire array. If it is, we then iterate through all possible split points `i`. For each `i`, we maintain a running count of the global dominant element in the left subarray `nums[0...i]`. The count for the right subarray `nums[i+1...n-1]` can then be derived by subtracting the left count from the total count of the global dominant element. This allows for O(1) checks at each split point.

The core idea is that if a split is valid, both subarrays must share the *same* dominant element. This shared dominant element must also be the dominant element of the *entire* array. If the entire array does not have a dominant element, then no valid split can exist.

### Complexity Analysis
- **Time Complexity**: `O(N)`
    - First pass: `O(N)` to find a candidate for the global dominant element using Boyer-Moore Voting Algorithm.
    - Second pass: `O(N)` to verify the candidate and count its total occurrences in the array.
    - Third pass: `O(N)` to iterate through all possible split points `i` (from `0` to `N-2`). Inside the loop, calculations for left and right subarray counts and lengths are `O(1)`.
    - Total time complexity is dominated by these linear passes, resulting in `O(N)`.
- **Space Complexity**: `O(1)`
    - The Boyer-Moore Voting Algorithm uses constant extra space.
    - The subsequent passes only require a few variables to store counts and lengths, also consuming constant extra space.
    - Therefore, the overall space complexity is `O(1)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return -1

    # Step 1: Find a candidate for the dominant element of the entire array
    # using Boyer-Moore Voting Algorithm.
    candidate = -1
    count = 0
    for x in nums:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1

    # Step 2: Verify if the candidate is truly dominant and get its total count.
    # If the candidate is not dominant in the entire array, no valid split is possible.
    global_dominant_count = 0
    for x in nums:
        if x == candidate:
            global_dominant_count += 1

    if global_dominant_count * 2 <= n:
        return -1 # No dominant element in the entire array

    global_dominant = candidate

    # Step 3: Iterate through all possible split points (i from 0 to n-2).
    # Maintain the count of the global_dominant in the left subarray.
    left_dominant_count = 0
    for i in range(n - 1):
        # Update count for the left subarray
        if nums[i] == global_dominant:
            left_dominant_count += 1

        # Calculate lengths of left and right subarrays
        left_len = i + 1
        right_len = n - left_len

        # Calculate count of global_dominant in the right subarray
        right_dominant_count = global_dominant_count - left_dominant_count

        # Check if global_dominant is dominant in both subarrays
        is_left_dominant = (left_dominant_count * 2 > left_len)
        is_right_dominant = (right_dominant_count * 2 > right_len)

        if is_left_dominant and is_right_dominant:
            return i # Found the smallest valid split index

    # If no valid split is found after checking all possible indices
    return -1
```
</details>
