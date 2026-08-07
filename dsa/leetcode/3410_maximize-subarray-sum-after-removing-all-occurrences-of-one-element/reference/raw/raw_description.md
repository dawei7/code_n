## Description

You are given an integer array `nums`.

You can do the following operation on the array **at most** once:

	- Choose **any** integer `x` such that `nums` remains **non-empty** on removing all occurrences of `x`.

	- Remove **all** occurrences of `x` from the array.

Return the **maximum** <span data-keyword="subarray-nonempty">subarray</span> sum across **all** possible resulting arrays.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-3,2,-2,-1,3,-2,3]</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

We can have the following arrays after at most one operation:

	- The original array is `nums = [<span class="example-io">-3, 2, -2, -1, <u>**3, -2, 3**</u></span>]`. The maximum subarray sum is `3 + (-2) + 3 = 4`.

	- Deleting all occurences of `x = -3` results in `nums = [2, -2, -1, **<u><span class="example-io">3, -2, 3</span></u>**]`. The maximum subarray sum is `3 + (-2) + 3 = 4`.

	- Deleting all occurences of `x = -2` results in `nums = [<span class="example-io">-3, **<u>2, -1, 3, 3</u>**</span>]`. The maximum subarray sum is `2 + (-1) + 3 + 3 = 7`.

	- Deleting all occurences of `x = -1` results in `nums = [<span class="example-io">-3, 2, -2, **<u>3, -2, 3</u>**</span>]`. The maximum subarray sum is `3 + (-2) + 3 = 4`.

	- Deleting all occurences of `x = 3` results in `nums = [<span class="example-io">-3, <u>**2**</u>, -2, -1, -2</span>]`. The maximum subarray sum is 2.

The output is `max(4, 4, 7, 4, 2) = 7`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4]</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

It is optimal to not perform any operations.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^6 <= nums[i] <= 10^6`
