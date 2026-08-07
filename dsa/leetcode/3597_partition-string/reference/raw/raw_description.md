## Description

Given a string `s`, partition it into **unique segments** according to the following procedure:

	- Start building a segment beginning at index 0.

	- Continue extending the current segment character by character until the current segment has not been seen before.

	- Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index.

	- Repeat until you reach the end of `s`.

Return an array of strings `segments`, where `segments[i]` is the `i^th` segment created.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abbccccd"</span>

**Output:** <span class="example-io">["a","b","bc","c","cc","d"]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Index</th>
			<th style="border: 1px solid black;">Segment After Adding</th>
			<th style="border: 1px solid black;">Seen Segments</th>
			<th style="border: 1px solid black;">Current Segment Seen Before?</th>
			<th style="border: 1px solid black;">New Segment</th>
			<th style="border: 1px solid black;">Updated Seen Segments</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">"a"</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">""</td>
			<td style="border: 1px solid black;">["a"]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">"b"</td>
			<td style="border: 1px solid black;">["a"]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">""</td>
			<td style="border: 1px solid black;">["a", "b"]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">"b"</td>
			<td style="border: 1px solid black;">["a", "b"]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">"b"</td>
			<td style="border: 1px solid black;">["a", "b"]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">"bc"</td>
			<td style="border: 1px solid black;">["a", "b"]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">""</td>
			<td style="border: 1px solid black;">["a", "b", "bc"]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">"c"</td>
			<td style="border: 1px solid black;">["a", "b", "bc"]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">""</td>
			<td style="border: 1px solid black;">["a", "b", "bc", "c"]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">"c"</td>
			<td style="border: 1px solid black;">["a", "b", "bc", "c"]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">"c"</td>
			<td style="border: 1px solid black;">["a", "b", "bc", "c"]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">"cc"</td>
			<td style="border: 1px solid black;">["a", "b", "bc", "c"]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">""</td>
			<td style="border: 1px solid black;">["a", "b", "bc", "c", "cc"]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">"d"</td>
			<td style="border: 1px solid black;">["a", "b", "bc", "c", "cc"]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">""</td>
			<td style="border: 1px solid black;">["a", "b", "bc", "c", "cc", "d"]</td>
		</tr>
	</tbody>
</table>

Hence, the final output is `["a", "b", "bc", "c", "cc", "d"]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "aaaa"</span>

**Output:** <span class="example-io">["a","aa"]</span>

**Explanation:**

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Index</th>
			<th style="border: 1px solid black;">Segment After Adding</th>
			<th style="border: 1px solid black;">Seen Segments</th>
			<th style="border: 1px solid black;">Current Segment Seen Before?</th>
			<th style="border: 1px solid black;">New Segment</th>
			<th style="border: 1px solid black;">Updated Seen Segments</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">"a"</td>
			<td style="border: 1px solid black;">[]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">""</td>
			<td style="border: 1px solid black;">["a"]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">"a"</td>
			<td style="border: 1px solid black;">["a"]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">"a"</td>
			<td style="border: 1px solid black;">["a"]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">"aa"</td>
			<td style="border: 1px solid black;">["a"]</td>
			<td style="border: 1px solid black;">No</td>
			<td style="border: 1px solid black;">""</td>
			<td style="border: 1px solid black;">["a", "aa"]</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">"a"</td>
			<td style="border: 1px solid black;">["a", "aa"]</td>
			<td style="border: 1px solid black;">Yes</td>
			<td style="border: 1px solid black;">"a"</td>
			<td style="border: 1px solid black;">["a", "aa"]</td>
		</tr>
	</tbody>
</table>

Hence, the final output is `["a", "aa"]`.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` contains only lowercase English letters.
