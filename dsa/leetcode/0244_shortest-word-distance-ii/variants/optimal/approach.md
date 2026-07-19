## General
**Preprocess once for repeated queries**

Map each word to its increasing list of positions during one preprocessing pass.

**Merge the two sorted occurrence lists**

Use two pointers. Compare current positions, update the minimum, and advance the pointer at the smaller position because keeping it cannot improve a future distance against a larger opposing position.

Before each pointer step, every pair involving a discarded position has already been compared with its closest possible opposing position encountered so far, and the running minimum covers all such pairs.

**Advancing the smaller position cannot hide a better pair**

Suppose the current positions are $a < b$. Keeping `a` while advancing the other list can only produce positions at least as large as `b`, so every future distance from `a` is at least $b - a$. After recording that distance, `a` can be discarded safely. The symmetric argument applies when $b < a$, so the merge cannot skip the optimal cross-list pair.

## Complexity detail
Index construction is $O(n)$. A query is linear in the two occurrence-list lengths and at most $O(n)$, so `q` queries cost $O(n+qn)$ in the worst case. All stored positions use $O(n)$ space.

## Alternatives and edge cases
- **Rescan the entire dictionary per query:** uses no index but repeats $O(n)$ work regardless of occurrence frequency.
- **Compare all occurrence pairs:** can be quadratic per query.
- A word may appear many times; every query word is guaranteed present.
