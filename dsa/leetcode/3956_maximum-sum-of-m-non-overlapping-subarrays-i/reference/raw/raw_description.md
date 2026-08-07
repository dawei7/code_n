## Description

You are given an integer array `nums` of length `n`, and three integers `m`, `l`, and `r`.

Your task is to select **at least** one and **at most** `m` **non-overlapping <span data-keyword="subarray-nonempty">subarrays</span>** from `nums` such that:

	- Each selected **subarray** has a length between `[l, r]` (inclusive).

	- The total sum of all selected **subarrays** is **maximized**.

Return the **maximum** total sum you can achieve.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,1,-5,2], m = 2, l = 1, r = 3</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

One optimal strategy is to:

	- Select the subarray `[4, 1]` with sum `4 + 1 = 5` and the subarray `[2]` with sum 2. Both subarrays have length between `[l, r]`.

	- The total sum of these subarrays is `5 + 2 = 7`, which is the maximum achievable sum with at most `m = 2` subarrays.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,0,3,4], m = 2, l = 1, r = 2</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

One optimal strategy is to:

	- Select the subarray `[1]` with sum `1` and the subarray `[3, 4]` with sum `3 + 4 = 7`. Both subarrays have length between `[l, r]`.

	- The total sum of these subarrays is `1 + 7 = 8`, which is the maximum achievable sum with at most `m = 2` subarrays.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-1,7,-4], m = 1, l = 2, r = 3</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

	- Select the subarray `[-1, 7]` from `nums` which has length between `[l, r]`.

	- The total sum of this subarray is `-1 + 7 = 6`, which is the maximum achievable sum with at most `m = 1` subarray.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-3,-4,-1], m = 2, l = 1, r = 2</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

	- All subarrays of `nums` have negative sums. The optimal strategy is to select the subarray `[-1]`, which has length between `[l, r]`.

	- The total sum of this subarray is -1, which is the maximum achievable sum with at most `m = 2` subarrays.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 1000`

	- `-10^9 <= nums[i] <= 10^9​​​​​​​`

	- `1 <= m <= n`

	- `1 <= l <= r <= n`
