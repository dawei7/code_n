## General
Given the array `orders`, which represents the orders that customers have done in a restaurant. More specifically $\text{orders}[i]=[\text{customerName}_{i},\text{tableNumber}_{i},\text{foodItem}_{i}]$ where $\text{customer..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(N + F\log F + T\log T + TF)$ — Operation count bound.
- **Space Complexity**: $O(N + TF)$ — Auxiliary memory allocation bound.
