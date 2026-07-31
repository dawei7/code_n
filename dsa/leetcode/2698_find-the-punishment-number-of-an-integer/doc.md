# Find the Punishment Number of an Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2698 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-the-punishment-number-of-an-integer/) |

## Problem Description

### Goal

For a positive integer `n`, consider every integer $i$ from $1$ through $n$. Write $i^2$ in decimal and determine whether its digits can be divided into one or more nonempty contiguous substrings whose integer values sum to $i$.

A substring may contain leading zeroes, and its integer value is interpreted normally; for example, a piece `"00"` contributes zero. Every digit of the square must belong to exactly one piece, and the original digit order cannot change.

Return the sum of $i^2$ over all values of $i$ that admit at least one such partition. This sum is the punishment number of `n`.

### Function Contract

**Inputs**

- `n`: A positive integer with $1 \leq n \leq 1000$.

**Return value**

Return an integer equal to the sum of the squares of all qualifying values $i$ in the inclusive range $[1,n]$.

### Examples

**Example 1**

- Input: `n = 10`
- Output: `182`
- Explanation: The qualifying values are $1$, $9$, and $10$. Their squares are `1`, `81`, and `100`; partitions `8 + 1` and `10 + 0` establish the latter two.

**Example 2**

- Input: `n = 37`
- Output: `1478`
- Explanation: In addition to $1$, $9$, and $10$, the value $36$ qualifies because `1296` can be split as `1 + 29 + 6`. The four squares sum to $1478$.
