## Description

You are given a binary string `s` of length `n`, where:

<ul>
	<li>`'1'` represents an **active** section.</li>
	<li>`'0'` represents an **inactive** section.</li>
</ul>

You can perform **at most one trade** to maximize the number of active sections in `s`. In a trade, you:

<ul>
	<li>Convert a contiguous block of `'1'`s that is surrounded by `'0'`s to all `'0'`s.</li>
	<li>Afterward, convert a contiguous block of `'0'`s that is surrounded by `'1'`s to all `'1'`s.</li>
</ul>

Additionally, you are given a **2D array** `queries`, where `queries[i] = [l_i, r_i]` represents a <span data-keyword="substring-nonempty">substring</span> `s[l_i...r_i]`.

For each query, determine the **maximum** possible number of active sections in `s` after making the optimal trade on the substring `s[l_i...r_i]`.

Return an array `answer`, where `answer[i]` is the result for `queries[i]`.

**Note**

<ul>
	<li>For each query, treat `s[l_i...r_i]` as if it is **augmented** with a `'1'` at both ends, forming `t = '1' + s[l_i...r_i] + '1'`. The augmented `'1'`s **do not** contribute to the final count.</li>
	<li>The queries are independent of each other.</li>
</ul>
