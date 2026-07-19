## General
**Shrink random choice to the allowed count**

Let `bound = n - b`, where `b` is the blacklist size. A random choice from `[0, bound)` has exactly as many outcomes as the allowed domain, but some of those low outcomes may themselves be blacklisted.

**Reserve high allowed replacements**

Values in `[bound, n)` are never generated directly. Put every blacklisted value in a set, then walk upward from `bound`, skipping blacklisted high values. Assign each blacklisted low value a distinct remaining high value.

**Pick through one hash lookup**

Generate a raw value below `bound`. Return its mapped replacement when present and the raw value otherwise. App-local `draws` expose these raw choices deterministically so correctness cases and benchmarks are reproducible.

**Why the output is uniform and legal**

Unblacklisted low values map to themselves. Every blacklisted low value maps one-to-one onto an unblacklisted high value, and the counts of those two sets are equal. The mapping is therefore a bijection from the `bound` equally likely raw outcomes to all allowed values, preserving uniform probability while excluding every blacklisted number.

## Complexity detail
Building the blacklist set and at most one remap entry per blacklisted value takes expected $O(b)$ time and $O(b)$ space. Each of `p` picks uses one random draw and one expected constant-time hash lookup, so total time is $O(b + p)$.

## Alternatives and edge cases
- **Materialize every allowed value:** random indexing is simple afterward, but initialization and memory take $O(n)$, which violates the large-domain requirement.
- **Rejection sampling:** repeatedly draw from `[0, n)` until the value is allowed; it is unbiased but can become arbitrarily slow when most values are blacklisted.
- **Sorted blacklist plus rank adjustment:** binary-search how many blocked values precede a candidate; it can achieve $O(\log b)$ per pick without a remap.
- An empty blacklist makes every raw draw map to itself.
- Blacklisted values at or above `bound` need no map entry because raw draws never select them directly.
- The remap must skip high values that are also blacklisted.
- Duplicate blacklist entries are excluded by the problem contract.
