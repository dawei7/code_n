## Description

Given a string `s` consisting only of characters `'a'`, `'b'`, and `'c'`. You are asked to apply the following algorithm on the string any number of times:

<ol>
	<li>Pick a **non-empty** prefix from the string `s` where all the characters in the prefix are equal.</li>
	<li>Pick a **non-empty** suffix from the string `s` where all the characters in this suffix are equal.</li>
	<li>The prefix and the suffix should not intersect at any index.</li>
	<li>The characters from the prefix and suffix must be the same.</li>
	<li>Delete both the prefix and the suffix.</li>
</ol>

Return *the **minimum length** of *`s` *after performing the above operation any number of times (possibly zero times)*.
