## Description

Alice and Bob are opponents in an archery competition. The competition has set the following rules:

<ol>
	<li>Alice first shoots `numArrows` arrows and then Bob shoots `numArrows` arrows.</li>
	<li>The points are then calculated as follows:
	<ol>
		<li>The target has integer scoring sections ranging from `0` to `11` **inclusive**.</li>
		<li>For **each** section of the target with score `k` (in between `0` to `11`), say Alice and Bob have shot `a_k` and `b_k` arrows on that section respectively. If `a_k >= b_k`, then Alice takes `k` points. If `a_k < b_k`, then Bob takes `k` points.</li>
		<li>However, if `a_k == b_k == 0`, then **nobody** takes `k` points.</li>
	</ol>
	</li>
</ol>

<ul>
	<li>
	For example, if Alice and Bob both shot `2` arrows on the section with score `11`, then Alice takes `11` points. On the other hand, if Alice shot `0` arrows on the section with score `11` and Bob shot `2` arrows on that same section, then Bob takes `11` points.

	</li>
</ul>

You are given the integer `numArrows` and an integer array `aliceArrows` of size `12`, which represents the number of arrows Alice shot on each scoring section from `0` to `11`. Now, Bob wants to **maximize** the total number of points he can obtain.

Return *the array *`bobArrows`* which represents the number of arrows Bob shot on **each** scoring section from *`0`* to *`11`. The sum of the values in `bobArrows` should equal `numArrows`.

If there are multiple ways for Bob to earn the maximum total points, return **any** one of them.
