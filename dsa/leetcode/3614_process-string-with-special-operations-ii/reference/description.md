## Description

You are given a string `s` consisting of lowercase English letters and the special characters: `'*'`, `'#'`, and `'%'`.

You are also given an integer `k`.

Build a new string `result` by processing `s` according to the following rules from left to right:

<ul>
	<li>If the letter is a **lowercase** English letter append it to `result`.</li>
	<li>A `'*'` **removes** the last character from `result`, if it exists.</li>
	<li>A `'#'` **duplicates** the current `result` and **appends** it to itself.</li>
	<li>A `'%'` **reverses** the current `result`.</li>
</ul>

Return the `k^th` character of the final string `result`. If `k` is out of the bounds of `result`, return `'.'`.
