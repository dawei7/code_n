# Number of Ways to Reach a Position After Exactly k Steps

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2400 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/) |

## Problem Description

### Goal

Begin at `startPos` on an infinite integer number line. Every step moves
exactly one position: either one unit left or one unit right. Positions below
zero are part of the line and may be visited.

Count the different ordered sequences of exactly `k` steps that finish at
`endPos`. Two ways differ when their left/right step orders differ, even if
they visit some of the same positions. Because the count can be large, return
it modulo $10^9+7$.

### Function Contract

**Inputs**

- `startPos`: The positive starting coordinate.
- `endPos`: The positive required final coordinate.
- `k`: The exact positive number of unit steps to perform.

Each input integer is between 1 and 1000 inclusive.

**Return value**

Return the number of length-`k` sequences over left and right moves whose net
displacement is `endPos - startPos`, reduced modulo $10^9+7$. Return `0` when
the requested displacement cannot be achieved in exactly `k` steps.

### Examples

**Example 1**

- Input: `startPos = 1`, `endPos = 2`, `k = 3`
- Output: `3`
- Explanation: Each valid sequence contains two right steps and one left step,
  and the left step can occupy any of three positions.

**Example 2**

- Input: `startPos = 2`, `endPos = 5`, `k = 10`
- Output: `0`
- Explanation: The displacement is 3, whose parity differs from 10, so no
  exact-step sequence exists.

**Example 3**

- Input: `startPos = 5`, `endPos = 2`, `k = 5`
- Output: `5`
- Explanation: Reaching displacement $-3$ requires four left moves and one
  right move; the right move has five possible positions.
