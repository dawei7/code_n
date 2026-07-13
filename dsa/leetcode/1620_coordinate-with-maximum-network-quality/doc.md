# Coordinate With Maximum Network Quality

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1620 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [coordinate-with-maximum-network-quality](https://leetcode.com/problems/coordinate-with-maximum-network-quality/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/coordinate-with-maximum-network-quality/).

### Goal
Find the integer coordinate with the highest total signal quality from towers
within a given radius. Break ties by choosing the lexicographically smallest
coordinate.

### Function Contract
**Inputs**

- `towers`: entries `[x, y, quality]`.
- `radius`: maximum distance at which a tower contributes signal.

**Return value**

The best coordinate as `[x, y]`.

### Examples
**Example 1**

- Input: `towers = [[1, 2, 5], [2, 1, 7], [3, 1, 9]], radius = 2`
- Output: `[2, 1]`

**Example 2**

- Input: `towers = [[23, 11, 21]], radius = 9`
- Output: `[23, 11]`

**Example 3**

- Input: `towers = [[1, 2, 13], [2, 1, 7], [0, 1, 9]], radius = 2`
- Output: `[1, 2]`

---

## Solution
### Approach
The coordinate range is small enough to brute force all candidate integer
coordinates inside the bounding box of the towers. For each candidate, sum
`floor(q / (1 + distance))` for every tower whose Euclidean distance is within
`radius`, then keep the best quality and lexicographically smallest coordinate.

### Complexity Analysis
- **Time Complexity**: `O(A * T)`, where `A` is the number of candidate coordinates and `T` is the number of towers.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
