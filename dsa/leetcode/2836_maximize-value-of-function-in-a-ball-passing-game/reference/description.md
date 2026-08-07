### 1. Description

You are given an integer array `receiver` of length `n` and an integer `k`. `n` players are playing a ball-passing game.

You choose the starting player, `i`. The game proceeds as follows: player `i` passes the ball to player $\text{receiver}[i]$, who then passes it to $receiver[\text{receiver}[i]]$, and so on, for `k` passes in total. The game's score is the sum of the indices of the players who touched the ball, including repetitions, i.e. $i + \text{receiver}[i] + receiver[\text{receiver}[i]] + ... + receiver^(k)[i]$.

Return the **maximum** possible score.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

- `receiver` may contain duplicates.

- $\text{receiver}[i]$ may be equal to `i`.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** receiver = [2,0,1], k = 4

**Output:** 6

**Explanation:**

Starting with player $i = 2$ the initial score is 2:

<table>
	<tbody>
		<tr>
			<th>Pass</th>
			<th>Sender Index</th>
			<th>Receiver Index</th>
			<th>Score</th>
		</tr>
		<tr>
			<td>1</td>
			<td>2</td>
			<td>1</td>
			<td>3</td>
		</tr>
		<tr>
			<td>2</td>
			<td>1</td>
			<td>0</td>
			<td>3</td>
		</tr>
		<tr>
			<td>3</td>
			<td>0</td>
			<td>2</td>
			<td>5</td>
		</tr>
		<tr>
			<td>4</td>
			<td>2</td>
			<td>1</td>
			<td>6</td>
		</tr>
	</tbody>
</table>
</div>
#### Example 2

<div class="example-block">
**Input:** receiver = [1,1,1,2,3], k = 3

**Output:** 10

**Explanation:**

Starting with player $i = 4$ the initial score is 4:

<table>
	<tbody>
		<tr>
			<th>Pass</th>
			<th>Sender Index</th>
			<th>Receiver Index</th>
			<th>Score</th>
		</tr>
		<tr>
			<td>1</td>
			<td>4</td>
			<td>3</td>
			<td>7</td>
		</tr>
		<tr>
			<td>2</td>
			<td>3</td>
			<td>2</td>
			<td>9</td>
		</tr>
		<tr>
			<td>3</td>
			<td>2</td>
			<td>1</td>
			<td>10</td>
		</tr>
	</tbody>
</table>
</div>

### 5. Constraints

- $1 \le \text{receiver.length} = n \le 10^{5}$

- $0 \le \text{receiver}[i] \le n - 1$

- $1 \le k \le 10^{10}$