## Description

You are given a ​​​​​​​circular integer array​​​​​​​ `nums` of length `n`.

An index `i` is a **peak** if its value is **strictly greater** than its neighbors:

	- The **previous** neighbor of `i` is `nums[i - 1]` if `i > 0`, otherwise `nums[n - 1]`.

	- The **next** neighbor of `i` is `nums[i + 1]` if `i < n - 1`, otherwise `nums[0]`.

You are allowed to perform the following operation **any** number of times:

	- Choose any index `i` and **increase** `nums[i]` by 1.

Return an integer denoting the **minimum** number of operations required to make the array contain **at least** `k` peaks. If it is impossible, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,2], k = 1</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- To achieve at least `k = 1` peak, we can increase `nums[2] = 2` to 3.

	- After this operation, `nums[2] = 3` is strictly greater than its neighbors `nums[0] = 2` and `nums[1] = 1`.

	- Therefore, the minimum number of operations required is 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,5,3,6], k = 2</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- The array already contains at least `k = 2` peaks with zero operations.

	- Index 1: `nums[1] = 5` is strictly greater than its neighbors `nums[0] = 4` and `nums[2] = 3`.

	- Index 3: `nums[3] = 6` is strictly greater than its neighbors `nums[2] = 3` and `nums[0] = 4`.

	- Therefore, the minimum number of operations required is 0.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,7,3], k = 2</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

It is impossible to have at least `k = 2` peaks in this array. Therefore, the answer is -1.

</div>

**Constraints:**

	- `2 <= n == nums.length <= 5000`

	- `-10^5 <= nums[i] <= 10^5`

	- `0 <= k <= n`​​​​​​​
