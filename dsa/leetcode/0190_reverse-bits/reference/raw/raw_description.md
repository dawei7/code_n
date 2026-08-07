## Description

Reverse bits of a given 32 bits signed integer.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 43261596</span>

**Output:** <span class="example-io">964176192</span>

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>Integer</th>
			<th>Binary</th>
		</tr>
		<tr>
			<td>43261596</td>
			<td>00000010100101000001111010011100</td>
		</tr>
		<tr>
			<td>964176192</td>
			<td>00111001011110000010100101000000</td>
		</tr>
	</tbody>
</table>
</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 2147483644</span>

**Output:** <span class="example-io">1073741822</span>

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>Integer</th>
			<th>Binary</th>
		</tr>
		<tr>
			<td>2147483644</td>
			<td>01111111111111111111111111111100</td>
		</tr>
		<tr>
			<td>1073741822</td>
			<td>00111111111111111111111111111110</td>
		</tr>
	</tbody>
</table>
</div>

**Constraints:**

	- `0 <= n <= 2^31 - 2`

	- `n` is even.

**Follow up:** If this function is called many times, how would you optimize it?
