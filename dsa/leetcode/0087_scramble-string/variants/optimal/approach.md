## General
**Index intervals instead of allocating recursive substrings**

Represent a subproblem by `(start1, start2, length)`. Cache whether those equal-length intervals are scrambles so different higher-level split histories never recompute the same state. Indexing also avoids creating new substring objects at every recursive edge.

**Unequal character inventories prove failure before any split**

Build per-letter prefix counts for both strings. Interval counts are obtained by subtracting two prefix rows. Before trying splits, compare all 26 counts; recursive splitting and swapping never changes leaf characters, so different inventories prove immediate failure.

If the intervals are already character-for-character equal, return true without exploring alternative trees. Equal inventory alone is not sufficient, so a nonidentical pair must still test structural splits.

**Every root split has preserved and swapped orientations**

For every split position `cut` from `1` through `length - 1`, test two cases:

- **not swapped:** first left with second left, and first right with second right;
- **swapped:** first left with the second interval's length-`cut` suffix, and first right with its remaining prefix.

Both child pairs must succeed in either orientation. Stop at the first successful decomposition.

**A memo state asks exactly one recursive-tree equivalence question**

`scramble(a, b, length)` is true exactly when the specified intervals have recursive scramble trees with the same leaves. Every recursive call uses strictly shorter intervals, and memo entries record final answers for those interval pairs.

**Trace a swapped top-level child**

For `great` and `rgeat`, split after `gr`. The right children `eat` and `eat` are identical. The left pair `gr` and `rg` succeeds by splitting into $g | r$ and swapping the two one-character children. Combining those child results proves the full strings are scrambles.

**Every scramble tree begins with one tried root split**

Equal intervals require no further operations and form the base case. Any nontrivial scramble has a root partition at some position; its two children are either kept in order or swapped. The loop enumerates every split position and both arrangements, so it includes the root choice of every valid scramble tree.

Conversely, when both recursive child pairs succeed, joining their valid scramble trees under the tested kept-or-swapped root creates a permitted scramble of the full intervals. Memoized recursion therefore accepts exactly the states with a valid decomposition.

## Complexity detail
There are $O(n^3)$ interval-pair states and up to $O(n)$ split positions per state, giving $O(n^4)$ time with fixed-alphabet inventory checks. The cache stores $O(n^3)$ booleans, and recursion depth is $O(n)$.

## Alternatives and edge cases
- **Unmemoized recursion:** repeats interval states exponentially.
- **Bottom-up three-dimensional DP:** has the same asymptotic bounds but requires more indexing machinery.
- **Anagram equality alone:** is necessary but not sufficient; some equal-inventory strings have incompatible recursive split structure.
- One-character intervals succeed exactly when their characters match. Different full-string lengths fail immediately before interval recursion.
- Prefix counts rely on the lowercase alphabet constraint; a broader alphabet can use maps or compressed character indexing.
