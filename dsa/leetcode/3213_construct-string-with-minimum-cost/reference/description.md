## Description

You are given a string `target`, an array of strings `words`, and an integer array `costs`, both arrays of the same length.

Imagine an empty string `s`.

You can perform the following operation any number of times (including **zero**):

<ul>
	<li>Choose an index `i` in the range `[0, words.length - 1]`.</li>
	<li>Append `words[i]` to `s`.</li>
	<li>The cost of operation is `costs[i]`.</li>
</ul>

Return the **minimum** cost to make `s` equal to `target`. If it's not possible, return `-1`.
