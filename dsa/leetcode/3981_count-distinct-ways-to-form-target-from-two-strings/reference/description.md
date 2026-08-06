## Description

You are given three strings `word1`, `word2`, and `target`.

Your task is to count the number of ways to form `target` by choosing characters from `word1` and `word2` under the following conditions:

<ul>
	<li>For each character of `target`, choose one matching character from either `word1` or `word2`.</li>
	<li>The chosen indices from `word1` must be **strictly** increasing.</li>
	<li>The chosen indices from `word2` must be **strictly** increasing.</li>
	<li>**At least** one character must be chosen from **both** `word1` and `word2`.</li>
</ul>

Two ways are considered different if, for **at least** one position in `target`, the chosen character comes from a different string or a different index.

Return the number of ways. Since the answer may be very large, return it **modulo** `10^9 + 7`.
