## Description

You are given two strings of the same length `s1` and `s2` and a string `baseStr`.

We say `s1[i]` and `s2[i]` are equivalent characters.

<ul>
	<li>For example, if `s1 = "abc"` and `s2 = "cde"`, then we have `'a' == 'c'`, `'b' == 'd'`, and `'c' == 'e'`.</li>
</ul>

Equivalent characters follow the usual rules of any equivalence relation:

<ul>
	<li>**Reflexivity:** `'a' == 'a'`.</li>
	<li>**Symmetry:** `'a' == 'b'` implies `'b' == 'a'`.</li>
	<li>**Transitivity:** `'a' == 'b'` and `'b' == 'c'` implies `'a' == 'c'`.</li>
</ul>

For example, given the equivalency information from `s1 = "abc"` and `s2 = "cde"`, `"acd"` and `"aab"` are equivalent strings of `baseStr = "eed"`, and `"aab"` is the lexicographically smallest equivalent string of `baseStr`.

Return *the lexicographically smallest equivalent string of *`baseStr`* by using the equivalency information from *`s1`* and *`s2`.
