# Minimum Number of Operations to Make Word K-Periodic

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3137 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/) |

## Problem Description

### Goal

You are given a string `word` of length $n$ and an integer `k` that divides $n$.

In one operation, choose indices `i` and `j` that are both divisible by `k`. Replace the length-`k` substring `word[i..i + k - 1]` with the length-`k` substring `word[j..j + k - 1]`. Thus, an operation copies one aligned block of `word` over another aligned block.

Make `word` **k-periodic** using the minimum number of operations. A string is k-periodic when some string `s` of length `k` can be repeated and concatenated to form the entire string. Return that minimum operation count.

### Function Contract

Let $n = \lvert\texttt{word}\rvert$ and $B=n/k$ be the number of aligned length-`k` blocks.

**Inputs**

- `word`: A string of $n$ lowercase English letters, where $1 \le n \le 10^5$.
- `k`: A positive block length satisfying $1 \le k \le n$ and dividing $n$.

**Return value**

- Return the minimum number of aligned block-copy operations required to make every one of the $B$ blocks equal.

### Examples

#### Example 1

- **Input:** `word = "leetcodeleet", k = 4`
- **Output:** `1`
- **Explanation:** Copy the first block, `"leet"`, over the block beginning at index `4`, producing `"leetleetleet"`.

#### Example 2

- **Input:** `word = "leetcoleet", k = 2`
- **Output:** `3`
- **Explanation:** The five aligned blocks are `"le"`, `"et"`, `"co"`, `"le"`, and `"et"`. Either of the two most frequent blocks can be copied over the three remaining positions.
