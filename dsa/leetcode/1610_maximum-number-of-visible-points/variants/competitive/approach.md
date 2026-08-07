## General
Given an array `points`, an integer `angle`, and your `location`, where $location = [\text{pos}_{x}, \text{pos}_{y}]$ and $\text{points}[i] = [x_{i}, y_{i}]$ both denote **integral coordinates** on the X-Y plane, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n\log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
