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
