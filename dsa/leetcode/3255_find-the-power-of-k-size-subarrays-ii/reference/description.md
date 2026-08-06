## Description

You are given an array of integers `nums` of length `n` and a *positive* integer `k`.

The **power** of an array is defined as:

<ul>
	<li>Its **maximum** element if *all* of its elements are **consecutive** and **sorted** in **ascending** order.</li>
	<li>-1 otherwise.</li>
</ul>

You need to find the **power** of all <span data-keyword="subarray-nonempty">subarrays</span> of `nums` of size `k`.

Return an integer array `results` of size `n - k + 1`, where `results[i]` is the *power* of `nums[i..(i + k - 1)]`.
