## Description

A ride sharing system manages ride requests from riders and availability from drivers. Riders request rides, and drivers become available over time. The system should match riders and drivers in the order they arrive.

Implement the `RideSharingSystem` class:

<ul>
	<li>`RideSharingSystem()` Initializes the system.</li>
	<li>`void addRider(int riderId)` Adds a new rider with the given `riderId`.</li>
	<li>`void addDriver(int driverId)` Adds a new driver with the given `driverId`.</li>
	<li>`int[] matchDriverWithRider()` Matches the **earliest** available driver with the **earliest** waiting rider and removes both of them from the system. Returns an integer array of size 2 where `result = [driverId, riderId]` if a match is made. If no match is available, returns `[-1, -1]`.</li>
	<li>`void cancelRider(int riderId)` Cancels the ride request of the rider with the given `riderId` **if the rider exists** and has **not** yet been matched.</li>
</ul>
