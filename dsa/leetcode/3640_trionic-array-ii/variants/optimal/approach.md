## General

Maintain the best sum of a subarray ending at the current position in each partially completed phase:

- `increasing` has at least one strictly increasing edge.
- `decreasing` has completed the first phase and has at least one decreasing edge.
- `trionic` has completed both turns and has at least one edge in the final increasing phase.

When `current > previous`, an increasing state may either start with the pair `[previous, current]` or extend the prior increasing state. A trionic state may start its final phase by extending the prior decreasing state or continue an existing final increase. Decreasing becomes invalid.

When `current < previous`, only the decreasing phase can advance: it either starts from the prior increasing state or extends a prior decreasing state. An equality invalidates every strict phase ending at the current position.

Taking the larger extension in each transition retains exactly the best sum for that state and endpoint. Starting a new increasing pair permits a harmful earlier prefix to be discarded. Every trionic subarray follows one sequence of these transitions, and each finite `trionic` state represents such a subarray, so the maximum trionic state over all endpoints is the required answer.

## Complexity detail

Let $n$ be the array length. Each adjacent pair causes a constant number of state transitions, for $O(n)$ time. Only three phase sums and the global answer are retained, giving $O(1)$ auxiliary space.

The benchmark uses $S=n$. The accepted phase DP is $O(S)$, whereas starting a fresh phase scan at every left endpoint requires $O(S^2)$ time.

## Alternatives and edge cases

- **Enumerate l, p, q, and r:** Directly follows the definition but is far beyond the legal input scale.
- **Scan from every left endpoint:** Tracking phases avoids four nested loops but remains quadratic because long suffixes are revisited.
- **Prefix and suffix run sums:** They can describe candidate turns, but the constant-state DP handles restarts and negative values directly.
- **Negative values:** Never initialize the answer to zero; every valid trionic sum may be negative.
- **Equality:** A plateau breaks all strict phase states.
- **Restart within an increasing run:** Dropping a negative prefix may improve every later completed pattern.
- **Minimum length:** A valid range needs four values, one edge per phase.
- **Large sum:** Up to $10^5$ values of magnitude $10^9$ require 64-bit arithmetic in fixed-width languages.
