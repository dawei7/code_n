## General
Given Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp, the algorithm solves **Time Based Key-Value Store** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(Q\log Q)$ — Operation count bound.
- **Space Complexity**: $O(Q)$ — Auxiliary memory allocation bound.
