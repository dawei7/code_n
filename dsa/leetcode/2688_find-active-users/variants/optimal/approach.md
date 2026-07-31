## General

**Why adjacent timestamps are sufficient**

Partition purchases by `user_id` and sort each partition by `created_at`. If any two purchases are within seven days, then every timestamp between them divides that interval into smaller nonnegative gaps. Consequently, at least one adjacent pair in sorted order is also within seven days. It is therefore unnecessary to compare every pair.

Use `LAG` to attach the immediately preceding timestamp within the same user's ordered partition. The first row for each user has no predecessor and cannot establish activity by itself. Filter to rows whose current and previous timestamps differ by at most seven days. Equality at seven remains included, and duplicate same-time rows produce a zero-day gap.

Select distinct user IDs from the qualifying rows. This collapses multiple qualifying pairs for the same user without losing any active user. Since the contract allows any result order, no final ordering is required.

## Complexity detail

Let $R$ be the number of rows in `Users`. Partition ordering takes $O(R\log R)$ time in the general case; the window scan, filter, and deduplication are linear after sorting. Window and ordering state use $O(R)$ working space. The benchmark uses `size` as $R$ and compares this plan with a correct all-pairs self-join.

## Alternatives and edge cases

- **Self-join every user's purchases:** This directly exposes qualifying pairs but can compare $O(R^2)$ row pairs.
- **Correlated existence test:** Looking for a nearby row separately for each purchase can repeat full scans without a suitable index.
- **Minimum and maximum dates:** Comparing only a user's endpoints is wrong because two nearby purchases can coexist with distant outliers.
- Exactly seven days qualifies because the interval is inclusive.
- Duplicate purchase rows still represent two rows and form a zero-day qualifying pair.
- A single purchase cannot make its user active.
- Several qualifying pairs must still emit only one row for the user.
- Window partitioning prevents nearby timestamps from different users from forming a pair.
