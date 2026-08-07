## General
Given A ride sharing system manages ride requests from riders and availability from drivers. Riders request rides, and drivers become available over time. The system should match riders and drivers in the order they arrive, the algorithm solves **Design Ride Sharing System** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(Q)$ — Operation count bound.
- **Space Complexity**: $O(Q)$ — Auxiliary memory allocation bound.
