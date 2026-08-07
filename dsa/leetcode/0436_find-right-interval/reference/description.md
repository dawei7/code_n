## Description

You are given an array of `intervals`, where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$ and each $\text{start}_{i}$ is **unique**.

The **right interval** for an interval `i` is an interval `j` such that $\text{start}_{j} \ge \text{end}_{i}$ and $\text{start}_{j}$ is **minimized**. Note that `i` may equal `j`.

Return *an array of **right interval** indices for each interval `i`*. If no **right interval** exists for interval `i`, then put `-1` at index `i`.
### Function Contract

**Inputs**

- `intervals`: A list of two-element intervals `[start_i, end_i]` with unique start points.

**Return value**

Return one integer per input interval in the same order. Each value is the original index of the qualifying interval
with the smallest start, or `-1` when none exists.

### Examples
#### Example 1

- **Input:** $intervals = [[1,2]]$
- **Output:** `[-1]`
- **Explanation:** There is only one interval in the collection, so it outputs -1.
#### Example 2

- **Input:** $intervals = [[3,4],[2,3],[1,2]]$
- **Output:** `[-1,0,1]`
- **Explanation:** There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start_0 = 3 is the smallest start that is >= end_1 = 3.
The right interval for [1,2] is [2,3] since start_1 = 2 is the smallest start that is >= end_2 = 2.
#### Example 3

- **Input:** $intervals = [[1,4],[2,3],[3,4]]$
- **Output:** `[-1,2,-1]`
- **Explanation:** There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start_2 = 3 is the smallest start that is >= end_1 = 3.
### Constraints

- $1 \le \text{intervals.length} \le 2 * 10^{4}$

- $\text{intervals}[i].length = 2$

- $-10^{6} \le \text{start}_{i} \le \text{end}_{i} \le 10^{6}$

- The start point of each interval is **unique**.