# Count Good Meals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1711 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-good-meals/) |

## Problem Description
### Goal

A good meal consists of exactly two different food items whose deliciousness values add to a power of two. Items are distinguished by their indices, so two equal values at different positions may form a pair, while one item cannot be paired with itself.

Given the deliciousness value of every item, count the index pairs that form good meals. Count each unordered pair once and return the result modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `deliciousness`: a list of $n$ non-negative integers
- $1 \le n \le 10^5$
- $0 \le \texttt{deliciousness[i]} \le 2^{20}$

Let $B = 22$, the number of powers $2^0$ through $2^{21}$ that can equal a legal pair sum.

**Return value**

The number of pairs $(i,j)$ with $i<j$ whose values sum to a power of two, reduced modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `deliciousness = [1, 3, 5, 7, 9]`
- Output: `4`

The qualifying value pairs are `(1, 3)`, `(1, 7)`, `(3, 5)`, and `(7, 9)`.

**Example 2**

- Input: `deliciousness = [1, 1, 1, 3, 3, 3, 7]`
- Output: `15`

There are three pairs of ones, nine pairs combining a one and a three, and three pairs combining a one and a seven.

**Example 3**

- Input: `deliciousness = [0, 0, 1, 1]`
- Output: `5`

Each zero can pair with either one to make $1$, and the two ones form one pair summing to $2$.
