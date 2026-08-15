# Design an Array Statistics Tracker

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3369 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Binary Search, Design, Queue, Heap (Priority Queue), Data Stream, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-an-array-statistics-tracker/) |

## Problem Description

### Goal

Design a `StatisticsTracker` that begins empty and receives positive integers over time. An update may append a number or remove the earliest number that is still present, so removals follow insertion order. At any valid point, the tracker must answer the floored arithmetic mean, the median, and the mode of its current contents.

For a sorted collection of odd size, the median is its middle value. For an even size, use the larger of the two central values. The mode is the most frequent value; if several values share the greatest frequency, return the smallest. Removal and every statistical query are guaranteed to occur only while at least one number is present.

### Function Contract

**Inputs**

- `operations`: The class name followed by calls chosen from `addNumber`, `removeFirstAddedNumber`, `getMean`, `getMedian`, and `getMode`.
- `arguments`: The argument list paired with each operation. Construction and queries other than `addNumber` have no arguments.

Let $q$ be the total number of operations after construction and $m$ the current number of stored values. Every added `number` satisfies $1\leq\texttt{number}\leq10^9$, and $q\leq10^5$.

**Return value**

- A list aligned with `operations`: `null` for construction and mutating calls, and the requested integer for each statistical query.

### Examples

#### Example 1

- Operations: `["StatisticsTracker", "addNumber", "addNumber", "addNumber", "addNumber", "getMean", "getMedian", "getMode", "removeFirstAddedNumber", "getMode"]`
- Arguments: `[[], [4], [4], [2], [3], [], [], [], [], []]`
- **Output:** `[null, null, null, null, null, 3, 4, 4, null, 2]`

#### Example 2

- Operations: `["StatisticsTracker", "addNumber", "addNumber", "getMean", "removeFirstAddedNumber", "addNumber", "addNumber", "removeFirstAddedNumber", "getMedian", "addNumber", "getMode"]`
- Arguments: `[[], [9], [5], [], [], [5], [6], [], [], [8], []]`
- **Output:** `[null, null, null, 7, null, null, null, null, 6, null, 5]`

#### Example 3

- Operations: `["StatisticsTracker", "addNumber", "addNumber", "getMedian", "getMode", "removeFirstAddedNumber", "getMean"]`
- Arguments: `[[], [1], [10], [], [], [], []]`
- **Output:** `[null, null, null, 10, 1, null, 10]`
