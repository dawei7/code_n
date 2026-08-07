## Description

You are given an integer array `nums` and an integer `k`.

Return the **minimum** length of a **<span data-keyword="subarray-nonempty">subarray</span>** whose sum of the **distinct** values present in that subarray (each value counted once) is **at least** `k`. If no such subarray exists, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2,3,1], k = 4</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The subarray `[2, 3]` has distinct elements `{2, 3}` whose sum is `2 + 3 = 5`, which is ​​​​​​​at least `k = 4`. Thus, the answer is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,2,3,4], k = 5</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The subarray `[3, 2]` has distinct elements `{3, 2}` whose sum is `3 + 2 = 5`, which is ​​​​​​​at least `k = 5`. Thus, the answer is 2.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,5,4], k = 5</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The subarray `[5]` has distinct elements `{5}` whose sum is `5`, which is at least `k = 5`. Thus, the answer is 1.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- `1 <= k <= 10^9`
