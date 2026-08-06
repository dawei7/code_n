## Description

You are given two strings `word1` and `word2`.

A string `x` is called **almost equal** to `y` if you can change **at most** one character in `x` to make it *identical* to `y`.

A sequence of indices `seq` is called **valid** if:

<ul>
	<li>The indices are sorted in **ascending** order.</li>
	<li>*Concatenating* the characters at these indices in `word1` in **the same** order results in a string that is **almost equal** to `word2`.</li>
</ul>

Return an array of size `word2.length` representing the <span data-keyword="lexicographically-smaller-array">lexicographically smallest</span> **valid** sequence of indices. If no such sequence of indices exists, return an **empty** array.

**Note** that the answer must represent the *lexicographically smallest array*, **not** the corresponding string formed by those indices.<!-- notionvc: 2ff8e782-bd6f-4813-a421-ec25f7e84c1e -->
