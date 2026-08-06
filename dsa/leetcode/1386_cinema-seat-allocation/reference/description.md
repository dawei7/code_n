## Description

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/14/cinema_seats_1.png" style="width: 400px; height: 149px;" />

A cinema has `n` rows of seats, numbered from 1 to `n`. Each row has 10 seats, numbered from 1 to 10.

You are given a 2D integer array <code data-end="170" data-start="155">reservedSeats</code>, where <code data-end="212" data-start="178">reservedSeats[i] = [row_i, seat_i]</code> means that seat <code data-end="236" data-start="229">seat_i</code> in row <code data-end="250" data-start="244">row_i</code> is already reserved.

A four-person group must be assigned to four seats in the **same** row. The group can be seated in one of the following seat blocks:

<ul>
	<li>seats <code data-end="423" data-start="411">2, 3, 4, 5</code></li>
	<li>seats <code data-end="444" data-start="432">4, 5, 6, 7</code></li>
	<li>seats <code data-end="465" data-start="453">6, 7, 8, 9</code></li>
</ul>

A block can be used only if **none** of its seats are reserved. Each seat can be assigned to **at most **one group.

Return an integer denoting the **maximum** number of four-person groups that can be assigned.
