# Count Total Number of Colored Cells

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2579 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Count Total Number of Colored Cells](https://leetcode.com/problems/count-total-number-of-colored-cells/) |

## Problem Description

### Goal

Consider an infinite two-dimensional grid of initially uncolored unit cells. A coloring process runs for `n` minutes.

During minute $1$, any single cell is colored blue. During every later minute, every uncolored cell that shares a side with a blue cell is also colored blue. Previously colored cells remain blue.

Return the total number of blue cells after minute `n`.

### Function Contract

**Inputs**

- `n`: The positive number of minutes for which the process runs, with $1 \leq n \leq 10^5$.

**Return value**

- The total number of colored cells after `n` minutes.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `1`
- Explanation: Only the initially chosen cell is blue.

**Example 2**

- Input: `n = 2`
- Output: `5`
- Explanation: The center cell and its four side-adjacent neighbors are blue.
