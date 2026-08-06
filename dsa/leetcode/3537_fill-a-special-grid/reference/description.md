## Description

You are given a non-negative integer `<font face="monospace">n</font>` representing a `2^n x 2^n` grid. You must fill the grid with integers from 0 to `2^2n - 1` to make it **special**. A grid is **special** if it satisfies **all** the following conditions:

<ul>
	<li>All numbers in the top-right quadrant are smaller than those in the bottom-right quadrant.</li>
	<li>All numbers in the bottom-right quadrant are smaller than those in the bottom-left quadrant.</li>
	<li>All numbers in the bottom-left quadrant are smaller than those in the top-left quadrant.</li>
	<li>Each of its quadrants is also a special grid.</li>
</ul>

Return the **special** `2^n x 2^n` grid.

**Note**: Any 1x1 grid is special.
