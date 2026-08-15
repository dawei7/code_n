# Most Frequent IDs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3092 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/most-frequent-ids/) |

## Problem Description

### Goal

A collection contains integer IDs whose occurrence counts change over time. Two arrays, `nums` and `freq`, have the same length. At step `i`, the count of ID `nums[i]` changes by `freq[i]`.

A positive change adds that many copies of the ID. A negative change removes `-freq[i]` copies. The updates are guaranteed never to make an ID's count negative.

After every step, report the largest current count among all IDs. If the collection is empty, report `0` for that step. Return these per-step values in update order.

### Function Contract

**Inputs**

- `nums`: a list of the IDs updated at each step, where $1 \leq \texttt{nums[i]} \leq 10^5$.
- `freq`: a list of nonzero count changes, where $-10^5 \leq \texttt{freq[i]} \leq 10^5$.

The lists have the same length $n$, where $1 \leq n \leq 10^5$. Every prefix of updates leaves all ID counts nonnegative.

**Return value**

Return a list `answer` of length $n$. For each index `i`, `answer[i]` is the maximum ID count after applying update `i`, or `0` when every ID has count zero.

### Examples

#### Example 1

- **Input:** `nums = [2, 3, 2, 1]`, `freq = [3, 2, -3, 1]`
- **Output:** `[3, 3, 2, 2]`
- **Explanation:** ID 2 first reaches count 3, then ID 3 reaches 2. Removing all copies of ID 2 makes 2 the maximum, and the last update does not exceed it.

#### Example 2

- **Input:** `nums = [5, 5, 3]`, `freq = [2, -2, 1]`
- **Output:** `[2, 0, 1]`
- **Explanation:** Removing both copies of ID 5 empties the collection before ID 3 is added.

#### Example 3

- **Input:** `nums = [1, 2, 1, 2]`, `freq = [4, 4, -1, 2]`
- **Output:** `[4, 4, 4, 6]`
- **Explanation:** The first two IDs tie at 4; after ID 1 drops to 3, ID 2 remains the maximum and later rises to 6.
