## Description

Anti-theft security devices are activated inside a bank. You are given a **0-indexed** binary string array `bank` representing the floor plan of the bank, which is an `m x n` 2D matrix. `bank[i]` represents the `i^th` row, consisting of `'0'`s and `'1'`s. `'0'` means the cell is empty, while`'1'` means the cell has a security device.

There is **one** laser beam between any **two** security devices **if both** conditions are met:

<ul>
	<li>The two devices are located on two **different rows**: `r_1` and `r_2`, where `r_1 < r_2`.</li>
	<li>For **each** row `i` where `r_1 < i < r_2`, there are **no security devices** in the `i^th` row.</li>
</ul>

Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return *the total number of laser beams in the bank*.
