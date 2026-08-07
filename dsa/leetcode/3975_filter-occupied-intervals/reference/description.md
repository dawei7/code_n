## Description

You are given a 2D integer array `occupiedIntervals`, where $\text{occupiedIntervals}[i] = [\text{start}_{i}, \text{end}_{i}]$ represents a time interval during which you are occupied. Each interval starts at $\text{start}_{i}$ and ends at $\text{end}_{i}$, **inclusive**. These intervals may **overlap**.

You are also given two integers `freeStart` and `freeEnd`, which define a free time interval from `freeStart` to `freeEnd`, inclusive.

Your task is to merge **all** occupied intervals that overlap or touch, then remove **all** integer points in the free interval from the merged occupied intervals.

Two intervals touch if the second interval starts **immediately after** the first one ends. For example, `[1, 1]` and `[2, 2]` touch and should be merged into `[1, 2]`.

Return the **remaining** occupied intervals in **sorted** order. The returned intervals must be **non-overlapping** and must contain the **minimum** number of intervals possible. If there are no remaining occupied points, return an empty list.
### Function Contract

`solve(occupiedIntervals, freeStart, freeEnd) -> list[list[int]]`

**Inputs**

- `occupiedIntervals`: A nonempty array of inclusive integer intervals `[start, end]`; intervals may overlap, touch, and arrive unsorted.
- `freeStart`: The inclusive first integer point of the free interval.
- `freeEnd`: The inclusive final integer point of the free interval.

**Output**

Return all integer points covered by at least one occupied interval but not by `[freeStart, freeEnd]`, encoded as sorted inclusive intervals. Consecutive remaining integer points belong to the same output interval, so the result is non-overlapping and uses the minimum possible number of intervals.

### Examples
#### Example 1

<div class="example-block">
**Input:** occupiedIntervals = [[2,6],[4,8],[10,10],[10,12],[14,16]], freeStart = 7, freeEnd = 11

**Output:** [[2,6],[12,12],[14,16]]

**Explanation:**

- After merging, the occupied intervals are `[2, 8]`, `[10, 12]`, and `[14, 16]`.

- Excluding the free interval `[7, 11]` results in `[2, 6]`, `[12, 12]`, and `[14, 16]`.

</div>
#### Example 2

<div class="example-block">
**Input:** occupiedIntervals = [[1,5],[2,3]], freeStart = 3, freeEnd = 8

**Output:** [[1,2]]

**Explanation:**

- After merging, the occupied interval is `[1, 5]`.

- Excluding the free interval `[3, 8]` results in `[1, 2]`.

</div>
### Constraints

- $1 \le \text{occupiedIntervals.length} \le 5 * 10^{4}$

- $\text{occupiedIntervals}[i].length = 2$

- $1 \le \text{start}_{i} \le \text{end}_{i} \le 10^{9}$

- $1 \le freeStart \le freeEnd \le 10^{9}$