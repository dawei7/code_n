# Find the Pivot Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2485 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-pivot-integer/) |

## Problem Description

### Goal

Given a positive integer `n`, find an integer $x$ between $1$ and $n$ for which the inclusive sum from $1$ through $x$ equals the inclusive sum from $x$ through $n$. The left range starts at $1$, the right range ends at $n$, and the value $x$ contributes to both sums.

Return this pivot integer when it exists. Otherwise, return `-1`. The input is guaranteed to have at most one valid pivot.

### Function Contract

**Inputs**

- `n`: A positive integer with $1 \le n \le 1000$.

**Return value**

Return the unique integer $x \in [1,n]$ satisfying

$$
\sum_{i=1}^{x} i = \sum_{i=x}^{n} i.
$$

If no such integer exists, return `-1`.

### Examples

#### Example 1

- **Input:** `n = 8`
- **Output:** `6`
- **Explanation:** Both inclusive sums equal $21$: $1+2+3+4+5+6 = 6+7+8$.

#### Example 2

- **Input:** `n = 1`
- **Output:** `1`
- **Explanation:** The only possible pivot appears in both one-element sums.

#### Example 3

- **Input:** `n = 4`
- **Output:** `-1`
- **Explanation:** No integer from $1$ through $4$ balances the two inclusive sums.
