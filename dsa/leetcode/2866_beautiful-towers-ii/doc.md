# Beautiful Towers II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2866 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [beautiful-towers-ii](https://leetcode.com/problems/beautiful-towers-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/beautiful-towers-ii/).

### Goal
Given an array of integers representing the maximum allowed heights of towers at each index, construct a "mountain" configuration. A mountain configuration is defined as a sequence of heights where there exists a peak index `i` such that heights increase up to `i` and decrease thereafter. The heights must satisfy the constraint that each tower `j` has a height `h[j] <= maxHeights[j]`. The objective is to find the maximum possible sum of heights for any valid mountain configuration.

### Function Contract
**Inputs**

- `maxHeights`: A list of integers representing the upper bound for the height of each tower.

**Return value**

- An integer representing the maximum possible sum of heights of a mountain-shaped configuration.

### Examples
**Example 1**

- Input: `maxHeights = [5, 3, 4, 1, 1]`
- Output: `13`

**Example 2**

- Input: `maxHeights = [6, 5, 3, 9, 2, 7]`
- Output: `22`

**Example 3**

- Input: `maxHeights = [3, 2, 5, 5, 2, 3]`
- Output: `18`

---

## Solution
### Approach
The problem is solved using a **Monotonic Stack**. By calculating the prefix sums of the maximum possible heights to the left of each index (where heights are non-decreasing) and the suffix sums to the right (where heights are non-increasing), we can determine the total sum for a peak at any index `i` in $O(1)$ time after $O(n)$ preprocessing. The monotonic stack helps find the nearest smaller element to the left and right efficiently.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of `maxHeights`. We perform a constant number of linear passes over the array using the stack.
- **Space Complexity**: $O(n)$ to store the prefix/suffix sum arrays and the monotonic stack.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(maxHeights: list[int]) -> int:
    n = len(maxHeights)

    def get_sums(arr):
        sums = [0] * n
        stack = []  # Stores indices
        current_sum = 0
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                prev_idx = stack[-1] if stack else -1
                # Remove the contribution of the popped element
                current_sum -= (idx - prev_idx) * arr[idx]

            # Add contribution of current element
            prev_idx = stack[-1] if stack else -1
            current_sum += (i - prev_idx) * arr[i]
            sums[i] = current_sum
            stack.append(i)
        return sums

    left_sums = get_sums(maxHeights)
    right_sums = get_sums(maxHeights[::-1])[::-1]

    max_total = 0
    for i in range(n):
        # Total sum = left_sum + right_sum - peak_height
        total = left_sums[i] + right_sums[i] - maxHeights[i]
        if total > max_total:
            max_total = total

    return max_total
```
</details>
