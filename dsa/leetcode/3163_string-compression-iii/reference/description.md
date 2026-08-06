## Description

Given a string `word`, compress it using the following algorithm:

<ul>
	<li>Begin with an empty string `comp`. While `word` is **not** empty, use the following operation:

	<ul>
		<li>Remove a maximum length prefix of `word` made of a *single character* `c` repeating **at most** 9 times.</li>
		<li>Append the length of the prefix followed by `c` to `comp`.</li>
	</ul>
	</li>
</ul>

Return the string `comp`.
