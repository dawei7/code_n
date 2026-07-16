# Bank Account Summary II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1587 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/bank-account-summary-ii/) |

## Problem Description
### Goal

The `Users` table associates each bank account with its uniquely named owner. The `Transactions` table records changes to account balances: a positive `amount` adds money and a negative `amount` removes money. Every account begins with a zero balance.

Compute each account's balance as the sum of all its transaction amounts. Report the owner's name and resulting balance only when that balance is strictly greater than `10000`. A balance equal to the threshold does not qualify.

Return the qualifying rows in any order.

### Function Contract
**Inputs**

- `Users(account, name)`: one row per account; `account` is unique, and user names are also distinct.
- `Transactions(trans_id, account, amount, transacted_on)`: transaction rows keyed by `trans_id`; `account` identifies the affected user, and signed `amount` records the balance change.

Let $U$ be the number of users and $T$ the number of transactions.

**Return value**

Return columns `name` and `balance`, with one row for every user whose summed transaction amount is greater than `10000`.

### Examples
**Example 1**

- Input: Alice has amounts `7000`, `7000`, and `-3000`; Bob has `1000`; Charlie has `6000`, `6000`, and `-4000`
- Output: `[Alice, 11000]`

**Example 2**

- Input: one account has a single transaction of `10000`
- Output: an empty result because the comparison is strict

**Example 3**

- Input: Ann has `15000` and `-4000`, while Ben has `9000` and `2000`
- Output: `[Ann, 11000]` and `[Ben, 11000]`

### Required Complexity

- **Time:** $O((U+T)\log(U+T))$
- **Space:** $O(U+T)$

<details>
<summary>Approach</summary>

#### General

**Attach every transaction to its owner**

Inner-join `Users` and `Transactions` on `account`. Each joined row now carries the user name and one signed balance change. Users without transactions cannot have a positive balance above the threshold, so excluding them is correct.

**Aggregate before applying the threshold**

Group the joined rows by the account key and name, then compute `SUM(transactions.amount)`. Grouping by the unique account prevents different users from being merged; including `name` makes the selected non-aggregate column explicit and portable.

Apply `HAVING SUM(...) > 10000` after aggregation. A `WHERE amount > 10000` filter would be wrong because qualification depends on the net sum: several smaller deposits can qualify, and a withdrawal can reduce an otherwise large deposit below the threshold.

Alias the aggregate as `balance`. The join supplies exactly the transactions for each account, signed summation reconstructs its balance from the guaranteed zero starting point, and `HAVING` retains exactly the balances satisfying the strict inequality. Therefore every returned row, and only every returned row, meets the contract.

#### Complexity detail

Let $U$ and $T$ be the table sizes. Hash-based join and aggregation can approach $O(U+T)$ expected time. A portable sort-based upper bound for joining and grouping is $O((U+T)\log(U+T))$.

Join and aggregation state may retain $O(U+T)$ rows or hash entries.

#### Alternatives and edge cases

- **Aggregate transactions first:** group `Transactions` by account in a subquery, filter its sums, then join the qualifying balances to `Users`. It has the same principal complexity and avoids carrying names through aggregation.
- **Correlated sum per user:** compute a scalar `SUM` subquery for each account. It is correct, but without a supporting index it can rescan all $T$ transactions for each of $U$ users and take $O(UT)$ time.
- **Filter individual amounts:** applying the threshold in `WHERE` tests transactions rather than final balances and produces incorrect results.
- **Exactly `10000`:** exclude the account because the required balance is strictly higher.
- **Negative amounts:** withdrawals must remain in the sum; do not filter them out.
- **Several qualifying users:** return one aggregate row per account.
- **User without transactions:** the zero starting balance cannot qualify, so omission by the inner join is correct.
- **Transaction dates:** `transacted_on` does not affect the all-time balance.
- **Output order:** no `ORDER BY` clause is required.

</details>
