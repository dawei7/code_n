## Description

A **triplet** is an array of three integers. You are given a 2D integer array `triplets`, where `triplets[i] = [a_i, b_i, c_i]` describes the `i^th` **triplet**. You are also given an integer array `target = [x, y, z]` that describes the **triplet** you want to obtain.

To obtain `target`, you may apply the following operation on `triplets` **any number** of times (possibly **zero**):

<ul>
	<li>Choose two indices (**0-indexed**) `i` and `j` (`i != j`) and **update** `triplets[j]` to become `[max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]`.

	<ul>
		<li>For example, if `triplets[i] = [2, 5, 3]` and `triplets[j] = [1, 7, 5]`, `triplets[j]` will be updated to `[max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5]`.</li>
	</ul>
	</li>
</ul>

Return `true` *if it is possible to obtain the *`target`***triplet***`[x, y, z]`* as an** element** of *`triplets`*, or *`false`* otherwise*.
