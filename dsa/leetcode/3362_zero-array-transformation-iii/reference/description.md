## Description

You are given an integer array `nums` of length `n` and a 2D array `queries` where `queries[i] = [l_i, r_i]`.

Each `queries[i]` represents the following action on `nums`:

<ul>
	<li>Decrement the value at each index in the range `[l_i, r_i]` in `nums` by **at most**** **1.</li>
	<li>The amount by which the value is decremented can be chosen **independently** for each index.</li>
</ul>

A **Zero Array** is an array with all its elements equal to 0.

Return the **maximum **number of elements that can be removed from `queries`, such that `nums` can still be converted to a **zero array** using the *remaining* queries. If it is not possible to convert `nums` to a **zero array**, return -1.
