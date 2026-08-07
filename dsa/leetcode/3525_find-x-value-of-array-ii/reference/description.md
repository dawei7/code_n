### 1. Description

You are given an array of **positive** integers `nums` and a **positive** integer `k`. You are also given a 2D array `queries`, where $\text{queries}[i] = [\text{index}_{i}, \text{value}_{i}, \text{start}_{i}, x_{i}]$.

You are allowed to perform an operation **once** on `nums`, where you can remove any **suffix** from `nums` such that `nums` remains **non-empty**.

The **x-value** of `nums` **for a given** `x` is defined as the number of ways to perform this operation so that the **product** of the remaining elements leaves a *remainder* of `x` **modulo** `k`.

For each query in `queries` you need to determine the **x-value** of `nums` for $x_{i}$ after performing the following actions:

- Update $nums[\text{index}_{i}]$ to $\text{value}_{i}$. Only this step persists for the rest of the queries.

- **Remove** the prefix $nums[0..(\text{start}_{i} - 1)]$ (where `nums[0..(-1)]` will be used to represent the **empty** prefix).

Return an array `result` of size `queries.length` where $\text{result}[i]$ is the answer for the $$i^{\text{th}}$$ query.

A **prefix** of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A **suffix** of an array is a subarray that starts at any point within the array and extends to the end of the array.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

that the prefix and suffix to be chosen for the operation can be **empty**.

### 4. Note

that x-value has a *different* definition in this version.

### 5. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]

**Output:** [2,2,2]

**Explanation:**

- For query 0, `nums` becomes `[1, 2, 2, 4, 5]`, and the empty prefix **must** be removed. The possible operations are:

		<li>Remove the suffix `[2, 4, 5]`. `nums` becomes `[1, 2]`.

- Remove the empty suffix. `nums` becomes `[1, 2, 2, 4, 5]` with a product 80, which gives remainder 2 when divided by 3.

	</li>
- For query 1, `nums` becomes `[1, 2, 2, 3, 5]`, and the prefix `[1, 2, 2]` **must** be removed. The possible operations are:

		<li>Remove the empty suffix. `nums` becomes `[3, 5]`.

- Remove the suffix `[5]`. `nums` becomes `[3]`.

	</li>
- For query 2, `nums` becomes `[1, 2, 2, 3, 5]`, and the empty prefix **must** be removed. The possible operations are:

		<li>Remove the suffix `[2, 2, 3, 5]`. `nums` becomes `[1]`.

- Remove the suffix `[3, 5]`. `nums` becomes `[1, 2, 2]`.

	</li>

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]

**Output:** [1,0]

**Explanation:**

- For query 0, `nums` becomes `[2, 2, 4, 8, 16, 32]`. The only possible operation is:

		<li>Remove the suffix `[2, 4, 8, 16, 32]`.

	</li>
- For query 1, `nums` becomes `[2, 2, 4, 8, 16, 32]`. There is no possible way to perform the operation.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]

**Output:** [5]

</div>

### 6. Constraints

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le k \le 5$

- $1 \le \text{queries.length} \le 2 * 10^{4}$

- $\text{queries}[i] = [\text{index}_{i}, \text{value}_{i}, \text{start}_{i}, x_{i}]$

- $0 \le \text{index}_{i} \le \text{nums.length} - 1$

- $1 \le \text{value}_{i} \le 10^{9}$

- $0 \le \text{start}_{i} \le \text{nums.length} - 1$

- $0 \le x_{i} \le k - 1$