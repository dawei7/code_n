## Description

A **happy string** is a string that:

<ul>
	<li>consists only of letters of the set `['a', 'b', 'c']`.</li>
	<li>`s[i] != s[i + 1]` for all values of `i` from `1` to `s.length - 1` (string is 1-indexed).</li>
</ul>

For example, strings **"abc", "ac", "b"** and **"abcbabcbcb"** are all happy strings and strings **"aa", "baa"** and **"ababbc"** are not happy strings.

Given two integers `n` and `k`, consider a list of all happy strings of length `n` sorted in lexicographical order.

Return *the kth string* of this list or return an **empty string** if there are less than `k` happy strings of length `n`.
