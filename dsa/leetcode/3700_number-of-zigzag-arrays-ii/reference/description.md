## Description

You are given three integers `n`, `l`, and `r`.

A **ZigZag** array of length `n` is defined as follows:

<ul>
	<li>Each element lies in the range `[l, r]`.</li>
	<li>No **two** adjacent elements are equal.</li>
	<li>No **three** consecutive elements form a **strictly increasing** or **strictly decreasing** sequence.</li>
</ul>

Return the total number of valid **ZigZag** arrays.

Since the answer may be large, return it **modulo** `10^9 + 7`.

A **sequence** is said to be **strictly increasing** if each element is strictly greater than its previous one (if exists).

A **sequence** is said to be **strictly decreasing** if each element is strictly smaller than its previous one (if exists).
