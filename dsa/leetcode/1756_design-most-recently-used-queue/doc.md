# Design Most Recently Used Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1756 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Linked List, Divide and Conquer, Design, Simulation, Doubly-Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-most-recently-used-queue/) |

## Problem Description

### Goal

Design a queue that initially contains the integers from $1$ through $n$ in ascending order. It supports a `fetch(k)` operation that selects the current $k$-th element, removes that element from its position, places it at the back of the queue, and returns its value.

Positions are one-indexed and are evaluated against the queue's current order, so every fetch can affect later results. The queue size never changes: the fetched element becomes the most recently used element at the back while all other elements preserve their relative order.

### Function Contract

**Inputs**

- `operations`: a serialized method sequence whose first entry is `"MRUQueue"` and whose remaining entries are `"fetch"`.
- `arguments`: arguments aligned with `operations`; construction receives `[n]`, while each fetch receives `[k]`.

The constructor satisfies $1 \le n \le 2000$. At most 2000 calls are made to `fetch`, and every call satisfies $1 \le k \le n$.

**Return value**

- Return one result per operation: `null` for construction and the fetched integer for every `fetch(k)` call.

### Examples

**Example 1**

- Input: `operations = ["MRUQueue", "fetch", "fetch", "fetch", "fetch"], arguments = [[8], [3], [5], [2], [8]]`
- Output: `[null, 3, 6, 2, 2]`
- Explanation: The first call moves `3` to the back. The later positions are interpreted in each updated queue, ending with the previously moved `2` fetched from position eight.

**Example 2**

- Input: `operations = ["MRUQueue", "fetch", "fetch", "fetch"], arguments = [[1], [1], [1], [1]]`
- Output: `[null, 1, 1, 1]`
- Explanation: A one-element queue is unchanged when its only element is moved to the back.

**Example 3**

- Input: `operations = ["MRUQueue", "fetch", "fetch", "fetch"], arguments = [[5], [5], [1], [4]]`
- Output: `[null, 5, 1, 5]`
- Explanation: Fetching the original back element changes nothing, fetching the front moves `1` behind `5`, and position four then contains `5`.
