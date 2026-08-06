## Description

You are given an integer array `nums`, an integer `k`, and an integer `multiplier`.

You need to perform `k` operations on `nums`. In each operation:

<ul>
	<li>Find the **minimum** value `x` in `nums`. If there are multiple occurrences of the minimum value, select the one that appears **first**.</li>
	<li>Replace the selected minimum value `x` with `x * multiplier`.</li>
</ul>

After the `k` operations, apply **modulo** `10^9 + 7` to every value in `nums`.

Return an integer array denoting the *final state* of `nums` after performing all `k` operations and then applying the modulo.
