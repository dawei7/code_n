## Description

You are given two numeric strings `num1` and `num2` and two integers `max_sum` and `min_sum`. We denote an integer `x` to be *good* if:

<ul>
	<li>`num1 <= x <= num2`</li>
	<li>`min_sum <= digit_sum(x) <= max_sum`.</li>
</ul>

Return *the number of good integers*. Since the answer may be large, return it modulo `10^9 + 7`.

Note that `digit_sum(x)` denotes the sum of the digits of `x`.
