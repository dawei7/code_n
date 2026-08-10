## General

The bulbs are arranged in fixed positions from `1` through `n`, but they turn on in a time order given by `bulbs`. On day `i`, the bulb at position `bulbs[i - 1]` turns on. The question is therefore not asking whether two positions are far enough apart in the original permutation. It asks for the first day on which two already-lit endpoint bulbs have exactly `k` still-unlit bulbs between them.

If the left endpoint is at position `y` and the right endpoint is at position `x`, exactly `k` positions lie strictly between them precisely when

$$
x-y-1=k,
$$

or equivalently when their distance is `k + 1`. This observation means that when a new bulb at `x` turns on, only two other positions could form a newly valid pair with it:

$$
y=x-k-1
$$

on the left, and

$$
y=x+k+1
$$

on the right. No other endpoint has exactly `k` positions between it and `x`.

**Why it is enough to inspect pairs involving the bulb that turned on today**

Suppose day `i` is the first day on which a valid pair exists. At least one endpoint of that pair must have turned on during day `i`. If both endpoints had already been on at the end of day `i-1`, and every interior bulb was off then, the same pair would already have been valid one day earlier. That would contradict the choice of day `i` as the first valid day.

Consequently, after the new bulb `x` is switched on, the algorithm only needs to test the possible left partner and possible right partner of `x`. It never needs to recheck every pair of old bulbs.

**The two pieces of maintained information**

The code maintains:

- `vis[position]`, which is `True` exactly when that position has already turned on; and
- a binary indexed tree, also called a Fenwick tree, that stores `1` at every lit position and `0` at every unlit position.

The Boolean array answers the endpoint question in constant time: “Is the possible partner bulb already on?” The Fenwick tree answers an interval-count question: “How many bulbs strictly between these endpoints are already on?”

Both are necessary for the way this implementation is organized. An interval count of zero alone would not prove that the far endpoint is lit. Conversely, knowing that both endpoints are lit would not reveal whether one of the `k` interior positions is also lit.

**What the Fenwick tree represents**

The tree uses one-based indices, which align directly with the source's bulb positions. Its array `c` has length `n + 1` so that positions `1` through `n` are valid and index `0` can remain unused.

Calling `update(x, 1)` records that position `x` has become lit. The expression `x & -x` isolates the lowest set bit of `x`. Adding that value moves from one Fenwick node to the next ancestor whose represented range also contains position `x`. Thus one point update modifies only logarithmically many stored partial sums.

Calling `query(x)` returns the number of lit bulbs in the inclusive prefix from position `1` through position `x`. During a query, subtracting `x & -x` moves to the preceding Fenwick range. Those disjoint stored ranges together cover the requested prefix exactly.

From prefix sums, the count in an arbitrary interval can be obtained by subtraction. In particular, if `y < x`, then

$$
\operatorname{query}(x-1)-\operatorname{query}(y)
$$

counts lit positions from `y+1` through `x-1`. These are exactly the positions strictly between `y` and `x`. The left endpoint is removed because `query(y)` includes it, and the right endpoint is absent because the first query stops at `x-1`.

Similarly, if `x < y`, then

$$
\operatorname{query}(y-1)-\operatorname{query}(x)
$$

counts lit positions from `x+1` through `y-1`.

**Processing one day**

The outer loop uses `enumerate(bulbs, 1)`, so `i` is the one-based day number expected by the answer and `x` is the position lit on that day.

First, the code calls `tree.update(x, 1)` and sets `vis[x] = True`. After these operations, both data structures describe the complete state at the end of the current day. Updating before checking is safe because both interval formulas deliberately exclude `x`.

For a possible partner on the left, the code computes `y = x - k - 1`. Three conditions are required:

1. `y > 0`, so the position lies within the row of bulbs.
2. `vis[y]` is true, so the left endpoint is on.
3. `tree.query(x - 1) - tree.query(y) == 0`, so none of the positions strictly between `y` and `x` is on.

If all three hold, the endpoints are on and all exactly `k` interior bulbs are off. The current day is returned immediately.

The right-side test is symmetric. It computes `y = x + k + 1`, checks `y <= n` and `vis[y]`, and uses `tree.query(y - 1) - tree.query(x)` to count only the strict interior.

**A small trace**

Take `bulbs = [1, 3, 2]` and `k = 1`.

