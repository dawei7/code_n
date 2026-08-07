## General
Given two string arrays $\text{positive}_{feedback}$ and $\text{negative}_{feedback}$, containing the words denoting positive and negative feedback, respectively. Note that **no** word is both positive and negative, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(F + n log n)$ — Operation count bound.
- **Space Complexity**: $O(F + n)$ — Auxiliary memory allocation bound.
