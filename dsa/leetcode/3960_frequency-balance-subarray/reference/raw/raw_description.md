## Description

You are given an integer array ​​​​​​​`nums`.

Define a **frequency balance <span data-keyword="subarray-nonempty">subarray</span>** as follows:

	- If the subarray contains only one distinct value, it is frequency balanced.

	- Otherwise, there must exist a positive integer `f` such that every distinct value in the subarray occurs either `f` or `2 * f` times, and both <span data-keyword="frequency-array">frequencies</span> occur among the distinct values.

Return an integer denoting the length of the **longest** frequency balance subarray.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,2,1,2,3,3,3]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- The longest frequency balance subarray is `[2, 1, 2, 3, 3]`.

	- The elements that appear most frequently are 2 and 3, both appearing twice.

	- The remaining element 1 appears once, meeting the requirements.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,5,5,5]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- The longest frequency balance subarray is `[5, 5, 5, 5]`.

	- The element that appears most frequently is 5.

	- There are no other elements meeting the requirements.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

Since all elements appear only once, the length of the longest frequency balance subarray is 1.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^​​​​​​​3`

	- `1 <= nums[i] <= 10^​​​​​​​9`
