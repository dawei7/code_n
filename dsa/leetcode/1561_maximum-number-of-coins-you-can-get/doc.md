# Maximum Number of Coins You Can Get

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1561 |
| Difficulty | Medium |
| Topics | Array, Math, Greedy, Sorting, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/) |

## Problem Description
### Goal

There are $3G$ coin piles. On each step, you choose any three remaining piles. Alice takes the largest of those three piles, you take the next-largest pile, and Bob takes the last pile. Continue until no piles remain.

Given the number of coins in every pile, choose the groups to maximize the total number of coins that you receive, and return that maximum total.

### Function Contract
**Inputs**

- `piles`: An array of $N=3G$ positive integers, where $3 \le N \le 10^5$ and $1 \le \texttt{piles[i]} \le 10^4$.
- The array length is divisible by three; pile positions have no effect because each chosen triple may use arbitrary remaining piles.

**Return value**

Return the maximum total number of coins you can collect after all $G$ steps.

### Examples
**Example 1**

- Input: `piles = [2,4,1,2,7,8]`
- Output: `9`

**Example 2**

- Input: `piles = [2,4,5]`
- Output: `4`

**Example 3**

- Input: `piles = [9,8,7,6,5,1,2,3,4]`
- Output: `18`
