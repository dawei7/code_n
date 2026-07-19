# Bank Account Summary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1555 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/bank-account-summary/) |

## Problem Description
### Goal
The `Users` table stores each bank user's current starting credit. Every row in `Transactions` records money transferred from `paid_by` to `paid_to`: the amount must be subtracted from the payer's credit and added to the recipient's credit.

Report every user with the resulting balance after all transactions and indicate whether the credit limit has been breached. A limit is breached only when the final credit is strictly below zero, producing `"Yes"`; zero or a positive balance produces `"No"`. Users without any transaction must still appear with their original credit. Result order is unrestricted.

### Function Contract
**Inputs**

- `Users(user_id, user_name, credit)`: $u$ users keyed by the unique `user_id`.
- `Transactions(trans_id, paid_by, paid_to, amount, transacted_on)`: $t$ transfers keyed by the unique `trans_id`.
- Let $N=u+t$ be the total number of source rows.

**Return value**

A table with columns `user_id`, `user_name`, `credit`, and `credit_limit_breached`. The credit is the starting value plus all received amounts minus all paid amounts. The final column is `"Yes"` exactly for negative balances and `"No"` otherwise.

### Examples
**Example 1**

- Input: users Moustafa, Jonathan, Winston, and Luis, with transfers of 400 from Moustafa to Winston, 500 from Winston to Jonathan, and 200 from Jonathan to Moustafa
- Output: balances `-100`, `500`, `9900`, and `800`, respectively
- Explanation: Luis remains unchanged; only Moustafa finishes below zero and receives `"Yes"`.

**Example 2**

- Input: a user with credit zero and no transactions
- Output: that user with credit zero and `credit_limit_breached = "No"`
- Explanation: The breach test is strictly less than zero.

**Example 3**

- Input: one user pays 75 and receives 20 from separate users
- Output: the starting credit adjusted by a net change of `-55`
- Explanation: Incoming and outgoing amounts contribute with opposite signs.
