# Range Frequency Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2080 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Design, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/range-frequency-queries/) |

## Problem Description

### Goal

Design a data structure over a fixed zero-indexed integer array. Each query supplies an inclusive index interval and a value, and asks how many times that value occurs inside the corresponding contiguous subarray. Both boundary positions belong to the queried range.

The array does not change after construction. Support as many as $10^5$ queries without rescanning every position in each requested range.

### Function Contract

**Inputs**

- `RangeFreqQuery(arr)` constructs the structure from an array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{arr[i]} \le 10^4$.
- `query(left, right, value)` receives indices satisfying $0 \le \texttt{left} \le \texttt{right} < n$ and a value between 1 and $10^4$.
- At most $Q=10^5$ calls are made to `query`. Let $f$ be the total number of occurrences of the queried value in the full array.

**Return value**

- The constructor returns no value.
- Each `query` returns the number of indices $i$ with $\texttt{left} \le i \le \texttt{right}$ and `arr[i] == value`.

### Examples

**Example 1**

- Input: `operations = ["RangeFreqQuery","query","query"], arguments = [[[12,33,4,56,22,2,34,33,22,12,34,56]],[1,2,4],[0,11,33]]`
- Output: `[null,1,2]`
- Explanation: Value 4 appears once from indices 1 through 2, while value 33 appears twice in the full array.

**Example 2**

- Input: `operations = ["RangeFreqQuery","query","query"], arguments = [[[1,1,2,2,2]],[0,4,2],[0,1,2]]`
- Output: `[null,3,0]`
- Explanation: The inclusive whole-array query sees all three 2s; the prefix query sees none.

**Example 3**

- Input: `operations = ["RangeFreqQuery","query","query"], arguments = [[[5]],[0,0,5],[0,0,1]]`
- Output: `[null,1,0]`
- Explanation: A one-position range contains its stored value once and an absent value zero times.

### Required Complexity

- **Time:** $O(n+Q\log n)$
- **Space:** $O(n+Q)$

<details>
<summary>Approach</summary>

#### General

**Index every value's occurrences**

During construction, scan `arr` from left to right and append each index to the list associated with its value. Because indices arrive in increasing order, every occurrence list is already sorted without an additional sorting step. Across all values, these lists store exactly $n$ indices.

**Turn an inclusive range into two boundaries**

For a query, select the occurrence list for `value`. Binary-search for the first stored index greater than or equal to `left`; call its insertion position `lower`. Then search for the first stored index strictly greater than `right`; call that position `upper`. Exactly the entries from `lower` through `upper - 1` lie inside the inclusive range, so the answer is `upper - lower`.

**Handle absent values without special traversal**

If a value never occurs, use an empty position list. Both binary searches return zero, producing frequency zero. Repeated queries are read-only and need no state changes.

#### Complexity detail

Construction takes $O(n)$ time and stores $O(n)$ indices. A query performs two binary searches on a list of length $f$, taking $O(\log f)$ time and $O(1)$ auxiliary space. Across $Q$ calls, the total is $O(n+Q\log n)$ time. The index uses $O(n)$ space, while an app-level operation sequence also returns $O(Q)$ outputs.

#### Alternatives and edge cases

- **Scan each subarray:** Counting directly from `left` through `right` uses no index but can take $O(nQ)$ total time.
- **Prefix counts for every value:** A full value-by-position table answers in constant time but can require $O(nV)$ space for $V$ possible values.
- **Segment tree of frequency maps:** Supports related dynamic or richer range queries, but this immutable point-frequency problem needs only sorted position lists.
- **Inclusive right boundary:** Use an upper-bound search for `right`, not a lower-bound search, so an occurrence exactly at `right` is counted.
- **Absent value:** Both insertion positions are zero and the answer is zero.
- **Single-element range:** It returns either one or zero according to that exact position.

</details>
