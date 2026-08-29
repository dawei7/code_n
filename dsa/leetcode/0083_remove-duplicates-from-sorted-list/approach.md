## General

**Sorted order turns duplicate removal into neighbor comparison**

Because the linked list is sorted in ascending order, all nodes with the same value appear consecutively. To know whether the next node is a duplicate that should be removed, the algorithm only needs to compare `cur.val` with `cur.next.val`. No frequency map or lookahead across unrelated values is needed.

The goal here is to retain one node from every equal-value run. `cur` points to the retained representative of the run currently being processed. Duplicate successors are bypassed, while a different successor becomes the representative of the next run.

**Bypass one duplicate without moving the representative**

When `cur.val == cur.next.val`, the next node is an extra copy. The assignment `cur.next = cur.next.next` changes the current retained node's link so it skips that duplicate and points to the following node.

`cur` deliberately does not advance in this branch. The newly exposed `cur.next` may have the same value again. For a run such as `1 -> 1 -> 1 -> 2`, the first iteration skips the second node, and the next iteration compares the retained first node with the third. Holding `cur` in place removes an arbitrarily long run down to one node.

The bypassed node may still point to its old successor internally, but it is no longer reachable from `head`, so it is deleted from the returned list's structure.

**Advance only after reaching a new value**

If `cur.val != cur.next.val`, sorted order proves the next node starts a different run. It cannot equal any earlier retained value because values never decrease and the immediate predecessor already differs. The source advances `cur = cur.next` so this new node becomes the representative for the next run.

No pointer rewrite is needed in this branch. The existing link already preserves the correct relative order between distinct values.

The asymmetry between the branches is crucial: advance after a distinct value, but recheck after deleting a duplicate. Advancing in both branches would leave every other duplicate in a long run.

**The loop guard protects both needed nodes**

The comparison requires both `cur` and `cur.next`. The condition `while cur and cur.next` handles an empty list, a one-node list, and arrival at the final node without special code inside the loop.

For an empty list, `cur` is `None` and short-circuit evaluation never accesses `.next`. For a one-node list, `cur.next` is `None`, so the node is returned unchanged. For a longer list, termination with `cur.next == None` means the final retained representative has no remaining successor to classify.

**Trace a run followed by another run**

For `1 -> 1 -> 2 -> 3 -> 3`, `cur` starts at the first 1. Equality with the next node causes a bypass, leaving `1 -> 2 -> 3 -> 3`. The next comparison differs, so `cur` advances to 2. It differs from 3, so `cur` advances again. At the first 3, equality bypasses the final 3. The returned chain is `1 -> 2 -> 3`.

Notice that the first node of each run is the one retained. The contract cares about values, not node identity, but reusing these existing representatives achieves the result without allocation.

**A loop invariant**

At the start of each iteration, every node reachable from `head` before and including `cur` has a distinct value relative to its retained predecessor, and `cur` is the one retained representative of its current value among nodes examined so far.

If the next node is equal, bypassing it leaves the retained prefix unchanged and exposes the next unclassified node. If it is different, advancing adds a value that sorted order guarantees is distinct from all earlier retained values. Thus each branch preserves the invariant.

When the loop ends, there is no unclassified successor after `cur`, or the list was empty. Every original run has been reduced to its first node, and their sorted order is unchanged. Returning the original `head` is correct because this problem never removes the first representative of any run; even a duplicated head value keeps its first head node.

**Difference from removing all repeated values**

For `[1,1,2]`, this method returns `[1,2]`. The related “Sorted List II” problem would delete both ones and return `[2]`. Here equality means “remove the next extra copy,” not “remove the complete run.” Keeping this contract distinction prevents an otherwise common sentinel-based over-deletion.

## Complexity detail

Let $n$ be the number of nodes. Every iteration either bypasses one node or advances `cur` to one node. No pointer moves backward, so at most a constant amount of work is charged to each original node. Total time is $O(n)$, matching the manifest.

The source stores one pointer and rewires existing `next` links. It allocates no dummy, collection, or recursion frames, so auxiliary space is $O(1)$, also matching the manifest.

## Alternatives and edge cases

- **Runner per run:** Move a second pointer past all equal successors and link the representative directly to the next distinct node. It performs one rewrite per run and is the competitive variant's style.
- **Recursive processing:** Deduplicate the suffix and reconnect it, but recursion uses $O(n)$ stack space in the worst case.
- **Frequency map:** It is unnecessary for sorted input and uses extra storage.
- **Empty list:** The guard fails immediately and `None` is returned.
- **One node:** It is already one representative and remains unchanged.
- **All nodes equal:** Repeated bypasses keep only the original head.
- **Duplicates at the tail:** `cur.next` eventually becomes `None`, correctly terminating the retained node.
- **Several distinct runs:** `cur` advances once between runs and stays fixed within duplicate removal.
- **Negative values:** Equality and sorted adjacency work independently of sign.
- **Head stability:** The first node is never removed, so returning the original head reference is correct.
- **Do not advance after deletion:** The exposed successor may still be an equal duplicate.
- **Sorted-order dependency:** Neighbor equality captures total duplication only because equal values are contiguous.
- **Input mutation:** The returned list reuses original nodes and intentionally changes links.
