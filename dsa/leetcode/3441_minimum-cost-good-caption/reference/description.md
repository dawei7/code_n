## Description

You are given a string `caption` of length `n`. A **good** caption is a string where **every** character appears in groups of **at least 3** consecutive occurrences.

For example:

<ul>
	<li>`"aaabbb"` and `"aaaaccc"` are **good** captions.</li>
	<li>`"aabbb"` and `"ccccd"` are **not** good captions.</li>
</ul>

You can perform the following operation **any** number of times:

Choose an index `i` (where `0 <= i < n`) and change the character at that index to either:

<ul>
	<li>The character immediately **before** it in the alphabet (if `caption[i] != 'a'`).</li>
	<li>The character immediately **after** it in the alphabet (if `caption[i] != 'z'`).</li>
</ul>

Your task is to convert the given `caption` into a **good** caption using the **minimum** number of operations, and return it. If there are **multiple** possible good captions, return the **<span data-keyword="lexicographically-smaller-string">lexicographically smallest</span>** one among them. If it is **impossible** to create a good caption, return an empty string `""`.
