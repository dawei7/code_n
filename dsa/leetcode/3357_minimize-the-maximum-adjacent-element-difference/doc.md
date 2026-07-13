# Minimize the Maximum Adjacent Element Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3357 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimize-the-maximum-adjacent-element-difference](https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/).

### Goal
Given an array containing integers and placeholders represented by `-1`, choose one pair of positive integers `(x, y)`. Every `-1` must be replaced with either `x` or `y`. Minimize the maximum absolute difference between adjacent elements after all replacements.

### Function Contract
**Inputs**

- `nums`: A list of integers where `-1` represents a value that must be replaced by either of the two chosen values.

**Return value**

- An integer representing the minimum possible value for the maximum adjacent difference.

### Examples
**Example 1**

- Input: `nums = [1, 2, -1, 10, 8]`
- Output: `4`
- Explanation: Replacing -1 with 6 results in `[1, 2, 6, 10, 8]`. Differences are `|1-2|=1, |2-6|=4, |6-10|=4, |10-8|=2`. Max is 4.

**Example 2**

- Input: `nums = [-1, -1, -1]`
- Output: `0`
- Explanation: Choose `(4, 4)` and replace every missing value with `4`.

**Example 3**

- Input: `nums = [-1, 10, -1, 8]`
- Output: `1`
- Explanation: Choose `(11, 9)` and form `[11, 10, 9, 8]`.

---

## Solution
### Approach
The problem is solved using **Binary Search on the Answer**. Since the maximum difference is monotonic (if a difference $X$ is achievable, any $Y > X$ is also achievable), we search for the smallest $X$ in the range $[0, 10^9]$. For a fixed $X$, we use a **Greedy** approach to validate if it is possible to fill the -1s such that no adjacent difference exceeds $X$.

### Complexity Analysis
- **Time Complexity**: $O(N \log M)$, where $N$ is the length of the array and $M$ is the maximum possible value in the array ($10^9$). The binary search takes $\log M$ steps, and each check takes $O(N)$.
- **Space Complexity**: $O(N)$ to store the processed array or auxiliary structures during the validation check.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    max_fixed_gap = 0
    min_boundary = 10**9
    max_boundary = 0

    for left, right in zip(nums, nums[1:]):
        if (left == -1) != (right == -1):
            value = max(left, right)
            min_boundary = min(min_boundary, value)
            max_boundary = max(max_boundary, value)
        elif left != -1:
            max_fixed_gap = max(max_fixed_gap, abs(left - right))

    if max_boundary == 0:
        return max_fixed_gap

    def check_single_gap(a: int, b: int, limit: int, x: int, y: int) -> bool:
        return min(max(abs(a - x), abs(b - x)), max(abs(a - y), abs(b - y))) <= limit

    def check_multiple_gap(a: int, b: int, limit: int, x: int, y: int) -> bool:
        ax = abs(a - x)
        ay = abs(a - y)
        bx = abs(b - x)
        by = abs(b - y)
        xy = abs(x - y)
        return min(max(ax, bx), max(ay, by), max(ax, xy, by), max(ay, xy, bx)) <= limit

    def check_boundary_gap(value: int, limit: int, x: int, y: int) -> bool:
        return min(abs(value - x), abs(value - y)) <= limit

    def feasible(limit: int) -> bool:
        x = min_boundary + limit
        y = max_boundary - limit
        gap_length = 0
        previous = 0

        for value in nums:
            if value == -1:
                gap_length += 1
                continue
            if previous > 0 and gap_length > 0:
                if gap_length == 1 and not check_single_gap(previous, value, limit, x, y):
                    return False
                if gap_length > 1 and not check_multiple_gap(previous, value, limit, x, y):
                    return False
            previous = value
            gap_length = 0

        if nums[0] == -1:
            first = next((value for value in nums if value != -1), -1)
            if first != -1 and not check_boundary_gap(first, limit, x, y):
                return False

        if nums[-1] == -1:
            last = next((value for value in reversed(nums) if value != -1), -1)
            if last != -1 and not check_boundary_gap(last, limit, x, y):
                return False

        return True

    low = max_fixed_gap
    high = max(low, (max_boundary - min_boundary + 1) // 2)
    while low < high:
        mid = (low + high) // 2
        if feasible(mid):
            high = mid
        else:
            low = mid + 1

    return low
```
</details>
