## Description

You are given an integer array `nums` of length `n` and a 2D array `queries` where `queries[i] = [l_i, r_i]`.

Each `queries[i]` represents the following action on `nums`:

	- Decrement the value at each index in the range `[l_i, r_i]` in `nums` by **at most**** **1.

	- The amount by which the value is decremented can be chosen **independently** for each index.

A **Zero Array** is an array with all its elements equal to 0.

Return the **maximum **number of elements that can be removed from `queries`, such that `nums` can still be converted to a **zero array** using the *remaining* queries. If it is not possible to convert `nums` to a **zero array**, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

After removing `queries[2]`, `nums` can still be converted to a zero array.

	- Using `queries[0]`, decrement `nums[0]` and `nums[2]` by 1 and `nums[1]` by 0.

	- Using `queries[1]`, decrement `nums[0]` and `nums[2]` by 1 and `nums[1]` by 0.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

We can remove `queries[2]` and `queries[3]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4], queries = [[0,3]]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

`nums` cannot be converted to a zero array even after using all the queries.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^5`

	- `1 <= queries.length <= 10^5`

	- `queries[i].length == 2`

	- `0 <= l_i <= r_i < nums.length`
