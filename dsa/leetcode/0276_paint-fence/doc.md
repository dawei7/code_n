# Paint Fence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 276 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/paint-fence/) |

## Problem Description
### Goal
Given `n` fence posts in a row and `k` available colors, assign one color to every post. The only restriction is that no run of three consecutive posts may all have the same color; two adjacent posts may share a color.

Return the number of distinct valid colorings, where choices at labeled post positions make arrangements different. Colors may be reused throughout the fence as long as the length-three restriction holds. Account for short fences where no triple exists and for small color counts that sharply limit later choices. The function returns the count rather than enumerating the color sequences.

### Function Contract
**Inputs**

- `n`: number of fence posts
- `k`: available colors

**Return value**

The number of valid colorings.

### Examples
**Example 1**

- Input: `n = 3, k = 2`
- Output: `6`

**Example 2**

- Input: `n = 1, k = 1`
- Output: `1`

**Example 3**

- Input: `n = 3, k = 1`
- Output: `0`
