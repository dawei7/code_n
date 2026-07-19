# Find N Unique Integers Sum up to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1304 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/) |

## Problem Description
### Goal
Given a positive integer `n`, construct an array containing exactly `n` integers. Every returned integer must be unique, and the sum of all returned values must equal zero.

Any array satisfying those properties is valid; the values do not need to appear in a prescribed order or match one particular example. Return one such construction.

The contract therefore judges the length, distinctness, and total of the returned values, not a particular arrangement.

### Function Contract
**Inputs**

- `n`: the required array length, where $1 \le n \le 1000$.

**Return value**

Any integer array `result` satisfying $\lvert\texttt{result}\rvert=n$, containing $n$ distinct values, and obeying

$$
\sum_{x \in \texttt{result}} x=0.
$$

### Examples
**Example 1**

- Input: `n = 5`
- Output: `[-2,-1,0,1,2]`
- Explanation: The five values are distinct and sum to zero; many other answers are also valid.

**Example 2**

- Input: `n = 3`
- Output: `[-1,0,1]`

**Example 3**

- Input: `n = 1`
- Output: `[0]`
