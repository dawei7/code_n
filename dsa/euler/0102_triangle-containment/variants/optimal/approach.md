# Triangle Containment - Optimal Approach

## Algorithm Explanation

Find the number of triangles in `triangles.txt` whose interior contains the origin $O(0, 0)$.

### 2D Vector Cross Product Test:
For a triangle with directed vertices $A(x_a, y_a), B(x_b, y_b), C(x_c, y_c)$, the origin $O(0,0)$ lies strictly inside $\triangle ABC$ if and only if $O$ lies on the same relative side of all three directed edges $(A \to B, B \to C, C \to A)$.

The 2D cross product sign for each edge relative to origin:
- $c_1 = x_a y_b - x_b y_a$
- $c_2 = x_b y_c - x_c y_b$
- $c_3 = x_c y_a - x_a y_c$

$O(0,0)$ is contained inside $\triangle ABC \iff (c_1 > 0 \land c_2 > 0 \land c_3 > 0) \lor (c_1 < 0 \land c_2 < 0 \land c_3 < 0)$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N = 1000$ triangles ($6$ integer operations per triangle). Runs in $< 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Text input storage.
