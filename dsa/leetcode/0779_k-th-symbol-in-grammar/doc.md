# K-th Symbol in Grammar

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 779 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Bit Manipulation, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/k-th-symbol-in-grammar/) |

## Problem Description

### Goal

The first grammar row is `0`. To create each following row, replace every `0` in the previous row with `01` and every `1` with `10`, preserving the order of all replacement pairs.

Given a one-based row number `n` and a one-based position `k`, return the symbol at that position of row `n`. The result is the integer `0` or `1`; the row may be exponentially long, but the requested symbol is defined by the recursive grammar.

### Function Contract

**Inputs**

- `n`: a positive row number.
- `k`: a one-based position satisfying $1 \le k \le 2^{(n - 1)}$.

**Return value**

- The integer `0` or `1` stored at position `k` of row `n`.

### Examples

**Example 1**

- Input: `n = 1, k = 1`
- Output: `0`
- Explanation: The first row contains only its initial zero.

**Example 2**

- Input: `n = 2, k = 1`
- Output: `0`
- Explanation: Expanding the first row produces `01`.

**Example 3**

- Input: `n = 2, k = 2`
- Output: `1`
- Explanation: The second position of `01` is one.
