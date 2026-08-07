## General
Given an array of integers `citations` where $\text{citations}[i]$ is the number of citations a researcher received for their $$i^{\text{th}}$$ paper and `citations` is sorted in **non-descending order**, return *the resear..., the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(\log n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
