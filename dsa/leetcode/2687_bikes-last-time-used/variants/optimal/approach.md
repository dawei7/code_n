## General

**Define “last used” by the latest end time**

Each row is one bike ride. For a fixed bike, the requested last-use timestamp is the greatest `end_time` among all of that bike's rides.

SQL's `MAX` aggregate expresses exactly this selection. Datetime values have chronological ordering, so the maximum is the most recent timestamp.

The query does not need the row's `ride_id` or `start_time` to determine when a ride finished.

**Create one group per bike**

`GROUP BY bike_number` partitions the `Bikes` table into all rides belonging to the same bike.

Within each group, `MAX(end_time)` examines every ending timestamp and returns one value. The result therefore has exactly one row per distinct bike number.

This avoids returning several rides for a bike or requiring a separate lookup after identifying its latest time.

**Name the aggregate as the expected column**

The selected expression is:

`MAX(end_time) AS end_time`.

The alias makes the grouped maximum appear under the expected output name `end_time` rather than a database-generated expression label.

It also allows the later `ORDER BY end_time DESC` to refer clearly to the aggregated result.

**Sort bikes by recency**

The result must list the most recently used bikes first.

`ORDER BY end_time DESC` sorts the computed group maxima from greatest datetime to smallest. `DESC` is essential: the default ascending direction would place the oldest last-use time first.

Ordering happens after aggregation conceptually, so each bike is positioned according to its own latest ride, not according to every underlying ride.

**Trace a bike with several rides**

Suppose bike W00576 has end times:

- 2012-03-25 12:40:00;
- 2012-03-25 09:10:00;
- 2012-03-28 02:50:00.

Grouping brings these three rows together. `MAX` chooses 2012-03-28 02:50:00.

Earlier rides remain part of the group but cannot change the maximum. Only one W00576 output row is produced.

**Trace several bikes**

Assume the grouped maxima are:

- W00576 at March 28;
- W00455 at March 26;
- W00300 at March 25.

Descending order produces W00576, W00455, then W00300. A bike with only one ride simply has that ride's `end_time` as its maximum.

**Why choosing the greatest ride ID would be wrong**

`ride_id` is unique, but uniqueness does not guarantee chronological ordering.

A numerically larger ID could describe an older ride. The problem defines recency through time, so `MAX` must be applied to `end_time` itself.

Similarly, maximum `start_time` is not the requested field; rides may have different durations, and the last ending ride is determined by `end_time`.

**Why a self-join is unnecessary**

One could join every ride to other rides for the same bike and retain rows for which no later end time exists.

That expresses the same idea indirectly and must handle ties and duplicates carefully. Grouped `MAX` directly computes the one value needed from each group.

It is both clearer and usually easier for the database optimizer.

**Ties between bikes**

If two different bikes have the same latest `end_time`, both belong at the same recency rank.

The query provides no secondary ordering key, and the problem does not require one. Their relative order may therefore be database-dependent while still satisfying descending order by last-use time.

**Ties within one bike**

If several rides for the same bike end at the same latest timestamp, `MAX` still returns that timestamp once.

Because the output requests only the bike number and time, there is no ambiguity about which ride row to return.

**Logical execution flow**

The query can be understood as:

1. scan `Bikes`;
2. partition rides by `bike_number`;
3. find the largest `end_time` in every partition;
4. emit the bike number and that maximum under alias `end_time`;
5. sort emitted rows by the maximum descending.

No modification is made to the source table.


For each bike group, `MAX(end_time)` is by definition at least every end time in that group and equals one of the greatest timestamps. It is therefore exactly the last time that bike was used.

Grouping emits this value once for every distinct bike. Descending ordering arranges those last-use values from most recent to least recent. Thus both the contents and ordering of the result meet the contract.

**Why aggregation scales well**

The query summarizes any number of rides for a bike into one value while scanning them.

It does not materialize every pair of rides or repeatedly search the table for each bike. A database may implement grouping with hashing, sorting, or an index over bike and time.

## Complexity detail

Let $R$ be the number of ride rows and $B$ the number of distinct bikes. Reading and aggregating rows requires at least $O(R)$ work. Without assuming a supporting index, grouping and sorting are conservatively bounded by $O(R\log R)$ time.

The grouped state and result require up to $O(B)$ logical space, bounded by $O(R)$. A physical database plan may use temporary memory, index traversal, or disk-based sorting, so the manifest states the safe $O(R)$ bound.

## Alternatives and edge cases

- **Window function with row numbers:** Can rank rides per bike and keep rank one, but returns more row detail than needed.
- **Anti-join against later rides:** Correct when carefully written, but more complex and potentially more expensive.
- **Correlated `MAX` subquery:** Produces the right value but may repeat aggregation for many rows.
- **Maximum ride ID:** Incorrect because unique IDs are not guaranteed chronological.
- **Maximum start time:** Answers a different question from latest end time.
- **One ride for a bike:** Its end time is returned directly by `MAX`.
- **Several rides for a bike:** Only the greatest ending timestamp survives.
- **Equal latest times across bikes:** Relative tie order is unspecified without a secondary key.
- **Equal latest times within one bike:** The grouped result still contains one bike row.
- **Descending direction:** Required to place most recently used bikes first.
- **Column alias:** Ensures the aggregate has the expected output name.
- **Source preservation:** The query reads and summarizes rows without modifying `Bikes`.
