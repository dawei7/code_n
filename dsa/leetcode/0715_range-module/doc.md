# Range Module

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 715 |
| Difficulty | Hard |
| Topics | Design, Segment Tree, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/range-module/) |

## Problem Description
### Goal
A `RangeModule` tracks portions of the real-number line using half-open intervals. Interval `[left, right)` contains every real number `x` satisfying `left <= x < right`, including the left endpoint but excluding the right.

Implement `addRange(left, right)` to track every point in the interval, `removeRange(left, right)` to stop tracking those points, and `queryRange(left, right)` to return whether every point in the requested interval is currently tracked. Overlapping operations combine according to coverage, and a query is false when even one portion is missing.

### Function Contract
**Inputs**

- `operations`: ordered `addRange(left, right)`, `removeRange(left, right)`, or `queryRange(left, right)` calls with `left < right`

**Return value**

- A list containing each query result in operation order; a query is true only when every point in `[left, right)` is currently tracked

### Examples
**Example 1**

- Input: `operations = [["addRange",10,20],["removeRange",14,16],["queryRange",10,14],["queryRange",13,15],["queryRange",16,17]]`
- Output: `[true,false,true]`

**Example 2**

- Input: `operations = [["queryRange",1,2],["addRange",1,2],["queryRange",1,2]]`
- Output: `[false,true]`

**Example 3**

- Input: `operations = [["addRange",5,10],["addRange",10,15],["queryRange",5,15]]`
- Output: `[true]`
