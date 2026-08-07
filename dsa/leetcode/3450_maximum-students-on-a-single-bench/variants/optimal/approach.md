## General
Given a 2D integer array of student data `students`, where $\text{students}[i] = [\text{student}_{id}, \text{bench}_{id}]$ represents that student $\text{student}_{id}$ is sitting on the bench $\text{bench}_{id}$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
