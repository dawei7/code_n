## General
Given You want to schedule a list of jobs in `d` days. Jobs are dependent (i.e To work on the $$i^{\text{th}}$$ job, you have to finish all the jobs `j` where $0 \le j < i$), the algorithm executes a single-pass linear scan through input elements.

## Complexity detail
- **Time Complexity**: $O(dn^2)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
