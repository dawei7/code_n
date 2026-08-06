## Description

You are given an integer `k` and an integer `x`. The price of a number `num` is calculated by the count of <span data-keyword="set-bit">set bits</span> at positions `x`, `2x`, `3x`, etc., in its binary representation, starting from the least significant bit. The following table contains examples of how price is calculated.

<table border="1">
	<tbody>
		<tr>
			<th>x</th>
			<th>num</th>
			<th>Binary Representation</th>
			<th>Price</th>
		</tr>
		<tr>
			<td>1</td>
			<td>13</td>
			<td><u>0</u><u>0</u><u>0</u><u>0</u><u>0</u>**<u>1</u>****<u>1</u>**<u>0</u>**<u>1</u>**</td>
			<td>3</td>
		</tr>
		<tr>
			<td>2</td>
			<td>13</td>
			<td>0<u>0</u>0<u>0</u>0**<u>1</u>**1<u>0</u>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>233</td>
			<td>0**<u>1</u>**1**<u>1</u>**0**<u>1</u>**0<u>0</u>1</td>
			<td>3</td>
		</tr>
		<tr>
			<td>3</td>
			<td>13</td>
			<td><u>0</u>00<u>0</u>01**<u>1</u>**01</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>362</td>
			<td>**<u>1</u>**01**<u>1</u>**01<u>0</u>10</td>
			<td>2</td>
		</tr>
	</tbody>
</table>

The **accumulated price** of `num` is the **total** price of numbers from `1` to `num`. `num` is considered **cheap** if its accumulated price is less than or equal to `k`.

Return the **greatest** cheap number.
