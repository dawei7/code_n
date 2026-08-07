## General
Given There is a supermarket that is frequented by many customers. The products sold at the supermarket are represented as two parallel integer arrays `products` and `prices`, where the $$i^{\text{th}}$$ product has an ID o..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(P+L)$ — Operation count bound.
- **Space Complexity**: $O(P)$ — Auxiliary memory allocation bound.
