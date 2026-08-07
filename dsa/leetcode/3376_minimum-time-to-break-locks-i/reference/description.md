### 1. Description

Bob is stuck in a dungeon and must break `n` locks, each requiring some amount of **energy** to break. The required energy for each lock is stored in an array called `strength` where $\text{strength}[i]$ indicates the energy needed to break the $$i^{\text{th}}$$ lock.

To break a lock, Bob uses a sword with the following characteristics:

- The initial energy of the sword is 0.

- The initial factor `x` by which the energy of the sword increases is 1.

- Every minute, the energy of the sword increases by the current factor `x`.

- To break the $$i^{\text{th}}$$ lock, the energy of the sword must reach **at least** $\text{strength}[i]$.

- After breaking a lock, the energy of the sword resets to 0, and the factor `x` increases by a given value `k`.

Your task is to determine the **minimum** time in minutes required for Bob to break all `n` locks and escape the dungeon.

Return the **minimum **time required for Bob to break all `n` locks.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** strength = [3,4,1], k = 1

**Output:** 4

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Time</th>
			<th style="border: 1px solid black;">Energy</th>
			<th style="border: 1px solid black;">x</th>
			<th style="border: 1px solid black;">Action</th>
			<th style="border: 1px solid black;">Updated x</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Nothing</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Break 3^rd Lock</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">Nothing</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">Break 2^nd Lock</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">Break 1^st Lock</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
	</tbody>
</table>

The locks cannot be broken in less than 4 minutes; thus, the answer is 4.

</div>
#### Example 2

<div class="example-block">
**Input:** strength = [2,5,4], k = 2

**Output:** 5

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Time</th>
			<th style="border: 1px solid black;">Energy</th>
			<th style="border: 1px solid black;">x</th>
			<th style="border: 1px solid black;">Action</th>
			<th style="border: 1px solid black;">Updated x</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Nothing</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Nothing</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Break 1^st Lock</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">Nothing</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">Break 2^n^d Lock</td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">Break 3^r^d Lock</td>
			<td style="border: 1px solid black;">7</td>
		</tr>
	</tbody>
</table>

The locks cannot be broken in less than 5 minutes; thus, the answer is 5.

</div>

### 4. Constraints

- $n = \text{strength.length}$

- $1 \le n \le 8$

- $1 \le k \le 10$

- $1 \le \text{strength}[i] \le 10^{6}$