## General

The array must support both aggregate queries and changes to element order. A fixed-index segment tree can handle updates and XOR, but reversing a range would move many values. Instead, represent the current sequence with an implicit treap: in-order position supplies the key, while a pseudo-random priority keeps the tree balanced in expectation.

Each node stores its subtree size and subtree XOR. These summaries make a split by the first $c$ sequence elements and a merge of adjacent sequences take expected $O(\log n)$ time. Splitting before `left` and after `right` isolates any inclusive range. Its stored XOR answers a type-2 query; changing the isolated single node handles a point update.

For reversal, swap the isolated subtree's children and toggle a lazy flag. XOR is independent of order, so its aggregate remains valid. Before a later split or merge descends through that node, push the flag to both children, applying the same swap-and-toggle operation. Thus the tree's in-order traversal always represents the logical array whenever structure is inspected, without visiting every reversed element.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$ and $q = \lvert\texttt{queries}\rvert$. With pseudo-random priorities, the treap height is $O(\log n)$ in expectation. Construction by successive merges costs $O(n \log n)$ expected time, and every update, range XOR, or reversal uses a constant number of splits and merges for $O(\log n)$ expected time. Total time is $O((n + q) \log n)$ expected, and the $n$ nodes use $O(n)$ space.

## Alternatives and edge cases

- **Mutable list simulation:** Slicing can reverse a range conveniently, but a long reversal or XOR scan costs $O(n)$ and leads to $O(nq)$ worst-case time.
- **Fixed segment tree:** It supports point updates and XOR queries, but arbitrary subarray reversal is not a simple fixed-index lazy operation because positions cross many node boundaries.
- **Lazy propagation:** A reversal must swap children immediately and pass the pending flag downward before any structural descent.
- **Single-element ranges:** Updating, querying, or reversing one position is valid; reversal leaves the sequence unchanged.
- **Repeated reversals:** Two pending reversals cancel because the lazy flag is toggled rather than assigned unconditionally.
- **Zero values:** Zero is a normal XOR operand and does not require special handling.
