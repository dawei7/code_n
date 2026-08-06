## Description

A sequence `x_1, x_2, ..., x_n` is *Fibonacci-like* if:

<ul>
	<li>`n >= 3`</li>
	<li>`x_i + x_i+1 == x_i+2` for all `i + 2 <= n`</li>
</ul>

Given a **strictly increasing** array `arr` of positive integers forming a sequence, return *the **length** of the longest Fibonacci-like subsequence of* `arr`. If one does not exist, return `0`.

A **subsequence** is derived from another sequence `arr` by deleting any number of elements (including none) from `arr`, without changing the order of the remaining elements. For example, `[3, 5, 8]` is a subsequence of `[3, 4, 5, 6, 7, 8]`.
