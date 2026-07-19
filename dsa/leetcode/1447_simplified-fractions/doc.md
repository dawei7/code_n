# Simplified Fractions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1447 |
| Difficulty | Medium |
| Topics | Math, String, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/simplified-fractions/) |

## Problem Description
### Goal

Given an integer `n`, list every simplified fraction strictly between $0$ and
$1$ whose denominator is at most `n`. A fraction is simplified when its
positive numerator and denominator share no common divisor greater than one;
equivalent representations such as `"1/2"` and `"2/4"` must therefore not
both appear.

Represent each retained fraction as a string in the form
`"numerator/denominator"`. Return every qualifying value exactly once. The
list may be arranged in any order.

### Function Contract
**Inputs**

- `n`: an integer satisfying $1 \le n \le 100$.

**Return value**

Return a list of strings `"a/b"` containing exactly the fractions for which
$1 \le a < b \le n$ and $\gcd(a,b)=1$. The order of the strings is not part of
the result contract.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `["1/2"]`

**Example 2**

- Input: `n = 3`
- Output: `["1/2", "1/3", "2/3"]`

**Example 3**

- Input: `n = 4`
- Output: `["1/2", "1/3", "1/4", "2/3", "3/4"]`
- Explanation: `"2/4"` is excluded because reducing it produces the already
  represented fraction `"1/2"`.

**Example 4**

- Input: `n = 1`
- Output: `[]`
- Explanation: No denominator at most one admits a positive numerator that is
  smaller than it.
