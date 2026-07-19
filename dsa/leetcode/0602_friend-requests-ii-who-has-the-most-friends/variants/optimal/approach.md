## General
**Treat friendship as an undirected connection**

Although each row stores a requester and an accepter, both users gain one friend when the request is accepted. Each endpoint must therefore contribute one occurrence to its user's total.

**Normalize both endpoint columns**

Select every `requester_id` as a common `id` column, then combine it with every `accepter_id` using `UNION ALL`. Keeping all occurrences is essential because each row represents one friendship contribution.

**Count normalized occurrences**

Group the combined endpoint stream by `id`. The group size is exactly that user's number of incident accepted requests. Order counts descending and retain the first row; the contract guarantees a unique maximum.

**Why the winning count is exact**

Every accepted friendship produces precisely two normalized rows, one for each endpoint. Thus a user's normalized occurrences are in one-to-one correspondence with that user's friends in the accepted-pair table. Grouping calculates all exact degrees, and the descending first group is the unique maximum.

## Complexity detail
For `n` accepted requests, normalization creates `2n` endpoint rows. Grouping and ordering generally take $O(n \log n)$ time and $O(n)$ working space.

## Alternatives and edge cases
- **Aggregate each endpoint column first:** count requesters and accepters separately, union those partial totals, then sum by user; it has the same asymptotic bound.
- **Correlated incident-edge count per user:** is correct but may rescan all requests for every distinct user and take $O(n^2)$ time.
- **Use `UNION` instead of `UNION ALL`:** incorrectly removes repeated endpoint occurrences and undercounts users with several friends.
- **User in both columns:** contributions from both roles must be added.
- **Nonconsecutive user identifiers:** are ordinary grouping keys.
- **One accepted pair per friendship:** each endpoint gains one count.
- **Unique winner guarantee:** no tie-breaker should determine the result.
