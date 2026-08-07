## Description

You are given an array `nums` consisting of integers. You are also given a 2D array `queries`, where `queries[i] = [pos_i, x_i]`.

For query `i`, we first set `nums[pos_i]` equal to `x_i`, then we calculate the answer to query `i` which is the **maximum** sum of a <span data-keyword="subsequence-array">subsequence</span> of `nums` where **no two adjacent elements are selected**.

Return the *sum* of the answers to all queries.

Since the final answer may be very large, return it **modulo** `10^9 + 7`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,5,9], queries = [[1,-2],[0,-3]]</span>

**Output:** <span class="example-io">21</span>

**Explanation:**

After the 1^st query, `nums = [3,-2,9]` and the maximum sum of a subsequence with non-adjacent elements is `3 + 9 = 12`.

After the 2^nd query, `nums = [-3,-2,9]` and the maximum sum of a subsequence with non-adjacent elements is 9.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,-1], queries = [[0,-5]]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

After the 1^st query, `nums = [-5,-1]` and the maximum sum of a subsequence with non-adjacent elements is 0 (choosing an empty subsequence).

</div>

**Constraints:**

	- `1 <= nums.length <= 5 * 10^4`

	- `-10^5 <= nums[i] <= 10^5`

	- `1 <= queries.length <= 5 * 10^4`

	- `queries[i] == [pos_i, x_i]`

	- `0 <= pos_i <= nums.length - 1`

	- `-10^5 <= x_i <= 10^5`
