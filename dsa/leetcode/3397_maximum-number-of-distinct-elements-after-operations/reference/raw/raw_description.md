## Description

You are given an integer array `nums` and an integer `k`.

You are allowed to perform the following **operation** on each element of the array **at most** *once*:

	- Add an integer in the range `[-k, k]` to the element.

Return the **maximum** possible number of **distinct** elements in `nums` after performing the **operations**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,2,3,3,4], k = 2</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

`nums` changes to `[-1, 0, 1, 2, 3, 4]` after performing operations on the first four elements.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,4,4,4], k = 1</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

By adding -1 to `nums[0]` and 1 to `nums[1]`, `nums` changes to `[3, 5, 4, 4]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `0 <= k <= 10^9`
