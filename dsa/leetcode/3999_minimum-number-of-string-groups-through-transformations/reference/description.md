## Description

You are given an array of strings `words`.

Define a **transformation** on a string `s` as follows:

<ul>
	<li>Let `E` be the <span data-keyword="subsequence-string">subsequence</span> of characters at even indices of `s`.</li>
	<li>Let `O` be the **subsequence** of characters at odd indices of `s`.</li>
	<li>**Independently** cyclically shift `E` and `O` by **any** number of positions to the right, possibly zero.</li>
	<li>Reconstruct the string by placing the shifted `E` characters back into even indices and the shifted `O` characters back into odd indices.</li>
</ul>

Two strings are **equivalent** if one can be transformed into the other by a **single** transformation.

Partition `words` into the **minimum** number of groups such that:

<ul>
	<li>Every string belongs to **exactly** one group.</li>
	<li>Every pair of strings in the same group are **equivalent**.</li>
</ul>

Return an integer denoting the **minimum** number of groups.
