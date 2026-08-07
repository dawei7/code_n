## Description

You are given an integer `n` and an integer array `prices` of length `n`, where `prices[i]` is the price of apples at shop `i`.

You are also given a 2D integer array `roads`, where `roads[i] = [u_i, v_i, cost_i, tax_i]` represents a **bidirectional** road:

	- `u_i` and `v_i` are the shops connected by the road.

	- `cost_i` is the cost to travel the road **without** carrying apples.

	- `tax_i` is the multiplier applied to `cost_i` when traveling **with** apples.

For each shop `i`, you can either:

	- Buy apples locally at shop `i` for `prices[i]`.

	- Travel **empty** to any shop `j` using **any** number of roads, buy apples for `prices[j]`, and return to shop `i` while carrying apples, paying `cost * tax` on each road used for the return trip.

The forward path, where you travel empty, and the return path may be **different**.

Return an integer array `ans` of length `n`, where `ans[i]` is the **minimum** total cost to buy apples starting from shop `i`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 2, prices = [8,3], roads = [[0,1,1,2]]</span>

**Output:** <span class="example-io">[6,3]</span>

**Explanation:**

![](images/screenshot-2025-08-23-at-23341-am.png)

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<thead>
		<tr>
			<th>Shop `i`</th>
			<th>`prices[i]`</th>
			<th>Shop `j`</th>
			<th>`prices[j]`</th>
			<th>`cost_i`</th>
			<th>`tax_i`</th>
			<th>Travel cost</th>
			<th>Return cost</th>
			<th>Total</th>
			<th>Minimum</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>8</td>
			<td>1</td>
			<td>3</td>
			<td>1</td>
			<td>2</td>
			<td>1</td>
			<td>`1 * 2 = 2`</td>
			<td>`1 + 2 + 3 = 6`</td>
			<td>`min(8, 6) = 6`</td>
		</tr>
		<tr>
			<td>1</td>
			<td>3</td>
			<td>0</td>
			<td>8</td>
			<td>1</td>
			<td>2</td>
			<td>1</td>
			<td>`1 * 2 = 2`</td>
			<td>`1 + 2 + 8 = 11`</td>
			<td>`min(3, 11) = 3`</td>
		</tr>
	</tbody>
</table>

Thus, the answer is `[6, 3]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, prices = [9,4,6], roads = [[0,1,1,3],[1,2,4,2]]</span>

**Output:** <span class="example-io">[8,4,6]</span>

**Explanation:**

![](images/screenshot-2025-08-23-at-23736-am.png)

**​​​​​​​**

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<thead>
		<tr>
			<th>Shop `i`</th>
			<th>`prices[i]`</th>
			<th>Shop `j`</th>
			<th>`prices[j]`</th>
			<th>`cost_i`</th>
			<th>`tax_i`</th>
			<th>Travel cost</th>
			<th>Return cost</th>
			<th>Total</th>
			<th>Minimum</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>9</td>
			<td>1</td>
			<td>4</td>
			<td>1</td>
			<td>3</td>
			<td>1</td>
			<td>`1 * 3 = 3`</td>
			<td>`1 + 3 + 4 = 8`</td>
			<td>`min(9, 8) = 8`</td>
		</tr>
		<tr>
			<td>1</td>
			<td>4</td>
			<td>2</td>
			<td>6</td>
			<td>4</td>
			<td>2</td>
			<td>4</td>
			<td>`4 * 2 = 8`</td>
			<td>`4 + 8 + 6 = 18`</td>
			<td>`min(4, 18) = 4`</td>
		</tr>
		<tr>
			<td>2</td>
			<td>6</td>
			<td>1</td>
			<td>4</td>
			<td>4</td>
			<td>2</td>
			<td>4</td>
			<td>`4 * 2 = 8`</td>
			<td>`4 + 8 + 4 = 16`</td>
			<td>`min(6, 16) = 6`</td>
		</tr>
	</tbody>
</table>

Thus, the answer is `[8, 4, 6]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, prices = [10,11,1], roads = [[0,2,1,3],[1,2,3,4],[0,1,5,2]]</span>

**Output:** <span class="example-io">[5,11,1]</span>

**Explanation:**

**​​​​​​​​​​​​​​**

![](images/screenshot-2025-08-23-at-24644-am.png)

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<thead>
		<tr>
			<th>Shop `i`</th>
			<th>`prices[i]`</th>
			<th>Shop `j`</th>
			<th>`prices[j]`</th>
			<th>`cost_i`</th>
			<th>`tax_i`</th>
			<th>Travel cost</th>
			<th>Return cost</th>
			<th>Total</th>
			<th>Minimum</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>10</td>
			<td>2</td>
			<td>1</td>
			<td>1</td>
			<td>3</td>
			<td>1</td>
			<td>`1 * 3 = 3`</td>
			<td>`1 + 3 + 1 = 5`</td>
			<td>`min(10, 5) = 5`</td>
		</tr>
		<tr>
			<td>1</td>
			<td>11</td>
			<td>2</td>
			<td>1</td>
			<td>3</td>
			<td>4</td>
			<td>3</td>
			<td>`3 * 4 = 12`</td>
			<td>`3 + 12 + 1 = 16`</td>
			<td>`min(11, 16) = 11`</td>
		</tr>
		<tr>
			<td>2</td>
			<td>1</td>
			<td>0</td>
			<td>10</td>
			<td>1</td>
			<td>3</td>
			<td>1</td>
			<td>`1 * 3 = 3`</td>
			<td>`1 + 3 + 10 = 14`</td>
			<td>`min(1, 14) = 1`</td>
		</tr>
	</tbody>
</table>

Thus, the answer is `[5, 11, 1]`.

</div>

**Constraints:**

	- `1 <= n <= 1000`

	- `prices.length == n`

	- `1 <= prices[i] <= 10^9`

	- `0 <= roads.length <= min(n × (n - 1) / 2, 2000)`

	- `roads[i] = [u_i, v_i, cost_i, tax_i]`

	- `0 <= u_i, v_i <= n - 1`

	- `u_i != v_i`

	- `1 <= cost_i <= 10^9`

	- `​​​​​​​1 <= tax_​​​​​​​i <= 100`​​​​​​​

	- There are no **repeated** edges.
