## General

**Turn two existence requirements into grouped counts**

The output needs one row per user who has at least one `'Refinance'` loan and at least one `'Mortgage'` loan. Other loan types neither help nor disqualify the user.

The query groups all loan rows by `user_id`. Within each group, MySQL evaluates comparison expressions as numeric Boolean values:

- `loan_type = 'Refinance'` is one for a matching row and zero for another non-null type;
- `loan_type = 'Mortgage'` behaves similarly.

Summing each expression therefore counts rows of that target type.

The `HAVING` clause requires both sums to be greater than zero. This exactly means both loan categories exist at least once in the user’s group.

**Why `HAVING` is the right stage**

`WHERE` can filter individual loan rows but cannot by itself assert that one user has rows in two different categories. `HAVING` evaluates after all of a user’s rows have been collected and the two sums have been computed.

The logical flow is:

1. partition loan rows by user;
2. count refinance matches in each partition;
3. count mortgage matches in each partition;
4. retain partitions with both counts positive;
5. output the partition key once.

Because each group yields at most one output row, `user_id` values are automatically distinct. A separate `DISTINCT` is unnecessary.

**Why unrelated loan types are harmless**

An `'AutoLoan'` row contributes zero to both sums. It remains in the group but does not change either existence test. This is faithful to “at least one” requirements: extra categories do not invalidate a qualifying user.

Repeated loans of a target type contribute multiple ones, but the predicate only asks whether the sum is greater than zero. One and ten both satisfy it, so duplicates do not alter membership.

**Trace the sample**

User 101 has one Mortgage but no Refinance. Its sums are one and zero, so the conjunction fails. User 102 has at least one of each, so both sums are positive and the group survives. User 103 has only Refinance, and user 104 only Mortgage, so each fails one side.

The result contains user 102 once, regardless of its third unrelated loan.

**The exact source differs slightly from the manifest wording**

The manifest summary describes a “filtered distinct count.” The executable SQL does not use `COUNT(DISTINCT loan_type)` and does not prefilter to the two target categories. It uses two independent Boolean sums over all rows.

This is not a correctness problem. In fact, the two-sum form makes the separate existence conditions explicit and does not depend on a distinct-count value equaling two. The approach document follows these exact expressions.

**Ordering**

`ORDER BY 1` sorts the first selected column, `user_id`, ascending by default. This satisfies the required output order. Numeric user IDs therefore appear from smallest to largest.


If a user is returned, the first positive sum proves at least one row in its group has loan type Refinance, and the second proves at least one row has Mortgage. Thus every output user qualifies.

If a user qualifies, each required row contributes one to its corresponding sum. Both sums are positive, so the group passes `HAVING` and is returned. This proves completeness.

**MySQL-specific Boolean aggregation**

The concise syntax relies on MySQL converting true and false comparisons to one and zero in numeric context. In SQL dialects without that behavior, the portable form is:

`SUM(CASE WHEN loan_type = 'Refinance' THEN 1 ELSE 0 END)`.

The solution file is explicitly MySQL, so its shorter expression is valid.

If `loan_type` were `NULL`, each comparison would yield `NULL` and `SUM` would ignore it. Such a row would contribute to neither target count, which is a reasonable existence interpretation. The enum-like source data is intended to contain named types.

## Complexity detail

Let $R$ be the loan-row count and $U$ the number of users. A hash aggregation can scan rows and update two counters per user in expected $O(R)$ time with $O(U)$ group space. A sort-based implementation may take $O(R\log R)$ time.

The final ordering of at most $U$ qualifying users costs $O(U\log U)$. The manifest’s $O(R\log R)$ time and $O(R)$ worst-case space safely cover both because $U\le R$. Actual execution depends on indexes and MySQL’s grouping plan.

## Alternatives and edge cases

- **`COUNT(DISTINCT loan_type) = 2` after filtering:** This is equivalent if a `WHERE loan_type IN (...)` filter is added, but the exact query uses two Boolean sums.
- **Self-join Loans:** Joining one Mortgage row to one Refinance row per user proves existence but can multiply duplicates and then require `DISTINCT`.
- **Two correlated `EXISTS` tests:** They are readable and can use indexes, but grouping scans all user evidence in one relation.
- **Only one required type:** One sum is zero, so the conjunction correctly rejects the user.
- **Many loans of both types:** Positive sums remain sufficient and the grouped output still contains one row.
- **Unrelated categories:** They contribute zero to both sums and do not disqualify anyone.
- **Null loan type:** It contributes to neither sum under MySQL’s three-valued logic.
- **Dialect portability:** Replace Boolean sums with `CASE` expressions outside MySQL.
- **Output order:** `ORDER BY 1` provides ascending distinct user IDs.
