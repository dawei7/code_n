## Description

You are given two strings, `str1` and `str2`, of lengths `n` and `m`, respectively.

A string `word` of length `n + m - 1` is defined to be **generated** by `str1` and `str2` if it satisfies the following conditions for **each** index `0 <= i <= n - 1`:

<ul>
	<li>If `str1[i] == 'T'`, the **<span data-keyword="substring-nonempty">substring</span>** of `word` with size `m` starting at index `i` is **equal** to `str2`, i.e., `word[i..(i + m - 1)] == str2`.</li>
	<li>If `str1[i] == 'F'`, the **<span data-keyword="substring-nonempty">substring</span>** of `word` with size `m` starting at index `i` is **not equal** to `str2`, i.e., `word[i..(i + m - 1)] != str2`.</li>
</ul>

Return the **<span data-keyword="lexicographically-smaller-string">lexicographically smallest</span>** possible string that can be **generated** by `str1` and `str2`. If no string can be generated, return an empty string `""`.
