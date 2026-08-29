## General

**“Duplicate” means remove every occurrence of a repeated value.** This problem differs from the common operation that keeps one copy. If a value appears two or more times anywhere in the unsorted list, none of its nodes may remain. A node can therefore be judged only after the algorithm knows the value’s frequency in the entire list. That need for global information motivates two passes.

**First pass: count every value.** `cnt = Counter()` starts an empty frequency map. Pointer `cur` walks from `head` to the end. For each node, `cnt[cur.val] += 1` records one more occurrence, then `cur = cur.next` advances.

After this pass, `cnt[v]` equals the total number of nodes whose value is `v`. The list is unsorted, but order is irrelevant to counting. A repeated value can appear in adjacent nodes or at opposite ends and receives the same correct total.

The first pass deliberately makes no pointer changes. Removing a value as soon as its second copy is discovered would be awkward because an earlier copy might already have been passed. Counting first separates discovery from modification and makes every later keep-or-delete decision constant time.

**Use a dummy node so deleting the head is ordinary.** The second pass creates `dummy = ListNode(0, head)`. Its value zero has no semantic role; only its `next` pointer matters. `pre` starts at this dummy, and `cur` starts at the original head.

Without a dummy, deleting the first node would require assigning a new head, and deleting several leading nodes would need repeated special handling. With the dummy, even the original head has a predecessor. Removing it is the same pointer update used anywhere else: `pre.next = cur.next`. The returned head is always `dummy.next`, whether it still points to the original head, a later surviving node, or `None`.

**Second pass: keep only frequency-one nodes.** At each node, the code inspects `cnt[cur.val]`.

- If the count is greater than one, every node with that value must disappear. The assignment `pre.next = cur.next` bypasses `cur`. Importantly, `pre` does not advance, because it must remain the last retained node and may need to bypass another repeated node immediately afterward.
- If the count is exactly one, the node belongs in the result. The code advances `pre = cur`, making this retained node the new tail of the filtered prefix.

In either case, `cur = cur.next` moves to the next original node. Even after `pre.next` bypasses `cur`, the removed node’s own `next` field still points to that next node, so traversal proceeds safely.

**Trace a list with separated duplicates.** For `[3, 2, 2, 1, 3, 2, 4]`, the first pass records counts three maps to two, two maps to three, one maps to one, and four maps to one.

- The first node three is bypassed because its count is two. `pre` remains the dummy.
- Both following two nodes are bypassed for count three. `pre` still remains the dummy.
- Node one has count one, so it is retained and `pre` advances to it.
- The later three and two are bypassed by changing node one’s `next` each time.
- Node four has count one, so it is retained after node one.

The returned chain is `[1, 4]`. The algorithm never needs to search backward for the earlier copies because the count map already labels every occurrence.

For `[2, 1, 1, 2]`, both values have count two. Every original node is bypassed while `pre` stays at the dummy. Eventually `dummy.next` becomes `None`, correctly returning an empty list.

**The filtered prefix invariant.** Before each second-pass iteration, the chain from `dummy.next` through `pre` contains exactly the frequency-one nodes that appeared before `cur`, in their original relative order. If `cur` is repeated, bypassing it leaves that chain unchanged and reconnects it to the unprocessed suffix. If `cur` is unique, leaving the link intact and advancing `pre` extends the filtered chain by exactly the next desired node. The invariant therefore holds throughout the traversal.

At termination, there is no unprocessed suffix. The chain beginning at `dummy.next` consists of all and only values with total frequency one, and their order matches the input because nodes were never rearranged. This proves the returned list is correct.

**The operation is in place with respect to list nodes.** The method allocates one dummy node and a frequency map, but it does not allocate replacement nodes for survivors. It rewires `next` pointers in the original list. A caller retaining references to original nodes may observe those link changes. Removed nodes are merely disconnected from the returned chain; Python’s memory management handles reclamation when no references remain.

**Why one pass with a seen set is insufficient.** A seen set can identify the second occurrence, but the first occurrence may already be part of the retained prefix. Removing that earlier node from a singly linked list would require additional predecessor tracking by value or another cleanup pass. Frequencies make the second pass uniform and easy to verify.

## Complexity detail

Let `n` be the number of nodes and `u` the number of distinct values. The first pass visits `n` nodes, and the second pass visits `n` nodes again. Counter updates and lookups take expected `O(1)` time, so total expected time is `O(n)`.

The counter stores `u` entries, giving `O(u)` auxiliary space and `O(n)` in the worst case when every node has a different value. The dummy node and pointer variables use `O(1)` additional space. The surviving linked list reuses input nodes and is not counted as newly allocated output storage.

## Alternatives and edge cases

- **Recursive filtering after counting:** Recursion can rebuild links while unwinding, but a list of 100,000 nodes risks exceeding Python’s recursion limit and adds `O(n)` call-stack space.
- **One-pass predecessor map:** Tracking the first node and predecessor for every value can support later removal, but pointer updates become much more complicated than the clean two-pass method.
- **Repeated scans without a map:** Counting a node’s value by scanning the whole list yields `O(n^2)` time.
- **All values unique:** Every count is one, no link is changed, and the original head is returned.
- **All values repeated:** Every node is bypassed and `dummy.next` becomes `None`.
- **Repeated values at the head:** The dummy node lets any number of leading nodes be deleted without a special head branch.
- **Repeated values at the tail:** The last retained node’s `next` is set to `None` as the tail duplicates are bypassed.
- **Consecutive duplicate nodes:** `pre` intentionally stays fixed during deletions, allowing one retained predecessor to bypass the entire run.
- **Nonconsecutive duplicates:** Global counts mark every occurrence even when copies are far apart.
- **Single-node list:** Its count is one, so the node is retained.
- **Stable order:** The method only bypasses nodes and never swaps them, so surviving unique values keep their original order.
- **Input mutation:** Original `next` pointers are modified. Callers needing an untouched list would have to construct a separate result list.
