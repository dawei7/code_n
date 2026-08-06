## Description

You are given two integers `l` and `r`, and a string `directions` consisting of **exactly** three `'D'` characters and three `'R'` characters.

For each integer `x` in the range `[l, r]` (inclusive), perform the following steps:

<ol>
	<li>If `x` has fewer than 16 digits, pad it on the left with **leading zeros** to obtain a 16-digit string.</li>
	<li>Place the 16 digits into a `4 × 4` grid in **row-major** order (the first 4 digits form the first row from left to right, the next 4 digits form the second row, and so on).</li>
	<li>Starting at the **top-left** cell (`row = 0`, `column = 0`), apply the 6 characters of `directions` in order:
	<ul>
		<li>`'D'` increments the row by 1.</li>
		<li>`'R'` increments the column by 1.</li>
	</ul>
	</li>
	<li>Record the sequence of digits visited along the path (including the starting cell), producing a sequence of length 7.</li>
</ol>

The integer `x` is considered **good** if the recorded sequence is **non-decreasing**.

Return an integer representing the number of good integers in the range `[l, r]`.
