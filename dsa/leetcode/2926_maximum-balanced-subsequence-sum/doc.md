# Maximum Balanced Subsequence Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2926 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-balanced-subsequence-sum](https://leetcode.com/problems/maximum-balanced-subsequence-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-balanced-subsequence-sum/).

### Goal
Given an array of integers `nums`, identify a subsequence such that for any two elements at indices `i` and `j` (where `i < j`), the condition `nums[j] - nums[i] >= j - i` holds. The objective is to find the maximum possible sum of elements in such a "balanced" subsequence.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input sequence.

**Return value**

- An integer representing the maximum sum of a balanced subsequence.

### Examples
**Example 1**

- Input: `nums = [3, 3, 5, 6]`
- Output: `14`
- Explanation: The subsequence `[3, 5, 6]` is balanced. Sum = 14.

**Example 2**

- Input: `nums = [5, -1, -3, 8]`
- Output: `13`
- Explanation: The subsequence `[5, 8]` is balanced. Sum = 13.

**Example 3**

- Input: `nums = [-2, -1]`
- Output: `-1`
- Explanation: The subsequence `[-1]` is balanced. Sum = -1.

---

## Solution
### Approach
The problem can be transformed by rearranging the condition `nums[j] - nums[i] >= j - i` into `nums[j] - j >= nums[i] - i`. By defining `b[i] = nums[i] - i`, the condition becomes `b[j] >= b[i]`. This is a variation of the Longest Increasing Subsequence problem, specifically finding the Maximum Weight Increasing Subsequence. We use coordinate compression on the values of `b[i]` combined with a Fenwick Tree (Binary Indexed Tree) to efficiently query the maximum prefix sum of balanced subsequences in $O(n \log n)$ time.

### Complexity Analysis
- **Time Complexity**: $O(n \log n)$, where $n$ is the length of the input array, due to sorting for coordinate compression and $n$ operations on the Fenwick Tree.
- **Space Complexity**: $O(n)$ to store the Fenwick Tree and the coordinate mapping.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    # Transform the condition: nums[j] - nums[i] >= j - i
    # nums[j] - j >= nums[i] - i
    # Let b[i] = nums[i] - i. We want to find a subsequence with non-decreasing b[i]
    # that maximizes the sum of nums[i].

    n = len(nums)
    b = [nums[i] - i for i in range(n)]

    # Coordinate compression for b values
    sorted_b = sorted(list(set(b)))
    rank = {val: i + 1 for i, val in enumerate(sorted_b)}

    # Fenwick Tree to store the maximum sum for a given rank
    # bit[i] stores the max sum of a balanced subsequence ending with a value of rank i
    bit = [0] * (len(sorted_b) + 1)

    def update(idx, val):
        while idx < len(bit):
            bit[idx] = max(bit[idx], val)
            idx += idx & (-idx)

    def query(idx):
        res = 0
        while idx > 0:
            res = max(res, bit[idx])
            idx -= idx & (-idx)
        return res

    max_total_sum = float('-inf')

    for i in range(n):
        r = rank[b[i]]
        # Current max sum ending at this b[i] is nums[i] + max sum of previous elements with b[j] <= b[i]
        # We only add nums[i] if it improves the sum (or if it's the first element)
        prev_max = query(r)
        current_sum = max(nums[i], prev_max + nums[i])

        update(r, current_sum)
        max_total_sum = max(max_total_sum, current_sum)

    return max_total_sum
```
</details>
