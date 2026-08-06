## Description

You are given an integer `n` and a **0-indexed** **2D array** `queries` where `queries[i] = [type_i, index_i, val_i]`.

Initially, there is a **0-indexed** `n x n` matrix filled with `0`'s. For each query, you must apply one of the following changes:

<ul>
	<li>if `type_i == 0`, set the values in the row with `index_i` to `val_i`, overwriting any previous values.</li>
	<li>if `type_i == 1`, set the values in the column with `index_i` to `val_i`, overwriting any previous values.</li>
</ul>

Return *the sum of integers in the matrix after all queries are applied*.
