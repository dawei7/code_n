# Minimum Operations to Equalize Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3666 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/) |

## Problem Description
### Goal

Given a binary string `s` and an integer `k`, one operation must select exactly `k` distinct string indices. Flip the bit at every selected index: each `0` becomes `1`, and each `1` becomes `0`.

Indices may be selected again in later operations, but no index may appear twice within one operation. Every operation always flips exactly `k` positions; selecting fewer positions is not allowed.

Find the minimum number of operations needed to make every character equal to `1`. Return `-1` if no sequence of legal operations can reach the all-ones string.

### Function Contract

**Inputs**

- `s`: a nonempty binary string of length $n$, where $1\le n\le10^5$.
- `k`: the exact number of distinct indices flipped per operation, where $1\le k\le n$.

**Return value**

Return the smallest number of operations that transforms `s` into `"1" * n`, or `-1` when the target is unreachable.

### Examples

**Example 1**

- Input: `s = "110"`, `k = 1`
- Output: `1`
- Flip the only zero directly.

**Example 2**

- Input: `s = "0101"`, `k = 3`
- Output: `2`
- Two selections of three indices can correct both initial zeros while re-flipping the necessary ones.

**Example 3**

- Input: `s = "101"`, `k = 2`
- Output: `-1`
- The required flip-count parity cannot be achieved.
