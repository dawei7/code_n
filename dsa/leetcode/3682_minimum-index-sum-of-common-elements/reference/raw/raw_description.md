## Description

You are given two integer arrays `nums1` and `nums2` of equal length `n`.

We define a pair of indices `(i, j)` as a **good pair** if `nums1[i] == nums2[j]`.

Return the **minimum index sum** `i + j` among all possible good pairs. If no such pairs exist, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [3,2,1], nums2 = [1,3,1]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- Common elements between `nums1` and `nums2` are 1 and 3.

	- For 3, `[i, j] = [0, 1]`, giving an index sum of `i + j = 1`.

	- For 1, `[i, j] = [2, 0]`, giving an index sum of `i + j = 2`.

	- The minimum index sum is 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [5,1,2], nums2 = [2,1,3]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- Common elements between `nums1` and `nums2` are 1 and 2.

	- For 1, `[i, j] = [1, 1]`, giving an index sum of `i + j = 2`.

	- For 2, `[i, j] = [2, 0]`, giving an index sum of `i + j = 2`.

	- The minimum index sum is 2.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [6,4], nums2 = [7,8]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

	- Since no common elements between `nums1` and `nums2`, the output is -1.

</div>

**Constraints:**

	- `1 <= nums1.length == nums2.length <= 10^5`

	- `-10^5 <= nums1[i], nums2[i] <= 10^5`
