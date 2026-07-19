# Finding MK Average

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/finding-mk-average/) |
| Frontend ID | 1825 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Design, Queue, Heap (Priority Queue), Data Stream, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Maintain a stream of positive integers for fixed parameters `m` and `k`. Once at least `m` values have arrived, the current window is the last `m` stream elements. Sort a copy of that window, discard its smallest `k` elements and largest `k` elements, then average the remaining `m - 2*k` values using floor division. Duplicate occurrences are separate elements and may occupy several trimmed positions.

Implement `MKAverage(m, k)`, `addElement(num)`, and `calculateMKAverage()`. Adding beyond `m` values evicts the oldest value from the active window. A calculation before the window is full returns `-1`; otherwise it returns the trimmed, rounded-down average without changing the stream.

### Function Contract

**Inputs**

- `MKAverage(m, k)` initializes an empty stream with $3 \le m \le 10^5$ and $1 < 2k < m$.
- `addElement(num)` appends one value with $1 \le \texttt{num} \le 10^5$.
- `calculateMKAverage()` takes no arguments.
- At most $10^5$ method calls follow construction. Let $q$ denote their count and $U=10^5$ the value-domain limit.

**Return value**

- Construction and `addElement` return no value.
- `calculateMKAverage` returns `-1` before `m` values exist; afterward it returns the floor of the sum of the middle `m - 2*k` sorted window elements divided by that count.

### Examples

**Example 1**

- Operations: `["MKAverage","addElement","addElement","calculateMKAverage","addElement","calculateMKAverage","addElement","addElement","addElement","calculateMKAverage"]`
- Arguments: `[[3,1],[3],[1],[],[10],[],[5],[5],[5],[]]`
- Output: `[null,null,null,-1,null,3,null,null,null,5]`

The first calculation is too early. Window `[3,1,10]` retains only `3`; after three fives arrive, the active window is `[5,5,5]`.
