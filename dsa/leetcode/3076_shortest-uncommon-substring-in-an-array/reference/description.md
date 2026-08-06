## Description

You are given an array `arr` of size `n` consisting of **non-empty** strings.

Find a string array `answer` of size `n` such that:

<ul>
	<li>`answer[i]` is the **shortest** <span data-keyword="substring">substring</span> of `arr[i]` that does **not** occur as a substring in any other string in `arr`. If multiple such substrings exist, `answer[i]` should be the <span data-keyword="lexicographically-smaller-string">lexicographically smallest</span>. And if no such substring exists, `answer[i]` should be an empty string.</li>
</ul>

Return *the array *`answer`.
