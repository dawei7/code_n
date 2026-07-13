# Count Alternating Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3101 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-alternating-subarrays](https://leetcode.com/problems/count-alternating-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-alternating-subarrays/).

### Goal
Given a binary array, identify the total number of contiguous subarrays where no two adjacent elements are identical (i.e., the values alternate between 0 and 1).

### Function Contract
**Inputs**

- `nums`: A list of integers containing only 0s and 1s.

**Return value**

- An integer representing the total count of alternating subarrays.

### Examples
**Example 1**

- Input: `nums = [0, 1, 1, 1]`
- Output: `5`
- Explanation: The alternating subarrays are [0], [1], [1], [1], and [0, 1].

**Example 2**

- Input: `nums = [1, 0, 1, 0]`
- Output: `10`
- Explanation: Every contiguous subarray is alternating. For an array of length 4, the number of subarrays is 4*(4+1)/2 = 10.

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `3`
- Explanation: Only subarrays of length 1 are alternating.

---

## Solution
### Approach
The problem can be solved using a **Dynamic Programming** approach or a **Sliding Window/Greedy** counting technique. By iterating through the array, we maintain the length of the current "alternating chain" ending at the current index. If `nums[i] != nums[i-1]`, the chain length increases by 1; otherwise, it resets to 1. The total count is the sum of these chain lengths at each position.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass through the data.
- **Space Complexity**: `O(1)`, as we only store a few integer variables regardless of input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of alternating subarrays in O(n) time and O(1) space.
    """
    if not nums:
        return 0

    total_count = 0
    current_chain_length = 0

    for i in range(len(nums)):
        # If not the first element and current element differs from previous,
        # extend the current alternating chain.
        if i > 0 and nums[i] != nums[i - 1]:
            current_chain_length += 1
        else:
            # Otherwise, start a new chain of length 1.
            current_chain_length = 1

        # The number of alternating subarrays ending at index i is equal
        # to the length of the alternating chain ending at i.
        total_count += current_chain_length

    return total_count
```
</details>
