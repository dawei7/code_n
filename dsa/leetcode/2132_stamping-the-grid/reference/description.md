## Description

You are given an `m x n` binary matrix `grid` where each cell is either `0` (empty) or `1` (occupied).

You are then given stamps of size `stampHeight x stampWidth`. We want to fit the stamps such that they follow the given **restrictions** and **requirements**:

<ol>
	<li>Cover all the **empty** cells.</li>
	<li>Do not cover any of the **occupied** cells.</li>
	<li>We can put as **many** stamps as we want.</li>
	<li>Stamps can **overlap** with each other.</li>
	<li>Stamps are not allowed to be **rotated**.</li>
	<li>Stamps must stay completely **inside** the grid.</li>
</ol>

Return `true` *if it is possible to fit the stamps while following the given restrictions and requirements. Otherwise, return* `false`.
