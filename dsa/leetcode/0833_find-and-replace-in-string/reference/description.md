## Description

You are given a **0-indexed** string `s` that you must perform `k` replacement operations on. The replacement operations are given as three **0-indexed** parallel arrays, `indices`, `sources`, and `targets`, all of length `k`.

To complete the `i^th` replacement operation:

<ol>
	<li>Check if the **substring** `sources[i]` occurs at index `indices[i]` in the **original string** `s`.</li>
	<li>If it does not occur, **do nothing**.</li>
	<li>Otherwise if it does occur, **replace** that substring with `targets[i]`.</li>
</ol>

For example, if `s = "<u>ab</u>cd"`, `indices[i] = 0`, `sources[i] = "ab"`, and `targets[i] = "eee"`, then the result of this replacement will be `"<u>eee</u>cd"`.

All replacement operations must occur **simultaneously**, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will **not overlap**.

<ul>
	<li>For example, a testcase with `s = "abc"`, `indices = [0, 1]`, and `sources = ["ab","bc"]` will not be generated because the `"ab"` and `"bc"` replacements overlap.</li>
</ul>

Return *the **resulting string** after performing all replacement operations on *`s`.

A **substring** is a contiguous sequence of characters in a string.
