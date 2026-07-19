## General
**Deduplicate requests by directed pair**

Select distinct `(sender_id, send_to_id)` combinations from `FriendRequest`. Dates describe repeated events and do not create additional pairs in the denominator.

**Deduplicate acceptances independently**

Select distinct `(requester_id, accepter_id)` combinations from `RequestAccepted`. This gives the numerator without allowing repeated acceptance events to inflate it.

**Divide with decimal and zero-safe arithmetic**

Count the two deduplicated relations, convert the division to non-integer arithmetic, and protect the request count with `NULLIF`. Replace a null quotient with zero, then round the final rate to two decimal places.

**Why the rate is exact**

Each directed pair contributes at most one row to its deduplicated relation, matching the problem's definitions of total requests and total acceptances. Their counts are therefore the exact denominator and numerator. Decimal division forms the requested ratio, while the explicit zero case defines the only otherwise undefined denominator.

## Complexity detail
For `R` request rows and `A` acceptance rows, distinct grouping generally uses hashing or sorting in $O((R + A) \log(R + A))$ time and $O(R + A)$ working space. The scalar counts and division are constant additional work.

## Alternatives and edge cases
- **Group by each pair:** produces the same deduplicated relations as `SELECT DISTINCT`.
- **Concatenate identifiers for `COUNT(DISTINCT ...)`:** can collide unless the encoding is unambiguous; grouping separate columns is safer.
- **Correlated earliest-event filtering:** can deduplicate pairs but may rescan each event table per row and take quadratic time.
- **Count raw rows:** is incorrect when a pair appears on several dates.
- **Integer division:** can truncate every proper fraction to zero; force decimal arithmetic.
- **No requests:** return zero rather than null or division-by-zero.
- **Repeated request dates:** still contribute one denominator pair.
- **Repeated acceptance dates:** still contribute one numerator pair.
- **Rounding:** round the final ratio to two decimal places.
