# Can Convert String in K Moves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1540 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/can-convert-string-in-k-moves/) |

## Problem Description
### Goal
You are given lowercase strings `s` and `t` and may perform at most `k` numbered moves. On move $i$, either do nothing or choose one position that has never been chosen before and advance its character by exactly $i$ alphabet steps. Shifts wrap around from `z` to `a`.

Each position can therefore be changed at most once, and two positions cannot both use the same move number. Determine whether some choices among moves $1$ through $k$ transform every character of `s` into the corresponding character of `t`. Strings of different lengths cannot be converted.

### Function Contract
**Inputs**

- `s`: the source string of lowercase English letters.
- `t`: the desired string of lowercase English letters.
- `k`: the greatest available move number, where $0 \le k \le 10^9$.
- Each string length is between $1$ and $10^5$.

**Return value**

`True` if `s` can be converted into `t` using no more than the first `k` moves; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "input", t = "ouput", k = 9`
- Output: `True`
- Explanation: Use move `6` for `i` to `o` and move `7` for `n` to `u`.

**Example 2**

- Input: `s = "abc", t = "bcd", k = 10`
- Output: `False`
- Explanation: All three positions need shift `1`, but only move `1` supplies that residue within ten moves.

**Example 3**

- Input: `s = "aab", t = "bbb", k = 27`
- Output: `True`
- Explanation: The two `a` positions can use moves `1` and `27`, which are congruent modulo 26.
