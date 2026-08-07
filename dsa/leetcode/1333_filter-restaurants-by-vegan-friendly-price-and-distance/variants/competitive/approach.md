## General
Given the array `restaurants` where  $\text{restaurants}[i] = [\text{id}_{i}, \text{rating}_{i}, \text{veganFriendly}_{i}, \text{price}_{i}, \text{distance}_{i}]$. You have to filter the restaurants using three filters, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n\log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
