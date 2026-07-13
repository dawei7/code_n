# Maximum Product After K Increments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2233 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-product-after-k-increments](https://leetcode.com/problems/maximum-product-after-k-increments/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-product-after-k-increments/).

### Goal
Perform exactly `k` operations, each increasing one array value by one. Maximize the final product and return it modulo `1,000,000,007`.

### Function Contract
**Inputs**

- `nums`: a list of nonnegative integers.
- `k`: the exact number of unit increments.

**Return value**

The maximum possible product modulo `1,000,000,007`.

### Examples
**Example 1**

- Input: `nums = [0, 4]`, `k = 5`
- Output: `20`

**Example 2**

- Input: `nums = [6, 3, 3, 2]`, `k = 2`
- Output: `216`

**Example 3**

- Input: `nums = [1]`, `k = 3`
- Output: `4`

---

## Solution
### Approach
Put all values in a min-heap. Repeatedly remove the smallest value, increment it, and push it back. Equalizing the smallest factors maximizes the product for a fixed increment budget. After all operations, multiply heap values modulo the required constant.

### Complexity Analysis
- **Time Complexity**: `O((n + k) log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
