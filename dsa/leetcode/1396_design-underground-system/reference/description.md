## Description

An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the `UndergroundSystem` class:

<ul>
	<li>`void checkIn(int id, string stationName, int t)`

	<ul>
		<li>A customer with a card ID equal to `id`, checks in at the station `stationName` at time `t`.</li>
		<li>A customer can only be checked into one place at a time.</li>
	</ul>
	</li>
	<li>`void checkOut(int id, string stationName, int t)`
	<ul>
		<li>A customer with a card ID equal to `id`, checks out from the station `stationName` at time `t`.</li>
	</ul>
	</li>
	<li>`double getAverageTime(string startStation, string endStation)`
	<ul>
		<li>Returns the average time it takes to travel from `startStation` to `endStation`.</li>
		<li>The average time is computed from all the previous traveling times from `startStation` to `endStation` that happened **directly**, meaning a check in at `startStation` followed by a check out from `endStation`.</li>
		<li>The time it takes to travel from `startStation` to `endStation` **may be different** from the time it takes to travel from `endStation` to `startStation`.</li>
		<li>There will be at least one customer that has traveled from `startStation` to `endStation` before `getAverageTime` is called.</li>
	</ul>
	</li>
</ul>

You may assume all calls to the `checkIn` and `checkOut` methods are consistent. If a customer checks in at time `t_1` then checks out at time `t_2`, then `t_1 < t_2`. All events happen in chronological order.
