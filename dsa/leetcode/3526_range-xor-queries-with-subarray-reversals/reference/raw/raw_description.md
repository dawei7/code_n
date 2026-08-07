## Description

You are given an integer array `nums` of length `n` and a 2D integer array `queries` of length `q`, where each query is one of the following three types:

	- **Update**: `queries[i] = [1, index, value]`<br data-end="259" data-start="256" />
	Set `nums[index] = value`.

	- **Range XOR Query**: `queries[i] = [2, left, right]`<br data-end="348" data-start="345" />
	Compute the bitwise XOR of all elements in the <span data-keyword="subarray">subarray</span> `nums[left...right]`, and record this result.

	- **Reverse Subarray**: `queries[i] = [3, left, right]`<br data-end="511" data-start="508" />
	Reverse the <span data-keyword="subarray">subarray</span> `nums[left...right]` in place.

Return *an array of the results of all range XOR queries* in the order they were encountered.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5], queries = [[2,1,3],[1,2,10],[3,0,4],[2,0,4]]</span>

**Output:** <span class="example-io">[5,8]</span>

**Explanation:**

	- **Query**** 1****:** `[2, 1, 3]` – Compute XOR of subarray `[2, 3, 4]` resulting in 5.

	- **Query 2:** `[1, 2, 10]` – Update `nums[2]` to 10, updating the array to `[1, 2, 10, 4, 5]`.

	- **Query 3:** `[3, 0, 4]` – Reverse the entire array to get `[5, 4, 10, 2, 1]`.

	- **Query 4:** `[2, 0, 4]` – Compute XOR of subarray `[5, 4, 10, 2, 1]` resulting in 8.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,8,9], queries = [[1,0,3],[2,0,2],[3,1,2]]</span>

**Output:** <span class="example-io">[2]</span>

**Explanation:**

	- **Query 1:** `[1, 0, 3]` – Update `nums[0]` to 3, updating the array to `[3, 8, 9]`.

	- **Query 2:** `[2, 0, 2]` – Compute XOR of subarray `[3, 8, 9]` resulting in 2.

	- **Query 3:** `[3, 1, 2]` – Reverse the subarray `[8, 9]` to get `[9, 8]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`

	- `1 <= queries.length <= 10^5`

	- `queries[i].length == 3​`

	- `queries[i][0] ∈ {1, 2, 3}​`

	- If `queries[i][0] == 1`:`​`

		<li data-end="691" data-start="606">`0 <= index < nums.length​`

		- `0 <= value <= 10^9`

	</li>
	- If `queries[i][0] == 2` or `queries[i][0] == 3`:`​`

		<li data-end="959" data-start="874">`0 <= left <= right < nums.length​`

	</li>
