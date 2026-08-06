## Description

You are given a **0-indexed** integer array `nums` and an integer `pivot`. Rearrange `nums` such that the following conditions are satisfied:

<ul>
	<li>Every element less than `pivot` appears **before** every element greater than `pivot`.</li>
	<li>Every element equal to `pivot` appears **in between** the elements less than and greater than `pivot`.</li>
	<li>The **relative order** of the elements less than `pivot` and the elements greater than `pivot` is maintained.
	<ul>
		<li>More formally, consider every `p_i`, `p_j` where `p_i` is the new position of the `i^th` element and `p_j` is the new position of the `j^th` element. If `i < j` and **both** elements are smaller (*or larger*) than `pivot`, then `p_i < p_j`.</li>
	</ul>
	</li>
</ul>

Return `nums`* after the rearrangement.*
