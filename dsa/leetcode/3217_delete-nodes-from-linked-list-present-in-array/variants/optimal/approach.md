## General

**Make deletion membership fast.** For each linked-list node, the algorithm must decide whether its value appears in `nums`. Searching the whole array for every node would cost $O(mn)$ in the worst case. `s = set(nums)` preprocesses the deletion values so each membership test is expected $O(1)$.

The input guarantees unique values in `nums`, but the set would also remove duplicates automatically. Only membership matters.

**Use a dummy predecessor to unify head and interior deletion.** Removing the original head is awkward if code stores only a pointer to that node, because the returned head may need to change repeatedly. The source creates

`dummy = ListNode(next=head)`

and sets `pre` to this dummy. Every real node, including the original head, now has a predecessor whose `next` link can be rewritten. The final head is always `dummy.next`.

**Inspect the node after `pre`.** The loop continues while `pre.next` exists. There are two cases:

- If `pre.next.val in s`, that node must be removed. Assigning `pre.next = pre.next.next` bypasses it.
- Otherwise, the node must remain. Move `pre = pre.next` so it becomes the confirmed tail of the retained prefix.

The pointer does not advance after a deletion. This is essential for consecutive removable nodes: the predecessor's new next node must be tested before moving forward.

**A precise traversal invariant.** Before each iteration:

1. every original node before `pre.next` has been processed;
2. the chain from `dummy.next` through `pre` contains exactly the processed nodes whose values are not in `s`;
3. `pre.next` is the first unprocessed node.

If the next node should be deleted, bypassing it preserves the retained chain and exposes the following unprocessed node. If it should stay, moving `pre` incorporates it into the retained prefix. The invariant therefore advances in both cases.

When `pre.next` becomes null, every original node has been processed and the chain after `dummy` contains exactly the required survivors. Returning `dummy.next` is correct.

**Why no node is skipped.** A retained node is checked once and then becomes `pre`. A deleted node is checked once and detached, while `pre` stays fixed. Even a long run of deletions is processed one by one through the same predecessor link. Pointer rewiring never jumps over an unchecked retained candidate.

**Trace consecutive head removals.** With `nums=[1,2,3]` and list `1 -> 2 -> 3 -> 4 -> 5`, `pre` begins at the dummy. Its next value one is removed, leaving dummy next at two. The pointer remains at dummy and similarly removes two and three. Value four is retained, so `pre` moves to it, then to five. Returning dummy next yields `4 -> 5`.

For `nums=[1]` and `1 -> 2 -> 1 -> 2 -> 1 -> 2`, each removed one is bypassed while its predecessor stays, and each two advances the predecessor. The resulting links connect the three original two-nodes in order.

**The operation reuses nodes.** No replacement list is constructed. Surviving nodes keep their identity, value, and relative order; only `next` pointers are changed. In Python, detached nodes become eligible for garbage collection when no external references remain. The method does not explicitly free memory.

The problem guarantees at least one node survives, but the dummy technique would also return `None` correctly if every node were removed.

## Complexity detail

Let $m$ be `len(nums)` and $n$ the number of linked-list nodes. Building the set takes $O(m)$ expected time. The traversal processes each node once, and each set lookup is expected $O(1)$, for $O(n)$ expected time. Total expected time is $O(m+n)$.

The set stores up to $m$ values, so auxiliary space is $O(m)$. The dummy node and pointers use $O(1)$ additional space. No recursion or output-sized replacement list is used.

Hash-set bounds are expected rather than worst-case adversarial bounds. Ordinary Python integer hashes provide the intended behavior here.

## Alternatives and edge cases

- **Remove leading nodes separately:** Advance `head` while it should be deleted, then process interior links. It works, but the dummy node eliminates this special case.
- **Build a new linked list:** Copy every retained value into new nodes. This preserves the original list but uses $O(n)$ additional memory and loses node identity.
- **Search `nums` linearly per node:** It uses constant extra space but can take $O(mn)$ time.
- **Boolean lookup array:** Values are bounded by $10^5$, so a Boolean table works in $O(m+n)$ time with $O(10^5)$ space. A set scales with actual input size.
- **Original head removed:** Dummy next is updated just like any interior link.
- **Several removable nodes in a row:** `pre` must not advance after unlinking one.
- **No matching values:** Every node is retained, and the original chain is returned through dummy next.
- **All nodes removable outside the guarantee:** The loop leaves `dummy.next = None` and returns null safely.
- **Repeated node values:** Every occurrence whose value belongs to the set is removed.
- **Unique `nums` values:** This guarantee is not required for correctness because set construction deduplicates automatically.
- **At least one survivor:** The official guarantee means the returned head is non-null, although the implementation is more general.
- **Relative order:** Only deletions occur; surviving nodes never change order.
- **Caller-visible mutation:** The original list's links are modified in place. External references to retained or removed nodes may observe changed connectivity.
- **Platform node type:** `ListNode` is supplied by the execution environment; the solution only instantiates one dummy node.
