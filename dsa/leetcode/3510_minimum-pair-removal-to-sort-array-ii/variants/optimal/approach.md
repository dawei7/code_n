## General

The operation sequence is deterministic, but directly rebuilding the current array would be too slow. Represent every surviving value by the original index of its leftmost constituent. `previous` and `following` arrays connect these active nodes as an implicit doubly linked list, so removing the right node of a chosen pair and reconnecting its neighbors takes constant time.

Put every adjacent pair in a min-heap as `(pair_sum, left, right)`. Original indices remain increasing along the linked list, even after merges. Therefore the `left` field orders current pairs from left to right and automatically implements the required tie rule after `pair_sum`.

A merge changes nearby sums, so old heap entries become stale. Rather than search for and delete them, validate each popped entry lazily: both nodes must still be active, `right` must still follow `left`, and their current values must still produce the stored sum. Discard entries that fail any check. After merging, push only the new pair with the preceding node and the new pair with the following node.

To detect when the current list is non-decreasing without another full scan, maintain `inversions`, the number of active links whose left value exceeds their right value. Before a merge, subtract the contributions of up to three disappearing links: `before -> left`, `left -> right`, and `right -> after`. After relinking and assigning the sum to `left`, add the contributions of the two possible new links. The sequence is non-decreasing exactly when this count reaches zero.

The linked-list invariant makes heap index order identical to current left-to-right order. Lazy validation ensures every accepted heap minimum is the required current pair, and the local inversion update preserves the exact number of descending links. Thus each simulated operation matches the contract, and stopping at zero inversions returns the first—and therefore minimum—valid operation count.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Initial arrays and heap construction take $O(n)$ time. There are at most $n-1$ merges. Each merge pushes at most two heap entries, so only $O(n)$ entries are ever created; every stale or valid entry is popped at most once. Heap operations take $O(\log n)$ each, giving $O(n\log n)$ total time.

The values, links, activity flags, and heap each contain $O(n)$ entries, so auxiliary space is $O(n)$. The benchmark uses decreasing negative arrays, which remain unsorted until all $n-1$ merges occur. It contrasts the linked heap with correct direct simulation that rescans and shifts the current list every round, taking $O(n^2)$ time.

## Alternatives and edge cases

- **Direct list simulation:** Scanning every pair and replacing a list slice is correct but quadratic over as many as $n-1$ operations.
- **Heap without stale validation:** Neighbor sums change after merges; accepting an obsolete entry can select a non-adjacent or nonminimum pair.
- **Track only inversion pairs in the heap:** The mandated minimum-sum pair need not be an inversion, so every adjacent pair must remain eligible.
- **Rescan for sortedness:** A full order check after each merge reintroduces quadratic work; the local inversion count gives constant-time termination updates.
- **Leftmost tie:** Heap keys use the surviving original left index after the sum, matching current list order.
- **Negative values:** Merging can decrease values and recreate a previously seen sum; adjacency, activity, and current-sum checks together remain valid.
- **Large merged values:** Up to $10^5$ values of magnitude $10^9$ can accumulate, so fixed-width implementations need 64-bit arithmetic.
- **Already non-decreasing or singleton:** The initial inversion count is zero, so the algorithm returns without popping the heap.
- **Input preservation:** Values are copied before merging because the contract does not require mutating `nums`.
