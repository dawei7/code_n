## Function Contract

**Inputs**

- `n`: The index of the destination step and the number of entries in `costs`.
- `costs`: The serialized step costs. Its first list element represents conceptual `costs[1]`, the cost of landing on step $1$; in general, Python element `costs[k - 1]` represents step $k$.

Only jumps of length $1$, $2$, or $3$ are permitted. Landing on step $j$ after leaving step $i$ adds `costs[j] + (j - i)^2` under the statement's one-based cost notation.

**Return value**

Return the minimum total cost of any valid route from step $0$ to step $n$.
