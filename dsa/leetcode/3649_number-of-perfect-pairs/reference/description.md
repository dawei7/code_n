## Description

You are given an integer array `nums`.

A pair of indices `(i, j)` is called **perfect** if the following conditions are satisfied:

<ul>
	<li>`i < j`</li>
	<li>Let `a = nums[i]`, `b = nums[j]`. Then:
	<ul>
		<li>`min(|a - b|, |a + b|) <= min(|a|, |b|)`</li>
		<li>`max(|a - b|, |a + b|) >= max(|a|, |b|)`</li>
	</ul>
	</li>
</ul>

Return the number of **distinct** perfect pairs.

**Note:** The absolute value `|x|` refers to the **non-negative** value of `x`.
