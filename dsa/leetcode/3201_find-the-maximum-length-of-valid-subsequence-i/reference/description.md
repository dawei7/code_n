## Description

You are given an integer array `nums`.
A <span data-keyword="subsequence-array">subsequence</span> `sub` of `nums` with length `x` is called **valid** if it satisfies:

<ul>
	<li>`(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.`</li>
</ul>

Return the length of the **longest** **valid** subsequence of `nums`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
