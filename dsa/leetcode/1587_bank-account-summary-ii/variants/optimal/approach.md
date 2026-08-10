## General

**From transaction changes to account balances**

Every account begins with balance zero. Each transaction’s `amount` is a signed change: positive amounts add money and negative amounts subtract money. Therefore, an account’s final balance is the sum of `amount` over all transaction rows carrying that account number.

The query needs two pieces from different tables:

- `Transactions` supplies the signed amounts and account identifier needed for aggregation;
- `Users` supplies the human-readable `name` required in the output.

The checked-in query joins these tables first, groups the joined transaction rows by account, calculates `SUM(amount)`, and keeps only sums strictly greater than 10000.

**Joining each transaction to its owner**

The `FROM` clause is:

`Users JOIN Transactions USING (account)`.

`USING (account)` is shorthand for an equality join on the same-named `account` column in both tables. Each transaction is matched with the user whose primary-key account number equals the transaction’s account number.

Because `Users.account` is unique, one transaction can match at most one user. Thus the join attaches a name without multiplying a transaction across several user rows. After joining, each row conceptually contains the transaction’s amount together with its owner’s name and account.

This is an inner join. A user with no transactions produces no joined row. Such a user’s balance is zero because all accounts start at zero, so that user cannot satisfy a balance greater than 10000. Excluding the user early is therefore safe.

**Grouping at the account level**

`GROUP BY account` places every joined transaction for the same bank account into one group. The selected aggregate

`SUM(amount) AS balance`

adds all signed changes in that group. Deposits increase the sum, transfers out decrease it, and the final sum is exactly the account balance.

The alias `balance` gives the calculated column the required output name. It is also reused in the `HAVING` clause.

Grouping by account rather than by transaction is necessary because an account may have many transactions. Grouping by name could also distinguish users under this particular contract because names are unique, but the account is the relational key shared by the tables and directly identifies the balance being calculated.

MySQL permits selecting `name` while grouping by `account` because `Users.account` is a primary key and functionally determines exactly one `Users.name`. Within any account group, all joined rows carry the same name. In database modes or systems that do not infer this functional dependency, grouping by both `account` and `name` would express the same result more explicitly.

**Why filtering uses `HAVING`**

The threshold applies to the completed aggregate balance, not to individual transaction amounts. `WHERE` filters rows before grouping, when `SUM(amount)` does not yet exist. `HAVING` filters groups after aggregation, so it can evaluate:

`HAVING balance > 10000`.

This distinction prevents a common error. Filtering transaction rows with `WHERE amount > 10000` would ignore combinations of smaller deposits whose total exceeds the threshold, and it would incorrectly discard negative transactions that must reduce the final balance.

The comparison is strictly greater than 10000. An account with balance exactly 10000 must not appear. The alias `balance` refers to the `SUM(amount)` result in MySQL, making the clause equivalent to `HAVING SUM(amount) > 10000`.

**Walking through the example**

Alice’s joined rows contain amounts 7000, 7000, and -3000. They form one account group, and `SUM` produces 11000. Since 11000 is greater than 10000, Alice’s group survives.

Bob’s only amount sums to 1000, so the group is removed by `HAVING`. Charlie’s two deposits and one outgoing transfer sum to 8000, so that group is also removed. The selected rows therefore contain only Alice’s name and balance.

The outgoing amounts must remain in the group. Summing only positive amounts would report 14000 for Alice instead of the correct 11000 and could qualify accounts whose actual balances are below the threshold.

**Why the result is correct**

Take any row returned by the query. Its joined rows all share one account and its unique user name. `SUM(amount)` includes every transaction matched to that account, so `balance` is the account’s final balance from its zero starting point. The `HAVING` condition proves that balance is greater than 10000. Every returned row is therefore valid.

Now take any user whose balance is greater than 10000. A positive final balance of that size implies at least one transaction, so the inner join contains all that account’s transaction rows. They are grouped together, their signed amounts sum to the true balance, and the `HAVING` comparison succeeds. The account contributes one output row with its uniquely determined name. Therefore, no qualifying user is missed.

Every account forms at most one group, so no qualifying user is duplicated. The absence of `ORDER BY` is correct because the statement accepts result rows in any order.

**What the query does not use**

`trans_id` is irrelevant because individual transaction identity does not change the sum. `transacted_on` is irrelevant because the balance includes all transactions rather than a date range. The query reads only the relationship key, the requested name, and the signed amount needed for aggregation.

## Complexity detail

Let $U$ be the number of users and $T$ the number of transactions.

SQL’s physical complexity depends on indexes and the optimizer. With primary-key access on `Users.account` and a hash or indexed join, transaction attachment can be close to $O(U+T)$ expected time, followed by aggregation proportional to the joined rows. A sort-based join or grouping plan may take $O((U+T)\log(U+T))$ time, which matches the package manifest.

The manifest’s working-space bound is $O(U+T)$ for join and grouping state in a general plan. A streaming or hash aggregation may use closer to $O(U)$ group state, while sorting can materialize a larger intermediate relation. The exact database plan should be inspected with `EXPLAIN` when operational performance matters.

The output contains at most $U$ rows, one for each account whose balance passes the strict threshold.

## Alternatives and edge cases

- **Aggregate transactions before joining:** A subquery can compute `SUM(amount)` per account, filter with `HAVING`, and then join the smaller qualifying result to `Users`. It expresses the same logic and may reduce join volume.
- **`LEFT JOIN` from users:** This would retain users without transactions and require `COALESCE` to treat their sum as zero. Since zero cannot exceed 10000, the checked-in inner join is simpler and sufficient.
- **Filtering with `WHERE amount > 10000`:** This is incorrect because the condition belongs to the total balance, not each transaction. It also drops negative adjustments that must be included.
- **Summing only deposits:** Negative amounts represent outgoing money and are part of the balance. Ignoring them can falsely qualify an account.
- **Balance exactly 10000:** The strict `> 10000` condition rejects it. Replacing it with `>=` would violate the statement.
- **No transactions for a user:** The inner join omits the user. Their starting balance remains zero, so omission is correct.
- **One transaction:** The account qualifies exactly when that signed amount is greater than 10000.
- **Many transactions:** Every joined row in the account group contributes once to `SUM(amount)`, regardless of date or transaction identifier.
- **Net negative balance:** The signed sum is negative and cannot pass the positive threshold.
- **Unique account key:** It prevents a transaction from joining to multiple names and makes `name` functionally dependent on the grouping column.
- **Unique names:** The contract also says names do not repeat, but the query correctly groups by account, the actual balance identity.
- **Strict SQL grouping modes:** MySQL can infer that primary-key `account` determines `name`. For portability, write `GROUP BY account, name` if the database requires every selected nonaggregate column to appear explicitly.
- **Alias use in `HAVING`:** MySQL permits `HAVING balance > 10000`. A dialect that does not allow select aliases there should repeat `SUM(amount)`.
- **`USING (account)` support:** It is standard shorthand when both inputs share the same column name. An explicit `ON Users.account = Transactions.account` is equivalent and more portable across unusual dialects.
- **Output order:** No ordering is promised or needed. Add `ORDER BY` only if a consumer imposes a separate presentation requirement.
