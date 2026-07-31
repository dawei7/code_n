## Description

A ride-sharing service receives ride requests from riders while drivers report their availability over time. Whenever a match is requested, riders and drivers must be paired according to the order in which each group arrived.

Implement the `RideSharingSystem` class:

- `RideSharingSystem()` creates an empty system.
- `void addRider(int riderId)` adds the rider identified by `riderId` to the waiting riders.
- `void addDriver(int driverId)` adds the driver identified by `driverId` to the available drivers.
- `int[] matchDriverWithRider()` pairs the earliest available driver with the earliest waiting rider and removes both from the system. Return `[driverId, riderId]` when a pair is formed, or `[-1, -1]` when either side is unavailable.
- `void cancelRider(int riderId)` cancels the request for `riderId` only if that rider currently exists in the system and has not already been matched.
