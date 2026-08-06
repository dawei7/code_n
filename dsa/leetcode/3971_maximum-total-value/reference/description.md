## Description

You are given two integer arrays `value` and `decay`, and an integer `m`.

<ul>
	<li>`value[i]` represents the initial value at index `i`.</li>
	<li>`decay[i]` represents how much the value decreases after each selection of index `i`.</li>
</ul>

You may select any index **multiple** times. The total number of selections across all indices must not exceed `m`.

If you select index `i` for the `t^th` time, where `t` is 1-indexed, the value gained is `value[i] - decay[i] * (t - 1)`.

Return the **maximum** total value you can obtain. Since the answer may be large, return it **modulo** `10^9 + 7`.
