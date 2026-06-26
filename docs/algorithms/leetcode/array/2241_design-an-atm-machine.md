# Design an ATM Machine

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2241 |
| Difficulty | Medium |
| Topics | Array, Greedy, Design |
| Official Link | [design-an-atm-machine](https://leetcode.com/problems/design-an-atm-machine/) |

## Problem Description & Examples
### Goal
Design an ATM holding banknotes of denominations `20`, `50`, `100`, `200`, and `500`. Deposits add note counts. Withdrawals must greedily use as many higher-denomination notes as possible; if that mandated strategy cannot produce the amount, return failure without changing inventory.

### Function Contract
**Inputs**

- `deposit(banknotesCount)` receives counts aligned with `[20, 50, 100, 200, 500]`.
- `withdraw(amount)` receives a positive multiple of `10` to attempt.

**Return value**

`deposit` returns nothing. A successful `withdraw` returns the dispensed counts in denomination order; failure returns `[-1]` and leaves all notes in the ATM.

### Examples
**Example 1**

- Input: deposit `[0, 0, 1, 2, 1]`, then withdraw `600`
- Output: `[0, 0, 1, 0, 1]`

**Example 2**

- Input: deposit `[0, 1, 0, 3, 1]`, then withdraw `600`
- Output: `[-1]`

**Example 3**

- Input: deposit `[1, 1, 1, 1, 1]`, then withdraw `870`
- Output: `[1, 1, 1, 1, 1]`

---

## Underlying Base Algorithm(s)
Store five inventory counts. For withdrawal, traverse denominations from `500` down to `20`, tentatively taking the smaller of available notes and `remaining / denomination`. If a remainder survives, discard the tentative plan and preserve inventory. Otherwise subtract the selected counts and return them. This intentionally does not backtrack to lower denominations.

---

## Complexity Analysis
- **Time Complexity**: `O(1)` per operation because there are five denominations
- **Space Complexity**: `O(1)`
