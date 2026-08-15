### 1. Description

You are given a 2D array `intervals`, where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$ represents the start and the end of interval `i`. You are also given an integer `k`.

You must add **exactly one** new interval `[start_new, end_new]` to the array such that:

- The length of the new interval, $\text{end}_{new} - \text{start}_{new}$, is at most `k`.

- After adding, the number of **connected groups** in `intervals` is **minimized**.

A **connected group** of intervals is a maximal collection of intervals that, when considered together, cover a continuous range from the smallest point to the largest point with no gaps between them. Here are some examples:

- A group of intervals `[[1, 2], [2, 5], [3, 3]]` is connected because together they cover the range from 1 to 5 without any gaps.

- However, a group of intervals `[[1, 2], [3, 4]]` is not connected because the segment `(2, 3)` is not covered.

Return the **minimum** number of connected groups after adding **exactly one** new interval to the array.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** intervals = [[1,3],[5,6],[8,10]], k = 3

- **Output:** 2

- **Explanation:** After adding the interval `[3, 5]`, we have two connected groups: `[[1, 3], [3, 5], [5, 6]]` and `[[8, 10]]`.

#### Example 2

- **Input:** intervals = [[5,10],[1,1],[3,3]], k = 1

- **Output:** 3

- **Explanation:** After adding the interval `[1, 1]`, we have three connected groups: `[[1, 1], [1, 1]]`, `[[3, 3]]`, and `[[5, 10]]`.

### 4. Constraints

- $1 \le \text{intervals.length} \le 10^{5}$

- $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$

- $1 \le \text{start}_{i} \le \text{end}_{i} \le 10^{9}$

- $1 \le k \le 10^{9}$
