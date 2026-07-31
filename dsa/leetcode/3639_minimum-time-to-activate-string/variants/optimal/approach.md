## General

**Count the complement of valid substrings.** There are $n(n+1)/2$ nonempty substrings in total. At a fixed time, an invalid substring contains no activated position, so it lies entirely inside one maximal contiguous run of inactive indices. A run of length $L$ contributes $L(L+1)/2$ invalid substrings. Subtracting the sum over all inactive runs gives the valid count.

**Represent the entire timeline once.** Invert the permutation into `activation_time[index]`. During a feasibility check for time $t$, an index is active exactly when its stored activation time is at most $t$. One left-to-right scan accumulates lengths of inactive runs and determines whether the valid count reaches `k`.

**Binary-search the first feasible time.** Activating another position cannot invalidate a previously valid substring, so the valid count is monotone non-decreasing over time. Binary search times from 0 through $n-1$, retaining the left half whenever its midpoint is active. If $k$ exceeds the total number of substrings, return `-1` before searching.

The final converged time is feasible, and every earlier time was excluded by a failed monotone check, so it is the minimum.

## Complexity detail

Building activation times costs $O(n)$. Binary search performs $O(\log n)$ feasibility checks, each scanning $n$ indices, for total $O(n\log n)$ time. The activation-time array uses $O(n)$ auxiliary space.

The benchmark uses $S=n$. The accepted method is $O(S\log S)$, while checking times sequentially and rescanning all runs after each replacement requires $O(S^2)$ time.

## Alternatives and edge cases

- **Simulate every time:** Correctly finds the first active state but repeats an $O(n)$ count up to $n$ times.
- **Ordered activated positions:** Maintaining gaps dynamically can update the valid count online in $O(\log n)$ per activation, also giving $O(n\log n)$ total time.
- **Count valid substrings directly:** Overlaps between activated positions complicate addition; inactive runs form a disjoint complement.
- **Time zero:** The first replacement may already create enough valid substrings.
- **All substrings required:** Every position must eventually be activated, so the answer is $n-1$.
- **Impossible k:** The absolute maximum is $n(n+1)/2$.
- **Original letters:** Their values never affect validity; only activated positions matter.
- **Inclusive threshold:** A valid count exactly equal to `k` activates the string.
