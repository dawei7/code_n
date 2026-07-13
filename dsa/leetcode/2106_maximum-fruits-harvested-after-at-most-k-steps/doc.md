# Maximum Fruits Harvested After at Most K Steps

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2106 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-fruits-harvested-after-at-most-k-steps](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/).

### Goal
Fruit piles lie at positions on a number line. Starting at `startPos`, walk at most `k` steps and collect every visited pile; maximize collected fruit.

### Function Contract
**Inputs**

- `fruits`: sorted pairs `[position, amount]`.
- `startPos`: starting coordinate.
- `k`: maximum walking distance.

**Return value**

Return the maximum fruit that can be harvested.

### Examples
**Example 1**

- Input: `fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4`
- Output: `9`

**Example 2**

- Input: `fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4`
- Output: `14`

**Example 3**

- Input: `fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2`
- Output: `0`

---

## Solution
### Approach
Any useful route covers a contiguous interval of fruit positions and changes direction at most once. Use a sliding window over intervals; for endpoints `left` and `right`, compute the minimum steps needed by trying left-first and right-first routes, and keep windows whose cost is at most `k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` beyond input/prefix data.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
