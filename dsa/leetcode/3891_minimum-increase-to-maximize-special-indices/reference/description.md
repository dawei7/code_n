## Description

You are given an integer array `nums` of length `n`.

An index `i` (`0 < i < n - 1`) is **special** if `nums[i] > nums[i - 1]` and `nums[i] > nums[i + 1]`.

You may perform operations where you choose **any** index `i` and **increase** `nums[i]` by 1.

Your goal is to:

<ul>
	<li>**Maximize** the number of **special** indices.</li>
	<li>**Minimize** the total number of **operations** required to achieve that **maximum**.</li>
</ul>

Return an integer denoting the **minimum** total number of operations required.
