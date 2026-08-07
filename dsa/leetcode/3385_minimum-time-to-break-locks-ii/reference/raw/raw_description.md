## Description

Bob is stuck in a dungeon and must break `n` locks, each requiring some amount of **energy** to break. The required energy for each lock is stored in an array called `strength` where `strength[i]` indicates the energy needed to break the `i^th` lock.

To break a lock, Bob uses a sword with the following characteristics:

	- The initial energy of the sword is 0.

	- The initial factor `<font face="monospace">X</font>` by which the energy of the sword increases is 1.

	- Every minute, the energy of the sword increases by the current factor `X`.

	- To break the `i^th` lock, the energy of the sword must reach at least `strength[i]`.

	- After breaking a lock, the energy of the sword resets to 0, and the factor `X` increases by 1.

Your task is to determine the **minimum** time in minutes required for Bob to break all `n` locks and escape the dungeon.

Return the **minimum **time required for Bob to break all `n` locks.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">strength = [3,4,1]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>Time</th>
			<th>Energy</th>
			<th>X</th>
			<th>Action</th>
			<th>Updated X</th>
		</tr>
		<tr>
			<td>0</td>
			<td>0</td>
			<td>1</td>
			<td>Nothing</td>
			<td>1</td>
		</tr>
		<tr>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>Break 3^rd Lock</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>2</td>
			<td>2</td>
			<td>Nothing</td>
			<td>2</td>
		</tr>
		<tr>
			<td>3</td>
			<td>4</td>
			<td>2</td>
			<td>Break 2^nd Lock</td>
			<td>3</td>
		</tr>
		<tr>
			<td>4</td>
			<td>3</td>
			<td>3</td>
			<td>Break 1^st Lock</td>
			<td>3</td>
		</tr>
	</tbody>
</table>

The locks cannot be broken in less than 4 minutes; thus, the answer is 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">strength = [2,5,4]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>Time</th>
			<th>Energy</th>
			<th>X</th>
			<th>Action</th>
			<th>Updated X</th>
		</tr>
		<tr>
			<td>0</td>
			<td>0</td>
			<td>1</td>
			<td>Nothing</td>
			<td>1</td>
		</tr>
		<tr>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>Nothing</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>2</td>
			<td>1</td>
			<td>Break 1^st Lock</td>
			<td>2</td>
		</tr>
		<tr>
			<td>3</td>
			<td>2</td>
			<td>2</td>
			<td>Nothing</td>
			<td>2</td>
		</tr>
		<tr>
			<td>4</td>
			<td>4</td>
			<td>2</td>
			<td>Break 3^rd Lock</td>
			<td>3</td>
		</tr>
		<tr>
			<td>5</td>
			<td>3</td>
			<td>3</td>
			<td>Nothing</td>
			<td>3</td>
		</tr>
		<tr>
			<td>6</td>
			<td>6</td>
			<td>3</td>
			<td>Break 2^nd Lock</td>
			<td>4</td>
		</tr>
	</tbody>
</table>

The locks cannot be broken in less than 6 minutes; thus, the answer is 6.

</div>

**Constraints:**

	- `n == strength.length`

	- `1 <= n <= 80`

	- `1 <= strength[i] <= 10^6`
