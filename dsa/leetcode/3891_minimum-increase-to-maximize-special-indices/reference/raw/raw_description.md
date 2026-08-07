## Description

You are given an integer array `nums` of length `n`.

An index `i` (`0 < i < n - 1`) is **special** if `nums[i] > nums[i - 1]` and `nums[i] > nums[i + 1]`.

You may perform operations where you choose **any** index `i` and **increase** `nums[i]` by 1.

Your goal is to:

	- **Maximize** the number of **special** indices.

	- **Minimize** the total number of **operations** required to achieve that **maximum**.

Return an integer denoting the **minimum** total number of operations required.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,2]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**​​​​​​​

	- Start with `nums = [1, 2, 2]`.

	- Increase `nums[1]` by 1, array becomes `[1, 3, 2]`.

	- The final array is `[1, 3, 2]` has 1 special index, which is the maximum achievable.

	- It is impossible to achieve this number of special indices with fewer operations. Thus, the answer is 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,1,3]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**​​​​​​​

	- Start with `nums = [2, 1, 1, 3]`.

	- Perform 2 operations at index 1, array becomes `[2, 3, 1, 3]`.

	- The final array is `[2, 3, 1, 3]` has 1 special index, which is the maximum achievable. Thus, the answer is 2.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,2,1,4,3]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**​​​​​​​​​​​​​​​​​​​​​

	- Start with `nums = [5, 2, 1, 4, 3]`.

	- Perform 4 operations at index 1, array becomes `[5, 6, 1, 4, 3]`.

	- The final array is `[5, 6, 1, 4, 3]` has 2 special indices, which is the maximum achievable. Thus, the answer is 4.​​​​​​​

</div>

**Constraints:**

	- `3 <= n <= 10^5`

	- `1 <= nums[i] <= 10^9`
