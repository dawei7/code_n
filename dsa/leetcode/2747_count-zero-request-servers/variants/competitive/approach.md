## General
Given an integer `n` denoting the total number of servers and a **2D** **0-indexed **integer array `logs`, where $\text{logs}[i] = [\text{server}_{id}, time]$ denotes that the server with id $\text{server}_{id}$ received a ..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window.

## Complexity detail
- **Time Complexity**: $O(m log m + q log q)$ — Operation count bound.
- **Space Complexity**: $O(n + q)$ — Auxiliary memory allocation bound.
