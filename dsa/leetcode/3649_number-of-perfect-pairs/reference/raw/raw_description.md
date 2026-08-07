## Description

You are given an integer array `nums`.

A pair of indices `(i, j)` is called **perfect** if the following conditions are satisfied:

	- `i < j`

	- Let `a = nums[i]`, `b = nums[j]`. Then:

		<li>`min(|a - b|, |a + b|) <= min(|a|, |b|)`

		- `max(|a - b|, |a + b|) >= max(|a|, |b|)`

	</li>

Return the number of **distinct** perfect pairs.

**Note:** The absolute value `|x|` refers to the **non-negative** value of `x`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,1,2,3]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

There are 2 perfect pairs:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`(i, j)`</th>
			<th style="border: 1px solid black;">`(a, b)`</th>
			<th style="border: 1px solid black;">`min(|a − b|, |a + b|)`</th>
			<th style="border: 1px solid black;">`min(|a|, |b|)`</th>
			<th style="border: 1px solid black;">`max(|a − b|, |a + b|)`</th>
			<th style="border: 1px solid black;">`max(|a|, |b|)`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">(1, 2)</td>
			<td style="border: 1px solid black;">(1, 2)</td>
			<td style="border: 1px solid black;">`min(|1 − 2|, |1 + 2|) = 1`</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`max(|1 − 2|, |1 + 2|) = 3`</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(2, 3)</td>
			<td style="border: 1px solid black;">(2, 3)</td>
			<td style="border: 1px solid black;">`min(|2 − 3|, |2 + 3|) = 1`</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`max(|2 − 3|, |2 + 3|) = 5`</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
	</tbody>
</table>
</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-3,2,-1,4]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

There are 4 perfect pairs:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`(i, j)`</th>
			<th style="border: 1px solid black;">`(a, b)`</th>
			<th style="border: 1px solid black;">`min(|a − b|, |a + b|)`</th>
			<th style="border: 1px solid black;">`min(|a|, |b|)`</th>
			<th style="border: 1px solid black;">`max(|a − b|, |a + b|)`</th>
			<th style="border: 1px solid black;">`max(|a|, |b|)`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">(0, 1)</td>
			<td style="border: 1px solid black;">(-3, 2)</td>
			<td style="border: 1px solid black;">`min(|-3 - 2|, |-3 + 2|) = 1`</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`max(|-3 - 2|, |-3 + 2|) = 5`</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(0, 3)</td>
			<td style="border: 1px solid black;">(-3, 4)</td>
			<td style="border: 1px solid black;">`min(|-3 - 4|, |-3 + 4|) = 1`</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">`max(|-3 - 4|, |-3 + 4|) = 7`</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(1, 2)</td>
			<td style="border: 1px solid black;">(2, -1)</td>
			<td style="border: 1px solid black;">`min(|2 - (-1)|, |2 + (-1)|) = 1`</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">`max(|2 - (-1)|, |2 + (-1)|) = 3`</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(1, 3)</td>
			<td style="border: 1px solid black;">(2, 4)</td>
			<td style="border: 1px solid black;">`min(|2 - 4|, |2 + 4|) = 2`</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">`max(|2 - 4|, |2 + 4|) = 6`</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
	</tbody>
</table>
</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,10,100,1000]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There are no perfect pairs. Thus, the answer is 0.

</div>

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`
