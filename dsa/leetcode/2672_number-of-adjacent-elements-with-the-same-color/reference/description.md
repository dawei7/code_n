## Description

You are given an integer `n` representing an array `colors` of length `n` where all elements are set to 0's meaning **uncolored**. You are also given a 2D integer array `queries` where `queries[i] = [index_i, color_i]`. For the `i^th` **query**:

<ul>
	<li>Set `colors[index_i]` to `color_i`.</li>
	<li>Count the number of adjacent pairs in `colors` which have the same color (regardless of `color_i`).</li>
</ul>

Return an array `answer` of the same length as `queries` where `answer[i]` is the answer to the `i^th` query.
