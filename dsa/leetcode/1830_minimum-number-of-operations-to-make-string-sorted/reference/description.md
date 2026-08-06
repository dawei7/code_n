## Description

You are given a string `s` (**0-indexed**)​​​​​​. You are asked to perform the following operation on `s`​​​​​​ until you get a sorted string:

<ol>
	<li>Find **the largest index** `i` such that `1 <= i < s.length` and `s[i] < s[i - 1]`.</li>
	<li>Find **the largest index** `j` such that `i <= j < s.length` and `s[k] < s[i - 1]` for all the possible values of `k` in the range `[i, j]` inclusive.</li>
	<li>Swap the two characters at indices `i - 1`​​​​ and `j`​​​​​.</li>
	<li>Reverse the suffix starting at index `i`​​​​​​.</li>
</ol>

Return *the number of operations needed to make the string sorted.* Since the answer can be too large, return it **modulo** `10^9 + 7`.
