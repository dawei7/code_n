## General
**Attach every transaction to its owner**

Inner-join `Users` and `Transactions` on `account`. Each joined row now carries the user name and one signed balance change. Users without transactions cannot have a positive balance above the threshold, so excluding them is correct.

**Aggregate before applying the threshold**

Group the joined rows by the account key and name, then compute `SUM(transactions.amount)`. Grouping by the unique account prevents different users from being merged; including `name` makes the selected non-aggregate column explicit and portable.

Apply `HAVING SUM(...) > 10000` after aggregation. A `WHERE amount > 10000` filter would be wrong because qualification depends on the net sum: several smaller deposits can qualify, and a withdrawal can reduce an otherwise large deposit below the threshold.

Alias the aggregate as `balance`. The join supplies exactly the transactions for each account, signed summation reconstructs its balance from the guaranteed zero starting point, and `HAVING` retains exactly the balances satisfying the strict inequality. Therefore every returned row, and only every returned row, meets the contract.

## Complexity detail
Let $U$ and $T$ be the table sizes. Hash-based join and aggregation can approach $O(U+T)$ expected time. A portable sort-based upper bound for joining and grouping is $O((U+T)\log(U+T))$.

Join and aggregation state may retain $O(U+T)$ rows or hash entries.

## Alternatives and edge cases
- **Aggregate transactions first:** group `Transactions` by account in a subquery, filter its sums, then join the qualifying balances to `Users`. It has the same principal complexity and avoids carrying names through aggregation.
- **Correlated sum per user:** compute a scalar `SUM` subquery for each account. It is correct, but without a supporting index it can rescan all $T$ transactions for each of $U$ users and take $O(UT)$ time.
- **Filter individual amounts:** applying the threshold in `WHERE` tests transactions rather than final balances and produces incorrect results.
- **Exactly `10000`:** exclude the account because the required balance is strictly higher.
- **Negative amounts:** withdrawals must remain in the sum; do not filter them out.
- **Several qualifying users:** return one aggregate row per account.
- **User without transactions:** the zero starting balance cannot qualify, so omission by the inner join is correct.
- **Transaction dates:** `transacted_on` does not affect the all-time balance.
- **Output order:** no `ORDER BY` clause is required.
