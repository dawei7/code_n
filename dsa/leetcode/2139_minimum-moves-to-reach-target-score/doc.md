# Minimum Moves to Reach Target Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2139 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-moves-to-reach-target-score](https://leetcode.com/problems/minimum-moves-to-reach-target-score/) |

## Problem Description

### Goal

Begin a game with the integer `1` and reach the integer `target`. A move may
either increment the current value by one or double it. Incrementing is
unrestricted, but doubling may be used at most `maxDoubles` times.

The score must follow the chosen operations exactly: an increment changes
`x` to `x + 1`, whereas a double changes `x` to `2 * x`. The doubling limit is
an upper bound, so a valid strategy may leave some permitted doubles unused.

Return the minimum number of moves needed to obtain `target` exactly.

### Function Contract

**Inputs**

- `target`: The positive integer score that must be reached, where
  $1 \leq \texttt{target} \leq 10^9$.
- `maxDoubles`: The maximum permitted number of doubling moves, where
  $0 \leq \texttt{maxDoubles} \leq 100$.

**Return value**

Return the smallest number of increment and double moves that transform `1`
into `target` without exceeding the doubling limit.

### Examples

**Example 1**

- Input: `target = 5, maxDoubles = 0`
- Output: `4`
- Explanation: With no doubles available, four increments are necessary.

**Example 2**

- Input: `target = 19, maxDoubles = 2`
- Output: `7`
- Explanation: One optimal sequence reaches `4` with three increments, doubles
  to `8`, increments to `9`, doubles to `18`, and increments once more.

**Example 3**

- Input: `target = 10, maxDoubles = 4`
- Output: `4`
- Explanation: Increment to `2`, double to `4`, increment to `5`, and double
  to `10`.
