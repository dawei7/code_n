## General

Queries may arrive in any order, but the votes are fixed and their times are strictly increasing. The efficient strategy is to preprocess the leader immediately after every vote. A query then needs only to find the latest vote time not greater than `t`.

The constructor maintains:

- `cnt[p]`: votes received by candidate `p` so far;
- `cur`: leader after the processed prefix;
- `wins[i]`: leader immediately after vote `i`.

For each person `p`, the code increments their count and tests

```text
if cnt[cur] <= cnt[p]:
    cur = p
```

The non-strict `<=` is essential. If `p` merely ties the current leader, the newest vote belongs to `p`, so `p` wins the tie under the problem rule. If `p` exceeds the leader, `p` obviously takes the lead. If `p` remains below, `cur` stays unchanged.

**Why only the current leader needs comparison.** Could a third candidate with an old count matter? Before this vote, `cur` had at least as many votes as everyone else and was the most recently voted among tied leaders. Only candidate `p` changes count. Every other candidate remains no stronger than `cur`. Therefore the new leader is either the old `cur` or the newly voted `p`; comparing those two is sufficient.

**Preprocessing invariant.** After processing vote index `i`:

- `cnt` contains exact counts through that vote;
- `cur` is the correct leader using recency to break count ties;
- `wins[i] == cur`.

The first vote establishes the invariant. Even though `cur` initializes to candidate 0, its count is zero unless it received the vote. The first actual candidate reaches count one and replaces it. For later votes, the two-candidate comparison argument preserves the invariant.

**Answer a time query with upper-bound search.** Votes cast exactly at time `t` must count. `bisect_right(self.times, t)` returns the insertion position after all times less than or equal to `t`. Subtracting one gives the index of the last vote whose timestamp is at most `t`:

```text
i = bisect_right(times, t) - 1
```

The precomputed `wins[i]` is exactly the leader after all votes included in the query.

Using `bisect_left` without adjustment could exclude a vote occurring exactly at `t`. The right-biased search directly models the inclusive time boundary.

The constraints guarantee `t >= times[0]`, so the computed index is never negative. Query times after the final vote select the last `wins` entry and correctly return the final leader.

**Tie example.** Suppose counts of candidates 0 and 1 are both two after a vote for 1. The `<=` check changes `cur` to 1 because that vote is the most recent among the tied candidates. If a later vote makes candidate 0 tie at three, the same rule changes the leader back to 0. The stored leader sequence captures these changes at every timestamp, so queries between votes need no recounting.

For the sample prefix `persons = [0,1,1,0]`, stored leaders become `[0,1,1,0]`. After the second vote, counts tie at one and recent candidate 1 leads. After the third, candidate 1 leads outright. After the fourth, counts tie at two and the new vote makes candidate 0 leader. A query at the fourth vote's exact time indexes this final prefix entry, while a query just before it indexes the preceding leader 1.

The constructor stores the original `times` reference and a parallel leader list. It does not need to store `persons` after preprocessing.

## Complexity detail

Let $v$ be the number of votes and $r$ the number of queries.

- **Preprocessing time:** $O(v)$ expected with Counter operations.
- **Time per query:** $O(\log v)$ for binary search.
- **Total time:** $O(v+r\log v)$.
- **Space complexity:** $O(v)$ for `times`, `wins`, and up to $O(v)$ candidate counts.

Each query returns in logarithmic time regardless of whether query times are sorted.

## Alternatives and edge cases

- **Replay votes for every query:** Counting the prefix each time costs $O(v)$ per query and repeats work.
- **Sort queries offline:** Queries could be answered in one sweep, but the class must support online calls in arbitrary order.
- **Store only leader-change times:** Compress timestamps where `cur` changes and binary-search those. This may use less space but is not necessary at the constraints.
- **Use strict `<` in the leader update:** It would keep the older leader on a tie and violate the recency rule.
- **Query exactly at a vote time:** `bisect_right` includes that vote.
- **Query between votes:** It selects the most recent earlier vote's leader.
- **Query after all votes:** It returns the final stored leader.
- **First candidate is not zero:** The zero-count placeholder is replaced on the first iteration.
- **Repeated votes for one candidate:** Counts rise and the same candidate remains or becomes leader.
- **Several tied candidates:** Only the newly voted candidate can become the most recent tied leader on that step.
- **Strictly increasing times:** Binary search relies on this contract; duplicate timestamps would require defining within-time order more carefully.
- **Arbitrary candidate labels within bounds:** Counter keys handle candidates without a dense count array.
- **Times reference:** The code does not copy the list. Caller mutation after construction would invalidate alignment, but judge inputs are treated as fixed.
