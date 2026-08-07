## Description

You are given an integer array `nums`. In this array:

	- Exactly one element appears **once**.

	- Exactly one element appears **twice**.

	- All other elements appear **exactly three times**.

Return an integer array of length 2, where the first element is the one that appears **once**, and the second is the one that appears **twice**.

Your solution must run in **O(n)** time and **O(1)** space.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2,3,2,5,5,5,7,7]</span>

**Output:** <span class="example-io">[3,7]</span>

**Explanation:**

The element 3 appears **once**, and the element 7 appears **twice**. The remaining elements each appear **three times**.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,4,6,4,9,9,9,6,8]</span>

**Output:** <span class="example-io">[8,6]</span>

**Explanation:**

The element 8 appears **once**, and the element 6 appears **twice**. The remaining elements each appear **three times**.

</div>

**Constraints:**

	- `3 <= nums.length <= 10^5`

	- `-2^31 <= nums[i] <= 2^31 - 1`

	- `nums.length` is a multiple of 3.

	- Exactly one element appears once, one element appears twice, and all other elements appear three times.
