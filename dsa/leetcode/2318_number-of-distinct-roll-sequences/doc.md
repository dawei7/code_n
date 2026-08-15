# Number of Distinct Roll Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2318 |
| Difficulty | Hard |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-distinct-roll-sequences/) |

## Problem Description

### Goal

Roll a six-sided die exactly `n` times and consider the ordered sequence of
faces. Two neighboring rolls are allowed only when their greatest common
divisor is $1$. In addition, equal faces must be separated by more than two
positions, so a face may match neither the immediately preceding roll nor the
roll two positions earlier.

Count all distinct sequences satisfying both restrictions. Sequences are
different when any position differs. Because the count grows rapidly, return
the result modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The number of die rolls, with $1\le n\le10^4$.

**Return value**

The number of valid length-`n` roll sequences modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `n = 4`
- **Output:** `184`
- **Explanation:** Adjacent values must be coprime, and positions two apart cannot
  be equal.

#### Example 2

- **Input:** `n = 2`
- **Output:** `22`
