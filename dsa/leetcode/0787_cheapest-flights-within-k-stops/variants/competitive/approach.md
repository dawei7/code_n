## General
Given There are `n` cities connected by some number of flights. You are given an array `flights` where $\text{flights}[i] = [\text{from}_{i}, \text{to}_{i}, \text{price}_{i}]$ indicates that there is a flight from city $\te..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((k + 1) \cdot E)$ — Operation count bound.
- **Space Complexity**: $O(V)$ — Auxiliary memory allocation bound.
