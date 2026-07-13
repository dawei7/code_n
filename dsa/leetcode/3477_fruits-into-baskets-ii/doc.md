# Fruits Into Baskets II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3477 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search, Segment Tree, Simulation, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [fruits-into-baskets-ii](https://leetcode.com/problems/fruits-into-baskets-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/fruits-into-baskets-ii/).

### Goal
You are given a sequence of fruits with specific sizes and a sequence of baskets with specific capacities. Each fruit must be placed into a basket sequentially. For each fruit, you must find the first available basket that has a capacity greater than or equal to the fruit's size. Once a basket is used, it cannot be used again. The goal is to determine how many fruits can be successfully placed into baskets.

### Function Contract
**Inputs**

- `fruits`: A list of integers representing the sizes of the fruits in the order they appear.
- `baskets`: A list of integers representing the capacities of the baskets in the order they appear.

**Return value**

- An integer representing the total count of fruits that were successfully placed into a basket.

### Examples
**Example 1**

- Input: `fruits = [4, 2, 5], baskets = [3, 5, 4]`
- Output: `3`

**Example 2**

- Input: `fruits = [3, 6, 1], baskets = [6, 4, 7]`
- Output: `2`

**Example 3**

- Input: `fruits = [1, 2, 3], baskets = [1, 2, 3]`
- Output: `3`

---

## Solution
### Approach
The problem is a greedy simulation. For each fruit in the input order, we iterate through the available baskets from left to right. The first basket that satisfies the capacity requirement is marked as "used" (e.g., by setting its capacity to -1 or using a boolean tracking array) and the fruit is considered placed.

### Complexity Analysis
- **Time Complexity**: `O(N * M)`, where `N` is the number of fruits and `M` is the number of baskets. In the worst case, for each fruit, we may scan all baskets.
- **Space Complexity**: `O(1)` if we modify the input array in-place, or `O(M)` if we use an auxiliary boolean array to track basket availability.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(fruits: list[int], baskets: list[int]) -> int:
    placed = 0
    n = len(baskets)
    used = [False] * n

    for fruit in fruits:
        for i in range(n):
            if not used[i] and baskets[i] >= fruit:
                used[i] = True
                placed += 1
                break

    return n - placed
```
</details>
