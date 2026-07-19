## General
**Binary-search a monotone length:** If a substring of length $L$ repeats, then its prefix of every smaller length also repeats at the same starting positions. Therefore feasibility changes only once as $L$ increases, allowing binary search from zero through $N-1$.

**Hash every fixed-length window:** Precompute powers and prefix hashes for two independent moduli. A substring hash is then obtained in constant time from two prefix entries. For a candidate length, slide across all windows and group their paired hashes. A repeated pair is a strong candidate for equal substring contents.

**Confirm equality exactly:** Hashes are only filters. When a paired hash has appeared before, compare the current substring with the prior substring before declaring the length feasible. This preserves exact correctness even if a collision occurs. With ordinary hash behavior, each length check examines $O(N)$ windows, and binary search retains the largest feasible length.

If the check succeeds, two distinct starts contain equal substrings of the tested length. If it fails, every window has distinct contents, so no substring of that length repeats. Monotonicity then makes the final successful binary-search boundary exactly the requested maximum.

## Complexity detail
Prefix hashes and powers require $O(N)$ time and space. Binary search performs $O(\log N)$ checks, each scanning $O(N)$ windows, for expected $O(N\log N)$ time and $O(N)$ auxiliary space. Exact comparisons occur only for matching paired hashes; pathological deliberate collisions could increase the worst-case time, but they cannot change the answer.

## Alternatives and edge cases
- **Dynamic programming on suffix pairs:** Track the common suffix length for every pair of ending positions. It is collision-free and simple but costs $O(N^2)$ time and $O(N)$ optimized space.
- **Suffix array plus longest-common-prefix scan:** It is deterministic and can achieve efficient bounds, but its construction is substantially more involved.
- **Store sliced substrings in a set:** It simplifies the feasibility check, but creating each length-$L$ slice costs $O(L)$ and can make a nominal binary search quadratic.
- **Overlapping occurrences:** They are valid; only the starting positions must differ. For example, `"aaaaa"` has a repeated substring of length four.
- **Single-character string:** No non-empty substring can have two starts, so return `0`.
- **All unique characters:** Every positive length is infeasible, leaving the binary-search result at zero.
- **Several longest substrings:** Only their common maximum length is returned, not a particular substring.
