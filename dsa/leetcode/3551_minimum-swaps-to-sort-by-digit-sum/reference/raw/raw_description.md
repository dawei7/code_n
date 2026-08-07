## Description

You are given an array `nums` of **distinct** positive integers. You need to sort the array in **increasing** order based on the sum of the digits of each number. If two numbers have the same digit sum, the **smaller** number appears first in the sorted order.

Return the **minimum** number of swaps required to rearrange `nums` into this sorted order.

A **swap** is defined as exchanging the values at two distinct positions in the array.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [37,100]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- Compute the digit sum for each integer: `[3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]`

	- Sort the integers based on digit sum: `[100, 37]`. Swap `37` with `100` to obtain the sorted order.

	- Thus, the minimum number of swaps required to rearrange `nums` is 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [22,14,33,7]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- Compute the digit sum for each integer: `[2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]`

	- Sort the integers based on digit sum: `[22, 14, 33, 7]`. The array is already sorted.

	- Thus, the minimum number of swaps required to rearrange `nums` is 0.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [18,43,34,16]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- Compute the digit sum for each integer: `[1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]`

	- Sort the integers based on digit sum: `[16, 34, 43, 18]`. Swap `18` with `16`, and swap `43` with `34` to obtain the sorted order.

	- Thus, the minimum number of swaps required to rearrange `nums` is 2.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `nums` consists of **distinct** positive integers.
