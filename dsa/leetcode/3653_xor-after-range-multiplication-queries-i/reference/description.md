## Description

You are given an integer array `nums` of length `n` and a 2D integer array `queries` of size `q`, where `queries[i] = [l_i, r_i, k_i, v_i]`.

For each query, you must apply the following operations in order:

<ul>
	<li>Set `idx = l_i`.</li>
	<li>While `idx <= r_i`:
	<ul>
		<li>Update: `nums[idx] = (nums[idx] * v_i) % (10^9 + 7)`</li>
		<li>Set `idx += k_i`.</li>
	</ul>
	</li>
</ul>

Return the **bitwise XOR** of all elements in `nums` after processing all queries.
