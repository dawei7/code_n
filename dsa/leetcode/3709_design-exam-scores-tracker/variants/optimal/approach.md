## General

The tracker needs two operations with different demands:

- recording should preserve chronological data efficiently;
- an inclusive time-range query should sum many scores without scanning all records.

Strictly increasing record times mean timestamps are already supplied in sorted order. The exact source stores them in one array and stores cumulative scores in a parallel prefix-sum array. Binary search finds the records just outside a query interval, and one subtraction returns the total.

**Sentinel initialization**

The constructor creates:

`self.times = [0]`

`self.pre = [0]`.

Index zero is a sentinel, not an actual exam. Real times are at least one, so sentinel time zero sorts before every record.

The prefix value zero represents the total score before any exam. This sentinel avoids separate boundary branches when a query begins before the first recorded exam.

**Recording an exam**

Calls to `record` have strictly increasing `time`. Therefore:

`self.times.append(time)`

preserves sorted order without insertion or resorting.

The new cumulative score is:

`self.pre.append(self.pre[-1] + score)`.

After $r$ records:

- `times[j]` is the timestamp of real record $j$ for $1\le j\le r$;
- `pre[j]` is the sum of scores from real records one through $j$.

Both arrays stay aligned by index.

Appending to a Python list takes amortized constant time. Scores and times are never removed.

**Finding the position before `startTime`**

`bisect_left(self.times, startTime)` returns the first index whose timestamp is at least `startTime`.

Subtracting one gives:

`l = bisect_left(...) - 1`,

the index of the last record strictly before the query interval.

If the first real record is already at or after `startTime`, the result is sentinel index zero. The time constraints ensure `startTime >= 1`, so the sentinel never belongs to the requested interval.

**Finding the last position at or before `endTime`**

The interval includes its right endpoint. The source searches for:

`endTime + 1`.

Since timestamps are integers, the first time at least `endTime + 1` is the first time strictly greater than `endTime`. Subtracting one gives:

`r = bisect_left(self.times, endTime + 1) - 1`,

the index of the last exam whose time is at most `endTime`.

This correctly includes an exam recorded exactly at the right boundary.

**Subtracting prefix sums**

The records inside the interval occupy indices `l + 1` through `r`. Their score is:

$$
\texttt{pre}[r]-\texttt{pre}[l].
$$

`pre[r]` includes every score through the right boundary. `pre[l]` contains exactly the scores before the left boundary, so subtraction removes them.

If no exam falls in the interval, the last record before the interval is also the last record no later than its end, making `l == r`. The subtraction naturally returns zero.

**Tracing the example**

After recording score 98 at time one and score 99 at time five:

`times = [0, 1, 5]`

`pre = [0, 98, 197]`.

For query `[2, 5]`:

- the last time below two is index one;
- the last time at most five is index two;
- the result is `pre[2] - pre[1] = 197 - 98 = 99`.

For query `[3, 4]`, both binary searches identify index one as the surrounding prefix boundary. The result is zero.

**Why chronological guarantees matter**

Binary search is valid only because `times` remains sorted. Strictly increasing record times also imply at most one exam occurs at each timestamp, though the prefix-sum approach would still work with nondecreasing duplicate times if insertion order remained sorted.

The guarantee that queries never ask beyond the latest record means no future data is needed. The binary-search formula would still return the known sum for a later empty suffix, but the API contract rules out such calls.

**Why every qualifying score appears exactly once**

The left search excludes all timestamps below `startTime`. The right search includes all timestamps through `endTime` and excludes every larger timestamp. Prefix subtraction leaves precisely the records in the inclusive interval.

No score is duplicated because each record occupies one prefix position, and no interval record is omitted because sorted timestamps form one contiguous index range.

## Complexity detail

Let $r$ be the number of recorded exams and $u$ the number of `totalScore` queries.

Each `record` performs two list appends and one addition, taking amortized $O(1)$ time.

Each query performs two binary searches over $r+1$ timestamps, taking $O(\log r)$ time, followed by constant-time subtraction. Across an operation sequence, the precise total is:

$$
O(r+u\log r).
$$

Since $q=r+u$ is the total number of post-construction calls, the manifest's $O(q\log r)$ is a valid worst-case upper bound.

The two arrays store one sentinel plus one entry per record, requiring $O(r)$ space. Queries allocate no growing storage.

Prefix sums may reach $10^{14}$ under the constraints. Python integers handle this; fixed-width implementations need 64-bit totals.

## Alternatives and edge cases

- **Scan all records per query:** This can cost $O(ru)$ overall and is too slow for $10^5$ calls.
- **Balanced search tree with augmented sums:** It supports out-of-order insertions, but the chronological guarantee makes append-only arrays simpler and faster.
- **Fenwick tree:** Coordinate compression plus a Fenwick tree can answer prefix sums, yet future times are unknown and direct prefix arrays already exploit append order.
- **Query exactly one recorded time:** The two boundaries isolate one prefix entry and return that score.
- **No record in the interval:** `l == r`, so prefix subtraction returns zero.
- **Start before the first real record:** The sentinel provides prefix index zero without a branch.
- **End exactly at a record:** Searching for `endTime + 1` includes that record.
- **Large gaps between times:** Array positions represent records, not every time unit, so gaps consume no extra memory.
- **Strictly increasing times:** Simple append preserves the sorting required by `bisect_left`.
- **First operation after construction:** The contract guarantees it is `record`, so later queries always have at least one real timestamp available.
