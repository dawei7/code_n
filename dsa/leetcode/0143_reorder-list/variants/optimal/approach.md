## General
**Split so the front half keeps the middle node**

Move `slow` one edge and `fast` two until `slow` is the last node of the front half. For odd length, that half includes the middle node; for even length, both halves have equal size. Save `slow.next` as `second`, then set `slow.next = None` so the halves are disjoint. Detaching here prevents a stale link from forming a cycle during the later weave.

**Reverse the back half into the required tail order**

Reverse `second` with the standard `previous`, `following`, and current-node updates. The resulting chain begins with the original tail, followed by the original second-to-last node, exactly the order in which those nodes must be inserted.

**Weave one node from each disjoint chain**

Before changing links, save `first_next` and `second_next`. Connect the current front node to the current reversed-back node, connect that node to the saved front successor, and advance both pointers. Each iteration appends the next unused low-position node followed by the next unused high-position node, so the completed prefix always has the required order. The back half cannot be longer; when it is exhausted, an odd-length front half already leaves its middle node as the null-terminated tail.

Because the split partitions the original nodes, reversal preserves every node exactly once, and weaving consumes each half without allocating or changing values, the final list has precisely the requested identity order.

## Complexity detail
Midpoint discovery, reversal, and weaving each process at most $n$ nodes, giving $O(n)$ total time. A fixed number of node references uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Array of node references:** makes alternating endpoint access simple but uses $O(n)$ auxiliary space.
- **Repeatedly search for the current tail:** retains constant space but takes $O(n^2)$ time.
- **Create new nodes or exchange values:** violates the in-place node-identity contract.
- One- and two-node legal inputs retain their existing order.
- The implementation also safely returns for a null app-local head, although the source contract is nonempty.
- Detaching the halves before reversal is essential to avoid stale links and cycles.
