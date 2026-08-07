## Description

You are given a 2D integer array `intervals`, where $\text{intervals}[i] = [l_{i}, r_{i}, \text{weight}_{i}]$. Interval `i` starts at position $l_{i}$ and ends at $r_{i}$, and has a weight of $\text{weight}_{i}$. You can choose *up to* 4 **non-overlapping** intervals. The **score** of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from `intervals` with **maximum** score, representing your choice of non-overlapping intervals.

Two intervals are said to be **non-overlapping** if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

**Output:** [2,3]

**Explanation:**

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

</div>
#### Example 2

<div class="example-block">
**Input:** intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

**Output:** [1,3,5,6]

**Explanation:**

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

</div>
### Constraints

- $1 \le \text{intevals.length} \le 5 * 10^{4}$

- $\text{intervals}[i].length = 3$

- $\text{intervals}[i] = [l_{i}, r_{i}, \text{weight}_{i}]$

- $1 \le l_{i} \le r_{i} \le 10^{9}$

- $1 \le \text{weight}_{i} \le 10^{9}$