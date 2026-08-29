## General

**Convert each transaction to a signed change**

A deposit increases balance, while a withdrawal decreases it. The query transforms one row with

`IF(type = 'Deposit', amount, -amount)`.

Because `type` is restricted to Deposit or Withdraw, the true branch covers deposits and the false branch covers withdrawals.

The starting balance is zero, so the balance after a transaction is the cumulative sum of these signed changes up to that row.

**Keep accounts independent with partitioning**

The window clause uses `PARTITION BY account_id`. Each account receives its own running-sum sequence beginning conceptually from zero.

Transactions from another account never enter the current account's balance, even when their dates interleave globally.

**Put transactions in chronological order**

Within each account partition, `ORDER BY day` arranges changes from earliest to latest.

The window `SUM` at a row includes the current signed change and all preceding changes in that ordered partition. It therefore reports the balance immediately after that day's transaction.

The composite primary key `(account_id,day)` guarantees that one account cannot have two transactions on the same day. There are no within-account order ties, so the cumulative order is deterministic.

**Understand the default window frame**

The query does not spell out `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. MySQL supplies its default ordered window frame.

Because `day` is unique within each account, the default peer-aware behavior contains exactly the earlier dates plus the current row. There are no equal-day peers that could be included together unexpectedly.

An explicit `ROWS` frame would make the intent clearer but produces the same result under the primary-key guarantee.

**Trace account one**

The signed changes are positive 2000, negative 1000, and positive 3000 in day order.

Their running sums are:

- `0 + 2000 = 2000`;
- `2000 - 1000 = 1000`;
- `1000 + 3000 = 4000`.

These are exactly the three output balances.

**Why withdrawals never make balance negative**

The source does not validate transaction legality or clamp balances. It trusts the statement's guarantee that account balances never fall below zero.

The negative signed amount remains essential; the guarantee describes the data, not a different arithmetic rule.

**Order the final report**

The outer `ORDER BY 1, 2` refers to the first and second selected expressions: `account_id` and `day`.

This sorts accounts ascending and, within an account, dates ascending as required. Window ordering determines calculation order, while outer ordering determines presentation order; both are necessary concepts even though they use the same day sequence.

These two orderings solve different problems. Removing the window's `ORDER BY day` would turn the sum into a whole-partition total rather than a running balance. Removing the outer `ORDER BY` could leave every balance numerically correct but present rows in an unspecified order. The query includes both, so it satisfies both calculation and reporting semantics.

**Why every output row is correct**

For any transaction row, its partition contains exactly that account's records. The window order places exactly earlier transactions before it. Summing their signed effects plus the current effect starts from the stipulated zero balance and performs every account change in order.

Thus the computed value is the balance after that transaction. Every source row produces one output row, and final sorting satisfies the report order.

**Why no grouping is used**

`GROUP BY` would collapse several transaction rows into one account summary. The task needs a balance after each transaction, so window aggregation is the correct tool: it aggregates context while preserving every row.

**Deposits and withdrawals share one recurrence**

After converting types to signed amounts, no later logic needs to branch on transaction type. If `b` is the balance after the previous row and `d` is the current signed change, the new balance is simply `b+d`. The running `SUM` applies this recurrence to every account from its first transaction onward.

This transformation is why one window expression can handle arbitrary alternating sequences of deposits and withdrawals while still outputting each intermediate state.

## Complexity detail

Let $R$ be the number of transaction rows. A general execution plan sorts rows for partitioned day order and final output, costing $O(R\log R)$ time in the worst case. Window accumulation itself is linear after ordering.

Sorting and window processing can require $O(R)$ working space. A suitable index on `(account_id,day)` may let the database reuse ordered access and reduce explicit sort work, but the SQL source does not mandate a physical plan.

## Alternatives and edge cases

- **Explicit `ROWS` frame:** State `ROWS UNBOUNDED PRECEDING` to make cumulative-row semantics explicit.
- **Correlated subquery:** Sum all earlier transactions per row, but can become quadratic without optimization.
- **User variables:** Can simulate running totals in MySQL but are more fragile than window functions.
- **First transaction:** Its balance equals its signed amount because the initial balance is zero.
- **Withdrawal:** Contributes negative amount.
- **Deposit:** Contributes positive amount.
- **Withdraw entire balance:** Running sum may become exactly zero.
- **Several accounts:** Partitions reset accumulation independently.
- **Same day across different accounts:** Harmless because they are in separate partitions.
- **Same account and day:** Excluded by the composite primary key.
- **Final ordering:** `ORDER BY 1,2` uses selected column ordinals.
- **No mutation:** The query reads transactions and returns derived balances.
