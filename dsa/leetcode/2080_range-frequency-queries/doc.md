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
