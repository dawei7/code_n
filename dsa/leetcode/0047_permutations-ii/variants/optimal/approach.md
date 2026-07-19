## General
**Sort equal values so interchangeable choices are adjacent**

Sort `nums`, keep a `used` flag for each source position, and build a path. At each depth, consider every unused position. Skip index `i` when it has the same value as $i - 1$ and the earlier equal position is not already used in the current path.

That final condition is subtle. If the earlier equal copy is unused, choosing the later copy would start a sibling branch indistinguishable from the branch that chooses the earlier one. If the earlier copy is already used, choosing the later copy is necessary to permit repeated values within one permutation. Thus equal copies are selected in source order without being globally deduplicated.

**Canonical source-index order removes only duplicate branches**

The path contains exactly the positions marked used. For each group of equal values, chosen indices form an initial segment among copies available at the same decision level. Therefore no two branches differ only by exchanging indistinguishable positions.

**Trace distinguishable indices for indistinguishable values**

For sorted `[1a, 1b, 2]`, the root may choose `1a` or 2, but not `1b` while `1a` is unused. After choosing `1a`, choosing `1b` is allowed, producing `[1, 1, 2]`; other placements yield `[1, 2, 1]` and `[2, 1, 1]` once each.

**Equal copies use one canonical source order**

Every leaf uses each source position once, so it represents a valid permutation. For any desired value ordering, assign occurrences of each equal value to their sorted source copies from left to right. This canonical assignment represents the ordering without changing its visible values.

The skip rule permits an equal copy only after the preceding copy has already been used on the current path, exactly enforcing that canonical source order. Every unique value permutation retains one path, while paths differing only by exchanging indistinguishable copies are suppressed.

## Complexity detail
There are at most $n!$ unique outputs and copying each costs $O(n)$, yielding the same loose $O(n \cdot n!)$ output bound as distinct permutations; duplicates reduce actual leaves. The path, flags, and recursion use $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Generate all index permutations then use a set:** performs $n!$ work even when all values are equal and stores duplicate candidates.
- **Frequency-map recursion:** branches over distinct values and is also efficient, but requires maintaining counts rather than positional flags.
- **Swap recursion with a per-depth seen set:** correctly skips equal choices and offers a comparable invariant with extra temporary sets.
- If all values are equal, only one root-to-leaf path survives even though there are $n!$ positional permutations.
- Sorting changes exploration order but not the multiset of returned permutations. Copy each completed path before backtracking.
