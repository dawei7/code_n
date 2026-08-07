## Description

You are given an integer array `nums` of length `n`, where `nums` is a <span data-keyword="permutation-array">permutation</span> of the integers from 0 to `n - 1`.

You may perform **only** the following operations:

	- **Reverse** the entire array.

	- **Rotate Left by One**: Move the first element to the end of the array, and rest elements to left by one position.

Return an integer denoting the **minimum** number of operations required to sort the array in **increasing** order. If it is **not possible** to sort the array using only the given operations, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,2,1]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- Rotate Left by one: `[2, 1, 0]`

	- Reverse the array: `[0, 1, 2]`

The array becomes sorted in 2 operations, which is minimal

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,0,2]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- Reverse the array: `[2, 0, 1]`

	- Rotate Left by one: `[0, 1, 2]`

The array becomes sorted in 2 operations, which is minimal.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,0,1,3]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

It is impossible to reach `[2, 0, 1, 3]`. Thus, the answer is -1.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `0 <= nums[i] <= n - 1`

	- `nums` is a permutation of integers from 0 to `n - 1`.
