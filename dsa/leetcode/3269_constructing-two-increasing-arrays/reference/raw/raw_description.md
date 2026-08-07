## Description

Given 2 integer arrays `nums1` and `nums2` consisting only of 0 and 1, your task is to calculate the **minimum** possible **largest** number in arrays `nums1` and `nums2`, after doing the following.

Replace every 0 with an *even positive integer* and every 1 with an *odd positive integer*. After replacement, both arrays should be **increasing** and each integer should be used **at most** once.

Return the *minimum possible largest number* after applying the changes.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [], nums2 = [1,0,1,1]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

After replacing, `nums1 = []`, and `nums2 = [1, 2, 3, 5]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [0,1,0,1], nums2 = [1,0,0,1]</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

One way to replace, having 9 as the largest element is `nums1 = [2, 3, 8, 9]`, and `nums2 = [1, 4, 6, 7]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [0,1,0,0,1], nums2 = [0,0,0,1]</span>

**Output:** <span class="example-io">13</span>

**Explanation:**

One way to replace, having 13 as the largest element is `nums1 = [2, 3, 4, 6, 7]`, and `nums2 = [8, 10, 12, 13]`.

</div>

**Constraints:**

	- `0 <= nums1.length <= 1000`

	- `1 <= nums2.length <= 1000`

	- `nums1` and `nums2` consist only of 0 and 1.