- On day `1`, position `1` turns on. Its only distance-two candidate inside the array is position `3`, but `vis[3]` is false.
- On day `2`, position `3` turns on. Its left candidate is `3 - 1 - 1 = 1`, which is already on.
- The interior count is `query(2) - query(1)`. At this moment only positions `1` and `3` are lit, so both prefix queries equal `1` and their difference is zero.
- Position `2` is the single bulb between the endpoints and is still off, so day `2` is returned.

If position `2` had already been lit, the interval difference would be one and the pair would correctly be rejected.

**Why the first returned day is correct**

After every update, the Fenwick tree counts exactly the bulbs lit through that day, and `vis` identifies exactly the same set. Therefore, whenever the algorithm returns, both tested endpoints are lit, their positions differ by `k+1`, and the strict interior contains zero lit bulbs. The returned pair satisfies every condition.

For the other direction, consider the earliest valid day. The bulb switched on that day must be an endpoint of the newly valid pair. The algorithm tests both positions at distance `k+1` from that new endpoint. It will encounter the other endpoint, observe it in `vis`, and measure an interior count of zero. Hence it cannot miss the earliest valid pair.

Because days are processed in increasing order and the method returns as soon as a pair is found, no later answer can be returned in place of an earlier one. If every day is processed without success, no day contains such a pair, so `-1` is correct.

## Complexity detail

Let `n` be the number of bulbs.

Each of the `n` days performs one Fenwick point update. It then performs at most four Fenwick prefix queries: two for the left interval and two for the right interval. An update or prefix query follows Fenwick ancestors by repeatedly adding or subtracting the lowest set bit, so each operation takes `O(\log n)` time.

The exact implementation therefore takes

$$
O(n\log n)
$$

time in the worst case. It may return earlier, but `O(n\log n)` is the full-input bound. The `vis` lookup and all index arithmetic are constant-time additions to each iteration.

The Fenwick array `c` contains `n+1` integers, and `vis` contains `n+1` Boolean values. Apart from those arrays, the algorithm keeps only a constant number of variables. Its auxiliary space usage is

$$
O(n).
$$

The recursion stack is not involved because both Fenwick operations are iterative.

## Alternatives and edge cases

- **Linear sliding-window method:** Convert the activation order into an array `day[position]`, where each entry records when that bulb turns on. A carefully maintained window of endpoints at distance `k+1` can solve the problem in `O(n)` time and `O(n)` space. It is asymptotically faster, but its window-reset condition is subtler: an interior position invalidates the current endpoint pair when it turns on no later than either endpoint.

- **Ordered set of lit positions:** Insert each newly lit position into a balanced search tree and inspect its immediate predecessor and successor. If either neighbor is exactly `k+1` positions away, there cannot be another lit bulb between them. This also takes `O(n\log n)` time and `O(n)` space, but Python's standard library does not provide a built-in balanced ordered set.

- **Scan every interior interval:** After each bulb turns on, one could test possible endpoints and inspect all `k` interior positions directly. Repeated scanning can become quadratic and discards the prefix-count benefit supplied by the Fenwick tree.

- **The case `k = 0`:** The desired endpoints are adjacent. The strict interior is empty, so the relevant interval count is naturally zero. The formulas become `x-1` and `x+1` and require no special branch.

- **Candidate outside the row:** A left candidate at position zero or below and a right candidate above `n` are rejected by `y > 0` and `y <= n` before any invalid lookup is attempted.

- **Only one bulb:** No two endpoints exist. Both candidate positions fall outside the valid range, and the method returns `-1`.

- **A distance larger than the row can support:** If `k+1 >= n`, no two valid positions can have that separation. Every candidate fails a boundary check, so `-1` is returned.

- **Checking after the update:** The new position is already present in the Fenwick tree when interval counts are read. This does not create a false positive or false negative because the subtraction ranges exclude both endpoints, including the new one.

- **No duplicate activations:** `bulbs` is a permutation of positions `1` through `n`. Therefore every `update(x, 1)` changes a previously zero position to one. If duplicates were allowed, blindly adding one again would corrupt the interpretation as a lit-or-unlit count.

- **One-based indexing:** The Fenwick formulas depend on positive indices because `x & -x` is used to advance or retreat. The unused index zero prevents an update loop from getting stuck and matches the one-based bulb labels.

- **Both sides valid on the same day:** The code checks the left side first and returns immediately. The requested result is only the day number, so choosing one of two valid pairs on that same day has no observable effect.

- **Endpoint state and interior state are different questions:** The interval query intentionally excludes the distant endpoint. The separate `vis[y]` test must not be removed; otherwise an all-off interval with an unlit far endpoint could be mistaken for a valid pair.
