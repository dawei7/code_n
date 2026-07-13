# Maximum Unique Subarray Sum After Deletion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3487 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-unique-subarray-sum-after-deletion](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/).

### Goal
Given an array of integers, find the maximum possible sum of a subarray that contains only unique elements, with the added flexibility that you are permitted to delete exactly one element from the original array before selecting the subarray. If you choose not to delete any element, the problem reduces to finding the maximum sum of a subarray with unique elements.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.

**Return value**

- An integer representing the maximum sum achievable under the given constraints.

### Examples
**Example 1**

- Input: `nums = [4, 2, 4, 5, 6]`
- Output: `17`
- Explanation: Deleting the first '4' results in `[2, 4, 5, 6]`, which sums to 17.

**Example 2**

- Input: `nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]`
- Output: `8`
- Explanation: Deleting elements to form the subarray `[5, 2, 1]` yields the maximum sum.

**Example 3**

- Input: `nums = [1, 1, 1, 1]`
- Output: `1`
- Explanation: Deleting three '1's leaves a single '1'.

---

## Solution
### Approach
The problem is solved using a **Sliding Window (Two Pointers)** technique combined with a **Hash Set** to maintain the uniqueness of elements within the current window. To handle the "one deletion" constraint, we evaluate the maximum sum by considering the window state both with and without the deletion of a conflicting element.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. Each element is visited at most twice by the sliding window pointers.
- **Space Complexity**: `O(k)`, where `k` is the number of unique elements in the array, used to store the elements in the hash set.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    positives = {value for value in nums if value > 0}
    if positives:
        return sum(positives)
    return max(nums)
```
</details>
