## Description

You are given a **0-indexed** array of **unique** strings `words`.

A **palindrome pair** is a pair of integers `(i, j)` such that:

<ul>
	<li>`0 <= i, j < words.length`,</li>
	<li>`i != j`, and</li>
	<li>`words[i] + words[j]` (the concatenation of the two strings) is a <span data-keyword="palindrome-string">palindrome</span>.</li>
</ul>

Return *an array of all the **palindrome pairs** of *`words`.

You must write an algorithm with `O(sum of words[i].length)` runtime complexity.
