## Description

You are given an array `nums1` of `n` **distinct** integers.

You want to construct another array `nums2` of length `n` such that the elements in `nums2` are either **all odd or all even**.

For each index `i`, you must choose **exactly one** of the following (in any order):

	- `nums2[i] = nums1[i]`​​​​​​​

	- `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`, such that `nums1[i] - nums1[j] >= 1`

Return `true` if it is possible to construct such an array, otherwise return `false`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [1,4,7]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**​​​​​​​​​​​​​​

	- Set `nums2[0] = nums1[0] = 1`.

	- Set `nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3`.

	- Set `nums2[2] = nums1[2] = 7`.

	- `nums2 = [1, 3, 7]`, and all elements are odd. Thus, the answer is `true`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [2,3]</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

It is not possible to construct `nums2` such that all elements have the same parity. Thus, the answer is `false`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [4,6]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

	- Set `nums2[0] = nums1[0] = 4`.

	- Set `nums2[1] = nums1[1] = 6`.

	- `nums2 = [4, 6]`, and all elements are even. Thus, the answer is `true`.

</div>

**Constraints:**

	- `1 <= n == nums1.length <= 10^5`

	- `1 <= nums1[i] <= 10^9`

	- `nums1` consists of distinct integers.
