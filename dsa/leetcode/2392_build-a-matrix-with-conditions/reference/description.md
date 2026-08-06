## Description

You are given a **positive** integer `k`. You are also given:

<ul>
	<li>a 2D integer array `rowConditions` of size `n` where `rowConditions[i] = [above_i, below_i]`, and</li>
	<li>a 2D integer array `colConditions` of size `m` where `colConditions[i] = [left_i, right_i]`.</li>
</ul>

The two arrays contain integers from `1` to `k`.

You have to build a `k x k` matrix that contains each of the numbers from `1` to `k` **exactly once**. The remaining cells should have the value `0`.

The matrix should also satisfy the following conditions:

<ul>
	<li>The number `above_i` should appear in a **row** that is strictly **above** the row at which the number `below_i` appears for all `i` from `0` to `n - 1`.</li>
	<li>The number `left_i` should appear in a **column** that is strictly **left** of the column at which the number `right_i` appears for all `i` from `0` to `m - 1`.</li>
</ul>

Return ***any** matrix that satisfies the conditions*. If no answer exists, return an empty matrix.
