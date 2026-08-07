## Description

You are given an integer array `capacity`.

A <span data-keyword="subarray-nonempty">subarray</span> `capacity[l..r]` is considered **stable** if:

	- Its length is **at least** 3.

	- The **first** and **last** elements are each equal to the **sum** of all elements **strictly between** them (i.e., `capacity[l] = capacity[r] = capacity[l + 1] + capacity[l + 2] + ... + capacity[r - 1]`).

Return an integer denoting the number of **stable subarrays**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">capacity = [9,3,3,3,9]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- `[9,3,3,3,9]` is stable because the first and last elements are both 9, and the sum of the elements strictly between them is `3 + 3 + 3 = 9`.

	- `[3,3,3]` is stable because the first and last elements are both 3, and the sum of the elements strictly between them is 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">capacity = [1,2,3,4,5]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

No subarray of length at least 3 has equal first and last elements, so the answer is 0.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">capacity = [-4,4,0,0,-8,-4]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

`[-4,4,0,0,-8,-4]` is stable because the first and last elements are both -4, and the sum of the elements strictly between them is `4 + 0 + 0 + (-8) = -4`

</div>

**Constraints:**

	- `3 <= capacity.length <= 10^5`

	- `-10^9 <= capacity[i] <= 10^9`
