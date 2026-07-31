# Design a Number Container System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2349 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Design, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-a-number-container-system/) |

## Problem Description

### Goal

Design a mutable system that associates positive integer indices with positive
integer numbers. A change operation fills an unused index or replaces the
number currently stored there. A find operation asks for the smallest index
whose current number equals a requested value.

Replacing an index must remove its old association even if internal historical
records remain. If no current index contains the requested number, return
`-1`. Across one instance, at most $10^5$ calls are made to the two operations.

### Function Contract

**Inputs**

- `NumberContainers()`: Constructs an empty system.
- `change(index, number)`: Assigns `number` at `index`, replacing any previous
  assignment. Both values lie in $[1,10^9]$.
- `find(number)`: Queries the smallest currently assigned index containing
  `number`.

**Return value**

`change` returns nothing. `find` returns the smallest matching index, or `-1`
when no such index exists.

### Examples

**Example 1**

- Input: `operations = ["NumberContainers","find","change","change","change","change","find","change","find"]`,
  `arguments = [[],[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]]`
- Output: `[null,-1,null,null,null,null,1,null,2]`
- Explanation: Number 10 is initially absent, later has minimum index 1, and
  has minimum index 2 after index 1 is reassigned to 20.
