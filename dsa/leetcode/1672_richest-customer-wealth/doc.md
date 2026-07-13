# Richest Customer Wealth

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1672 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [richest-customer-wealth](https://leetcode.com/problems/richest-customer-wealth/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/richest-customer-wealth/).

### Goal
Each row of a matrix lists one customer's money across multiple accounts. Find the largest total wealth held by any customer.

### Function Contract
**Inputs**

- `accounts`: an `m x n` matrix of non-negative integers.

**Return value**

Return the maximum row sum.

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

---

## Solution
### Approach
Scan every row, compute its sum, and keep the largest sum seen.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
