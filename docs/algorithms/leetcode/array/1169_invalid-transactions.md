# Invalid Transactions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1169 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [invalid-transactions](https://leetcode.com/problems/invalid-transactions/) |

## Problem Description & Examples
### Goal
Return every transaction string that is invalid because its amount is too high or because the same person has another transaction in a different city within 60 minutes.

### Function Contract
**Inputs**

- `transactions`: strings formatted as `"name,time,amount,city"`.

**Return value**

All invalid transaction strings. Order is not important.

### Examples
**Example 1**

- Input: `transactions = ["alice,20,800,mtv","alice,50,100,beijing"]`
- Output: `["alice,20,800,mtv","alice,50,100,beijing"]`

**Example 2**

- Input: `transactions = ["alice,20,1200,mtv","bob,50,100,beijing"]`
- Output: `["alice,20,1200,mtv"]`

**Example 3**

- Input: `transactions = ["alice,20,100,mtv","alice,80,100,mtv"]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Parsing, grouping, and pairwise window checks.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)` in the straightforward grouping approach.
- **Space Complexity**: `O(n)`
