## Description

You are given an integer array `nums` of length `n`.

An integer `k` is called **sortable** if `k` **divides** `n` and you can sort `nums` in **non-decreasing** order by sequentially performing the following operations:

	- Partition `nums` into **consecutive <span data-keyword="subarray-nonempty">subarrays</span>** of length `k`.

	- **Cyclically rotate each subarray independently** any number of times to the left or to the right.

Return an integer denoting the sum of all possible sortable integers `k`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,1,2]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**​​​​​​​

	- For `n = 3`, possible divisors are 1 and 3.

	- For `k = 1`: each subarray has one element. No rotation can sort the array.

	- For `k = 3`: the single subarray `[3, 1, 2]` can be rotated once to produce `[1, 2, 3]`, which is sorted.

	- Only `k = 3` is sortable. Hence, the answer is 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,6,5]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- For `n = 3`, possible divisors are 1 and 3.

	- For `k = 1`: each subarray has one element. No rotation can sort the array.

	- For `k = 3`: the single subarray `[7, 6, 5]` cannot be rotated into non-decreasing order.

	- No `k` is sortable. Hence, the answer is 0.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,8]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**​​​​​​​

	- For `n = 2`, possible divisors are 1 and 2.

	- Since `[5, 8]` is already sorted, every divisor is sortable. Hence, the answer is `1 + 2 = 3`.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
