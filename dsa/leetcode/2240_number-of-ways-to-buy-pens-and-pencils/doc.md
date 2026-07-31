# Number of Ways to Buy Pens and Pencils

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2240 |
| Difficulty | Medium |
| Topics | Math, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/) |

## Problem Description

### Goal

You have `total` units of money. One pen costs `cost1`, and one pencil costs
`cost2`. You may buy any nonnegative quantity of either item, including none
of one or both kinds, and may spend either part or all of the available money.

Count the distinct ordered quantity pairs `(pens, pencils)` whose combined
price does not exceed `total`. Two choices are different when either purchased
quantity differs. The unused amount of money does not otherwise distinguish
choices.

### Function Contract

**Inputs**

- `total`: The available money.
- `cost1`: The price of one pen.
- `cost2`: The price of one pencil.

All three inputs are integers satisfying $1\le\texttt{total},
\texttt{cost1},\texttt{cost2}\le 10^6$. Let $T=\texttt{total}$,
$c_1=\texttt{cost1}$, and $c_2=\texttt{cost2}$.

**Return value**

Return the number of pairs of nonnegative integers $(a,b)$ satisfying
$ac_1+bc_2\le T$.

### Examples

**Example 1**

- Input: `total = 20, cost1 = 10, cost2 = 5`
- Output: `9`

**Example 2**

- Input: `total = 5, cost1 = 10, cost2 = 10`
- Output: `1`

**Example 3**

- Input: `total = 6, cost1 = 2, cost2 = 3`
- Output: `7`
