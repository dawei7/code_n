## General
Given You are asked to design an auction system that manages bids from multiple users in real time, the algorithm solves **Design Auction System** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(Q log Q)$ — Operation count bound.
- **Space Complexity**: $O(Q)$ — Auxiliary memory allocation bound.
