## General

The class must support two operations over time: insert a tweet occurrence and count occurrences inside consecutive time buckets. The checked-in design stores a separate sorted multiset of timestamps for each tweet name. Sorting makes each bucket count a difference between two binary-search positions.

**Initialize fixed frequency lengths**

`self.d` maps the three accepted frequency strings to their number of seconds:

- `"minute"` maps to sixty.
- `"hour"` maps to 3,600.
- `"day"` maps to 86,400.

`self.data = defaultdict(SortedList)` maps each tweet name to a `SortedList`. Accessing a new name automatically constructs an empty sorted collection for it.

**Keep timestamps ordered during recording**

`recordTweet` calls `self.data[tweetName].add(time)`. A sorted list inserts the timestamp at its ordered position. Duplicate timestamps are retained, which is necessary because two calls at the same second represent two tweet occurrences and both must be counted.

Keeping data sorted makes insertion more expensive than appending to an ordinary list, but it lets later queries locate interval boundaries without scanning every stored occurrence.

**Translate inclusive buckets into half-open searches**

For a query, `f = self.d[freq]` obtains the bucket width. The first bucket begins at `startTime`, and later buckets begin after adding `f`. The loop condition `t <= endTime` creates every start that still lies inside the requested inclusive period.

A full bucket beginning at `t` covers

$$
[t,\ t+f-1].
$$

The last bucket is shortened if that endpoint exceeds `endTime`. Binary-search APIs are easiest to use with a half-open interval, so the code counts timestamps in

$$
[t,\ \min(t+f,\ \texttt{endTime}+1)).
$$

The lower position `l = tweets.bisect_left(t)` is the first stored timestamp greater than or equal to `t`. The upper position is
`tweets.bisect_left(min(t + f, endTime + 1))`, the first timestamp at or beyond the exclusive upper boundary. Every list position from `l` through `r - 1` belongs to that bucket, so `r - l` is the exact count.

Using `endTime + 1` is what preserves the inclusive query endpoint. If the final bucket ends at time sixty, searching for the first timestamp at least sixty-one includes tweets recorded exactly at sixty.

For the query from zero through sixty with minute frequency, the loop produces starts zero and sixty. The first searches the half-open range from zero through sixty and counts seconds zero through fifty-nine. The second searches from sixty through sixty-one and counts the one-second final bucket.

After appending a count, `t += f` advances to the next nonoverlapping bucket. The buckets cover the requested period without gaps or overlap because one bucket’s exclusive end is the next bucket’s start, except that the final one is clipped to the query endpoint.

**Why the returned list is complete**

Each loop iteration corresponds to exactly one required bucket in chronological order. Binary-search positions include precisely the timestamps inside that bucket, including duplicates. Every queried timestamp falls into exactly one bucket because the intervals partition the inclusive period. Appending each difference therefore returns the required counts in order.

Requesting an unseen `tweetName` creates and uses an empty `SortedList`. Both binary searches return zero for every bucket, so the method returns the correct number of zero counts, though it also leaves an empty name entry in `self.data`.

## Complexity detail

Let $r$ be the number of recorded timestamps for the queried tweet name and $b$ the number of returned buckets:

$$
b = \left\lfloor\frac{\texttt{endTime}-\texttt{startTime}}{f}\right\rfloor + 1.
$$

Inserting into `SortedList` takes approximately $O(\log r)$ search time plus the library’s block-maintenance cost; its documented implementation is optimized around a list-of-lists structure rather than a plain array shift.

Each query bucket performs two `bisect_left` operations, each $O(\log r)$, and one append. Query time is therefore $O(b\log r)$, not a linear scan over all $r$ records. The output itself requires $O(b)$ space.

Across all names, stored timestamp occurrences use $O(R)$ persistent space for $R$ total calls to `recordTweet`. A query uses $O(b)$ new space for its returned list and constant scalar working state beyond the binary-search internals.

## Alternatives and edge cases

- **Append then sort lazily:** Store unsorted timestamps with cheap $O(1)$ appends and sort a name on its first query. This can help write-heavy workloads but needs dirty-state tracking after later inserts.
- **Ordinary sorted array:** Use binary search plus insertion into a Python list. Queries remain efficient, but insertion can shift $O(r)$ elements.
- **Balanced search tree with subtree counts:** It can support logarithmic insertion and range counting but is much more complex and is not built into Python’s standard library.
- **Scan every timestamp:** Simple filtering costs $O(r+b)$ or $O(r)$ per query and ignores the benefit of maintaining order.
- **Duplicate timestamps:** `SortedList` retains duplicates, and the index difference counts every occurrence.
- **Inclusive end time:** The exclusive search boundary must use `endTime + 1` for the final bucket.
- **Short final bucket:** `min(t + f, endTime + 1)` clips it without a separate branch.
- **Unseen tweet name:** Every returned bucket is zero; accessing the default dictionary also creates an empty stored entry.
- **Single-second period:** The loop executes once and counts timestamps exactly equal to that second.
- **Large absolute times:** Bucket construction depends on the difference and width, while binary search compares the absolute integer timestamps directly.
- **Invalid frequency outside the contract:** Indexing `self.d` would raise a key error. The contract guarantees one of the three supported strings.
- **Persistent versus query space:** Recorded timestamps remain in the object across calls; the returned count list is newly allocated for each query.
