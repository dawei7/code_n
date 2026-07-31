# Calculate Amount Paid in Taxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2303 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-amount-paid-in-taxes/) |

## Problem Description
### Goal
The zero-indexed array `brackets` describes a progressive tax schedule.
`brackets[i] = [upper_i, percent_i]` gives the inclusive income ceiling of
bracket $i$ and its percentage rate. The upper bounds are strictly increasing.

The first `upper_0` dollars are taxed at `percent_0`. Each later rate applies
only to the dollars above the preceding upper bound and no higher than its own
upper bound. Given the nonnegative amount `income`, calculate the total tax
owed across all portions of that income. The final bracket is guaranteed to
reach `income`.

### Function Contract
**Inputs**

- `brackets`: Between 1 and 100 pairs `[upper_i, percent_i]`, ordered by
  strictly increasing, unique `upper_i` values.
- `income`: The earned amount to distribute through the tax brackets.

Each upper bound is from 1 through 1000, every percentage is from 0 through
100, and $0 \le \texttt{income} \le 1000$. The last upper bound is at least
`income`.

**Return value**

The total tax as a floating-point monetary amount. An error of at most
$10^{-5}$ is accepted.

### Examples
**Example 1**

- Input: `brackets = [[3, 50], [7, 10], [12, 25]]`, `income = 10`
- Output: `2.65`
- Explanation: The taxable portions are $3$, $4$, and $3$ dollars, producing
  `3 * 50% + 4 * 10% + 3 * 25% = 2.65`.

**Example 2**

- Input: `brackets = [[1, 0], [4, 25], [5, 50]]`, `income = 2`
- Output: `0.25`
- Explanation: The first dollar has a zero rate and the second has a
  25-percent rate.

**Example 3**

- Input: `brackets = [[2, 50]]`, `income = 0`
- Output: `0.0`
- Explanation: There is no income to tax.
