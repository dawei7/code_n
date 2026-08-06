## Description

Given the following details of a matrix with `n` columns and `2` rows :

<ul>
	<li>The matrix is a binary matrix, which means each element in the matrix can be `0` or `1`.</li>
	<li>The sum of elements of the 0-th(upper) row is given as `upper`.</li>
	<li>The sum of elements of the 1-st(lower) row is given as `lower`.</li>
	<li>The sum of elements in the i-th column(0-indexed) is `colsum[i]`, where `colsum` is given as an integer array with length `n`.</li>
</ul>

Your task is to reconstruct the matrix with `upper`, `lower` and `colsum`.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.
