## Description

Given an array of integers `nums` and an integer `k`, return *the number of **unique** k-diff pairs in the array*.

A **k-diff** pair is an integer pair `(nums[i], nums[j])`, where the following are true:

<ul>
	<li>`0 <= i, j < nums.length`</li>
	<li>`i != j`</li>
	<li>`|nums[i] - nums[j]| == k`</li>
</ul>

**Notice** that `|val|` denotes the absolute value of `val`.
