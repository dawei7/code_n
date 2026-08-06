## Description

You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where `fruits[i]` represents the **quantity** of the `i^th` type of fruit, and `baskets[j]` represents the **capacity** of the `j^th` basket.

From left to right, place the fruits according to these rules:

<ul>
	<li>Each fruit type must be placed in the **leftmost available basket** with a capacity **greater than or equal** to the quantity of that fruit type.</li>
	<li>Each basket can hold **only one** type of fruit.</li>
	<li>If a fruit type **cannot be placed** in any basket, it remains **unplaced**.</li>
</ul>

Return the number of fruit types that remain unplaced after all possible allocations are made.
