## Description

You are given two strings, `word1` and `word2`. You want to construct a string in the following manner:

<ul>
	<li>Choose some **non-empty** subsequence `subsequence1` from `word1`.</li>
	<li>Choose some **non-empty** subsequence `subsequence2` from `word2`.</li>
	<li>Concatenate the subsequences: `subsequence1 + subsequence2`, to make the string.</li>
</ul>

Return *the **length** of the longest **palindrome** that can be constructed in the described manner. *If no palindromes can be constructed, return `0`.

A **subsequence** of a string `s` is a string that can be made by deleting some (possibly none) characters from `s` without changing the order of the remaining characters.

A **palindrome** is a string that reads the same forward as well as backward.
