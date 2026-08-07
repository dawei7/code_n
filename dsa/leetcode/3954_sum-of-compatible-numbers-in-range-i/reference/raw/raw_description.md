## Description

You are given two integers `n` and `k`.

A **positive** integer `x` is called **compatible** if it satisfies both of the following conditions:

    - `abs(n - x) <= k`

    - `(n & x) == 0`

Return the sum of all **compatible** integers `x`.

**Note**:

    - Here, `&` denotes the **bitwise AND** operator.

    - The **absolute** difference between integers `i` and `j` is defined as `abs(i - j)`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 2, k = 3</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

The compatible integers are:

	- `x = 1`, since `abs(2 - 1) = 1` and `2 & 1 = 0`.

	- `x = 4`, since `abs(2 - 4) = 2` and `2 & 4 = 0`.

	- `x = 5`, since `abs(2 - 5) = 3` and `2 & 5 = 0`.

Thus, the answer is `1 + 4 + 5 = 10`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, k = 1</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There are no compatible integers in the range `[4, 6]`. Thus, the answer is 0.

</div>

**Constraints:**

	- `1 <= n <= 100`

	- `1 <= k <= 100`
