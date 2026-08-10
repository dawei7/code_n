## General

**Turn consecutive dates into equal group keys**

For each customer, sort transactions by `transaction_date` and assign row numbers one, two, three, and so on.

On a run of consecutive days, both the date and row number advance by one each row. Subtracting the row number in days from the date therefore remains constant throughout the run.

For example, dates May 1, May 2, and May 3 with row numbers one, two, and three all map to April 30. A gap breaks this equality.

**First CTE computes the islands key**

CTE `s` selects `customer_id` and:

`DATE_SUB(transaction_date, INTERVAL ROW_NUMBER() ... DAY)`.

The window partitions by customer, so row numbering restarts independently for every customer. Ordering by date makes the offset technique meaningful.

The aliased output column is also called `transaction_date`, but it is no longer the original date. It is the derived group identifier for a consecutive island.

**Why unique customer-date rows matter**

The schema guarantees each customer has at most one transaction on a date. Therefore advancing to the next row corresponds to advancing to a distinct later date.

If duplicate dates existed, row number would increase while date did not, splitting or distorting islands. The uniqueness guarantee prevents that issue.

**Second CTE counts each streak**

CTE `t` groups by `customer_id` and the derived date key. Every group is one maximal consecutive-date streak for that customer.

`COUNT(1) AS cnt` is the number of transaction days in that streak. Amount and transaction ID are irrelevant to consecutive length.

A customer with dates May 1–3 and May 7–8 produces two rows in `t`, with counts three and two.

**Find the global maximum streak length**

The scalar subquery:

`SELECT MAX(cnt) FROM t`

finds the largest streak among every customer and every island.

The outer query keeps rows whose `cnt` equals that global value. This correctly includes ties: several customers may own streaks of the same maximum length.

**Order by customer ID**

`ORDER BY customer_id` uses ascending order by default, meeting the requested output ordering.

**Trace the example**

Customer 101's May 1, 2, and 3 rows receive one constant offset key and group count three.

Customer 102's May 1 is separated from May 3 and 4. Its groups have counts one and two.

Customer 105 has a three-day group. The maximum count in `t` is three, so the outer query selects customers 101 and 105 and sorts them ascending.

**Why the offset identifies maximal runs**

Within consecutive dates, `date - row_number` stays constant. Across a gap of at least two days, the date increases by more than the row number's one-day increment, so the key changes.

Because rows are ordered, a key change separates streaks. Could two later separated streaks accidentally regain the same key? Each gap permanently increases the offset by the number of skipped days, so the value cannot revert. Grouping by it is safe.

**A material behavior of the exact query**

The outer select does not use `DISTINCT customer_id`. It returns one row per maximum-length streak in `t`, not explicitly one row per customer.

If one customer has two separate streaks and both tie the global maximum, that customer can appear twice. The natural-language request says to find all customer IDs, which normally implies one row per customer. Adding `SELECT DISTINCT customer_id` or grouping the outer result would enforce that interpretation.

The protected source is taught exactly here: it is correct when each qualifying customer has one globally maximal streak, including the provided example, but it does not deduplicate the unusual multiple-max-streak case.


Apart from that output multiplicity caveat, every row in `t` is exactly one maximal consecutive sequence and `cnt` is its exact length. Filtering against the maximum therefore identifies precisely the globally longest streak rows.

## Complexity detail

Let $n$ be the transaction count. The window function generally requires ordering rows by customer and date, costing $O(n\log n)$ without a supporting order. Grouping derived keys and finding the maximum are typically $O(n)$ expected with hashing or $O(n\log n)$ with sorting.

A safe logical summary is $O(n\log n)$ time and $O(n)$ intermediate space, matching the manifest. Actual MySQL execution depends on indexes, optimizer choices, materialization, and disk spilling.

The final output size is the number of maximum streak rows, which may exceed the number of distinct qualifying customers in the caveat above.

## Alternatives and edge cases

- **LAG plus running group number:** Detect date gaps explicitly, cumulatively label islands, then group; more verbose but equally valid.
- **Recursive date walking:** Unnecessary and often slower than window-based islands and gaps.
- **Single transaction:** Forms a streak of length one.
- **Several customers tied:** All maximum streak rows pass the equality filter.
- **Multiple streaks for one customer:** They receive different offset keys and are counted separately.
- **Duplicate qualifying customer:** Exact query may output it twice if two of its streaks tie the global maximum.
- **Unique customer-date guarantee:** Essential to the simple row-number offset.
- **Large gap:** Changes the derived key and starts a new island.
- **Amount values:** Do not affect streak membership or length.
- **Output order:** Ascending customer ID is explicit, but uniqueness is not.
