## Description

You are given an integer array `nums` of length `n` and an integer `k`.

A pair of indices `(i, j)` is called **valid** if:

	- `0 <= i < j < n`

	- `j - i >= k`

Return the **maximum** value of `nums[i] + nums[j]` among all valid pairs.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,5,2,8], k = 2</span>

**Output:** <span class="example-io">13</span>

**Explanation:**

The valid pairs are:

	- `(0, 2)`: `nums[0] + nums[2] = 6`

	- `(0, 3)`: `nums[0] + nums[3] = 3`

	- `(0, 4)`: `nums[0] + nums[4] = 9`

	- `(1, 3)`: `nums[1] + nums[3] = 5`

	- `(1, 4)`: `nums[1] + nums[4] = 11`

	- `(2, 4)`: `nums[2] + nums[4] = 13`

Thus, the answer is 13.​​​​​​​

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,1,9], k = 1</span>

**Output:** <span class="example-io">14</span>

**Explanation:**

	- Since `k = 1`, every pair is valid.

	- The maximum value is obtained from a pair `(0, 2)`​​​​​​​, which is `nums[0] + nums[2] = 5 + 9 = 14`.

	- Thus, the answer is 14.

</div>

**Constraints:**

	- `2 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `1 <= k <= n - 1`
