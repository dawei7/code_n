## General

**Produce one group per transaction date.** The query groups source rows by `transaction_date`. Every date that appears in the table becomes one output row. The two requested totals are computed independently inside that same group.

`GROUP BY 1` uses positional notation: the first selected expression is `transaction_date`, so this is equivalent to grouping by the named date column.

**Use conditional aggregation for odd amounts.** The expression

`IF(amount % 2 = 1, amount, 0)`

returns the amount for an odd transaction and zero otherwise. `SUM` adds those selected values across the date group, yielding `odd_sum`.

The zero in the false branch is important. If a date has no odd transactions, every row contributes zero and the sum is numeric zero. A formulation that returned `NULL` might produce null instead, violating the requirement to display zero.

**Compute the even total in the same scan.** The second expression tests `amount % 2 = 0`. Even rows contribute their amount; odd rows contribute zero. Its sum becomes `even_sum`.

Every nonnegative integer is exactly one of odd or even, so each transaction amount contributes to exactly one of the two totals. No join or separate per-parity query is needed.

**Why grouping after the conditions is correct.** Consider one date group with rows $r_1,\ldots,r_q$. Conditional aggregation applies a projection to each row—either its amount or zero—then sums. This is algebraically the same as filtering the odd rows and summing them, while retaining the group even if no odd row exists. The even expression does the symmetric operation. Both see exactly the same date partition.

**Trace July 1.** Amounts $150$ and $200$ have remainder zero and contribute to `even_sum`. Amount $75$ has remainder one and contributes to `odd_sum`. The resulting row is date July 1, odd total $75$, even total $350$.

On July 2, both $300$ and $50$ are even. The odd conditional returns zero for both rows, so its sum is zero rather than null. The even sum is $350$.

**Order output dates explicitly.** `ORDER BY 1` sorts by the first selected column, `transaction_date`. Ascending is the default, so results appear chronologically from earliest to latest. Grouping alone does not promise an output order; the explicit clause is necessary.

**The transaction ID does not affect aggregation.** `transaction_id` uniquely identifies rows but is neither selected nor grouped. Each physical row still contributes once to its date's conditional sums. Multiple transactions with the same amount are separate rows and each contributes.

**A sign-sensitive detail in the exact predicate.** In MySQL-style arithmetic, a negative odd value can have remainder $-1$ for `amount % 2` rather than $1$. The exact odd test `= 1` would then fail to classify it, while the even test is also false. The local schema description does not explicitly state that `amount` is positive or nonnegative.

The source is correct for the sample and ordinary nonnegative transaction amounts. If negative amounts are legal, a robust odd predicate is `amount % 2 <> 0` or `ABS(amount) % 2 = 1`. This is a genuine contract sensitivity of the exact query.

## Complexity detail

Let $r$ be the number of transaction rows and $d$ the number of distinct dates. Every row must be read and assigned to a date group. Hash aggregation can perform this in expected $O(r)$ time with $O(d)$ group state. Sort-based grouping may cost $O(r\log r)$ time.

The final `ORDER BY` sorts $d$ result rows in $O(d\log d)$ time. Because $d\le r$, the manifest's broad $O(r\log r)$ time bound covers common execution strategies. The two numeric accumulators per date require $O(d)$ logical aggregation space, matching the manifest.

Actual SQL execution depends on indexes and the engine's plan. An index ordered by `transaction_date` may allow streaming groups and already ordered output with less temporary work.

## Alternatives and edge cases

- **Standard `CASE` expressions:** `SUM(CASE WHEN amount % 2 <> 0 THEN amount ELSE 0 END)` is more portable than MySQL `IF` and handles negative odd remainders when using `<> 0`.
- **Two aggregate subqueries joined by date:** One can filter odds and evens separately, but full outer handling is needed to preserve dates missing one parity. Conditional aggregation is simpler.
- **`UNION ALL` then regroup:** Tag parity totals in separate branches and combine them. It repeats work and still needs zero filling.
- **Date with only odd amounts:** `even_sum` is zero because every even conditional returns zero.
- **Date with only even amounts:** `odd_sum` is zero symmetrically.
- **Several identical transactions:** Unique transaction IDs make them distinct rows, and all amounts contribute.
- **Amount zero:** Zero is even and contributes zero; the even total remains numerically correct.
- **Negative odd amount:** The exact `% 2 = 1` predicate may miss it under MySQL remainder semantics. Use a nonzero remainder test if negatives belong to the domain.
- **Negative even amount:** Its remainder is zero and it contributes to the even sum.
- **No transactions:** No date groups exist, so the result is empty.
- **Missing calendar dates:** The query outputs only dates present in the table; it does not generate zero rows for absent days.
- **Null amounts:** `IF` conditions involving null are not true and return zero here, effectively ignoring such values. A nullable schema would need an explicit policy.
- **Ordering:** `ORDER BY 1` is positional and depends on transaction date remaining the first selected expression.
- **No rounding:** Amounts are integers and requested totals are exact sums.
