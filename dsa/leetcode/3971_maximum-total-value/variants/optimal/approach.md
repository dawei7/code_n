## General

For each index `i`, the positive gains form a decreasing arithmetic progression beginning at `value[i]` with common difference `-decay[i]`. Since there is no interaction between progressions and using fewer than `m` selections is allowed, an optimal choice consists of the largest `m` positive terms across all progressions, or every positive term when fewer than `m` exist.

First count the available positive terms. Progression `(initial, step)` contributes `(initial - 1) // step + 1`; cap the accumulated count at `m`, because only that many selected terms can matter. Call the resulting number `selections`.

For a positive threshold `g`, progression `(initial, step)` contains `(initial - g) // step + 1` terms at least `g` when `initial >= g`, and none otherwise. This total count is monotone non-increasing as `g` grows. Binary-search the largest threshold for which at least `selections` terms remain. It is exactly the value of the final selected term in sorted order.

At that threshold, sum every included prefix with the arithmetic-progression formula. If a progression contributes `terms` values, its final included value is `initial - (terms - 1) * step`, so its prefix sum is `terms * (initial + last) // 2`. The combined count can exceed `selections` only through copies equal to the threshold: by maximality, fewer than `selections` terms are strictly greater. Subtract one threshold value for each surplus copy, then apply the modulus.

This construction selects every term greater than the cutoff and exactly enough terms equal to it. Those are precisely the globally largest positive gains, so exchanging any chosen term for an unchosen one cannot increase the total. The computed sum is therefore optimal.

## Complexity detail

Let $n$ be the array length and $A = \max(\texttt{value})$. Positive-term counting and final summation each scan the arrays once. Binary search performs $O(\log A)$ count scans, so the total time is $O(n\log A)$. The algorithm uses $O(1)$ auxiliary space beyond its input arrays.

## Alternatives and edge cases

- **Priority queue per selection:** Repeatedly take the largest current gain and insert its successor. This is correct but costs $O(m\log n)$ time, which is infeasible when `m` reaches $10^9$.
- **Materialize and sort every positive term:** This directly exposes the global ordering but can create far more than $10^9$ values and cannot fit within the limits.
- **At most `m` selections:** Stop after all positive gains are exhausted. Taking zero or negative terms can never improve the objective.
- **Surplus cutoff copies:** Several progressions may contain the same threshold. Summing all of them and subtracting only the excess preserves the required number of tied selections.
- **Progressions that skip the cutoff:** Their smallest included term may exceed the threshold; maximality of the cutoff still guarantees that every removable surplus term equals the threshold somewhere else.
- **Modulo timing:** Compare and sum the actual gains first. Reducing intermediate candidates before deciding which terms are largest would change the optimization problem.
- **Large arithmetic sums:** The unmodded optimum can approach $10^{18}$, so fixed-width implementations need 64-bit arithmetic before taking the modulus.
