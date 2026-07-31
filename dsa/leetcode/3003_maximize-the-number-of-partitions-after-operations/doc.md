# Maximize the Number of Partitions After Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3003 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/) |

## Problem Description
### Goal
You are given a lowercase English string `s` and an integer `k`. Before
partitioning, you may replace at most one character of `s` with any lowercase
English letter.

Then repeatedly remove the longest remaining prefix containing at most `k`
distinct characters. Each removed prefix is one partition, and the unremoved
characters retain their order. Continue until no characters remain.

Choose the optional replacement to maximize the number of partitions and
return that maximum.

### Function Contract
**Inputs**

- `s`: the nonempty lowercase English string
- `k`: the maximum distinct-character count in one partition

Let $N=\lvert\texttt{s}\rvert$. The contract guarantees $1\le N\le10^4$
and $1\le\texttt{k}\le26$.

**Return value**

Return the maximum greedy partition count obtainable after at most one
character replacement.

### Examples
**Example 1**

- Input: `s = "accca", k = 2`
- Output: `3`

Changing the middle character to `b` produces `"acbca"`, partitioned as
`"ac"`, `"bc"`, and `"a"`.

**Example 2**

- Input: `s = "aabaab", k = 3`
- Output: `1`

One replacement cannot make the string contain more than three distinct
letters, so the whole string remains one prefix.

**Example 3**

- Input: `s = "xxyz", k = 1`
- Output: `4`

Replacing one repeated `x` with a new letter makes every adjacent character
start a separate one-distinct-letter partition.
