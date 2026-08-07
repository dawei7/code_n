## Description

You are given a straight road of length `l` km, an integer `n`, an integer `k`**, **and **two** integer arrays, `position` and `time`, each of length `n`.

The array `position` lists the positions (in km) of signs in **strictly** increasing order (with `position[0] = 0` and `position[n - 1] = l`).

Each `time[i]` represents the time (in minutes) required to travel 1 km between `position[i]` and `position[i + 1]`.

You **must** perform **exactly** `k` merge operations. In one merge, you can choose any **two** adjacent signs at indices `i` and `i + 1` (with `i > 0` and `i + 1 < n`) and:

	- Update the sign at index `i + 1` so that its time becomes `time[i] + time[i + 1]`.

	- Remove the sign at index `i`.

Return the **minimum** **total** **travel time** (in minutes) to travel from 0 to `l` after **exactly** `k` merges.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">l = 10, n = 4, k = 1, position = [0,3,8,10], time = [5,8,3,6]</span>

**Output:** <span class="example-io">62</span>

**Explanation:**

	- Merge the signs at indices 1 and 2. Remove the sign at index 1, and change the time at index 2 to `8 + 3 = 11`.

	- After the merge:

		<li data-end="214" data-start="145">`position` array: `[0, 8, 10]`

		- `time` array: `[5, 11, 6]`

		-

	</li>
	- <table data-end="386" data-start="231" style="border: 1px solid black;">
		<thead data-end="269" data-start="231">
			<tr data-end="269" data-start="231">
				<th data-end="241" data-start="231" style="border: 1px solid black;">Segment</th>
				<th data-end="252" data-start="241" style="border: 1px solid black;">Distance (km)</th>
				<th data-end="260" data-start="252" style="border: 1px solid black;">Time per km (min)</th>
				<th data-end="269" data-start="260" style="border: 1px solid black;">Segment Travel Time (min)</th>
			</tr>
		</thead>
		<tbody data-end="386" data-start="309">
			<tr data-end="347" data-start="309">
				<td style="border: 1px solid black;">0 → 8</td>
				<td style="border: 1px solid black;">8</td>
				<td style="border: 1px solid black;">5</td>
				<td style="border: 1px solid black;">8 × 5 = 40</td>
			</tr>
			<tr data-end="386" data-start="348">
				<td style="border: 1px solid black;">8 → 10</td>
				<td style="border: 1px solid black;">2</td>
				<td style="border: 1px solid black;">11</td>
				<td style="border: 1px solid black;">2 × 11 = 22</td>
			</tr>
		</tbody>
	</table>

	- Total Travel Time: `40 + 22 = 62`, which is the minimum possible time after exactly 1 merge.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">l = 5, n = 5, k = 1, position = [0,1,2,3,5], time = [8,3,9,3,3]</span>

**Output:** <span class="example-io">34</span>

**Explanation:**

	- Merge the signs at indices 1 and 2. Remove the sign at index 1, and change the time at index 2 to `3 + 9 = 12`.

	- After the merge:

		<li data-end="755" data-start="568">`position` array: `[0, 2, 3, 5]`

		- `time` array: `[8, 12, 3, 3]`

		-

	</li>
	- <table data-end="966" data-start="772" style="border: 1px solid black;">
		<thead data-end="810" data-start="772">
			<tr data-end="810" data-start="772">
				<th data-end="782" data-start="772" style="border: 1px solid black;">Segment</th>
				<th data-end="793" data-start="782" style="border: 1px solid black;">Distance (km)</th>
				<th data-end="801" data-start="793" style="border: 1px solid black;">Time per km (min)</th>
				<th data-end="810" data-start="801" style="border: 1px solid black;">Segment Travel Time (min)</th>
			</tr>
		</thead>
		<tbody data-end="966" data-start="850">
			<tr data-end="888" data-start="850">
				<td style="border: 1px solid black;">0 → 2</td>
				<td style="border: 1px solid black;">2</td>
				<td style="border: 1px solid black;">8</td>
				<td style="border: 1px solid black;">2 × 8 = 16</td>
			</tr>
			<tr data-end="927" data-start="889">
				<td style="border: 1px solid black;">2 → 3</td>
				<td style="border: 1px solid black;">1</td>
				<td style="border: 1px solid black;">12</td>
				<td style="border: 1px solid black;">1 × 12 = 12</td>
			</tr>
			<tr data-end="966" data-start="928">
				<td style="border: 1px solid black;">3 → 5</td>
				<td style="border: 1px solid black;">2</td>
				<td style="border: 1px solid black;">3</td>
				<td style="border: 1px solid black;">2 × 3 = 6</td>
			</tr>
		</tbody>
	</table>

	- Total Travel Time: `16 + 12 + 6 = 34`**, **which is the minimum possible time after exactly 1 merge.

</div>

**Constraints:**

	- `1 <= l <= 10^5`

	- `2 <= n <= min(l + 1, 50)`

	- `0 <= k <= min(n - 2, 10)`

	- `position.length == n`

	- `position[0] = 0` and `position[n - 1] = l`

	- `position` is sorted in strictly increasing order.

	- `time.length == n`

	- `1 <= time[i] <= 100​`

	- `1 <= sum(time) <= 100`​​​​​​
