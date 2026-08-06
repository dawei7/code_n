## Description

You are given a string `s` consisting of lowercase English letters.

You can perform the following operation any number of times (including zero):

<ul>
	<li>Remove **any** pair of **adjacent** characters in the string that are **consecutive** in the alphabet, in either order (e.g., `'a'` and `'b'`, or `'b'` and `'a'`).</li>
	<li>Shift the remaining characters to the left to fill the gap.</li>
</ul>

Return the **<span data-keyword="lexicographically-smaller-string">lexicographically smallest</span>** string that can be obtained after performing the operations optimally.

**Note:** Consider the alphabet as circular, thus `'a'` and `'z'` are consecutive.
