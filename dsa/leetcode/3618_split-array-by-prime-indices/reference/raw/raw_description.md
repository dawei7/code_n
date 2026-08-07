## Description

You are given an integer array `nums`.

Split `nums` into two arrays `A` and `B` using the following rule:

	- Elements at **<span data-keyword="prime-number">prime</span>** indices in `nums` must go into array `A`.

	- All other elements must go into array `B`.

Return the **absolute** difference between the sums of the two arrays: `|sum(A) - sum(B)|`.

**Note:** An empty array has a sum of 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3,4]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- The only prime index in the array is 2, so `nums[2] = 4` is placed in array `A`.

	- The remaining elements, `nums[0] = 2` and `nums[1] = 3` are placed in array `B`.

	- `sum(A) = 4`, `sum(B) = 2 + 3 = 5`.

	- The absolute difference is `|4 - 5| = 1`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-1,5,7,0]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- The prime indices in the array are 2 and 3, so `nums[2] = 7` and `nums[3] = 0` are placed in array `A`.

	- The remaining elements, `nums[0] = -1` and `nums[1] = 5` are placed in array `B`.

	- `sum(A) = 7 + 0 = 7`, `sum(B) = -1 + 5 = 4`.

	- The absolute difference is `|7 - 4| = 3`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`
