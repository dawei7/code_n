# Eat Pizzas!

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3457 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/eat-pizzas/) |

## Problem Description
### Goal
Every entry in `pizzas` is a pizza's weight. Over each day, eat exactly four unused pizzas whose sorted weights are $W \le X \le Y \le Z$. On odd-numbered days, only $Z$ is added to the gained weight; on even-numbered days, only $Y$ is added.

Use every pizza exactly once and maximize the total gained weight. The number of pizzas is divisible by four, so the process lasts exactly $n/4$ days. The day parity is fixed by its 1-indexed position, but the four pizzas assigned to each day may be chosen freely.

### Function Contract
**Inputs**

- `pizzas`: A list of $n$ positive integer pizza weights.

The constraints are $4 \le n \le 2 \cdot 10^5$, $n$ is divisible by $4$, and $1 \le \texttt{pizzas[i]} \le 10^5$.

**Return value**

Return the maximum total weight that can be gained after all pizzas are eaten.

### Examples
**Example 1**

- Input: `pizzas = [1, 2, 3, 4, 5, 6, 7, 8]`
- Output: `14`

The odd day can score $8$, and the even day can score $6$, for a total of $14$.

**Example 2**

- Input: `pizzas = [2, 1, 1, 1, 1, 1, 1, 1]`
- Output: `3`

The two days score $2$ and $1$.

**Example 3**

- Input: `pizzas = [1, 3, 5, 8]`
- Output: `8`
