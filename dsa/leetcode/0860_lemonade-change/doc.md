# Lemonade Change

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 860 |
| Difficulty | Easy |
| Topics | Array, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/lemonade-change/) |

## Problem Description
### Goal
Each lemonade costs `$5`. Customers wait in a queue and buy exactly one lemonade apiece, in the order listed by `bills`. A customer pays with a single `$5`, `$10`, or `$20` bill, and the transaction must leave that customer having paid a net `$5` after receiving the correct change.

The stand begins with no money, so change for a customer may use only bills collected from earlier customers. Given the bill presented by every customer in order, determine whether correct change can be given throughout the entire queue. Return `false` as soon as some transaction cannot be completed.

### Function Contract
**Inputs**

- `bills`: an array in queue order whose entries are each `5`, `10`, or `20`, with $1 \leq \lvert\texttt{bills}\rvert \leq 10^5$.

Let $n=\lvert\texttt{bills}\rvert$.

**Return value**

Return `true` if every customer can receive exact change using bills collected earlier; otherwise, return `false`.

### Examples
**Example 1**

- Input: `bills = [5,5,5,10,20]`
- Output: `true`

The `$10` customer receives one `$5`, and the `$20` customer receives one `$10` plus one `$5`.

**Example 2**

- Input: `bills = [5,5,10,10,20]`
- Output: `false`

Only two `$10` bills remain for the final customer, so `$15` of change cannot be made.

**Example 3**

- Input: `bills = [5,10]`
- Output: `true`
