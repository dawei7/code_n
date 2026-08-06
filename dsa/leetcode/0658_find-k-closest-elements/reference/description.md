## Description

Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

<ul>
	<li>`|a - x| < |b - x|`, or</li>
	<li>`|a - x| == |b - x|` and `a < b`</li>
</ul>
