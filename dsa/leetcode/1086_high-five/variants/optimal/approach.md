## General
Given a list of the scores of different students, `items`, where $\text{items}[i] = [\text{ID}_{i}, \text{score}_{i}]$ represents one score from a student with $\text{ID}_{i}$, calculate each student's **top five average**, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include the walrus operator (`:=`) for inline assignment and evaluation.

## Complexity detail
- **Time Complexity**: $O(N+S\log S)$ — Operation count bound.
- **Space Complexity**: $O(S)$ — Auxiliary memory allocation bound.
