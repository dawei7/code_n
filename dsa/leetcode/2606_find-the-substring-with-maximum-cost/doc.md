# Find the Substring With Maximum Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2606 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-substring-with-maximum-cost/) |

## Problem Description

### Goal

You are given a lowercase string `s`, a string `chars` containing distinct lowercase letters, and an integer array `vals` of the same length as `chars`. Each character has a numeric value.

A character listed at `chars[i]` has the custom value `vals[i]`. Every character not listed in `chars` keeps its one-indexed alphabet position: `a` is worth $1$, `b` is worth $2$, and so on through `z`, which is worth $26$.

The cost of a substring is the sum of its character values. The empty substring is permitted and has cost $0$. Return the maximum cost among all substrings of `s`.

### Function Contract

**Inputs**

- `s`: A nonempty lowercase string of length $n$, where $1 \leq n \leq 10^5$.
- `chars`: A string of $k$ distinct lowercase characters, where $1 \leq k \leq 26$.
- `vals`: A length-$k$ list in which `vals[i]` is the custom value of `chars[i]`, with $-1000 \leq \texttt{vals[i]} \leq 1000$.

**Return value**

- The greatest cost of any substring of `s`, including the empty substring.

### Examples

#### Example 1

- **Input:** `s = "adaa", chars = "d", vals = [-1000]`
- **Output:** `2`

The custom value makes `d` strongly negative, so the final substring `"aa"` has the maximum cost $1+1=2$.

#### Example 2

- **Input:** `s = "abc", chars = "abc", vals = [-1,-1,-1]`
- **Output:** `0`

Every nonempty substring has negative cost, so the empty substring is optimal.
