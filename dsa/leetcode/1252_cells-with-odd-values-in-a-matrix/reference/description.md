## Description

There is an `m x n` matrix that is initialized to all `0`'s. There is also a 2D array `indices` where each `indices[i] = [r_i, c_i]` represents a **0-indexed location** to perform some increment operations on the matrix.

For each location `indices[i]`, do **both** of the following:

<ol>
	<li>Increment **all** the cells on row `r_i`.</li>
	<li>Increment **all** the cells on column `c_i`.</li>
</ol>

Given `m`, `n`, and `indices`, return *the **number of odd-valued cells** in the matrix after applying the increment to all locations in *`indices`.
