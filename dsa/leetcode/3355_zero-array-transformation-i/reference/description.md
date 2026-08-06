## Description

You are given an integer array `nums` of length `n` and a 2D array `queries`, where `queries[i] = [l_i, r_i]`.

For each `queries[i]`:

<ul>
	<li>Select a <span data-keyword="subset">subset</span> of indices within the range `[l_i, r_i]` in `nums`.</li>
	<li>Decrement the values at the selected indices by 1.</li>
</ul>

A **Zero Array** is an array where all elements are equal to 0.

Return `true` if it is *possible* to transform `nums` into a **Zero Array **after processing all the queries sequentially, otherwise return `false`.
