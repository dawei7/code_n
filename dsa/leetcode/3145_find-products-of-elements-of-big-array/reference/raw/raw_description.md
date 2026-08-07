## Description

The **powerful array** of a non-negative integer `x` is defined as the shortest sorted array of powers of two that sum up to `x`. The table below illustrates examples of how the **powerful array** is determined. It can be proven that the powerful array of `x` is unique.

<table border="1">
	<tbody>
		<tr>
			<th>num</th>
			<th>Binary Representation</th>
			<th>powerful array</th>
		</tr>
		<tr>
			<td>1</td>
			<td>0000<u>1</u></td>
			<td>[1]</td>
		</tr>
		<tr>
			<td>8</td>
			<td>0<u>1</u>000</td>
			<td>[8]</td>
		</tr>
		<tr>
			<td>10</td>
			<td>0<u>1</u>0<u>1</u>0</td>
			<td>[2, 8]</td>
		</tr>
		<tr>
			<td>13</td>
			<td>0<u>11</u>0<u>1</u></td>
			<td>[1, 4, 8]</td>
		</tr>
		<tr>
			<td>23</td>
			<td><u>1</u>0<u>111</u></td>
			<td>[1, 2, 4, 16]</td>
		</tr>
	</tbody>
</table>

The array `big_nums` is created by concatenating the **powerful arrays** for every positive integer `i` in ascending order: 1, 2, 3, and so on. Thus, `big_nums` begins as `[<u>1</u>, <u>2</u>, <u>1, 2</u>, <u>4</u>, <u>1, 4</u>, <u>2, 4</u>, <u>1, 2, 4</u>, <u>8</u>, ...]`.

You are given a 2D integer matrix `queries`, where for `queries[i] = [from_i, to_i, mod_i]` you should calculate `(big_nums[from_i] * big_nums[from_i + 1] * ... * big_nums[to_i]) % mod_i`<!-- notionvc: a71131cc-7b52-4786-9a4b-660d6d864f89 -->.

Return an integer array `answer` such that `answer[i]` is the answer to the `i^th` query.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">queries = [[1,3,7]]</span>

**Output:** <span class="example-io">[4]</span>

**Explanation:**

There is one query.

`big_nums[1..3] = [2,1,2]`. The product of them is 4. The result is `4 % 7 = 4.`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">queries = [[2,5,3],[7,7,4]]</span>

**Output:** <span class="example-io">[2,2]</span>

**Explanation:**

There are two queries.

First query: `big_nums[2..5] = [1,2,4,1]`. The product of them is 8. The result is `8 % 3 = 2`.

Second query: `big_nums[7] = 2`. The result is `2 % 4 = 2`.

</div>

**Constraints:**

	- `1 <= queries.length <= 500`

	- `queries[i].length == 3`

	- `0 <= queries[i][0] <= queries[i][1] <= 10^15`

	- `1 <= queries[i][2] <= 10^5`
