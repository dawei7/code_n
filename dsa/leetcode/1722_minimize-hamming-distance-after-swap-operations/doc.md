# Minimize Hamming Distance After Swap Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1722 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Union-Find |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimize-hamming-distance-after-swap-operations](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/).

### Goal
You may swap values in `source` along any allowed index pair, any number of times. Minimize the Hamming distance between `source` and `target`.

### Function Contract
**Inputs**

- `source`: the starting integer array.
- `target`: the desired integer array.
- `allowedSwaps`: pairs of indices that may be swapped transitively.

**Return value**

Return the minimum possible number of positions where `source[i] != target[i]`.

### Examples
**Example 1**

- Input: `source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]`
- Output: `1`

**Example 2**

- Input: `source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []`
- Output: `2`

**Example 3**

- Input: `source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]`
- Output: `0`

---

## Solution
### Approach
Use union-find to group indices connected by allowed swaps. Within each component, values can be permuted arbitrarily. Count source values per component, then scan target positions and match one available equal value when possible; unmatched positions contribute to the minimum distance.

### Complexity Analysis
- **Time Complexity**: `O(n + m alpha(n))`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
