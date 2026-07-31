# Design an ATM Machine

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2241 |
| Difficulty | Medium |
| Topics | Array, Greedy, Design |
| Official Link | [LeetCode](https://leetcode.com/problems/design-an-atm-machine/) |

## Problem Description

### Goal

Design an ATM that stores banknotes in exactly five denominations: $20$, $50$,
$100$, $200$, and $500$. Its inventory starts empty. Deposits add supplied
counts in that denomination order, and successive operations share the same
inventory.

For a withdrawal, the ATM must greedily take as many available notes as
possible from the largest denomination before considering the next smaller
one. It may not replace an already preferred large note with smaller notes to
make a request succeed. If the greedy selection cannot form the exact amount,
return `[-1]` and leave the complete inventory unchanged. Otherwise, remove and
return the selected note counts in ascending denomination order.

### Function Contract

**Inputs**

- `operations`: A sequence beginning with `ATM`, followed by `deposit` and `withdraw` calls.
- `arguments`: Arguments aligned with the operations. A deposit receives five nonnegative counts; a withdrawal receives one positive amount.

At most 5,000 deposit and withdrawal calls occur. Each deposited count and
withdrawal amount is at most $10^9$, and the total number of deposited notes
does not exceed $10^9$.

**Return value**

Return one result per operation: `null` for construction and deposits, a
five-element note-count array for a successful withdrawal, or `[-1]` for a
rejected withdrawal.

### Examples

**Example 1**

- Input: `operations = ["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"]`, `arguments = [[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]]`
- Output: `[null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]`

**Example 2**

- Input: `operations = ["ATM", "deposit", "withdraw"]`, `arguments = [[], [[1,1,1,1,1]], [870]]`
- Output: `[null, null, [1,1,1,1,1]]`

**Example 3**

- Input: `operations = ["ATM", "deposit", "withdraw", "withdraw"]`, `arguments = [[], [[0,0,0,3,1]], [600], [500]]`
- Output: `[null, null, [-1], [0,0,0,0,1]]`
