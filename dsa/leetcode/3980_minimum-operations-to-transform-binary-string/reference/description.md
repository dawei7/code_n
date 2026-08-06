## Description

You are given two <span data-keyword="binary-string">binary strings</span> `s1` and `s2` of the same length `n`.

You can perform the following operations on `s1` any number of times, in any order:

<ul>
	<li>Choose an index `i` such that `s1[i] == '0'`, and change it to `'1'`.</li>
	<li>Choose an index `i` such that `0 <= i < n - 1`, and both `s1[i]` and `s1[i + 1]` are `'1'`. Change both characters to `'0'`.</li>
</ul>

Return the **minimum** number of operations required to make `s1` equal to `s2`. If it is impossible, return -1.
