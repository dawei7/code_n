# String Transformation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2851 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/string-transformation/) |

## Problem Description

### Goal

You are given lowercase strings `s` and `t` of the same length $n$. An operation on `s` chooses a suffix whose length $l$ satisfies $0 < l < n$, removes that suffix, and places it before the remaining prefix. For example, choosing the suffix `"cd"` from `"abcd"` produces `"cdab"`.

You are also given an integer `k`. Count the distinct sequences of suffix choices that transform `s` into `t` after exactly `k` operations. Reaching `t` earlier does not end a sequence; all `k` operations must still be performed, and different suffix choices count as different ways even when periodic characters make them produce the same visible string.

Return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$.
- `t`: A lowercase English string with the same length as `s`.
- `k`: The exact number of operations to perform.

The constraints are $2 \le n \le 5 \cdot 10^5$ and $1 \le k \le 10^{15}$.

**Return value**

- The number of length-`k` operation sequences that finish at `t`, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `s = "abcd", t = "cdab", k = 2`
- **Output:** `2`
- **Explanation:** One sequence moves the suffix beginning at index `3` twice. Another moves the suffix beginning at index `1` twice. Both finish at `"cdab"` after exactly two operations.

#### Example 2

- **Input:** `s = "ababab", t = "ababab", k = 1`
- **Output:** `2`
- **Explanation:** Moving the suffix beginning at index `2` or the one beginning at index `4` reproduces the same periodic string, and the two suffix choices are distinct ways.
