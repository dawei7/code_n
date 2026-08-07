## General
Given two string arrays, `names` and `columns`, both of size `n`. The $$i^{\text{th}}$$ table is represented by the name $\text{names}[i]$ and contains $\text{columns}[i]$ number of columns, the algorithm solves **Design SQL** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n + q + E)$ — Operation count bound.
- **Space Complexity**: $O(n + S)$ — Auxiliary memory allocation bound.
