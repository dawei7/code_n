## Description

You are given a **0-indexed** `m x n` binary matrix `grid`.

A **0-indexed** `m x n` difference matrix `diff` is created with the following procedure:

<ul>
	<li>Let the number of ones in the `i^th` row be `onesRow_i`.</li>
	<li>Let the number of ones in the `j^th` column be `onesCol_j`.</li>
	<li>Let the number of zeros in the `i^th` row be `zerosRow_i`.</li>
	<li>Let the number of zeros in the `j^th` column be `zerosCol_j`.</li>
	<li>`diff[i][j] = onesRow_i + onesCol_j - zerosRow_i - zerosCol_j`</li>
</ul>

Return *the difference matrix *`diff`.
