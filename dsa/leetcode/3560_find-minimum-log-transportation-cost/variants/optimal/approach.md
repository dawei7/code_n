## General

There are only three trucks, and an uncut log uses one of them. If both original logs were longer than `k`, each would need at least two pieces, requiring at least four trucks. The feasibility guarantee therefore means that at most one log exceeds the capacity.

Let $x=\max(n,m)$. If $x\le k$, both logs fit and the answer is zero. Otherwise, the length-$x$ log must be cut into positive lengths $a$ and $x-a$. Both pieces must be at most $k$, so the feasible cut positions satisfy

$$
x-k \le a \le k.
$$

The cutting cost is $a(x-a)$. This is a concave quadratic, so its minimum over the feasible interval occurs at an endpoint. Choosing either endpoint produces pieces of lengths $k$ and $x-k$, with cost $k(x-k)$. Thus the whole result is `max(0, max(n, m) - k) * k`.

## Complexity detail

The method performs a fixed number of comparisons and arithmetic operations. Its time complexity is $O(1)$ and its auxiliary space complexity is $O(1)$.

## Alternatives and edge cases

- **Enumerate every cut position:** Testing all $x-1$ positive splits and retaining the feasible minimum is correct but takes $O(k)$ time even though concavity identifies the best boundary directly.
- **Ternary search the quadratic:** The cost curve is concave rather than convex, so its minimum is at a feasible endpoint; searching its interior is unnecessary and can target the maximum instead.
- **Both logs fit:** When $\max(n,m)\le k$, no cut is needed and the cost is zero.
- **Exactly one log is over capacity:** The feasibility guarantee and the three-truck limit imply this is the only cutting case.
- **Log length $2k$:** Its only feasible split is $k+k$, giving cost $k^2$.
- **Integer width:** The answer can reach $10^{10}$, so fixed-width implementations need a 64-bit integer for the multiplication and return value.
