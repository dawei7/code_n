# Final Value of Variable After Performing Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2011 |
| Difficulty | Easy |
| Topics | Array, String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/) |

## Problem Description

### Goal

A small programming language has one integer variable, `X`, whose initial
value is zero. Its only statements are `++X`, `X++`, `--X`, and `X--`.

Both statements containing `++` increase `X` by one, regardless of whether the
operator appears before or after the variable. Similarly, either statement
containing `--` decreases `X` by one. Execute the supplied statements in their
given order and return the final value of `X`.

### Function Contract

**Inputs**

- `operations`: a list of $N$ strings, where $1\le N\le100$ and every string
  is exactly `++X`, `X++`, `--X`, or `X--`.

**Return value**

Return the integer value of `X` after applying every operation.

### Examples

**Example 1**

- Input: `operations = ["--X", "X++", "X++"]`
- Output: `1`
- Explanation: The successive values are $-1$, $0$, and $1$.

**Example 2**

- Input: `operations = ["++X", "++X", "X++"]`
- Output: `3`
- Explanation: Every operation increments the variable.

**Example 3**

- Input: `operations = ["X++", "++X", "--X", "X--"]`
- Output: `0`
- Explanation: Two increments and two decrements cancel.
