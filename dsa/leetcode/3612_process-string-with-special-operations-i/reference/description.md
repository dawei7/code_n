## Description

You are given a string `s` consisting of lowercase English letters and the special characters: `*`, `#`, and `%`.

Build a new string `result` by processing `s` according to the following rules from left to right:

<ul>
	<li>If the letter is a **lowercase** English letter append it to `result`.</li>
	<li>A `'*'` **removes** the last character from `result`, if it exists.</li>
	<li>A `'#'` **duplicates** the current `result` and **appends** it to itself.</li>
	<li>A `'%'` **reverses** the current `result`.</li>
</ul>

Return the final string `result` after processing all characters in `s`.
