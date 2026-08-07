## Description

You are given an integer array `nums`.

A **<span data-keyword="subarray-nonempty">subarray</span>** of `nums` is called **stable** if it contains **no inversions**, i.e., there is no pair of indices `i < j` such that `nums[i] > nums[j]`.

You are also given a **2D integer array** `queries` of length `q`, where each `queries[i] = [l_i, r_i]` represents a query. For each query `[l_i, r_i]`, compute the number of **stable subarrays** that lie entirely within the segment `nums[l_i..r_i]`.

Return an integer array `ans` of length `q`, where `ans[i]` is the answer to the `i^th` query.​​​​​​​​​​​​​​

**Note**:

	- A single element subarray is considered stable.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,1,2], queries = [[0,1],[1,2],[0,2]]</span>

**Output:** <span class="example-io">[2,3,4]</span>

**Explanation:**​​​​​

	- For `queries[0] = [0, 1]`, the subarray is `[nums[0], nums[1]] = [3, 1]`.

		<li>The stable subarrays are `[3]` and `[1]`. The total number of stable subarrays is 2.

	</li>
	- For `queries[1] = [1, 2]`, the subarray is `[nums[1], nums[2]] = [1, 2]`.

		<li>The stable subarrays are `[1]`, `[2]`, and `[1, 2]`. The total number of stable subarrays is 3.

	</li>
	- For `queries[2] = [0, 2]`, the subarray is `[nums[0], nums[1], nums[2]] = [3, 1, 2]`.

		<li>The stable subarrays are `[3]`, `[1]`, `[2]`, and `[1, 2]`. The total number of stable subarrays is 4.

	</li>

Thus, `ans = [2, 3, 4]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2], queries = [[0,1],[0,0]]</span>

**Output:** <span class="example-io">[3,1]</span>

**Explanation:**

	- For `queries[0] = [0, 1]`, the subarray is `[nums[0], nums[1]] = [2, 2]`.

		<li>The stable subarrays are `[2]`, `[2]`, and `[2, 2]`. The total number of stable subarrays is 3.

	</li>
	- For `queries[1] = [0, 0]`, the subarray is `[nums[0]] = [2]`.

		<li>The stable subarray is `[2]`. The total number of stable subarrays is 1.

	</li>

Thus, `ans = [3, 1]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- `1 <= queries.length <= 10^5`

	- `queries[i] = [l_i, r_i]`

	- `0 <= l_i <= r_i <= nums.length - 1`
