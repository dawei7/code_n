## Description

You are given an integer array `nums` of length `n`.

Construct an array `prefixGcd` where for each index `i`:

<ul>
	<li>Let `mx_i = max(nums[0], nums[1], ..., nums[i])`.</li>
	<li>`prefixGcd[i] = gcd(nums[i], mx_i)`.</li>
</ul>

After constructing `prefixGcd`:

<ul>
	<li>Sort `prefixGcd` in **non-decreasing** order.</li>
	<li>Form pairs by taking the **smallest unpaired** element and the **largest unpaired** element.</li>
	<li>Repeat this process until no more pairs can be formed.</li>
	<li>For each formed pair, **compute** the `gcd` of the two elements.</li>
	<li>If `n` is odd, the **middle** element in the `prefixGcd` array remains **unpaired** and should be ignored.</li>
</ul>

Return an integer denoting the **sum of the GCD** values of all formed pairs.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.
