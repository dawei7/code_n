# Find the Distinct Difference Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2670 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-distinct-difference-array](https://leetcode.com/problems/find-the-distinct-difference-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-distinct-difference-array/).

### Goal
Given a 0-indexed integer array `nums`, construct a new array `diff` of the same length. For each index `i` in `nums`, `diff[i]` should be calculated as the number of distinct elements in the prefix subarray `nums[0...i]` minus the number of distinct elements in the suffix subarray `nums[i+1...n-1]`. An empty subarray is considered to have 0 distinct elements.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
  - `1 <= nums.length <= 50`
  - `0 <= nums[i] <= 50`

**Return value**

- A list of integers, `diff`, where `diff[i]` is the calculated difference for each corresponding index `i` in `nums`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5]`
- Output: `[-3, -1, 1, 3, 5]`
  - `i = 0`: `prefix = [1]` (1 distinct), `suffix = [2,3,4,5]` (4 distinct). `diff[0] = 1 - 4 = -3`.
  - `i = 1`: `prefix = [1,2]` (2 distinct), `suffix = [3,4,5]` (3 distinct). `diff[1] = 2 - 3 = -1`.
  - `i = 2`: `prefix = [1,2,3]` (3 distinct), `suffix = [4,5]` (2 distinct). `diff[2] = 3 - 2 = 1`.
  - `i = 3`: `prefix = [1,2,3,4]` (4 distinct), `suffix = [5]` (1 distinct). `diff[3] = 4 - 1 = 3`.
  - `i = 4`: `prefix = [1,2,3,4,5]` (5 distinct), `suffix = []` (0 distinct). `diff[4] = 5 - 0 = 5`.

**Example 2**

- Input: `nums = [3,2,3,4,2]`
- Output: `[-2, -1, 0, 2, 3]`
  - `i = 0`: `prefix = [3]` (1 distinct), `suffix = [2,3,4,2]` (3 distinct: {2,3,4}). `diff[0] = 1 - 3 = -2`.
  - `i = 1`: `prefix = [3,2]` (2 distinct: {2,3}), `suffix = [3,4,2]` (3 distinct: {2,3,4}). `diff[1] = 2 - 3 = -1`.
  - `i = 2`: `prefix = [3,2,3]` (2 distinct: {2,3}), `suffix = [4,2]` (2 distinct: {2,4}). `diff[2] = 2 - 2 = 0`.
  - `i = 3`: `prefix = [3,2,3,4]` (3 distinct: {2,3,4}), `suffix = [2]` (1 distinct: {2}). `diff[3] = 3 - 1 = 2`.
  - `i = 4`: `prefix = [3,2,3,4,2]` (3 distinct: {2,3,4}), `suffix = []` (0 distinct). `diff[4] = 3 - 0 = 3`.

**Example 3**

- Input: `nums = [1]`
- Output: `[1]`
  - `i = 0`: `prefix = [1]` (1 distinct), `suffix = []` (0 distinct). `diff[0] = 1 - 0 = 1`.

---

## Solution
### Approach
The core idea involves efficiently counting distinct elements within subarrays. This is best achieved using hash sets (or frequency maps). The problem can be solved by pre-calculating prefix distinct counts and suffix distinct counts in separate passes, then combining them.

1.  **Prefix Distinct Counts:** Iterate from left to right, maintaining a hash set of elements encountered so far. The size of the set at each step `i` gives the distinct count for `nums[0...i]`.
2.  **Suffix Distinct Counts:** Iterate from right to left, maintaining a hash set of elements encountered in the suffix. The size of the set *before* adding the current element `nums[i]` (or rather, the size of the set for `nums[i+1...n-1]`) gives the distinct count for the suffix starting after `i`.
3.  **Final Calculation:** Iterate through the array one last time, subtracting the pre-calculated suffix distinct count from the prefix distinct count for each index `i`.

### Complexity Analysis
- **Time Complexity**: `O(N)`
  - We perform two linear passes over the array: one to compute all prefix distinct counts and another to compute all suffix distinct counts. Each operation (adding to a hash set, checking its size) takes `O(1)` on average. A final linear pass is used to compute the differences. Therefore, the total time complexity is proportional to the length of the input array `N`.
- **Space Complexity**: `O(N)`
  - We use two auxiliary arrays (or lists) to store the prefix distinct counts and suffix distinct counts, each of size `N`. Additionally, two hash sets are used, which in the worst case might store all `N` distinct elements. Thus, the total space complexity is `O(N)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> List[int]:
    n = len(nums)
    if n == 0:
        return []

    # Step 1: Calculate prefix distinct counts
    prefix_distinct_counts = [0] * n
    seen_prefix = set()
    for i in range(n):
        seen_prefix.add(nums[i])
        prefix_distinct_counts[i] = len(seen_prefix)

    # Step 2: Calculate suffix distinct counts
    # suffix_distinct_counts[i] will store the number of distinct elements in nums[i+1...n-1]
    suffix_distinct_counts = [0] * n
    seen_suffix = set()
    for i in range(n - 1, -1, -1):
        # The distinct count for the suffix nums[i+1...n-1] is the current size of seen_suffix
        # before adding nums[i]
        suffix_distinct_counts[i] = len(seen_suffix)
        seen_suffix.add(nums[i])

    # Step 3: Calculate the difference array
    diff = [0] * n
    for i in range(n):
        diff[i] = prefix_distinct_counts[i] - suffix_distinct_counts[i]

    return diff
```
</details>
