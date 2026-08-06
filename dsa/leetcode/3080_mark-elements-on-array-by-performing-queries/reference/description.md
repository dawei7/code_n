## Description

You are given a **0-indexed** array `nums` of size `n` consisting of positive integers.

You are also given a 2D array `queries` of size `m` where `queries[i] = [index_i, k_i]`.

Initially all elements of the array are **unmarked**.

You need to apply `m` queries on the array in order, where on the `i^th` query you do the following:

<ul>
	<li>Mark the element at index `index_i` if it is not already marked.</li>
	<li>Then mark `k_i` unmarked elements in the array with the **smallest** values. If multiple such elements exist, mark the ones with the smallest indices. And if less than `k_i` unmarked elements exist, then mark all of them.</li>
</ul>

Return *an array answer of size *`m`* where *`answer[i]`* is the **sum** of unmarked elements in the array after the *`i^th`* query*.
