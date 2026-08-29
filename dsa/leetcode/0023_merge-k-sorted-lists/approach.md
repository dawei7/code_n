## General

**Reduce a $k$-way choice to one heap minimum**

Each input list is sorted in ascending order. Among all nodes not yet placed in the output, the globally smallest value must be at the current head of one of the lists. A node deeper inside a list cannot be smaller than that list's head.

Scanning all $k$ current heads for every output node would cost $O(k)$ per selection. The selected implementation keeps the current candidates in a min-heap, which exposes a minimum in $O(1)$ and removes or inserts a candidate in $O(\log k)$.

**Teach `ListNode` how the heap should compare it**

Python's heap operations compare stored objects with `<`. The platform node class does not necessarily define that operation, so the source runs

```python
setattr(ListNode, "__lt__", lambda a, b: a.val < b.val)
```

This dynamically adds a less-than method to the `ListNode` class. Heap order is now based only on `val`. Equal values are allowed: neither equal node is less than the other, but either may be removed first because their output values are interchangeable. All duplicates remain in the heap and eventually appear in the result.

This line mutates the class globally for the rest of the Python process, not merely one node or one function call. It is convenient in the isolated judge environment, but a larger application may prefer heap tuples such as `(value, unique_counter, node)` to avoid changing shared class behavior.

**Seed one candidate per non-empty list**

The comprehension

```python
pq = [head for head in lists if head]
```

includes only non-`None` heads. Empty lists contribute no nodes and require no special handling later. `heapify(pq)` transforms these at most $k$ heads into a min-heap in $O(k)$ time.

The heap invariant is:

> For every input list that still has unmerged nodes, `pq` contains exactly its first unmerged node.

Initially that is precisely what the comprehension establishes. Keeping only one node per list is enough because sortedness guarantees that all later nodes in that list are no smaller than its candidate.

**Use a dummy node and a moving output tail**

The assignment

```python
dummy = cur = ListNode()
```

creates one artificial node. `dummy` stays fixed as an anchor; `cur` moves and denotes the final real node already attached. The dummy's value is irrelevant and it is excluded by returning `dummy.next`.

This avoids a separate branch for the first selected node. Every real node, including the first, is attached with `cur.next = node`.

**Pop one node and expose its successor**

Each loop iteration removes the heap minimum:

```python
node = heappop(pq)
```

By the candidate invariant, every unmerged node lies at or after one of the heap nodes. Since its list is sorted, it cannot be smaller than that candidate. The minimum heap candidate is consequently the minimum of all remaining nodes, so it is safe to append next.

If `node.next` exists, that successor becomes the first unmerged node of the same source list and is pushed into the heap. This replacement preserves exactly one candidate for that non-exhausted list. If there is no successor, the list is exhausted and contributes no replacement.

The source pushes the successor before linking `node` to the merged tail. At that moment, `node.next` still points to its original successor, so the reference is available. Then

```python
cur.next = node
cur = cur.next
```

adds the selected original node and advances the result tail.

**Why stale original links do not corrupt the result**

When a selected node has a successor, its old `next` link temporarily still points to that successor even though another list may supply the next global minimum. On the following iteration, `cur.next = node` overwrites that old link with the actually selected node. Thus the finalized portion through the previous tail is always correct.

When the heap finally empties, the last selected node must have no successor; otherwise a successor would have been pushed and the heap would not be empty. The final tail therefore already ends at `None`. No cleanup assignment is required.

**Trace the example candidates**

For `[[1,4,5], [1,3,4], [2,6]]`, the initial heap contains values `1`, `1`, and `2`. One `1` is removed, and its successor—either `4` or `3`, depending on which equal node the heap chose—is inserted. The other `1` is then removed. Next the heap minimum is `2`, followed by `3`, the two `4` nodes, `5`, and `6`.

The precise identity order of equal values is unspecified, but following `dummy.next` yields the required value sequence `[1,1,2,3,4,4,5,6]`.

**Why the result is complete and sorted**

Initially the heap has the first node of every non-empty list. Every iteration appends the smallest remaining node, so the merged prefix stays sorted. It then replaces that node with its successor when one exists, maintaining the candidate invariant. Each iteration removes exactly one original node from future consideration, so no node can be appended twice. A non-exhausted list always has a candidate, so the loop cannot end while any input node remains. The returned chain is therefore sorted and contains every input node exactly once.

The method splices original nodes. It rewrites `next` links and does not preserve the input lists as independent chains.

## Complexity detail

Let $k$ be the number of input lists and $N$ the total number of nodes across them.

- **Time complexity: $O(N\log k)$.** Heap construction is $O(k)$. Every one of the $N$ nodes is popped exactly once, and every node except a tail may cause one push. The heap never contains more than one candidate per list, so each operation costs $O(\log k)$. For $k=0$ or $k=1$, the practical work is linear or empty; the usual bound assumes $k\ge2$.
- **Auxiliary space: $O(k)$.** The heap contains at most one node reference per non-empty list. The dummy node and scalar references are constant space. The output reuses the $N$ input nodes and is not a copied allocation.

`setattr` adds one class-level function and does not scale with input size. Heap ties do not increase the bound.

## Alternatives and edge cases

- **Balanced pairwise merging:** Merge lists in pairs over $O(\log k)$ rounds. It also costs $O(N\log k)$ time and can use $O(1)$ auxiliary pointer space when the input array is reused.
- **Scan all heads:** Select the minimum by checking every active list for each node. This needs little extra storage but costs $O(Nk)$ time.
- **Flatten and sort values:** It costs $O(N\log N)$ time and $O(N)$ storage, and rebuilding nodes fails to exploit the existing chains as directly.
- **Sequentially merge into one accumulator:** Early nodes may be traversed repeatedly, producing $O(Nk)$ in an unfavorable distribution.
- **No lists:** The heap is empty and `dummy.next` remains `None`.
- **Only empty lists:** Filtering removes every head, producing the same empty result.
- **One non-empty list:** Its nodes are popped and pushed one by one; the output is the same chain, although a direct early return could avoid heap work.
- **Equal head values:** The injected `<` method leaves their relative order unspecified but retains both nodes and sorted values.
- **Negative values:** Heap comparison uses ordinary numeric ordering and needs no special case.
- **Class mutation:** Replacing `ListNode.__lt__` can affect other code using the class. A `(value, counter, node)` heap avoids that side effect and also supplies an explicit tie-breaker.
- **Input mutation:** Nodes are relinked into one chain; callers should treat the returned head as authoritative.
- **Aliased or cyclic lists:** The proof assumes independent finite acyclic inputs, as supplied by the problem. Shared nodes could be enqueued more than once and are outside the contract.
