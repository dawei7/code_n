# Maximum Difference Between Even and Odd Frequency II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3445 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Sliding Window, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/) |

## Problem Description

### Goal

Given a string `s` containing only the digits from `0` through `4`, choose a substring whose length is at least `k`. Within that substring, select two distinct characters `a` and `b` such that the frequency of `a` is odd while the frequency of `b` is non-zero and even.

Maximize `freq[a] - freq[b]` over every permitted substring and ordered pair of characters. Other distinct characters may also occur in the chosen substring; they place no restriction on the candidate. The input guarantees that at least one valid choice exists, so the maximum is always defined and may be negative.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $3\le n\le3\cdot10^4$, containing only `0`, `1`, `2`, `3`, and `4`.
- `k`: The minimum permitted substring length, with $1\le k\le n$.

At least one substring contains one character an odd number of times and another character a positive even number of times.

**Return value**

Return the maximum difference between the odd frequency and the positive even frequency among all valid substrings and ordered character pairs.

### Examples

#### Example 1

- **Input:** `s = "12233", k = 4`
- **Output:** `-1`

In `"12233"`, character `1` occurs once and character `3` occurs twice, producing `1 - 2 = -1`.

#### Example 2

- **Input:** `s = "1122211", k = 3`
- **Output:** `1`

The substring `"11222"` contains three `2` characters and two `1` characters, producing `3 - 2 = 1`.

#### Example 3

- **Input:** `s = "110", k = 3`
- **Output:** `-1`

The whole string has one `0` and two `1` characters, so their valid difference is `1 - 2 = -1`.
