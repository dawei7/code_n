## Description

Given a string `s`, partition it into **unique segments** according to the following procedure:

<ul>
	<li>Start building a segment beginning at index 0.</li>
	<li>Continue extending the current segment character by character until the current segment has not been seen before.</li>
	<li>Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index.</li>
	<li>Repeat until you reach the end of `s`.</li>
</ul>

Return an array of strings `segments`, where `segments[i]` is the `i^th` segment created.
