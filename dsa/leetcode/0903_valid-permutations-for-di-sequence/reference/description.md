## Description

You are given a string `s` of length `n` where `s[i]` is either:

<ul>
	<li>`'D'` means decreasing, or</li>
	<li>`'I'` means increasing.</li>
</ul>

A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` is called a **valid permutation** if for all valid `i`:

<ul>
	<li>If `s[i] == 'D'`, then `perm[i] > perm[i + 1]`, and</li>
	<li>If `s[i] == 'I'`, then `perm[i] < perm[i + 1]`.</li>
</ul>

Return *the number of **valid permutations** *`perm`. Since the answer may be large, return it **modulo** `10^9 + 7`.
