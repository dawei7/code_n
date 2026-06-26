# Simple Bank System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2043 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Design, Simulation |
| Official Link | [simple-bank-system](https://leetcode.com/problems/simple-bank-system/) |

## Problem Description & Examples
### Goal
Design a bank object that supports account validation, transfers, deposits, and withdrawals.

### Function Contract
**Inputs**

- Initial `balance`: account balances using 1-based account numbers.
- Operations: `transfer(account1, account2, money)`, `deposit(account, money)`, `withdraw(account, money)`.

**Return value**

Each operation returns whether it was valid and applied.

### Examples
**Example 1**

- Input: `["Bank","withdraw","transfer","deposit","transfer","withdraw"], [[[10,100,20,50,30]],[3,10],[5,1,20],[5,20],[3,4,15],[10,50]]`
- Output: `[null,true,true,true,false,false]`

**Example 2**

- Input: `balance = [5], operations = deposit(1,4), withdraw(1,10)`
- Output: `[true,false]`

**Example 3**

- Input: `balance = [8,2], operations = transfer(1,2,3), withdraw(2,4)`
- Output: `[true,true]`

---

## Underlying Base Algorithm(s)
Store balances in an array. A helper validates that an account number is within range. Transfers and withdrawals additionally check sufficient funds before mutating balances.

---

## Complexity Analysis
- **Time Complexity**: `O(1)` per operation.
- **Space Complexity**: `O(n)`
