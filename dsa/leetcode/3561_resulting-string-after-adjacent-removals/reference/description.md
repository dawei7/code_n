## Description

You are given a string `s` consisting of lowercase English letters.

You **must** repeatedly perform the following operation while the string `s` has **at least** two **consecutive **characters:

<ul>
	<li>Remove the **leftmost** pair of **adjacent** characters in the string that are **consecutive** in the alphabet, in either order (e.g., `'a'` and `'b'`, or `'b'` and `'a'`).</li>
	<li>Shift the remaining characters to the left to fill the gap.</li>
</ul>

Return the resulting string after no more operations can be performed.

**Note:** Consider the alphabet as circular, thus `'a'` and `'z'` are consecutive.
