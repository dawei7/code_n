## General

The ball's positions form a triangular wave. Starting at child $0$, it takes $n-1$ seconds to reach child $n-1$, then another $n-1$ seconds to return to child $0$. At that point both the position and the direction match the initial state, so the complete period is

$$
P = 2(n-1).
$$

Reduce `k` modulo $P$ to obtain an offset within one round trip. For offsets from $0$ through $n-1$, the ball is on the outbound rightward leg, and its child index equals the offset. Larger offsets lie on the return leg; mirroring the offset across the period gives child index `P - offset`.

These two branches exactly reproduce the passing process. The outbound formula advances one index per second from $0$ to $n-1$. The mirrored formula then decreases one index per second until it reaches $0$ at offset $P$, which is equivalent to offset $0$ of the next period.

## Complexity detail

The calculation uses a fixed number of arithmetic operations independent of both `n` and `k`, so it runs in $O(1)$ time and uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Second-by-second simulation:** Tracking a child and direction is straightforward and correct, but it performs $O(k)$ updates instead of using the repeated period directly.
- **Two-child line:** Every pass reaches the opposite endpoint, producing the alternating sequence $0,1,0,1,\ldots$; the same period formula gives $P=2$.
- **Exact right endpoint:** At offset $n-1$, the outbound branch must return child $n-1$ before the direction reverses for the next pass.
- **Exact full period:** An offset divisible by $2(n-1)$ returns child $0$, with the next movement again directed rightward.
- **Multiple round trips:** Taking the modulo discards complete cycles without losing either position or direction.
