## Description

You are given a list of strings of the **same length** `words` and a string `target`.

Your task is to form `target` using the given `words` under the following rules:

<ul>
	<li>`target` should be formed from left to right.</li>
	<li>To form the `i^th` character (**0-indexed**) of `target`, you can choose the `k^th` character of the `j^th` string in `words` if `target[i] = words[j][k]`.</li>
	<li>Once you use the `k^th` character of the `j^th` string of `words`, you **can no longer** use the `x^th` character of any string in `words` where `x <= k`. In other words, all characters to the left of or at index `k` become unusuable for every string.</li>
	<li>Repeat the process until you form the string `target`.</li>
</ul>

**Notice** that you can use **multiple characters** from the **same string** in `words` provided the conditions above are met.

Return *the number of ways to form `target` from `words`*. Since the answer may be too large, return it **modulo** `10^9 + 7`.
