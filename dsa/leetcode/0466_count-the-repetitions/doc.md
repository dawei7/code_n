# Count The Repetitions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 466 |
| Difficulty | Hard |
| Topics | Two Pointers, String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-repetitions/) |

## Problem Description
### Goal
Let `S1` be `s1` concatenated with itself `n1` times, and let one target group be `s2` concatenated `n2` times. Characters may be deleted from `S1` while preserving order to form repeated target groups as a subsequence.

Return the largest integer `m` such that `s2` repeated $n2 \cdot m$ times is a subsequence of `S1`. Matches may cross source-block boundaries, and unused source characters are allowed. If a required target character never occurs in `s1`, return zero. Avoid constructing the potentially enormous repeated strings; exploit repeated matching states across source blocks.

### Function Contract
**Inputs**

- `s1`: the source block
- `n1`: the number of source-block repetitions
- `s2`: the target block
- `n2`: the number of target-block repetitions that form one counted group

**Return value**

- The maximum integer `m` such that `s2` repeated $n2 \cdot m$ times is a subsequence of `s1` repeated `n1` times

### Examples
**Example 1**

- Input: `s1 = "acb", n1 = 4, s2 = "ab", n2 = 2`
- Output: `2`

**Example 2**

- Input: `s1 = "acb", n1 = 1, s2 = "acb", n2 = 1`
- Output: `1`

**Example 3**

- Input: `s1 = "aaa", n1 = 3, s2 = "aa", n2 = 1`
- Output: `4`
