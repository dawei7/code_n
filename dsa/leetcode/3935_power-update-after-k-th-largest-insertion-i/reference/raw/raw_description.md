## Description

You are given an integer array `nums` and an integer `p`.

You are also given a 2D integer array `queries`, where each `queries[i] = [val_i, k_i]` and the difference between **consecutive** `k_i` values is always **less** than 10.

For each query:

	- Insert `val_i` into `nums`.

	- Let `x` be the `k_i^th` **largest** element in the current `nums`.

	- **Update** `p` to `p^x % (10^9 + 7)`.

Return an array `ans` where the `ans[i]` represents the value of `p` after processing the `i^th` query.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2], p = 4, queries = [[3,1],[1,2]]</span>

**Output:** <span class="example-io">[64,4096]</span>

**Explanation:**

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<thead>
		<tr>
			<th>`i`</th>
			<th>`val_i`</th>
			<th>Current

			`nums`</th>
			<th>`k_i`</th>
			<th>`k_i^th`

			largest</th>
			<th>p</th>
			<th>New `p = p^k % (10^9 + 7)`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>3</td>
			<td>[2, 3]</td>
			<td>1</td>
			<td>3</td>
			<td>4</td>
			<td>4^3 % (10^9 + 7) = 64</td>
		</tr>
		<tr>
			<td>1</td>
			<td>1</td>
			<td>[2, 3, 1]</td>
			<td>2</td>
			<td>2</td>
			<td>64</td>
			<td>64^2 % (10^9 + 7) = 4096</td>
		</tr>
	</tbody>
</table>

Thus, `ans = [64, 4096]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,5], p = 6, queries = [[4,3],[7,2]]</span>

**Output:** <span class="example-io">[1296,220296870]</span>

**Explanation:**

<div class="example-block">
<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<thead>
		<tr>
			<th>`i`</th>
			<th>`val_i`</th>
			<th>Current​​​​​​​

			`nums`</th>
			<th>`k_i`</th>
			<th>`k_i^th`

			largest</th>
			<th>`p`</th>
			<th>New `p = p^k % (10^9 + 7)`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>4</td>
			<td>[7, 5, 4]</td>
			<td>3</td>
			<td>4</td>
			<td>6</td>
			<td>6^4 % (10^9 + 7) = 1296</td>
		</tr>
		<tr>
			<td>1</td>
			<td>7</td>
			<td>[7, 5, 4, 7]</td>
			<td>2</td>
			<td>7</td>
			<td>1296</td>
			<td>1296^7 % (10^9 + 7) = 220296870</td>
		</tr>
	</tbody>
</table>

Thus, `ans = [1296, 220296870]`

</div>
</div>

**Constraints:**

	- `1 <= nums.length <= 2 × 10^4`

	- `1 <= nums[i] <= 10^6`

	- `​​​​​​​1 <= p <= 10^6`

	- `1 <= queries.length <= 2 × 10^4`

	- `^​​​​​​​1 <= val_i <= 10^6`

	- `1 <= k_i <= n + i + 1`

	- `|k_i - k_i - 1| < 10` for `i > 0`
