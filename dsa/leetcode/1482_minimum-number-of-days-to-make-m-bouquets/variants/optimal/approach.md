## General
**Rejecting an impossible flower requirement**

Every bouquet consumes exactly `k` different flowers, so `m * k` positions are necessary regardless of bloom days. If `m * k > N`, no day can make the request feasible and the answer is immediately `-1`. This check also prevents performing a binary search for a solution that cannot exist.

**Defining a monotone feasibility predicate**

For a proposed day `day`, mark a flower available precisely when `bloom_day[i] <= day`. If the required bouquets can be made on that day, they remain possible on every later day because flowers never become unavailable. Thus `can_make(day)` changes at most once, from false to true, across increasing days.

This false-then-true structure is what permits binary search for the first feasible day rather than simulating every day in the potentially billion-wide range.

**Counting disjoint adjacent bouquets**

Scan the garden from left to right while maintaining `adjacent`, the length of the current run of available flowers not yet assigned to a bouquet. An unavailable flower resets the run to zero because a bouquet cannot cross that position. Whenever `adjacent == k`, form one bouquet and reset `adjacent` to zero so none of those flowers can be reused.

This greedy grouping maximizes the number of bouquets within every available run. A run of length $r$ can contain exactly $\lfloor r/k \rfloor$ disjoint bouquets, and taking each group as soon as it reaches length `k` realizes that bound. The scan may return true as soon as it has formed `m` bouquets.

**Finding the first feasible day**

After the impossibility check, `min(bloom_day)` is a valid lower search bound and `max(bloom_day)` is guaranteed feasible because all flowers have bloomed and $m k \le N$. At each step, test the midpoint. If it is feasible, keep it as a candidate by moving the right bound to `mid`; otherwise discard it and every earlier day by moving the left bound to `mid + 1`.

The bounds converge on one day. All smaller days have been proven infeasible, while the converged day is feasible, so it is exactly the minimum waiting time required.

## Complexity detail
The impossibility check and bound calculation take $O(N)$ time. Each feasibility test scans at most $N$ flowers using constant state. Binary search performs $O(\log D)$ tests over the inclusive day range, giving $O(N \log D)$ time overall. The scan and search retain only scalar counters and bounds, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Linear day simulation:** Test every integer day from the minimum bloom day upward. It is correct but can take $O(ND)$ time, which is prohibitive when bloom days differ by as much as $10^9$.
- **Linear scan over distinct bloom days:** Sort the $U$ distinct candidate days and test them one by one. This avoids empty numeric gaps but still takes $O(NU + U \log U)$ time in the worst case because it repeats the garden scan for every candidate.
- **Search only distinct bloom days:** Sort the unique values in `bloomDay` and binary-search that list. Feasibility changes only on bloom days, but building the candidates costs $O(N \log N)$ time and $O(N)$ space.
- **Activate flowers with a disjoint-set structure:** Process positions in bloom-day order, merge neighboring active segments, and track how many groups of size `k` they contribute. This can solve the problem in $O(N \log N)$ time but is substantially more intricate.
- **Ignoring adjacency:** Counting all flowers with `bloomDay[i] <= day` is insufficient because late flowers can split the available positions into short runs.
- **Reusing flowers:** Overlapping groups are invalid; resetting the run after forming a bouquet ensures each position is consumed at most once.
- **Exactly enough positions:** When $m k = N$, every flower must be available, so the answer is the maximum bloom day.
- **One flower per bouquet:** For `k = 1`, the answer is the day of the `m`-th flower to bloom.
- **One bouquet:** The task becomes finding the earliest day with a consecutive available run of length `k`.
- **Equal bloom days:** Several flowers may activate together; the first feasible day can equal that shared value.
- **Large products:** In fixed-width languages, evaluate $m k$ in a wide integer type before comparing it with $N$.
