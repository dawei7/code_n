## Description

You are given `nums`, an array of positive integers of size `2 * n`. You must perform `n` operations on this array.

In the `i^th` operation **(1-indexed)**, you will:

<ul>
	<li>Choose two elements, `x` and `y`.</li>
	<li>Receive a score of `i * gcd(x, y)`.</li>
	<li>Remove `x` and `y` from `nums`.</li>
</ul>

Return *the maximum score you can receive after performing *`n`* operations.*

The function `gcd(x, y)` is the greatest common divisor of `x` and `y`.
