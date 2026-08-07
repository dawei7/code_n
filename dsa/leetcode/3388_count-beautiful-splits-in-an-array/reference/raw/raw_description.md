## Description

You are given an array `nums`.

A split of an array `nums` is **beautiful** if:

	- The array `nums` is split into three <span data-keyword="subarray-nonempty">subarrays</span>: `nums1`, `nums2`, and `nums3`, such that `nums` can be formed by concatenating `nums1`, `nums2`, and `nums3` in that order.

	- The subarray `nums1` is a <span data-keyword="array-prefix">prefix</span> of `nums2` **OR** `nums2` is a <span data-keyword="array-prefix">prefix</span> of `nums3`.

Return the **number of ways** you can make this split.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,2,1]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The beautiful splits are:

	- A split with `nums1 = [1]`, `nums2 = [1,2]`, `nums3 = [1]`.

	- A split with `nums1 = [1]`, `nums2 = [1]`, `nums3 = [2,1]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There are 0 beautiful splits.

</div>

**Constraints:**

	- `1 <= nums.length <= 5000`

	- `<font face="monospace">0 <= nums[i] <= 50</font>`
