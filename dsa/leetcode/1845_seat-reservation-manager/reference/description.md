## Description

Design a system that manages the reservation state of `n` seats that are numbered from `1` to `n`.

Implement the `SeatManager` class:

<ul>
	<li>`SeatManager(int n)` Initializes a `SeatManager` object that will manage `n` seats numbered from `1` to `n`. All seats are initially available.</li>
	<li>`int reserve()` Fetches the **smallest-numbered** unreserved seat, reserves it, and returns its number.</li>
	<li>`void unreserve(int seatNumber)` Unreserves the seat with the given `seatNumber`.</li>
</ul>
