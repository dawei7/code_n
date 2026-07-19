# Maximum Performance of a Team

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1383 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/maximum-performance-of-a-team/) |

## Problem Description

### Goal

There are `n` engineers. Engineer `i` has speed `speed[i]` and efficiency `efficiency[i]`. Choose a nonempty team containing at most `k` engineers.

A team's performance is the sum of its members' speeds multiplied by the minimum efficiency among those members. Find the greatest performance obtainable from any allowed team, then return that maximum modulo $1{,}000{,}000{,}007$.

Every selected engineer contributes speed to the sum.

### Function Contract

**Inputs**

- `n`: the number of engineers.
- `speed`: an array of `n` positive engineer speeds.
- `efficiency`: an array of `n` positive engineer efficiencies.
- `k`: the maximum number of engineers that may be selected, with $1 \le k \le n$.

**Return value**

- The maximum raw team performance reduced modulo $1{,}000{,}000{,}007$.

### Examples

**Example 1**

- Input: `n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2`
- Output: `60`

**Example 2**

- Input: `n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3`
- Output: `68`

**Example 3**

- Input: `n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4`
- Output: `72`
