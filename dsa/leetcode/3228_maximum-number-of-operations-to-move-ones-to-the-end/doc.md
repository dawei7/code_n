# Maximum Number of Operations to Move Ones to the End

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3228 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/) |

## Problem Description

### Goal

You are given a binary string `s`. An operation may choose an adjacent `"10"` pair. Remove that `1` from its position and move it right across the entire consecutive block of zeroes, stopping immediately before the next `1` or at the end of the string.

Operations may be performed in any order and may move the same `1` more than once as later zero blocks become reachable. Return the maximum total number of operations that can be performed before no `"10"` boundary remains.

### Function Contract

**Inputs**

- `s`: A binary string with $1 \leq \lvert\texttt{s}\rvert \leq 10^5$.

**Return value**

Return the maximum possible number of valid move operations.

### Examples

**Example 1**

- Input: `s = "1001101"`
- Output: `4`
- Explanation: The two zero blocks can be crossed by one and three preceding `1` characters respectively.

**Example 2**

- Input: `s = "00111"`
- Output: `0`
- Explanation: No `1` has a zero immediately to its right.

**Example 3**

- Input: `s = "10"`
- Output: `1`
- Explanation: The single `1` moves across the final zero block once.
