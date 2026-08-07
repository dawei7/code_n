## General
Given a stream of **records** about a particular stock. Each record contains a **timestamp** and the corresponding **price** of the stock at that timestamp, the algorithm solves **Stock Price Fluctuation ** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(\log Q)$ — Operation count bound.
- **Space Complexity**: $O(Q)$ — Auxiliary memory allocation bound.
