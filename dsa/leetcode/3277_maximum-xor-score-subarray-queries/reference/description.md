## Description

You are given an array `nums` of `n` integers, and a 2D integer array `queries` of size `q`, where `queries[i] = [l_i, r_i]`.

For each query, you must find the **maximum XOR score** of any <span data-keyword="subarray">subarray</span> of `nums[l_i..r_i]`.

The **XOR score** of an array `a` is found by repeatedly applying the following operations on `a` so that only one element remains, that is the **score**:

<ul>
	<li>Simultaneously replace `a[i]` with `a[i] XOR a[i + 1]` for all indices `i` except the last one.</li>
	<li>Remove the last element of `a`.</li>
</ul>

Return an array `answer` of size `q` where `answer[i]` is the answer to query `i`.
