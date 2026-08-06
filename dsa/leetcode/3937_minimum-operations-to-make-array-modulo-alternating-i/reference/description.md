## Description

You are given an integer array `nums` and an integer `k`.

In one operation, you can **increase** or **decrease** any element of `nums` by 1.

An array is called **modulo alternating** if there exist two **distinct** integers `x` and `y` (`0 <= x, y < k`) such that:

<ul>
	<li>For every **even** index `i`, `nums[i] % k == x`</li>
	<li>For every **odd** index `i`, `nums[i] % k == y`</li>
</ul>

Return the **minimum** number of operations required to make `nums` **modulo alternating**.
