## Description

You are given a string of digits `num`, such as `"123456579"`. We can split it into a Fibonacci-like sequence `[123, 456, 579]`.

Formally, a **Fibonacci-like** sequence is a list `f` of non-negative integers such that:

<ul>
	<li>`0 <= f[i] < 2^31`, (that is, each integer fits in a **32-bit** signed integer type),</li>
	<li>`f.length >= 3`, and</li>
	<li>`f[i] + f[i + 1] == f[i + 2]` for all `0 <= i < f.length - 2`.</li>
</ul>

Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number `0` itself.

Return any Fibonacci-like sequence split from `num`, or return `[]` if it cannot be done.
