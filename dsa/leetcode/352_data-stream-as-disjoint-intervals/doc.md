# Data Stream as Disjoint Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 352 |
| Difficulty | Hard |
| Topics | Hash Table, Binary Search, Union-Find, Design, Data Stream, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) |

## Problem Description
### Goal
Design a `SummaryRanges` structure that receives nonnegative integers one at a time through `addNum(value)`. It must represent every distinct value seen so far using closed integer intervals, combining consecutive values into the same interval.

`getIntervals()` returns the smallest collection of disjoint intervals covering the current values, sorted by starting point in ascending order. A new value may create an isolated interval, extend one interval, or bridge and merge two neighbors. Repeated insertions change nothing. Preserve state across operations, and return snapshots whose interval boundaries reflect all additions made before that query without including unseen gap values.

### Function Contract
**Inputs**

- `values`: for the app adapter, stream values added in order. Native LeetCode calls `addNum(value)` and `getIntervals()` separately.

**Return value**

- The app adapter returns the interval snapshot after every insertion. Each snapshot is sorted by start. Native `getIntervals()` returns the current snapshot.

### Examples
**Example 1**

- Input: `values = [1, 3, 7, 2, 6]`
- Output: `[[[1,1]], [[1,1],[3,3]], [[1,1],[3,3],[7,7]], [[1,3],[7,7]], [[1,3],[6,7]]]`

**Example 2**

- Input: `values = [1, 2, 3]`
- Output: `[[[1,1]], [[1,2]], [[1,3]]]`

**Example 3**

- Input: `values = [5, 5]`
- Output: `[[[5,5]], [[5,5]]]`

### Required Complexity

- **Time:** $O(1) / O(k \log k)$
- **Space:** $O(v)$

<details>
<summary>Approach</summary>

#### General

**Index intervals from both endpoints**

An inserted value can interact only with intervals ending at `value - 1` or starting at `value + 1`. Keep a set of all present values for duplicate and neighbor checks, a map from every interval start to its end, and a reverse map from every interval end to its start.

**Classify the four possible local updates**

For a new value, four cases cover every possible update:

- Neither neighbor exists: create `[value, value]`.
- Only `value - 1` exists: extend its interval's right endpoint to `value`.
- Only `value + 1` exists: extend its interval's left endpoint to `value`.
- Both exist: join the left and right intervals through `value`.

**Why immediate neighbors reveal the endpoints**

The neighbor facts are enough to locate endpoints. If `value` is absent but `value - 1` is present, then `value - 1` must be the right endpoint of its interval; otherwise that interval would already contain `value`. The symmetric statement holds for `value + 1`. Endpoint maps therefore retrieve both affected intervals in expected constant time.

**Why maximal disjoint intervals are preserved**

After each update, the maps contain disjoint maximal intervals: the only new adjacency involving an old interval can pass through the inserted value, and the four cases merge every such adjacency immediately. No other intervals change. The present set prevents duplicates from applying an update twice. Sorting the start-map keys during `getIntervals()` yields the required order without affecting the maintained partition.

#### Complexity detail

`addNum` performs expected $O(1)$ hash operations. If `k` intervals currently exist, `getIntervals` sorts their starts in $O(k \log k)$ time and emits $O(k)$ pairs. With `v` distinct stream values, the presence set uses $O(v)$ space and the endpoint maps use $O(k)$, so total space is $O(v)$.

#### Alternatives and edge cases

- **Sorted interval array:** keeps queries ordered but may shift $O(k)$ interval entries during insertion or deletion.
- **Rebuild from all seen values:** costs $O(v \log v)$ for every snapshot after sorting `v` values again.
- **Balanced ordered map:** provides $O(\log k)$ insertion and ordered queries, but Python's standard library has no built-in implementation.
- Adding a duplicate is a no-op.
- Adding the one missing value between two intervals must merge both intervals, not merely extend one.
- Zero and isolated values become ordinary singleton intervals.

</details>
