# Append K Integers With Minimal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2195 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [append-k-integers-with-minimal-sum](https://leetcode.com/problems/append-k-integers-with-minimal-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/append-k-integers-with-minimal-sum/).

### Goal
Choose exactly `k` distinct positive integers absent from `nums` so their sum is as small as possible, and return that minimum sum.

### Function Contract
**Inputs**

- `nums`: positive integers whose values cannot be appended.
- `k`: the number of distinct values to choose.

**Return value**

The minimum possible sum of the chosen integers.

### Examples
**Example 1**

- Input: `nums = [1, 4, 25, 10, 25]`, `k = 2`
- Output: `5`

**Example 2**

- Input: `nums = [5, 6]`, `k = 6`
- Output: `25`

**Example 3**

- Input: `nums = [1, 2, 3]`, `k = 2`
- Output: `9`

---

## Solution
### Approach
Sort and deduplicate `nums`. Starting with the next candidate `1`, consume gaps before each forbidden value. For a gap, take as many of its smallest values as still needed and add their arithmetic-series sum in constant time. If values remain to choose after all forbidden numbers, take the next consecutive range.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` when deduplicating, or `O(1)` auxiliary space with in-place sorting and duplicate skipping

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
