## Description

A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` can be represented as a string `s` of length `n` where:

<ul>
	<li>`s[i] == 'I'` if `perm[i] < perm[i + 1]`, and</li>
	<li>`s[i] == 'D'` if `perm[i] > perm[i + 1]`.</li>
</ul>

Given a string `s`, reconstruct the permutation `perm` and return it. If there are multiple valid permutations perm, return **any of them**.
