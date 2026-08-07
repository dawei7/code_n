## Function Contract

**Inputs**

- `towers`: A non-empty list of triples `[x_i, y_i, q_i]`, giving one tower's coordinates and quality factor per entry.
- `center`: A two-element list `[cx, cy]` representing your location.
- `radius`: The inclusive maximum Manhattan distance at which a tower is reachable.

Let $N=\lvert\texttt{towers}\rvert$. For each tower, reachability is determined by

$$
\lvert x_i-cx\rvert+\lvert y_i-cy\rvert\le\texttt{radius}.
$$

**Return value**

Return `[x_i, y_i]` for the reachable tower with greatest $q_i$. Among equal greatest qualities, return the smallest coordinate under ordinary list lexicographic order. Return `[-1, -1]` if the reachable set is empty.
