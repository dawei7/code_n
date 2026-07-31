# Number of Divisible Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2950 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-divisible-substrings/) |

## Problem Description
### Goal
Each lowercase English letter has the following mapped value:

| Value | Letters |
|---:|---|
| 1 | `a`, `b` |
| 2 | `c`, `d`, `e` |
| 3 | `f`, `g`, `h` |
| 4 | `i`, `j`, `k` |
| 5 | `l`, `m`, `n` |
| 6 | `o`, `p`, `q` |
| 7 | `r`, `s`, `t` |
| 8 | `u`, `v`, `w` |
| 9 | `x`, `y`, `z` |

A nonempty string is divisible when the sum of its characters' mapped values
is divisible by the string's length. Given a lowercase English string `word`,
return the number of its contiguous nonempty substrings that are divisible.

### Function Contract
**Inputs**

- `word`: the lowercase English string whose substrings are examined

Let $N=\lvert\texttt{word}\rvert$. The contract guarantees
$1\le N\le2000$.

**Return value**

The number of nonempty substrings for which the mapped-value sum is divisible
by the substring length.

### Examples
**Example 1**

- Input: `word = "asdf"`
- Output: `6`
- Explanation: The four single letters, `"as"`, and `"sdf"` have sums divisible by their lengths.

**Example 2**

- Input: `word = "bdh"`
- Output: `4`
- Explanation: The three single letters and `"bdh"` are divisible.

**Example 3**

- Input: `word = "abcd"`
- Output: `6`
- Explanation: The four single letters together with `"ab"` and `"cd"` are divisible.
