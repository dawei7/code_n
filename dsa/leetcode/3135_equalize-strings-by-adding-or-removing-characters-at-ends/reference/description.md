## Description

Given two strings `initial` and `target`, your task is to modify `initial` by performing a series of operations to make it equal to `target`.

In one operation, you can add or remove **one character** only at the *beginning* or the *end* of the string `initial`.

Return the **minimum** number of operations required to *transform* `initial` into `target`.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

<div class="example-block">
**Input:** initial = "abcde", target = "cdef"

**Output:** 3

**Explanation:**

Remove `'a'` and `'b'` from the beginning of `initial`, then add `'f'` to the end.

</div>
#### Example 2

<div class="example-block">
**Input:** initial = "axxy", target = "yabx"

**Output:** 6

**Explanation:**

<table border="1">
	<tbody>
		<tr>
			<th>Operation</th>
			<th>Resulting String</th>
		</tr>
		<tr>
			<td>Add `'y'` to the beginning</td>
			<td>`"yaxxy"`</td>
		</tr>
		<tr>
			<td>Remove from end</td>
			<td>`"yaxx"`</td>
		</tr>
		<tr>
			<td>Remove from end</td>
			<td>`"yax"`</td>
		</tr>
		<tr>
			<td>Remove from end</td>
			<td>`"ya"`</td>
		</tr>
		<tr>
			<td>Add `'b'` to the end</td>
			<td>`"yab"`</td>
		</tr>
		<tr>
			<td>Add `'x'` to the end</td>
			<td>`"yabx"`</td>
		</tr>
	</tbody>
</table>
</div>
#### Example 3

<div class="example-block">
**Input:** initial = "xyz", target = "xyz"

**Output:** 0

**Explanation:**

No operations are needed as the strings are already equal.

</div>
### Constraints

- $1 \le \text{initial.length}, \text{target.length} \le 1000$

- `initial` and `target` consist only of lowercase English letters.