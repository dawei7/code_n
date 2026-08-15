# Count the Number of Powerful Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2999 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-powerful-integers/) |

## Problem Description

### Goal

You are given an inclusive integer range from `start` through `finish`, a digit
ceiling `limit`, and a nonempty decimal string `s` representing a positive
integer without a leading zero.

A positive integer is powerful when its decimal representation ends with `s`
and every one of its digits is at most `limit`. The suffix may occupy the
entire representation; for example, `25` is a suffix of both `25` and `5125`,
but not of `512`.

Return how many powerful integers lie in the supplied inclusive range.

### Function Contract

**Inputs**

- `start`: the inclusive lower bound
- `finish`: the inclusive upper bound
- `limit`: the largest permitted decimal digit
- `s`: the required nonzero-leading decimal suffix

The contract guarantees $1 \le \texttt{start} \le \texttt{finish} \le 10^{15}$,
$1 \le \texttt{limit} \le 9$, and $1 \le \lvert\texttt{s}\rvert \le
\lfloor\log_{10}(\texttt{finish})\rfloor+1$. Every digit of `s` is already at
most `limit`. Let $D$ be the number of decimal digits in `finish`.

**Return value**

Return the number of powerful integers in `[start, finish]`.

### Examples

#### Example 1

- **Input:** `start = 1, finish = 6000, limit = 4, s = "124"`
- **Output:** `5`

The valid values are `124`, `1124`, `2124`, `3124`, and `4124`.

#### Example 2

- **Input:** `start = 15, finish = 215, limit = 6, s = "10"`
- **Output:** `2`

Only `110` and `210` satisfy both the range and digit restrictions.

#### Example 3

- **Input:** `start = 1000, finish = 2000, limit = 4, s = "3000"`
- **Output:** `0`

The suffix value itself already exceeds the upper bound.
