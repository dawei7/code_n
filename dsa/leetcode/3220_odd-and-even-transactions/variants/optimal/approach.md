## General

Group rows by `transaction_date` so each output row represents one day. Inside each group, use two conditional `SUM` expressions. The odd expression contributes `amount` only when `amount % 2 = 1`; the even expression contributes it only when the remainder is zero.

Each `CASE` uses `ELSE 0`. Consequently, a group containing no amount of a requested parity still sums explicit zeroes and returns `0`, satisfying the contract without a separate join or `COALESCE`. Since every transaction belongs to exactly one date and exactly one parity branch, the two aggregates contain precisely the required amounts. Finally, `ORDER BY transaction_date` establishes the required ascending result order.

## Complexity detail

Let $r$ be the row count and $d$ the number of distinct dates. A conventional engine can group and order in $O(r\log r)$ time and retain $O(d)$ aggregate state; physical indexes and hash aggregation may improve the grouping phase. The query scans the source only once.

## Alternatives and edge cases

- **Two grouped subqueries plus a join:** This can produce the same columns but scans or aggregates the table twice and needs null handling for missing parities.
- **Correlated sums per date:** Rechecking the table for each distinct date can degrade toward $O(rd)$ work.
- A date containing only odd amounts must return `even_sum = 0`, not `NULL`.
- A date containing only even amounts must return `odd_sum = 0`.
- Multiple transactions with the same amount remain separate rows and all contribute to the sum.
- The final `ORDER BY` is required even if the input happens to arrive chronologically.
