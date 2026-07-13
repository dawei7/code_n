# Longest Happy String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1405 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-happy-string](https://leetcode.com/problems/longest-happy-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-happy-string/).

### Goal
Given integers `a`, `b`, `c` (counts of 'a', 'b', 'c'), return the longest string using those characters such that there are no three consecutive same characters.

### Function Contract
**Inputs**

- `a`: int - count of 'a'
- `b`: int - count of 'b'
- `c`: int - count of 'c'

**Return value**

str - longest happy string

### Examples
**Example 1**

- Input: `a = 1, b = 1, c = 7`
- Output: `"ccbccacc"`

**Example 2**

- Input: `a = 1, b = 1, c = 0`
- Output: `'ab'`

**Example 3**

- Input: `a = 0, b = 2, c = 0`
- Output: `'bb'`

---

## Solution
### Approach
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
