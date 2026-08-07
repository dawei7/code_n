## Description

We call an array `arr` of length `n` **consecutive** if one of the following holds:

	- `arr[i] - arr[i - 1] == 1` for *all* `1 <= i < n`.

	- `arr[i] - arr[i - 1] == -1` for *all* `1 <= i < n`.

The **value** of an array is the sum of its elements.

For example, `[3, 4, 5]` is a consecutive array of value 12 and `[9, 8]` is another of value 17. While `[3, 4, 3]` and `[8, 6]` are not consecutive.

Given an array of integers `nums`, return the *sum* of the **values** of all **consecutive **<span data-keyword="subarray-nonempty">subarrays</span>.

Since the answer may be very large, return it **modulo** `10^9 + 7.`

**Note** that an array of length 1 is also considered consecutive.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3]</span>

**Output:** <span class="example-io">20</span>

**Explanation:**

The consecutive subarrays are: `[1]`, `[2]`, `[3]`, `[1, 2]`, `[2, 3]`, `[1, 2, 3]`.

Sum of their values would be: `1 + 2 + 3 + 3 + 5 + 6 = 20`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,5,7]</span>

**Output:** <span class="example-io">16</span>

**Explanation:**

The consecutive subarrays are: `[1]`, `[3]`, `[5]`, `[7]`.

Sum of their values would be: `1 + 3 + 5 + 7 = 16`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,6,1,2]</span>

**Output:** <span class="example-io">32</span>

**Explanation:**

The consecutive subarrays are: `[7]`, `[6]`, `[1]`, `[2]`, `[7, 6]`, `[1, 2]`.

Sum of their values would be: `7 + 6 + 1 + 2 + 13 + 3 = 32`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
