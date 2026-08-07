## General
Given a 2D array of axis-aligned `rectangles`. Each $\text{rectangle}[i] = [x_{i1}, y_{i1}, x_{i2}, y_{i2}]$ denotes the $$i^{\text{th}}$$ rectangle where $(x_{i1}, y_{i1})$ are the coordinates of the **bottom-left corner**..., the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n\log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
