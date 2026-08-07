## Description

Given an array of integers `nums` and an integer `k`, an element `nums[i]` is considered **good** if it is **strictly** greater than the elements at indices `i - k` and `i + k` (if those indices exist). If neither of these indices *exists*, `nums[i]` is still considered **good**.

Return the **sum** of all the **good** elements in the array.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,2,1,5,4], k = 2</span>

**Output:** <span class="example-io">12</span>

**Explanation:**

The good numbers are `nums[1] = 3`, `nums[4] = 5`, and `nums[5] = 4` because they are strictly greater than the numbers at indices `i - k` and `i + k`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1], k = 1</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The only good number is `nums[0] = 2` because it is strictly greater than `nums[1]`.

</div>

**Constraints:**

	- `2 <= nums.length <= 100`

	- `1 <= nums[i] <= 1000`

	- `1 <= k <= floor(nums.length / 2)`
