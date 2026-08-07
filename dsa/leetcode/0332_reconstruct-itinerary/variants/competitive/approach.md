## General
Given a list of airline `tickets` where $\text{tickets}[i] = [\text{from}_{i}, \text{to}_{i}]$ represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(E \log E)$ — Operation count bound.
- **Space Complexity**: $O(E)$ — Auxiliary memory allocation bound.
