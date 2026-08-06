## Description

There is a test that has `n` types of questions. You are given an integer `target` and a **0-indexed** 2D integer array `types` where `types[i] = [count_i, marks_i]` indicates that there are `count_i` questions of the `i^th` type, and each one of them is worth `marks_i` points.

<ul>
</ul>

Return *the number of ways you can earn **exactly** *`target`* points in the exam*. Since the answer may be too large, return it **modulo** `10^9 + 7`.

**Note** that questions of the same type are indistinguishable.

<ul>
	<li>For example, if there are `3` questions of the same type, then solving the `1^st` and `2^nd` questions is the same as solving the `1^st` and `3^rd` questions, or the `2^nd` and `3^rd` questions.</li>
</ul>
