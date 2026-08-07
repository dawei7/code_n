## General
Given an integer array `nums` and two integers `limit` and `goal`. The array `nums` has an interesting property that $abs(\text{nums}[i]) \le limit$, the algorithm solves **Minimum Elements to Add to Form a Given Sum** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
