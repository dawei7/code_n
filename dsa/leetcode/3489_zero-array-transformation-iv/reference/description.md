## Description

You are given an integer array `nums` of length `n` and a 2D array `queries`, where $\text{queries}[i] = [l_{i}, r_{i}, \text{val}_{i}]$.

Each $\text{queries}[i]$ represents the following action on `nums`:

- Select a subset of indices in the range $[l_{i}, r_{i}]$ from `nums`.

- Decrement the value at each selected index by **exactly** $\text{val}_{i}$.

A **Zero Array** is an array with all its elements equal to 0.

Return the **minimum** possible **non-negative** value of `k`, such that after processing the first `k` queries in **sequence**, `nums` becomes a **Zero Array**. If no such `k` exists, return -1.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

**Output:** 2

**Explanation:**

- **For query 0 (l = 0, r = 2, val = 1):**

		<li>Decrement the values at indices `[0, 2]` by 1.

- The array will become `[1, 0, 1]`.

	</li>
- **For query 1 (l = 0, r = 2, val = 1):**

		<li>Decrement the values at indices `[0, 2]` by 1.

- The array will become `[0, 0, 0]`, which is a Zero Array. Therefore, the minimum value of `k` is 2.

	</li>

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

**Output:** -1

**Explanation:**

It is impossible to make nums a Zero Array even after all the queries.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,3,2,1], queries = [[0,1,1],[1,2,1],[2,3,2],[3,4,1],[4,4,1]]

**Output:** 4

**Explanation:**

- **For query 0 (l = 0, r = 1, val = 1):**

		<li>Decrement the values at indices `[0, 1]` by `1`.

- The array will become `[0, 1, 3, 2, 1]`.

	</li>
- **For query 1 (l = 1, r = 2, val = 1):**

		<li>Decrement the values at indices `[1, 2]` by 1.

- The array will become `[0, 0, 2, 2, 1]`.

	</li>
- **For query 2 (l = 2, r = 3, val = 2):**

		<li>Decrement the values at indices `[2, 3]` by 2.

- The array will become `[0, 0, 0, 0, 1]`.

	</li>
- **For query 3 (l = 3, r = 4, val = 1):**

		<li>Decrement the value at index 4 by 1.

- The array will become `[0, 0, 0, 0, 0]`. Therefore, the minimum value of `k` is 4.

	</li>

</div>
#### Example 4

<div class="example-block">
**Input:** nums = [1,2,3,2,6], queries = [[0,1,1],[0,2,1],[1,4,2],[4,4,4],[3,4,1],[4,4,5]]

**Output:** 4

</div>
### Constraints

- $1 \le \text{nums.length} \le 10$

- $0 \le \text{nums}[i] \le 1000$

- $1 \le \text{queries.length} \le 1000$

- $\text{queries}[i] = [l_{i}, r_{i}, \text{val}_{i}]$

- $0 \le l_{i} \le r_{i} < \text{nums.length}$

- $1 \le \text{val}_{i} \le 10$