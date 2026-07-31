# Maximum Twin Sum of a Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2130 |
| Difficulty | Medium |
| Topics | Linked List, Two Pointers, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/) |

## Problem Description
### Goal
Consider a linked list of even length $n$, indexed from $0$. For every index
$i$ in the first half, node $i$ and node $n-1-i$ are twins. Thus the first
node is paired with the last, the second with the second-to-last, and so on
until the two middle nodes form the final pair.

The twin sum of a pair is the sum of its two node values. Given the list's
head, find the greatest twin sum among all $n/2$ pairs.

### Function Contract
**Inputs**

- `head`: The values of a non-empty singly linked list whose length $n$ is
  even and satisfies $2\le n\le 10^5$. Every node value is between $1$ and
  $10^5$.

**Return value**

The maximum sum of two twin node values.

### Examples
**Example 1**

- Input: `head = [5, 4, 2, 1]`
- Output: `6`
- Explanation: Both twin pairs have sum $6$.

**Example 2**

- Input: `head = [4, 2, 2, 3]`
- Output: `7`
- Explanation: The outer pair sums to $7$, while the inner pair sums to $4$.

**Example 3**

- Input: `head = [1, 100000]`
- Output: `100001`
- Explanation: The two nodes form the only twin pair.
