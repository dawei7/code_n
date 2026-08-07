## Description

You are given an integer array `receiver` of length `n` and an integer `k`. `n` players are playing a ball-passing game.

You choose the starting player, `i`. The game proceeds as follows: player `i` passes the ball to player `receiver[i]`, who then passes it to `receiver[receiver[i]]`, and so on, for `k` passes in total. The game's score is the sum of the indices of the players who touched the ball, including repetitions, i.e. `i + receiver[i] + receiver[receiver[i]] + ... + receiver^(k)[i]`.

Return the **maximum** possible score.

**Notes:**

	- `receiver` may contain duplicates.

	- `receiver[i]` may be equal to `i`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">receiver = [2,0,1], k = 4</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

Starting with player `i = 2` the initial score is 2:

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

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">receiver = [1,1,1,2,3], k = 3</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

Starting with player `i = 4` the initial score is 4:

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

**Constraints:**

	- `1 <= receiver.length == n <= 10^5`

	- `0 <= receiver[i] <= n - 1`

	- `1 <= k <= 10^10`
