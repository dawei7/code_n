# Strictly Palindromic Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2396 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Two Pointers, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/strictly-palindromic-number/) |

## Problem Description

### Goal

An integer `n` is called strictly palindromic when its digit representation is
palindromic in every integer base $b$ from 2 through $n-2$, inclusive. A
palindromic representation reads identically from its most significant digit
to its least significant digit and in the reverse direction.

Given `n`, determine whether this condition holds for the complete required
range of bases. It is not enough for the representation to be palindromic in
one or several bases: every base in the interval must satisfy the condition.
Return `true` only in that case, and return `false` otherwise.

### Function Contract

**Inputs**

- `n`: An integer satisfying $4 \le n \le 10^5$.

**Return value**

Return `True` if the representation of `n` is palindromic in every base
$b \in \{2,3,\ldots,n-2\}$; otherwise return `False`.

### Examples

#### Example 1

- **Input:** `n = 9`
- **Output:** `False`
- **Explanation:** Although 9 is `1001` in base 2, its base-3 representation
  `100` is not palindromic.

#### Example 2

- **Input:** `n = 4`
- **Output:** `False`
- **Explanation:** The only required base is 2, where 4 is represented as `100`.

#### Example 3

- **Input:** `n = 5`
- **Output:** `False`
- **Explanation:** Base 3 is included, and $5 = 1\cdot3+2$ has representation
  `12`, whose two digits differ.
