## Description

You are given an integer array `nums` and two integers `a` and `b` such that `a < b`.

An array is called **good** if it can be split into three **contiguous** parts, in this order, such that:

	- Every element in the first part is **less than** `a`.

	- Every element in the second part is **in** the range `[a, b]` inclusive.

	- Every element in the third part is **greater than** `b`.

Any of the three parts **may be** empty.

In one **adjacent swap**, you may swap two **neighboring** elements of `nums`.

Return the **minimum number** of adjacent swaps required to make `nums` good. Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,2,4,5,6], a = 3, b = 4</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- Swap `nums[1]` and `nums[2]`. The array becomes `[1, 2, 3, 4, 5, 6]`.

	- This array is good because it can be split into `[1, 2]`, `[3, 4]`, and `[5, 6]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [9,7,5,3], a = 4, b = 8</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

One sequence of optimal swaps is as follows:

	- Swap `nums[2]` and `nums[3]`. The array becomes `[9, 7, 3, 5]`.

	- Swap `nums[1]` and `nums[2]`. The array becomes `[9, 3, 7, 5]`.

	- Swap `nums[0]` and `nums[1]`. The array becomes `[3, 9, 7, 5]`.

	- Swap `nums[1]` and `nums[2]`. The array becomes `[3, 7, 9, 5]`.

	- Swap `nums[2]` and `nums[3]`. The array becomes `[3, 7, 5, 9]`.

	- This array is good because it can be split into `[3]`, `[7, 5]`, and `[9]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,7,5,9], a = 4, b = 8</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The array is already good. No swaps are needed.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `​​​​​​​1 <= nums[i] <= 10^9`

	- `1 <= a < b <= 10^9​​​​​​​`
