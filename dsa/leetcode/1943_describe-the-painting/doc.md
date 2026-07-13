# Describe the Painting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1943 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [describe-the-painting](https://leetcode.com/problems/describe-the-painting/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/describe-the-painting/).

### Goal
Colored half-open segments are painted on a number line. Split the painted portion into maximal intervals where the sum of active color values is constant.

### Function Contract
**Inputs**

- `segments`: entries `[start, end, color]`.

**Return value**

Return intervals `[start, end, mixedColor]` for every non-empty painted stretch.

### Examples
**Example 1**

- Input: `segments = [[1,4,5],[4,7,7],[1,7,9]]`
- Output: `[[1,4,14],[4,7,16]]`

**Example 2**

- Input: `segments = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]`
- Output: `[[1,4,12],[4,7,12]]`

**Example 3**

- Input: `segments = [[1,10,5],[2,3,10]]`
- Output: `[[1,2,5],[2,3,15],[3,10,5]]`

---

## Solution
### Approach
Use a difference map: add each color at `start` and subtract it at `end`. Sweep sorted coordinates while carrying the active sum; the span from the previous coordinate to the current one is emitted when the carried sum is positive.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
