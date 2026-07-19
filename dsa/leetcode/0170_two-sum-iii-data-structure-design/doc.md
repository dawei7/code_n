# Two Sum III - Data structure design

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 170 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Design, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-sum-iii-data-structure-design/) |

## Problem Description
### Goal
Design a stateful `TwoSum` structure that accumulates integer occurrences through `add(number)`. Repeated additions are retained as separate occurrences rather than collapsed into one set entry, and values remain available for every later query.

For `find(value)`, return whether two distinct stored occurrences can sum to the requested value. A number may pair with itself only when it has been added at least twice; otherwise the two addends may be different values in either order. Process construction, additions, and queries sequentially, returning `None` for mutations and a boolean for each query without removing or consuming any stored occurrence.

### Function Contract
**Inputs**

- `operations`: method names beginning with `TwoSum`, followed by `add` and `find`
- `arguments`: one integer argument for each add or find operation

**Return value**

A result list aligned with operations: `None` for construction and add, and a boolean for each find query.

### Examples
**Example 1**

- Input: add `1`, `3`, `5`; find `4`; find `7`
- Output: `[null,null,null,null,true,false]`

**Example 2**

- Input: add `3` twice; find `6`
- Output: `True`

**Example 3**

- Input: add `-2` and `5`; find `3`
- Output: `True`
