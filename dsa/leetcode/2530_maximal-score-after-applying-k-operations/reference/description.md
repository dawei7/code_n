## Description

You are given a **0-indexed** integer array `nums` and an integer `k`. You have a **starting score** of `0`.

In one **operation**:

<ol>
	<li>choose an index `i` such that `0 <= i < nums.length`,</li>
	<li>increase your **score** by `nums[i]`, and</li>
	<li>replace `nums[i]` with `ceil(nums[i] / 3)`.</li>
</ol>

Return *the maximum possible **score** you can attain after applying **exactly*** `k` *operations*.

The ceiling function `ceil(val)` is the least integer greater than or equal to `val`.
