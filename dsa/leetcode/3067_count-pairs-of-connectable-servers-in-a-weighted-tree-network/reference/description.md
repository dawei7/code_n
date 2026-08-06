## Description

You are given an unrooted weighted tree with `n` vertices representing servers numbered from `0` to `n - 1`, an array `edges` where `edges[i] = [a_i, b_i, weight_i]` represents a bidirectional edge between vertices `a_i` and `b_i` of weight `weight_i`. You are also given an integer `signalSpeed`.

Two servers `a` and `b` are **connectable** through a server `c` if:

<ul>
	<li>`a < b`, `a != c` and `b != c`.</li>
	<li>The distance from `c` to `a` is divisible by `signalSpeed`.</li>
	<li>The distance from `c` to `b` is divisible by `signalSpeed`.</li>
	<li>The path from `c` to `b` and the path from `c` to `a` do not share any edges.</li>
</ul>

Return *an integer array* `count` *of length* `n` *where* `count[i]` *is the **number** of server pairs that are **connectable** through* *the server* `i`.
