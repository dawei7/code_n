### 1. Description

You are given two **positive** integers `n` and `k`. There are `n` children numbered from `0` to $n - 1$ standing in a queue *in order* from left to right.

Initially, child 0 holds a ball and the direction of passing the ball is towards the right direction. After each second, the child holding the ball passes it to the child next to them. Once the ball reaches **either** end of the line, i.e. child 0 or child $n - 1$, the direction of passing is **reversed**.

Return the number of the child who receives the ball after `k` seconds.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** n = 3, k = 5

- **Output:** 1

- **Explanation:** <table>
	<tbody>
		<tr>
			<th>Time elapsed</th>
			<th>Children</th>
		</tr>
		<tr>
			<td>`0`</td>
			<td>`[<u>0</u>, 1, 2]`</td>
		</tr>
		<tr>
			<td>`1`</td>
			<td>`[0, <u>1</u>, 2]`</td>
		</tr>
		<tr>
			<td>`2`</td>
			<td>`[0, 1, <u>2</u>]`</td>
		</tr>
		<tr>
			<td>`3`</td>
			<td>`[0, <u>1</u>, 2]`</td>
		</tr>
		<tr>
			<td>`4`</td>
			<td>`[<u>0</u>, 1, 2]`</td>
		</tr>
		<tr>
			<td>`5`</td>
			<td>`[0, <u>1</u>, 2]`</td>
		</tr>
	</tbody>
</table>

#### Example 2

- **Input:** n = 5, k = 6

- **Output:** 2

- **Explanation:** <table>
	<tbody>
		<tr>
			<th>Time elapsed</th>
			<th>Children</th>
		</tr>
		<tr>
			<td>`0`</td>
			<td>`[<u>0</u>, 1, 2, 3, 4]`</td>
		</tr>
		<tr>
			<td>`1`</td>
			<td>`[0, <u>1</u>, 2, 3, 4]`</td>
		</tr>
		<tr>
			<td>`2`</td>
			<td>`[0, 1, <u>2</u>, 3, 4]`</td>
		</tr>
		<tr>
			<td>`3`</td>
			<td>`[0, 1, 2, <u>3</u>, 4]`</td>
		</tr>
		<tr>
			<td>`4`</td>
			<td>`[0, 1, 2, 3, <u>4</u>]`</td>
		</tr>
		<tr>
			<td>`5`</td>
			<td>`[0, 1, 2, <u>3</u>, 4]`</td>
		</tr>
		<tr>
			<td>`6`</td>
			<td>`[0, 1, <u>2</u>, 3, 4]`</td>
		</tr>
	</tbody>
</table>

#### Example 3

- **Input:** n = 4, k = 2

- **Output:** 2

- **Explanation:** <table>
	<tbody>
		<tr>
			<th>Time elapsed</th>
			<th>Children</th>
		</tr>
		<tr>
			<td>`0`</td>
			<td>`[<u>0</u>, 1, 2, 3]`</td>
		</tr>
		<tr>
			<td>`1`</td>
			<td>`[0, <u>1</u>, 2, 3]`</td>
		</tr>
		<tr>
			<td>`2`</td>
			<td>`[0, 1, <u>2</u>, 3]`</td>
		</tr>
	</tbody>
</table>

### 4. Constraints

- $2 \le n \le 50$

- $1 \le k \le 50$

### 5. Note

This question is the same as <a href="https://leetcode.com/problems/pass-the-pillow/description/" target="_blank"> 2582: Pass the Pillow.</a>
