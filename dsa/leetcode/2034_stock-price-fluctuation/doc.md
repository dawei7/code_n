# Stock Price Fluctuation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2034 |
| Difficulty | Medium |
| Topics | Hash Table, Design, Heap (Priority Queue), Data Stream, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/stock-price-fluctuation/) |

## Problem Description

### Goal

A stream reports the price of one stock at particular timestamps. Reports may
arrive out of chronological order, and a later report may reuse a timestamp to
correct the price previously stored there. Only the most recent price reported
for each timestamp remains valid.

Design a `StockPrice` object that accepts those updates and answers three kinds
of query against the currently valid records: the price at the greatest
timestamp, the maximum recorded price, and the minimum recorded price.

### Function Contract

Let $Q$ be the total number of constructor, update, and query calls.

**Operations**

- `StockPrice()` creates an empty tracker.
- `update(timestamp, price)` stores `price` at `timestamp`, replacing any
  earlier price for that same timestamp.
- `current()` returns the price associated with the greatest recorded
  timestamp.
- `maximum()` returns the greatest currently valid price.
- `minimum()` returns the smallest currently valid price.

Both `timestamp` and `price` are integers from $1$ through $10^9$, and
$Q \le 10^5$. A query is made only after at least one update.

**Return value**

- The constructor and `update` return no value. Each query returns the integer
  described above.

### Examples

**Example 1**

- Input: `operations = ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]`, `arguments = [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]`
- Output: `[null, null, null, 5, 10, null, 5, null, 2]`
- Explanation: Correcting timestamp `1` from `10` to `3` removes `10` from
  consideration, so the next maximum is `5`.

**Example 2**

- Input: `operations = ["StockPrice", "update", "update", "current"]`, `arguments = [[], [5, 100], [2, 200], []]`
- Output: `[null, null, null, 100]`
- Explanation: Timestamp `5` remains the latest even though timestamp `2` was
  reported afterward.

**Example 3**

- Input: `operations = ["StockPrice", "update", "update", "minimum", "maximum"]`, `arguments = [[], [7, 20], [7, 12], [], []]`
- Output: `[null, null, null, 12, 12]`

### Required Complexity

- **Time:** $O(\log Q)$
- **Space:** $O(Q)$

<details>
<summary>Approach</summary>

#### General

**Keep one authoritative price per timestamp**

A hash map from timestamp to price represents the current records. An update
overwrites that entry, so both new reports and corrections have the same map
operation. Track the greatest timestamp seen separately; corrections never
remove timestamps, so this value can only increase. `current()` can therefore
read the map at that timestamp directly.

**Retain correction history in two lazy heaps**

Push `(price, timestamp)` into a min-heap and `(-price, timestamp)` into a
max-heap for every update. Replacing a map entry does not search either heap.
Instead, before returning an extreme, compare the heap-top pair with the
authoritative map. If the map now gives that timestamp a different price, the
heap entry is stale and can be popped. Repeat until the top is current.

Every valid record has an entry in both heaps from its most recent update, so a
heap cannot lose all valid candidates while stale entries are removed. Once
the first current pair reaches the top, heap ordering proves that no valid
price beyond it is more extreme. This establishes the correctness of both
`minimum()` and `maximum()`.

#### Complexity detail

Each update performs two heap insertions in $O(\log Q)$ time and one expected
$O(1)$ hash-map write. `current()` takes expected $O(1)$ time. An extreme query
may remove several obsolete entries, but each inserted entry is removed at
most once from each heap; across the full call sequence, `minimum()` and
`maximum()` take amortized $O(\log Q)$ time per call. The map and two heaps
store $O(Q)$ entries in total.

#### Alternatives and edge cases

- **Ordered multiset with frequencies:** Remove the corrected price and insert
  the replacement in $O(\log Q)$ time, then read either extreme directly. This
  avoids stale entries but needs an ordered multiset not built into Python.
- **Scan all current prices per query:** A timestamp map alone makes updates
  simple, but each minimum or maximum query costs $O(Q)$ and a long query
  sequence can become quadratic.
- An update with an older timestamp does not change which price is current.
- Correcting the greatest timestamp changes `current()` immediately.
- A stale value must not remain eligible for either extreme after correction.
- Multiple timestamps may share one price; correcting one does not invalidate
  the others.
- Timestamp and price values at $10^9$ fit ordinary integer comparisons; no
  chronological array indexed by timestamp is feasible.

</details>
