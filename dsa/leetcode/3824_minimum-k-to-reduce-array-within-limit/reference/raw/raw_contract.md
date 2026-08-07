## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

Let $N = \lvert\texttt{nums}\rvert$, let $V = \max(\texttt{nums})$, and define

$$
H = \max\left(V, \left\lceil\sqrt{N}\right\rceil\right).
$$

**Return value**

Return the minimum positive `k` whose minimum required operation count is at most $k^2$. Reaching exactly zero is sufficient because zero is non-positive, and reducing an element below zero is also allowed.
