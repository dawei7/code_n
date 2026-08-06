## Description

You are given a string `s` and an integer `k`.

A **k-subsequence** is a **subsequence** of `s`, having length `k`, and all its characters are **unique**, **i.e**., every character occurs once.

Let `f(c)` denote the number of times the character `c` occurs in `s`.

The **beauty** of a **k-subsequence** is the **sum** of `f(c)` for every character `c` in the k-subsequence.

For example, consider `s = "abbbdd"` and `k = 2`:

<ul>
	<li>`f('a') = 1`, `f('b') = 3`, `f('d') = 2`</li>
	<li>Some k-subsequences of `s` are:
	<ul>
		<li>`"<u>**ab**</u>bbdd"` -> `"ab"` having a beauty of `f('a') + f('b') = 4`</li>
		<li>`"<u>**a**</u>bbb**<u>d</u>**d"` -> `"ad"` having a beauty of `f('a') + f('d') = 3`</li>
		<li>`"a**<u>b</u>**bb<u>**d**</u>d"` -> `"bd"` having a beauty of `f('b') + f('d') = 5`</li>
	</ul>
	</li>
</ul>

Return *an integer denoting the number of k-subsequences **whose **beauty** is the **maximum** among all **k-subsequences***. Since the answer may be too large, return it modulo `10^9 + 7`.

A subsequence of a string is a new string formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

**Notes**

<ul>
	<li>`f(c)` is the number of times a character `c` occurs in `s`, not a k-subsequence.</li>
	<li>Two k-subsequences are considered different if one is formed by an index that is not present in the other. So, two k-subsequences may form the same string.</li>
</ul>
