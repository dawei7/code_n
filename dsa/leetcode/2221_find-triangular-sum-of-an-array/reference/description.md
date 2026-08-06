## Description

You are given a **0-indexed** integer array `nums`, where `nums[i]` is a digit between `0` and `9` (**inclusive**).

The **triangular sum** of `nums` is the value of the only element present in `nums` after the following process terminates:

<ol>
	<li>Let `nums` comprise of `n` elements. If `n == 1`, **end** the process. Otherwise, **create** a new **0-indexed** integer array `newNums` of length `n - 1`.</li>
	<li>For each index `i`, where `0 <= i < n - 1`, **assign** the value of `newNums[i]` as `(nums[i] + nums[i+1]) % 10`, where `%` denotes modulo operator.</li>
	<li>**Replace** the array `nums` with `newNums`.</li>
	<li>**Repeat** the entire process starting from step 1.</li>
</ol>

Return *the triangular sum of* `nums`.
