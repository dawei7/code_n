## Description

You are given an array of **positive** integers `nums`.

You need to select a <span data-keyword="subset">subset</span> of `nums` which satisfies the following condition:

<ul>
	<li>You can place the selected elements in a **0-indexed** array such that it follows the pattern: `[x, x^2, x^4, ..., x^k/2, x^k, x^k/2, ..., x^4, x^2, x]` (**Note** that `k` can be any **non-negative** power of `2`). For example, `[2, 4, 16, 4, 2]` and `[3, 9, 3]` follow the pattern while `[2, 4, 8, 4, 2]` does not.</li>
</ul>

Return *the **maximum** number of elements in a subset that satisfies these conditions.*
