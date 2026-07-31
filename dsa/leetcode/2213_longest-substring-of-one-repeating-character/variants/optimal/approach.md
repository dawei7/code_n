## General

**Store exactly what a merge needs**

For each segment-tree node, store its length, boundary characters, longest equal-character prefix and suffix, and longest run anywhere inside. A leaf has length, prefix, suffix, and best value one; padded leaves outside the string are empty identities.

When merging children, the best run is initially the larger child best. If the left child's right character equals the right child's left character, their suffix and prefix join, creating another candidate. The merged prefix extends into the right child only when the entire left child is one equal run; the suffix follows the symmetric rule.

**Repair one root path per query**

A replacement changes one leaf. Recompute its ancestors with the same merge until reaching the root, whose best field is the required answer.

The node fields describe all possible locations of an optimal run: wholly inside either child or crossing their boundary. The merge evaluates exactly those cases and extends boundary runs precisely when continuity permits. Induction from leaves therefore proves every node summary correct. Updating all and only the ancestors of the changed leaf restores that invariant globally.

## Complexity detail

Let $n$ be the initial string length and $q$ the query count. Building the tree takes $O(n)$ time. Each point update repairs $O(\log n)$ nodes, so total time is $O(n+q\log n)$.

The power-of-two segment tree uses $O(n)$ space.

## Alternatives and edge cases

- **Recompute every run:** Scanning the whole string after every update is simple but costs $O(nq)$ time.
- **Ordered run intervals:** Balanced ordered sets can split and merge affected runs in logarithmic time, but require more intricate bookkeeping.
- **No-op update:** Rewriting the same character still produces an answer; rebuilding its root path remains correct.
- **Bridge two runs:** One update can merge equal runs on both sides, so both prefix and suffix information is essential.
- **Split one run:** Changing an interior position can create two shorter runs; ancestor recomputation captures both.
- **Single character:** The root best remains one after every legal replacement.
