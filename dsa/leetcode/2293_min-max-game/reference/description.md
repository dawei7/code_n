## Description

You are given a **0-indexed** integer array `nums` whose length is a power of `2`.

Apply the following algorithm on `nums`:

<ol>
	<li>Let `n` be the length of `nums`. If `n == 1`, **end** the process. Otherwise, **create** a new **0-indexed** integer array `newNums` of length `n / 2`.</li>
	<li>For every **even** index `i` where `0 <= i < n / 2`, **assign** the value of `newNums[i]` as `min(nums[2 * i], nums[2 * i + 1])`.</li>
	<li>For every **odd** index `i` where `0 <= i < n / 2`, **assign** the value of `newNums[i]` as `max(nums[2 * i], nums[2 * i + 1])`.</li>
	<li>**Replace** the array `nums` with `newNums`.</li>
	<li>**Repeat** the entire process starting from step 1.</li>
</ol>

Return *the last number that remains in *`nums`* after applying the algorithm.*
