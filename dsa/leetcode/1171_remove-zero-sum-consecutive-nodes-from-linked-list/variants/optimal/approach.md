## General
**Translate zero-sum ranges into repeated prefix sums.** Place a dummy node of value zero before `head`. Let the prefix sum at a node include all values from the dummy through that node. If two nodes have the same prefix sum, every node strictly between them has total zero and may be bypassed.

**Remember the last node for every prefix sum.** Traverse from the dummy to the tail while mapping each prefix sum to its latest occurrence. Choosing the last occurrence is important: when a prefix sum repeats several times, jumping after its final occurrence removes the longest intervening zero-sum region. That single jump also accounts for removals that would otherwise expose further removable regions.

**Rebuild the surviving links.** Start a second traversal from the dummy and recompute the same prefix sums. At each current node, set `current.next` to `last[prefix].next`. The mapped node has the same prefix sum as `current`, so every skipped value sums to zero. If it is the current node itself, the link remains unchanged. Advance along the updated link and repeat. Every retained adjacent pair has no later equal-prefix occurrence between it, so no zero-sum consecutive sequence remains.

## Complexity detail
Each of the two traversals visits at most $n+1$ nodes, giving $O(n)$ time. The map stores at most one node per distinct prefix sum, so it uses $O(n)$ auxiliary space. Link updates reuse the original list nodes.

## Alternatives and edge cases
- **Repeatedly scan for one zero-sum sequence:** Removing the first range found and restarting is valid, but repeated full scans can take $O(n^2)$ time.
- **Check every start and end pair:** Prefix sums can identify a removable range for each pair, but enumerating all pairs is also $O(n^2)$.
- **Entire list sums to zero:** The dummy and tail share a prefix sum, so the dummy link jumps to `None`.
- **Zero-valued nodes:** A zero repeats the preceding prefix sum and is removed like any longer zero-sum sequence.
- **Overlapping choices:** Different valid deletion orders can produce different accepted lists; using the last prefix occurrence deterministically removes the longest available region.
- **No removable sequence:** Every stored prefix occurrence used by the second pass is the current node, so all original links are preserved.
