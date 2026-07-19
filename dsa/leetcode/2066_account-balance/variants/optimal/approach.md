## General
**Convert transaction types into signed changes**

Use a `CASE` expression to keep a deposit's `amount` positive and negate a withdrawal's amount. This turns the account balance into a running sum of signed transaction changes.

**Use an account-partitioned running window**

Apply `SUM(...) OVER (...)`, partitioning rows by `account_id` and ordering each partition by `day`. Because `(account_id, day)` is unique, each window position corresponds to exactly one transaction and its cumulative sum is the balance immediately afterward. Finally, order the produced rows by account and day; the window's logical ordering defines the calculation, while the query-level `ORDER BY` guarantees the required presentation order.

Within each account, the signed changes through a row's date are precisely all deposits minus all withdrawals made up to that moment. Their cumulative sum therefore equals the promised account balance. Partitioning prevents transactions from another account from entering that sum, so every output row receives exactly its own account's correct running balance.

## Complexity detail
Ordering the $R$ rows for window evaluation and final output costs $O(R\log R)$ time in the general case. The database may retain sorted rows and window state proportional to the input, giving $O(R)$ auxiliary space. A matching index can reduce physical sorting work, but the stated bound does not assume one.

## Alternatives and edge cases
- **Correlated prefix subquery:** Summing all earlier transactions separately for every row is correct, but it can rescan the table and require $O(R^2)$ time.
- **Self-join and aggregation:** Joining each transaction to all earlier rows of the same account also computes the balance, but materializes the same quadratic relationship.
- The first transaction of an account starts from zero rather than inheriting another account's balance.
- A withdrawal contributes a negative change even though `amount` itself is stored as a positive number.
- A balance may become exactly zero; the contract only rules out negative balances.
- Input row order is irrelevant because both the window and result explicitly order by `day`.
