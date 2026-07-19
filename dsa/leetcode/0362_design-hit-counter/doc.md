# Design Hit Counter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 362 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Design, Queue, Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/design-hit-counter/) |

## Problem Description
### Goal
Design a hit counter receiving chronological integer timestamps in seconds. Each `hit(timestamp)` records one occurrence, and several hits may share the same timestamp. Recorded events persist long enough to answer later window queries.

`getHits(timestamp)` returns the number of hits during the preceding five minutes, meaning timestamps in the interval `(timestamp - 300, timestamp]`. A hit exactly 300 seconds old is excluded, while every separate hit inside the window is counted. Process calls in nondecreasing timestamp order and discard or ignore expired history efficiently. The app returns results only for query operations; the native object exposes both methods.

### Function Contract
**Inputs**

- `operations`: for the app adapter, chronological `["hit", timestamp]` and `["getHits", timestamp]` operations

**Return value**

- A list containing the integer result of each `getHits` operation in query order. Native LeetCode calls the corresponding `HitCounter` methods directly.

### Examples
**Example 1**

- Input: `operations = [["hit",1],["hit",2],["hit",3],["getHits",4]]`
- Output: `[3]`

**Example 2**

- Input: `operations = [["hit",1],["hit",2],["hit",3],["hit",300],["getHits",300],["getHits",301]]`
- Output: `[4,3]`

**Example 3**

- Input: `operations = [["getHits",100]]`
- Output: `[0]`
