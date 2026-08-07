## Description

You are given an array of integers `nums` with length `n`, and a positive **odd** integer `k`.

Select exactly **`k`** disjoint <span data-keyword="subarray-nonempty">subarrays</span> **`sub_1, sub_2, ..., sub_k`** from `nums` such that the last element of `sub_i` appears before the first element of `sub_{i+1}` for all `1 <= i <= k-1`. The goal is to maximize their combined strength.

The strength of the selected subarrays is defined as:

`strength = k * sum(sub_1)- (k - 1) * sum(sub_2) + (k - 2) * sum(sub_3) - ... - 2 * sum(sub_{k-1}) + sum(sub_k)`

where **`sum(sub_i)`** is the sum of the elements in the `i`-th subarray.

Return the **maximum** possible strength that can be obtained from selecting exactly **`k`** disjoint subarrays from `nums`.

**Note** that the chosen subarrays **don't** need to cover the entire array.

**Example 1:**

**Input:** <span class="example-io">nums = [1,2,3,-1,2], k = 3</span>

**Output:** <span class="example-io">22</span>

**Explanation:**

The best possible way to select 3 subarrays is: nums[0..2], nums[3..3], and nums[4..4]. The strength is calculated as follows:

`strength = 3 * (1 + 2 + 3) - 2 * (-1) + 2 = 22`

**Example 2:**

**Input:** <span class="example-io">nums = [12,-2,-2,-2,-2], k = 5</span>

**Output:** <span class="example-io">64</span>

**Explanation:**

The only possible way to select 5 disjoint subarrays is: nums[0..0], nums[1..1], nums[2..2], nums[3..3], and nums[4..4]. The strength is calculated as follows:

`strength = 5 * 12 - 4 * (-2) + 3 * (-2) - 2 * (-2) + (-2) = 64`

**Example 3:**

**Input:** <span class="example-io">nums = [-1,-2,-3], k = </span>1

**Output:** <span class="example-io">-1</span>

**Explanation:**

The best possible way to select 1 subarray is: nums[0..0]. The strength is -1.

**Constraints:**

	- `1 <= n <= 10^4`

	- `-10^9 <= nums[i] <= 10^9`

	- `1 <= k <= n`

	- `1 <= n * k <= 10^6`

	- `k` is odd.
