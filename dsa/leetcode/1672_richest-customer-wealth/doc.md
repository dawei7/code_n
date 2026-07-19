# Richest Customer Wealth

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1672 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/richest-customer-wealth/) |

## Problem Description
### Goal
The rectangular integer matrix `accounts` records bank balances for several customers. Row `i` belongs to one customer, and column `j` gives that customer's balance at bank `j`. Every customer has a balance entry for the same number of banks, and every balance is positive.

A customer's wealth is the sum of every balance in that customer's row. Compute each customer's total and return the greatest such total. If several customers share the greatest wealth, the returned value is still that common total; no customer index needs to be reported.

### Function Contract
**Inputs**

- `accounts`: an $m \times n$ matrix of positive integers, where rows represent customers and columns represent banks.

Let $S = mn$ be the number of balances in the matrix.

**Return value**

Return the maximum row sum, representing the wealth held by the richest customer.

### Examples
**Example 1**

- Input: `accounts = [[1,2,3],[3,2,1]]`
- Output: `6`

**Example 2**

- Input: `accounts = [[1,5],[7,3],[3,5]]`
- Output: `10`

**Example 3**

- Input: `accounts = [[2,8,7],[7,1,3],[1,9,5]]`
- Output: `17`
