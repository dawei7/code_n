# Find the Count of Numbers Which Are Not Special

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3233 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/) |

## Problem Description

### Goal

For a positive integer $x$, its proper divisors are all positive divisors other than $x$ itself. Call $x$ special when it has exactly two proper divisors.

You are given positive integers `l` and `r`. Count how many integers in the inclusive interval $[l,r]$ are not special. The interval endpoints themselves are included, and the requested count is the interval length minus every special value it contains.

### Function Contract

**Inputs**

- `l`: The inclusive lower endpoint.
- `r`: The inclusive upper endpoint, with $1 \leq \texttt{l} \leq \texttt{r} \leq 10^9$.

Let $m=\lfloor\sqrt{\texttt{r}}\rfloor$.

**Return value**

Return the number of non-special integers in $[l,r]$.

### Examples

**Example 1**

- Input: `l = 5, r = 7`
- Output: `3`
- Explanation: None of $5$, $6$, and $7$ has exactly two proper divisors.

**Example 2**

- Input: `l = 4, r = 16`
- Output: `11`
- Explanation: The interval has $13$ values, and only $4=2^2$ and $9=3^2$ are special.

**Example 3**

- Input: `l = 4, r = 4`
- Output: `0`
- Explanation: The only value is special because its proper divisors are $1$ and $2$.
