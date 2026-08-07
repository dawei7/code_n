## Description

An array is considered **special** if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer `nums` and a 2D integer matrix `queries`, where for `queries[i] = [from_i, to_i]` your task is to check that <span data-keyword="subarray">subarray</span> `nums[from_i..to_i]` is **special** or not.

Return an array of booleans `answer` such that `answer[i]` is `true` if `nums[from_i..to_i]` is special.<!-- notionvc: e5d6f4e2-d20a-4fbd-9c7f-22fbe52ef730 -->

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,4,1,2,6], queries = [[0,4]]</span>

**Output:** <span class="example-io">[false]</span>

**Explanation:**

The subarray is `[3,4,1,2,6]`. 2 and 6 are both even.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,3,1,6], queries = [[0,2],[2,3]]</span>

**Output:** <span class="example-io">[false,true]</span>

**Explanation:**

	- The subarray is `[4,3,1]`. 3 and 1 are both odd. So the answer to this query is `false`.

	- The subarray is `[1,6]`. There is only one pair: `(1,6)` and it contains numbers with different parity. So the answer to this query is `true`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- `1 <= queries.length <= 10^5`

	- `queries[i].length == 2`

	- `0 <= queries[i][0] <= queries[i][1] <= nums.length - 1`
