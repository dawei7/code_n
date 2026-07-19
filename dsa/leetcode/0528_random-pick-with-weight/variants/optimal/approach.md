## General
**Lay the weights on one cumulative interval**

Build prefix sums of the weights. If the total is `T`, index `i` owns the half-open interval from the previous prefix sum through `prefix[i]`; its interval length is exactly `weights[i]`. Choosing a uniform target in `[0, T)` therefore lands on index `i` with probability `weights[i] / T`.

**Locate a draw with binary search**

Scale each unit-interval draw by `T`, then find the first prefix sum strictly greater than that target. The prefix sums are strictly increasing because every weight is positive, so binary search identifies the unique owning interval in $O(\log n)$ time.

**Keep local tests reproducible**

The app adapter receives the unit-interval draws explicitly and returns their selected indices. The platform-native class instead calls the random generator inside `pickIndex`. Both paths use the same interval mapping, so deterministic correctness checks do not alter the required probability distribution.

**Why the distribution is exact**

The cumulative intervals are disjoint and cover all of `[0, T)`. Index `i` receives an interval of length `weights[i]`; under a uniform draw, its probability is that length divided by the total length. The first-prefix-greater search returns precisely that interval's index, including a consistent half-open boundary rule.

## Complexity detail
For `n` weights and `q` picks, prefix construction takes $O(n)$ time and every binary search takes $O(\log n)$, for $O(n + q \log n)$ total time. The prefix array uses $O(n)$ space; the returned app-local trace uses $O(q)$ output space.

## Alternatives and edge cases
- **Linear scan of cumulative weights:** preserves the distribution but costs $O(n)$ per pick instead of $O(\log n)$.
- **Expanded index array:** repeats each index according to its weight for constant-time picks, but its memory depends on the potentially enormous weight sum.
- **Alias method:** supports expected $O(1)$ picks after $O(n)$ preprocessing, but is substantially more complex and floating-point table construction needs care.
- **Single weight:** every draw must select index zero.
- **Boundary draw:** a target equal to a prefix boundary belongs to the following half-open interval.
- **Large total weight:** integer prefix sums must not overflow in fixed-width language implementations.
- **Random endpoint:** unit draws are in `[0, 1)`, so the scaled target never equals the total.
