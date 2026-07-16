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

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Turn every transfer into signed balance changes**

Project each transaction twice with `UNION ALL`: emit `-amount` for `paid_by` and `+amount` for `paid_to`. `UNION ALL` is essential because repeated equal changes are separate transfers and must not be deduplicated.

**Aggregate one net change per involved user**

Group the signed rows by `user_id` and sum them. This produces the exact total received minus total paid for every user who appears in at least one transaction.

**Preserve users without transactions**

Left-join the net changes to `Users`. Replace a missing aggregate with zero using `COALESCE`, add it to the stored credit, and apply the same expression in a `CASE` test for negativity. Every transaction contributes once negatively and once positively, so the aggregate gives each user exactly the required net movement. The left join then covers both involved and uninvolved users.

The source permits any result order; the local query orders by `user_id` only to make fixtures and display deterministic.

#### Complexity detail

The signed intermediate relation contains $2t$ rows. Grouping and deterministic output ordering have a portable upper bound of $O(N\log N)$ time. The signed rows, grouped changes, and sorting workspace can use $O(N)$ auxiliary space. Hash aggregation may make the expected physical work closer to linear.

#### Alternatives and edge cases

- **Two separate aggregate joins:** independently sum outgoing and incoming transfers, then join both totals to users; this is correct but more verbose.
- **Correlated subqueries per user:** compute incoming and outgoing sums separately for every user, which can repeat transaction scans and approach $O(ut)$ time.
- **Inner join to transactions:** this incorrectly omits users who never paid or received money.
- A final balance of exactly zero does not breach the limit.
- A user can have only incoming or only outgoing transactions.
- Multiple transfers between the same users must all be counted.
- Transaction dates do not affect the final all-time balance.
- `UNION` without `ALL` could discard duplicate signed changes.
- User names do not need to be unique because grouping and joining use `user_id`.

</details>
