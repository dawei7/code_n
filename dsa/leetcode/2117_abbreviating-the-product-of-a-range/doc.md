# Abbreviating the Product of a Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2117 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/abbreviating-the-product-of-a-range/) |

## Problem Description
### Goal

Given positive integers `left` and `right`, form the product of every integer
in the inclusive range `[left, right]`.

First count and remove all trailing zeros from that product; call their number
$C$. Let $d$ be the number of decimal digits remaining. When $d \le 10$, keep
the entire zero-free product. When $d > 10$, abbreviate it as its first five
digits, three periods, and its last five digits. The five-digit suffix must
retain leading zeros.

Append `eC` to either representation and return the resulting string. Thus the
format is `valueeC` for at most ten significant digits and
`prefix...suffixeC` otherwise.

### Function Contract
**Inputs**

- `left`: The positive lower endpoint of the range.
- `right`: The positive upper endpoint, with `left <= right`.

Let $N = \texttt{right} - \texttt{left} + 1$ and $R = \texttt{right}$.

**Return value**

Return the prescribed abbreviation of
$\prod_{x=\texttt{left}}^{\texttt{right}} x$ after removing all trailing
zeros.

### Examples
**Example 1**

- Input: `left = 1, right = 4`
- Output: `"24e0"`

The product is $24$, with no trailing zeros.

**Example 2**

- Input: `left = 2, right = 11`
- Output: `"399168e2"`

Removing two zeros from $39916800$ leaves the six-digit value $399168$.

**Example 3**

- Input: `left = 371, right = 375`
- Output: `"7219856259e3"`

The product is $7219856259000$, so three zeros are removed and the remaining
ten digits are kept in full.
