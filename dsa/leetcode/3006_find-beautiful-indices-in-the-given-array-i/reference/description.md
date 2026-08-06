## Description

You are given a **0-indexed** string `s`, a string `a`, a string `b`, and an integer `k`.

An index `i` is **beautiful** if:

<ul>
	<li>`0 <= i <= s.length - a.length`</li>
	<li>`s[i..(i + a.length - 1)] == a`</li>
	<li>There exists an index `j` such that:
	<ul>
		<li>`0 <= j <= s.length - b.length`</li>
		<li>`s[j..(j + b.length - 1)] == b`</li>
		<li>`|j - i| <= k`</li>
	</ul>
	</li>
</ul>

Return *the array that contains beautiful indices in **sorted order from smallest to largest***.
