## Description

You are given an integer array `nums` and two integers, `k` and `limit`. Your task is to find a non-empty **<span data-keyword="subsequence-array">subsequence</span>** of `nums` that:

<ul>
	<li>Has an **alternating sum** equal to `k`.</li>
	<li>**Maximizes** the product of all its numbers *without the product exceeding* `limit`.</li>
</ul>

Return the *product* of the numbers in such a subsequence. If no subsequence satisfies the requirements, return -1.

The **alternating sum** of a **0-indexed** array is defined as the **sum** of the elements at **even** indices **minus** the **sum** of the elements at **odd** indices.
