## General
**Stay on a representative until its entire run is collapsed**

Walk with `current`, the retained representative of its sorted run. When its successor has the same value, bypass that successor with `current.next = current.next.next` and keep `current` in place because another duplicate may follow. Advance only when the successor begins a new value run.

**Sorted adjacency makes one comparison sufficient**

Before each comparison, the chain through `current` contains exactly one node for every distinct processed value, and `current` is the retained representative of its run. Because equal values are contiguous, a different successor proves the current run is complete.

**Trace staying on a run representative**

For `[1,1,2,3,3]`, bypass the second 1 while staying on the first. Advance to 2 and then 3; bypass the second 3. The remaining chain is `[1,2,3]`.

**Staying on the representative collapses an entire run**

Sorted order places every duplicate immediately after another node of the same run. While `current.next` matches, bypassing it removes one redundant occurrence and keeping `current` in place permits the next copy to be checked against the same representative.

A different successor begins a new value run and must be retained, so only then does `current` advance. Repeating this rule across all runs leaves their first nodes linked in sorted order and removes every later copy.

## Complexity detail
Each node is examined or bypassed once, for $O(n)$ time. One traversal pointer uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Copy distinct values into new nodes:** uses $O(n)$ extra space and discards reusable nodes.
- **Hash-set filtering:** ignores sorted adjacency and spends unnecessary memory.
- **Recursive deduplication:** is correct but uses $O(n)$ stack space.
- Empty and one-node lists require no link change. A run of any length retains its first node and bypasses all later copies.
- Nodes are reused and their values are not modified; only redundant links are bypassed.
