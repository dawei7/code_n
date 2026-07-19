# Form Largest Integer With Digits That Add up to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1449 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/) |

## Problem Description
### Goal

Nine painting costs are given, one for each decimal digit from `1` through
`9`: painting digit `i + 1` costs `cost[i]`. A digit may be painted any number
of times. Choose a non-empty sequence of these digits whose total cost is
exactly `target`; digit `0` is unavailable.

Among every integer that can be formed under those rules, return the
numerically largest one. The answer can contain thousands of digits, so return
its decimal representation as a string rather than converting it to a numeric
type. If no non-empty sequence has exactly the required total cost, return
`"0"`.

### Function Contract
**Inputs**

- `cost`: a list of exactly nine integers. `cost[i]` is the cost of digit
  `i + 1`, and $1 \le \texttt{cost[i]} \le 5000$.
- `target`: the exact total cost to spend, with $1 \le \texttt{target} \le 5000$.

Let $T=\texttt{target}$. Because every digit has positive cost, any feasible
answer contains at most $T$ digits.

**Return value**

Return the decimal string for the largest positive integer whose digit costs
sum to exactly `target`. Return `"0"` when the exact cost is unreachable.

### Examples
**Example 1**

- Input: `cost = [4, 3, 2, 5, 6, 7, 2, 5, 5], target = 9`
- Output: `"7772"`
- Explanation: Three `7` digits cost $3\cdot2$ and digit `2` costs $3$, for a
  total of $9$. Although `"977"` is also feasible, the four-digit answer is
  numerically larger.

**Example 2**

- Input: `cost = [7, 6, 5, 5, 5, 6, 8, 7, 8], target = 12`
- Output: `"85"`

**Example 3**

- Input: `cost = [2, 4, 6, 2, 4, 6, 4, 4, 4], target = 5`
- Output: `"0"`
- Explanation: Every available cost is even, so no combination totals the odd
  target.

**Example 4**

- Input: `cost = [1, 1, 1, 1, 1, 1, 1, 1, 1], target = 3`
- Output: `"999"`
- Explanation: Every three-digit choice has the same cost and length, so the
  largest digit is selected at every position.
