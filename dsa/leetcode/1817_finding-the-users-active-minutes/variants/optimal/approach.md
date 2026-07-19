## General
**Deduplicate minutes separately for every user**

Maintain a hash map from each user ID to a set of minutes. For every `[user_id, minute]` log, insert the minute into that user's set. Set insertion naturally collapses repeated actions in the same minute, while the outer map keeps equal minute values belonging to different users independent.

**Convert per-user sets into the requested distribution**

Create `answer` with `k` zeros. For each set in the map, its size is that user's UAM. A UAM of $j$ belongs at zero-based index $j-1$, so increment that position once. The constraint on `k` guarantees every observed set size has a valid position.

**Why each user is counted once in the correct bucket**

After processing all logs, a user's set contains a minute exactly when at least one of that user's actions occurred then. Its cardinality is therefore precisely the defined UAM, regardless of duplicate log rows. The second pass visits each recorded user once and increments only the bucket corresponding to that cardinality, yielding the required count for every UAM value.

## Complexity detail
Across all users, at most $n$ distinct `(user, minute)` associations are stored. Expected hash insertion time over all logs is $O(n)$, iterating the user sets' cardinalities is $O(n)$ in the worst case, and initializing the result costs $O(k)$. Total time and output-inclusive space are $O(n+k)$.

## Alternatives and edge cases
- **Rescan all logs for each user:** It can reconstruct every user's minute set correctly, but may revisit all $n$ entries for each of $\Theta(n)$ users and take $O(n^2)$ time.
- **Store minutes in lists:** Avoiding duplicates with linear list membership checks can also degrade to $O(n^2)$ when one user has many distinct minutes.
- **Duplicate log entries:** Multiple identical `[user_id, minute]` rows still contribute one active minute.
- **Shared minute across users:** Each user counts that minute independently because UAM is defined per user.
- **Sparse distribution:** Most of the `k` buckets may be zero, but the returned array must still have exactly `k` positions.
- **Large user IDs:** IDs are map keys rather than array indices, so values near $10^9$ require no oversized allocation.
- **UAM equal to `k`:** Increment the final array position, index `k - 1`.
