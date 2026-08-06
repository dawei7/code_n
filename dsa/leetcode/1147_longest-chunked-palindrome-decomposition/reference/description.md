## Description

You are given a string `text`. You should split it to k substrings `(subtext_1, subtext_2, ..., subtext_k)` such that:

<ul>
	<li>`subtext_i` is a **non-empty** string.</li>
	<li>The concatenation of all the substrings is equal to `text` (i.e., `subtext_1 + subtext_2 + ... + subtext_k == text`).</li>
	<li>`subtext_i == subtext_k - i + 1` for all valid values of `i` (i.e., `1 <= i <= k`).</li>
</ul>

Return the largest possible value of `k`.
