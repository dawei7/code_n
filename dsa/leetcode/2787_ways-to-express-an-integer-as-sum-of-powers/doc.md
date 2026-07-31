# Ways to Express an Integer as Sum of Powers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2787 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/) |

## Problem Description

### Goal

Given positive integers `n` and `x`, count how many sets of distinct positive integers have $x$-th powers that sum to `n`. The order of the selected integers does not create a different way: each valid choice is a set, and no positive integer may appear more than once.

Equivalently, count the sets $\{a_1, a_2, \ldots, a_k\}$ that satisfy

$$
n = a_1^x + a_2^x + \cdots + a_k^x,
$$

where all $a_i$ are positive and pairwise distinct. Return the count modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `n`: The positive target sum, with $1 \le n \le 300$.
- `x`: The positive exponent applied to every selected integer, with $1 \le x \le 5$.

Let

$$
m = \left\lfloor n^{1/x} \right\rfloor
$$

be the number of positive bases whose $x$-th powers do not exceed `n`.

**Return value**

Return the number of distinct sets whose powered values sum to `n`, reduced modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `n = 10, x = 2`
- Output: `1`
- Explanation: The only set is $\{1, 3\}$ because $1^2 + 3^2 = 10$.

**Example 2**

- Input: `n = 4, x = 1`
- Output: `2`
- Explanation: The valid sets are $\{4\}$ and $\{1, 3\}$.

**Example 3**

- Input: `n = 25, x = 2`
- Output: `2`
- Explanation: Both $\{5\}$ and $\{3, 4\}$ produce $25$ after squaring their members.
