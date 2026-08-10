## General

**Exploit the smallest-head property**

Because both input chains are sorted in non-decreasing order, the smallest unmerged node must be one of the two current heads. A node deeper in `l1` cannot be smaller than `l1`, and the same is true for `l2`. The competitive implementation repeatedly compares only those two heads, attaches the smaller one to the result tail, and advances that input.

This is the linked-list version of the merge operation used by merge sort. It never searches backward and never needs to sort the combined values again.

**Anchor the output with a dummy node**

The source initializes

```python
curr = dummy = ListNode(0)
```

Both variables initially reference the same new node. `dummy` remains fixed so the method can later return `dummy.next`, while `curr` moves and always identifies the final node of the merged prefix.

The dummy's value `0` is irrelevant. It is not compared with either list and is not part of the returned chain. Its purpose is to eliminate a first-node special case: every selected real node can be assigned to `curr.next`, even when the merged prefix is currently empty.

**Maintain a merged-prefix invariant**

At the start of each loop iteration:

- nodes from `dummy.next` through `curr` form a non-decreasing merged prefix;
- that prefix contains exactly the input nodes already consumed;
- `l1` and `l2` point to the first unconsumed nodes of their respective lists; and
- every value in the prefix is no greater than either available current head.

The invariant holds initially because the merged prefix contains no real nodes and both heads are unconsumed.

While both heads exist, the code chooses one. If `l1.val < l2.val`, then `l1` is the smallest unconsumed node. The code attaches it with `curr.next = l1` and advances `l1 = l1.next`. Otherwise it performs the symmetric operations for `l2`. In either branch, the chosen node is removed from one unconsumed suffix and added exactly once to the merged prefix.

After the branch,

```python
curr = curr.next
```

moves the tail pointer onto the node just attached. This step is essential. Without it, the next iteration would overwrite the dummy's or previous tail's `next` link instead of extending the result.

**Tie handling deliberately selects list 2**

The comparison uses `<`, not `<=`. Therefore equal head values enter the `else` branch and attach the node from `l2` first. This differs from the recursive Optimal source, which gives list 1 priority on equality.

Both choices satisfy non-decreasing value order because equal values are interchangeable for the problem's output. The unchosen equal node remains at its head and will be considered again. Thus duplicates are preserved, not removed. The distinction matters only if a caller tracks the identities of equal-valued nodes, which the required value output does not expose.

**Attach the remaining suffix all at once**

The main loop stops as soon as `l1` or `l2` becomes `None`. At that moment, at most one input suffix remains. The source executes

```python
curr.next = l1 or l2
```

Python returns the non-`None` node operand, or `None` if both are exhausted. There is no need to attach the surviving suffix node by node. It is already sorted, and its current head is no smaller than the last node placed into the prefix; otherwise that head would have been selected earlier. Connecting the entire suffix therefore preserves sortedness.

This optimization does not change the complexity class, but it avoids needless pointer updates once only one list remains.

**Trace `[1, 2, 4]` with `[1, 3, 4]`**

The first head values tie, so the `<` condition is false and the second list's `1` is attached. Then the first list's `1` is smaller than `3` and is attached, followed by `2`, then `3`. The `4` values tie, so the second list's `4` is selected. `l2` becomes empty, the loop stops, and the first list's remaining `4` is attached as a whole suffix.

Following `dummy.next` now gives `[1, 1, 2, 3, 4, 4]`. The dummy itself is excluded from the return.

**Why the method is complete and sorted**

In each iteration, sorted inputs guarantee that the smaller current head is the smallest node remaining anywhere. Attaching it after the already sorted prefix therefore preserves non-decreasing order. Advancing only the selected list preserves every unselected node for a later decision.

The loop consumes one node per iteration, so it makes progress and eventually exhausts a list. At that point, the suffix-attachment argument shows that all remaining nodes can follow the prefix unchanged. Every original node is either chosen during an iteration or belongs to that final suffix, and no node enters both categories. Hence the result contains every input node exactly once in sorted order.

**Splicing changes the original chains**

Assignments to `curr.next` reuse and redirect original nodes. The method does not allocate output nodes beyond the dummy. Consequently, references to the original heads may now traverse through nodes formerly belonging to the other list. This mutation is intentional because the problem requests a merge made by splicing nodes.

The implementation assumes the normal contract of separate, acyclic input lists. If the lists shared a suffix, treating the shared node as two independent unconsumed nodes could create incorrect aliasing; such inputs are outside the problem.

## Complexity detail

Let $m$ and $n$ denote the initial lengths of `l1` and `l2`.

- **Time complexity: $O(m+n)$.** Each loop iteration advances exactly one input pointer and the output tail. No node can be consumed twice. The final suffix attachment is $O(1)$, so total work is bounded by the combined node count.
- **Auxiliary space: $O(1)$.** The algorithm allocates one dummy node and stores a constant number of references. It uses no recursion, array, hash table, or newly copied output chain. The returned structure consists of the original nodes, so it is not counted as auxiliary allocation.

Although the source comment writes $O(n)$ time using one symbol for total input size, the manifest's $O(m+n)$ makes the two list lengths explicit; the claims are equivalent when $n$ in the comment denotes their combined size.

## Alternatives and edge cases

- **Recursive head selection:** It mirrors the mathematical recurrence elegantly, but the exact Python recursion uses up to $O(m+n)$ stack space and may encounter recursion limits on large lists.
- **Allocate copied nodes:** This avoids mutating either input but requires $O(m+n)$ additional node storage.
- **Flatten, sort, and rebuild:** It wastes the already-sorted property, increasing time to $O((m+n)\log(m+n))$ and memory to $O(m+n)$.
- **Both lists empty:** The loop is skipped, `l1 or l2` is `None`, and `dummy.next` is returned as `None`.
- **One list empty initially:** The loop is skipped and the non-empty chain is attached directly to the dummy.
- **Equal heads:** The source chooses `l2` first because its condition is strict `<`; both equal nodes still appear.
- **All nodes of one list precede the other:** The earlier list is consumed, then the later list is connected in one assignment.
- **Interleaved values:** The invariant chooses one node per comparison and handles arbitrary alternation between lists.
- **Negative and repeated values:** Ordinary numeric comparison is sufficient; neither sign nor uniqueness is assumed.
- **Dummy value:** `0` never enters the returned chain and need not be smaller than input values.
- **Use the returned head:** Since the merge rewires nodes and either input may contribute the first result node, callers should continue from `dummy.next`, the function's return value.
- **Unsupported cyclic or aliased lists:** The progress and exact-once arguments rely on ordinary finite, independent singly linked lists.
