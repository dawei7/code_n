## Description

You are given three integers `n`, `m`, `k`. A **good array** `arr` of size `n` is defined as follows:

	- Each element in `arr` is in the **inclusive** range `[1, m]`.

	- *Exactly* `k` indices `i` (where `1 <= i < n`) satisfy the condition `arr[i - 1] == arr[i]`.

Return the number of **good arrays** that can be formed.

Since the answer may be very large, return it **modulo **`10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, m = 2, k = 1</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- There are 4 good arrays. They are `[1, 1, 2]`, `[1, 2, 2]`, `[2, 1, 1]` and `[2, 2, 1]`.

	- Hence, the answer is 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, m = 2, k = 2</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

	- The good arrays are `[1, 1, 1, 2]`, `[1, 1, 2, 2]`, `[1, 2, 2, 2]`, `[2, 1, 1, 1]`, `[2, 2, 1, 1]` and `[2, 2, 2, 1]`.

	- Hence, the answer is 6.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, m = 2, k = 0</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- The good arrays are `[1, 2, 1, 2, 1]` and `[2, 1, 2, 1, 2]`. Hence, the answer is 2.

</div>

**Constraints:**

	- `1 <= n <= 10^5`

	- `1 <= m <= 10^5`

	- `0 <= k <= n - 1`
