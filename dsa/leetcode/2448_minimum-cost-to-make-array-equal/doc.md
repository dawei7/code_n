# Minimum Cost to Make Array Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2448 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-to-make-array-equal](https://leetcode.com/problems/minimum-cost-to-make-array-equal/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-to-make-array-equal/).

### Goal
Given two arrays representing values and their associated costs, determine the minimum total cost required to make all elements in the values array equal to a single target integer. The cost to change a value `nums[i]` to a target `x` is defined as `|nums[i] - x| * cost[i]`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the values to be equalized.
- `cost`: A list of integers representing the cost per unit of difference for each corresponding value in `nums`.

**Return value**

- An integer representing the minimum total cost to make all elements in `nums` equal.

### Examples
**Example 1**

- Input: `nums = [1,3,5,2], cost = [2,3,1,14]`
- Output: `8`

**Example 2**

- Input: `nums = [2,2,2,2,2], cost = [4,2,8,1,3]`
- Output: `0`

**Example 3**

- Input: `nums = [1,10], cost = [2,3]`
- Output: `18`

---

## Solution
### Approach
The problem is a variation of the "Weighted Median" problem. The total cost function is convex, meaning we can find the minimum using Ternary Search or by finding the weighted median of the values. Sorting the pairs by value allows us to use prefix sums to calculate the cost for any target value in O(1) time after O(N log N) preprocessing.

### Complexity Analysis
- **Time Complexity**: `O(N log N)` due to the sorting of the input arrays, where N is the number of elements. The subsequent search (binary or ternary) takes `O(N log(max(nums)))`.
- **Space Complexity**: `O(N)` to store the zipped pairs of values and costs.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], cost: list[int]) -> int:
    # Combine nums and cost, then sort by the value
    data = sorted(zip(nums, cost))
    n = len(data)

    # Calculate prefix sums of costs to compute total cost efficiently
    prefix_costs = [0] * (n + 1)
    for i in range(n):
        prefix_costs[i + 1] = prefix_costs[i] + data[i][1]

    total_cost_sum = prefix_costs[n]

    # The optimal target value is the weighted median
    median_weight = total_cost_sum / 2
    median_val = 0
    for i in range(n):
        if prefix_costs[i + 1] >= median_weight:
            median_val = data[i][0]
            break

    # Calculate total cost for the chosen median_val
    ans = 0
    for val, c in data:
        ans += abs(val - median_val) * c

    return ans
```
</details>
