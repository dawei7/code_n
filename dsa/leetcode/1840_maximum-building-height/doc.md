# Maximum Building Height

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1840 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-building-height](https://leetcode.com/problems/maximum-building-height/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-building-height/).

### Goal
There are buildings `1..n`; building `1` must have height `0`, adjacent buildings can differ by at most `1`, and some buildings have maximum height restrictions. Find the largest possible height of any building.

### Function Contract
**Inputs**

- `n`: the number of buildings.
- `restrictions`: a list of `[id, maxHeight]` constraints.

**Return value**

Return the maximum height achievable by any building while satisfying all rules.

### Examples
**Example 1**

- Input: `n = 5, restrictions = [[2,1],[4,1]]`
- Output: `2`

**Example 2**

- Input: `n = 6, restrictions = []`
- Output: `5`

**Example 3**

- Input: `n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]`
- Output: `5`

---

## Solution
### Approach
Add implicit restrictions for building `1` at height `0` and building `n` with a loose maximum, then sort by building id. Sweep left-to-right and right-to-left to tighten every restriction by the adjacent-difference rule. Between two restricted buildings, the tallest possible peak is reached by rising from one side and descending to the other; compute that peak for each interval.

### Complexity Analysis
- **Time Complexity**: `O(r log r)`
- **Space Complexity**: `O(r)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
