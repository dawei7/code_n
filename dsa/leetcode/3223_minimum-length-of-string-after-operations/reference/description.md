## Description

You are given a string `s`.

You can perform the following process on `s` **any** number of times:

<ul>
	<li>Choose an index `i` in the string such that there is **at least** one character to the left of index `i` that is equal to `s[i]`, and **at least** one character to the right that is also equal to `s[i]`.</li>
	<li>Delete the **closest** occurrence of `s[i]` located to the **left** of `i`.</li>
	<li>Delete the **closest** occurrence of `s[i]` located to the **right** of `i`.</li>
</ul>

Return the **minimum** length of the final string `s` that you can achieve.
