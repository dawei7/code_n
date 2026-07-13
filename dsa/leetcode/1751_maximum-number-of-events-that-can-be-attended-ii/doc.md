# Maximum Number of Events That Can Be Attended II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1751 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-events-that-can-be-attended-ii](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/).

### Goal
Each event has a start day, end day, and value. Attend at most `k` non-overlapping events and maximize the total value.

### Function Contract
**Inputs**

- `events`: a list of `[start, end, value]` triples.
- `k`: the maximum number of events that may be attended.

**Return value**

Return the maximum total value obtainable.

### Examples
**Example 1**

- Input: `events = [[1,2,4],[3,4,3],[2,3,1]], k = 2`
- Output: `7`

**Example 2**

- Input: `events = [[1,2,4],[3,4,3],[2,3,10]], k = 2`
- Output: `10`

**Example 3**

- Input: `events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3`
- Output: `9`

---

## Solution
### Approach
Sort events by start day. Use DP where `dp(i, remaining)` is the best value starting from event index `i` with `remaining` choices left. Either skip event `i`, or take it and jump by binary search to the first event whose start day is after `events[i].end`.

### Complexity Analysis
- **Time Complexity**: `O(n * k * log n)` with memoized binary-search transitions
- **Space Complexity**: `O(n * k)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
