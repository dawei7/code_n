## General

**Only adjacent sorted dates need comparison**

Partition purchases by user and sort each partition by `purchase_date`. For any two sorted dates with other purchases between them, every intervening adjacent gap is no larger than the full endpoint gap. Therefore, if any pair is at most seven days apart, at least one adjacent pair is also at most seven days apart.

Use `LAG` to attach the previous purchase date within each user's ordered partition. The first row for a user receives no previous date and cannot qualify by itself.

**Collapse qualifying rows to users**

Filter the ordered rows to non-null adjacent gaps of at most seven days. Same-day purchases have a zero-day gap, and the inclusive comparison retains exactly seven-day gaps. Select distinct user IDs from the remaining rows, then order them numerically.

Every emitted user has an explicit qualifying pair: the current row and its lagged predecessor. Conversely, the adjacent-gap property ensures that a user with any qualifying pair has a qualifying adjacent pair and is emitted. Distinct selection removes repeated evidence without removing a qualifying user.

## Complexity detail

Let $r$ be the number of rows in `Purchases`. Partition ordering takes $O(r\log r)$ time in the general case; the window scan, filtering, and deduplication are linear after ordering. The total time is therefore $O(r\log r)$.

Window and ordering state can hold $O(r)$ rows. Exact index use, sort strategy, and temporary storage depend on the database engine.

## Alternatives and edge cases

- **Self-join all purchases:** Comparing every pair for the same user is direct but may require $O(r^2)$ candidate comparisons.
- **Correlated existence query:** Testing every row against the whole table expresses the condition clearly but can repeat scans without a suitable composite index.
- **Group by date range:** Comparing only `MIN` and `MAX` is wrong because a user can have two nearby purchases plus a distant outlier.
- **Exactly seven days:** The boundary is inclusive, so a seven-day gap qualifies.
- **Same day:** Two distinct purchase rows on one date have a zero-day gap and qualify.
- **Single purchase:** Its lagged date is null, so the user is not emitted.
- **Several qualifying pairs:** `DISTINCT` returns the user only once.
- **Input row order:** The window's explicit date ordering makes table storage order irrelevant.
