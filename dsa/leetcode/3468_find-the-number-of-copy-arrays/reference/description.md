## Description

You are given an array `original` of length `n` and a 2D array `bounds` of length `n x 2`, where `bounds[i] = [u_i, v_i]`.

You need to find the number of **possible** arrays `copy` of length `n` such that:

<ol>
	<li>`(copy[i] - copy[i - 1]) == (original[i] - original[i - 1])` for `1 <= i <= n - 1`.</li>
	<li>`u_i <= copy[i] <= v_i` for `0 <= i <= n - 1`.</li>
</ol>

Return the number of such arrays.
