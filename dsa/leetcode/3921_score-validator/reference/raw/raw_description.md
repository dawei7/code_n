## Description

You are given a string array `events`.

Initially, `score = 0` and `counter = 0`. Each element in `events` is one of the following:

	- `"0"`, `"1"`, `"2"`, `"3"`, `"4"`, `"6"`: Add that value to the total score.

	- `"W"`: Increase the counter by 1. No score is added.

	- `"WD"`: Add 1 to the total score.

	- `"NB"`: Add 1 to the total score.

Process the array from left to right. Stop processing when either:

	- All elements in `events` have been processed, or

	- The counter becomes 10.

Return an integer array `[score, counter]`, where:

	- `score` is the final total score.

	- `counter` is the final counter value.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">events = ["1","4","W","6","WD"]</span>

**Output:** <span class="example-io">[12,1]</span>

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>Event</th>
			<th>Score</th>
			<th>Counter</th>
		</tr>
		<tr>
			<td>`"1"`</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>`"4"`</td>
			<td>5</td>
			<td>0</td>
		</tr>
		<tr>
			<td>`"W"`</td>
			<td>5</td>
			<td>1</td>
		</tr>
		<tr>
			<td>`"6"`</td>
			<td>11</td>
			<td>1</td>
		</tr>
		<tr>
			<td>`"WD"`</td>
			<td>12</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

Final result: `[12, 1]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">events = ["WD","NB","0","4","4"]</span>

**Output:** <span class="example-io">[10,0]</span>

**Explanation:**

<table>
	<tbody>
		<tr>
			<th>Event</th>
			<th>Score</th>
			<th>Counter</th>
		</tr>
		<tr>
			<td>`"WD"`</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>`"NB"`</td>
			<td>2</td>
			<td>0</td>
		</tr>
		<tr>
			<td>`"0"`</td>
			<td>2</td>
			<td>0</td>
		</tr>
		<tr>
			<td>`"4"`</td>
			<td>6</td>
			<td>0</td>
		</tr>
		<tr>
			<td>`"4"`</td>
			<td>10</td>
			<td>0</td>
		</tr>
	</tbody>
</table>

Final result: `[10, 0]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">events = ["W","W","W","W","W","W","W","W","W","W","W"]</span>

**Output:** <span class="example-io">[0,10]</span>

**Explanation:**

After 10 occurrences of `"W"`, the counter reaches 10, so processing stops. The remaining events are ignored.

</div>

**Constraints:**

	- `1 <= events.length <= 1000`

	- `events[i]` is one of `"0"`, `"1"`, `"2"`, `"3"`, `"4"`, `"6"`, `"W"`, `"WD"`, or `"NB"`.
