### 1. Description

You are given two integers `n` and `k`.

Initially, you start with an array `a` of `n` integers where $a[i] = 1$ for all $0 \le i \le n - 1$. After each second, you simultaneously update each element to be the sum of all its preceding elements plus the element itself. For example, after one second, $a[0]$ remains the same, $a[1]$ becomes $a[0] + a[1]$, $a[2]$ becomes $a[0] + a[1] + a[2]$, and so on.

Return the **value** of $a[n - 1]$ after `k` seconds.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** n = 4, k = 5

- **Output:** 56

- **Explanation:** <table border="1">
	<tbody>
		<tr>
			<th>Second</th>
			<th>State After</th>
		</tr>
		<tr>
			<td>0</td>
			<td>[1,1,1,1]</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[1,2,3,4]</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[1,3,6,10]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[1,4,10,20]</td>
		</tr>
		<tr>
			<td>4</td>
			<td>[1,5,15,35]</td>
		</tr>
		<tr>
			<td>5</td>
			<td>[1,6,21,56]</td>
		</tr>
	</tbody>
</table>

#### Example 2

- **Input:** n = 5, k = 3

- **Output:** 35

- **Explanation:** <table border="1">
	<tbody>
		<tr>
			<th>Second</th>
			<th>State After</th>
		</tr>
		<tr>
			<td>0</td>
			<td>[1,1,1,1,1]</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[1,2,3,4,5]</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[1,3,6,10,15]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[1,4,10,20,35]</td>
		</tr>
	</tbody>
</table>

### 4. Constraints

- $1 \le n, k \le 1000$
