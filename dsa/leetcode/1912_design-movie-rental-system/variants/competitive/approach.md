## General
Given You have a movie renting company consisting of `n` shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the cu..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(E \log E + Q \log(E + Q))$ — Operation count bound.
- **Space Complexity**: $O(E + Q)$ — Auxiliary memory allocation bound.
