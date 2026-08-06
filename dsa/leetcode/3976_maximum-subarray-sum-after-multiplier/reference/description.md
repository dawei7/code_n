## Description

You are given an integer array `nums` and a positive integer `k`.

You must choose **exactly** one <span data-keyword="subarray-nonempty">subarray</span> of `nums` and perform **exactly** one of the following operations:

<ol>
	<li>Multiply each number in the chosen subarray by `k`.</li>
	<li>Divide each number in the chosen subarray by `k`.
	<ul>
		<li>When dividing a positive number by `k`, use the **floor** value of the division result.</li>
		<li>When dividing a negative number by `k`, use the **ceiling** value of the division result.</li>
	</ul>
	</li>
</ol>

Return the **maximum** possible sum of a **non-empty** subarray in the resulting array.

Note that the subarray chosen for the operation and the subarray chosen for the sum may be **different**.
