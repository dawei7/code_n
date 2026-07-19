# Allocate Mailboxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1478 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/allocate-mailboxes/) |

## Problem Description
### Goal

The array `houses` gives the distinct positions of houses along a one-dimensional street. Place exactly `k` mailboxes at any street positions. Each house is served by its nearest mailbox and contributes the absolute distance between its position and that mailbox.

Choose the mailbox positions to minimize the sum of these nearest-mailbox distances over every house, and return that minimum total. The input positions need not be sorted, and the result is guaranteed to fit in a 32-bit integer.

### Function Contract
**Inputs**

Let $N$ be the number of houses.

- `houses`: an array of $N$ distinct integer positions, where $1 \le N \le 100$ and $1 \le \texttt{houses[i]} \le 10^4$.
- `k`: the exact number of mailboxes to allocate, where $1 \le k \le N$.

**Return value**

Return the minimum possible value of

$$
\sum_{x\in\texttt{houses}}\min_{b\in B}\lvert x-b\rvert,
$$

where $B$ is the set of the $k$ chosen mailbox positions.

### Examples
**Example 1**

- Input: `houses = [1,4,8,10,20], k = 3`
- Output: `5`
- Explanation: Mailboxes at positions $3$, $9$, and $20$ give distances $2+1+1+1+0=5$.

**Example 2**

- Input: `houses = [2,3,5,12,18], k = 2`
- Output: `9`
- Explanation: Mailboxes at $3$ and $14$ give total distance $1+0+2+2+4=9$.

**Example 3**

- Input: `houses = [7,4,6,1], k = 1`
- Output: `8`
- Explanation: After sorting to `[1,4,6,7]`, any point between the two middle positions $4$ and $6$ is optimal; choosing either endpoint gives total distance $8$.
