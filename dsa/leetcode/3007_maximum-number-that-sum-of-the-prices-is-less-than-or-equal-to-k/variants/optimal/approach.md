## General

**Count one selected bit position over a prefix.** For 1-indexed position $p$,
the corresponding bit is zero for $2^{p-1}$ consecutive numbers and then one
for the next $2^{p-1}$, repeating in cycles of length $2^p$. Across integers
from 0 through `number`, complete cycles contribute exactly half their entries,
and the final partial cycle contributes any positions beyond its zero half.

Sum this cycle formula for $p=x,2x,3x,\ldots$ while the bit can occur in
`number`. Zero contributes no set bits, so the result is also the required sum
from 1 through `number`.

**Search the monotone boundary.** Accumulated price never decreases. Double an
upper bound until it is not cheap, then binary-search between the last known
lower region and that upper bound. Feasible midpoints move the lower endpoint;
infeasible ones move the upper endpoint. The final lower endpoint is the
greatest cheap number.

## Complexity detail

Evaluating one accumulated price inspects $O(\log K)$ relevant bit positions,
and exponential bracketing plus binary search performs $O(\log K)$ such
evaluations. The total bound is $O(\log^2 K)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every number:** Adding each number's price until the budget is exceeded is correct but linear in the returned number.
- **Digit DP:** A bitwise digit DP can count the same selected positions, but the regular on/off cycles give a simpler closed form.
- **One-indexed positions:** Position `x` corresponds to zero-indexed bit `x - 1`; shifting by `x` would be off by one.
- **Zero-price prefix:** For large `x`, many initial numbers have price zero and are still cheap.
- **Exact budget:** A number whose accumulated price equals `k` remains feasible.
- **Large answer:** Exponential bracketing avoids assuming that the answer fits near `k`.
