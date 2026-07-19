# Count Salary Categories

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1907 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Count Salary Categories](https://leetcode.com/problems/count-salary-categories/) |

## Problem Description

### Goal

The `Accounts` table contains one row per bank account and records that account's monthly `income`. Classify every account into exactly one salary category: `"Low Salary"` for income strictly below `20000`, `"Average Salary"` for income from `20000` through `50000` inclusive, and `"High Salary"` for income strictly above `50000`.

Return one row for each of these three category names with the number of matching accounts. All three rows are mandatory even when a category has no accounts, in which case its count must be zero. Result row order is unrestricted.

### Function Contract

**Input table**

- `Accounts(account_id, income)`
- `account_id` is the table's unique primary key.
- `income` is the account's monthly income.

**Return value**

Return columns `category` and `accounts_count`, with exactly one row for each required salary category and its count.

### Examples

**Example 1**

- Input rows: `(3, 108939)`, `(2, 12747)`, `(8, 87709)`, `(6, 91796)`
- Output rows: `("Low Salary", 1)`, `("Average Salary", 0)`, `("High Salary", 3)`

**Example 2**

- Input rows: `(1, 20000)`, `(2, 50000)`
- Output rows: `("Low Salary", 0)`, `("Average Salary", 2)`, `("High Salary", 0)`

**Example 3**

- Input: an empty `Accounts` table
- Output: all three categories with count `0`
