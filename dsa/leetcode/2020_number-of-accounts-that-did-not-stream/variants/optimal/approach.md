## General
**Identify subscriptions that touch the target year.** An interval overlaps
2021 when `start_date <= '2021-12-31'` and
`end_date >= '2021-01-01'`. This includes subscriptions that begin earlier,
finish later, or touch either boundary date.

**Build the set of accounts that streamed during 2021.** Filter `Streams` to
the inclusive target dates and deduplicate `account_id`. Left join this set to
the overlapping subscriptions, then retain rows whose joined account is
missing. Counting those rows returns the requested value, including zero when
no account qualifies.

The overlap predicate selects exactly the subscriptions active on at least one
target-year date. The filtered stream relation contains an account exactly
when it has at least one disqualifying session. Therefore, a missing joined
row is equivalent to satisfying both required conditions, and each primary-key
subscription contributes at most once.

## Complexity detail
Here $S$ and $T$ are the input row counts. With ordinary hash aggregation and
join execution, filtering and deduplicating streams plus scanning
subscriptions takes $O(S+T)$ expected time. The target-year account set uses
$O(T)$ space in the worst case. A database may instead use indexed
$O((S+T)\log T)$ operations while preserving the same relational plan.

## Alternatives and edge cases
- **Correlated `NOT EXISTS`:** This is concise and MySQL can optimize it into
  an anti-join, but an engine without a suitable index may rescan all streams
  per subscription and take $O(ST)$ time.
- **`NOT IN` subquery:** It can express the exclusion but requires careful
  null semantics; an explicit anti-join is clearer.
- Streams before or after 2021 do not disqualify an account.
- Subscriptions spanning either year boundary still overlap 2021.
- The aggregate must return one row with zero when every account streamed or
  no subscription overlaps the year.
