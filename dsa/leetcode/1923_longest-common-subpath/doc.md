# Longest Common Subpath

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1923 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Rolling Hash, Suffix Array, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-common-subpath](https://leetcode.com/problems/longest-common-subpath/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-common-subpath/).

### Goal
Several paths through cities are given. Find the maximum length of a contiguous subpath that appears in every path.

### Function Contract
**Inputs**

- `n`: the number of cities.
- `paths`: a list of integer city paths.

**Return value**

Return the length of the longest common contiguous subpath.

### Examples
**Example 1**

- Input: `n = 5, paths = [[0,1,2,3,4],[2,3,4],[4,0,1,2,3]]`
- Output: `2`

**Example 2**

- Input: `n = 3, paths = [[0],[1],[2]]`
- Output: `0`

**Example 3**

- Input: `n = 5, paths = [[0,1,2,3,4],[4,3,2,1,0]]`
- Output: `1`

---

## Solution
### Approach
Binary search the subpath length. For a candidate length, compute rolling hashes of all subpaths of that length in each path, intersect the hash sets across paths, and check whether any hash remains. Double hashing or collision-aware verification is used in robust implementations.

### Complexity Analysis
- **Time Complexity**: `O(total path length * log min_path_length)`
- **Space Complexity**: `O(total path length)` for candidate hash sets

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
