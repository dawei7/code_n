## General

**Use one dummy and one tail per partition**

`dummySmaller` begins the chain for nodes with values below `x`, and `dummyGreater` begins the chain for nodes with values at least `x`. `smaller` and `greater` always point to the current tails of those chains.

The dummy value `-1` has no semantic role. It is not compared with `x` and is excluded from the returned list. Dummies solve the structural problem of adding the first node to an initially empty chain: every append can assign through an existing tail's `next` field.

The module-level `ListNode` definition supplies the linked-list structure; the algorithm's additional per-call nodes are only the two dummies.

**Classify each original node exactly once**

The scan checks `head.val < x`. A true result appends the node through `smaller.next` and advances `smaller`. A false result includes both equality and greater values, appending through `greater.next` and advancing `greater`.

The two conditions are exhaustive and disjoint, so every input node enters exactly one output chain. The scan never changes a node's value and never creates a replacement node.

**Why tail appending is the stability mechanism**

Within each category, nodes arrive in original left-to-right order. Appending each arrival after the current category tail preserves that order automatically.

For example, if values 4, 3, and 5 all belong to the greater-or-equal side and appear in that order, their chain remains `4 -> 3 -> 5`. The problem does not ask to sort them numerically; it asks only to move the entire category after the smaller nodes.

This is why the solution needs both a head reference and a tail reference for each chain. A head alone would make efficient stable append awkward, while inserting at the head would reverse the order.

**Continue through original links before final cleanup**

After appending the current node, the code executes `head = head.next`. Its `next` still reflects the original list at that instant, letting traversal continue without a saved successor variable.

As a consequence, the two partial chains are not necessarily isolated during the scan. A current tail can still point to an unprocessed node that will later belong to the opposite category. These temporary links do not affect classification because traversal follows the original sequence, but they must be repaired before returning.

**Join the chains and cut the obsolete tail link**

`smaller.next = dummyGreater.next` connects the final smaller node—or the smaller dummy when that side is empty—to the first real greater-or-equal node.

`greater.next = None` then terminates the final list. In this source the join assignment happens first, so there may be a momentary stale path or cycle if the greater tail originally pointed into the smaller chain. No result is observed during that moment, and the immediately following termination removes it before return.

Ending the greater chain is not optional. If the original final greater-category node was followed by a smaller-category node, its old link is invalid after partitioning and could duplicate nodes or cycle back into the front chain.

Returning `dummySmaller.next` omits both dummies and yields the first real node of the concatenated result.

**Trace an alternating list**

For `2 -> 1 -> 4 -> 0` with `x = 2`, the smaller chain receives 1 then 0. The greater chain receives 2 then 4. Joining yields `1 -> 0 -> 2 -> 4`.

Within the smaller group, 1 still precedes 0. Within the greater group, 2 still precedes 4. The list is not globally numerically sorted, nor should it be; it is stably partitioned around the threshold.

**A correctness invariant**

After any number of iterations, the smaller dummy reaches exactly the processed nodes below `x` in encounter order, and the greater dummy reaches exactly the processed nodes at least `x` in encounter order. Their tail variables identify the last such nodes.

The next input node satisfies exactly one branch, and appending it extends only the appropriate ordered subsequence. Thus the invariant holds through the complete scan.

Joining the smaller subsequence before the greater subsequence establishes the partition property. Since each subsequence kept encounter order, stability holds. Terminating the greater tail guarantees an acyclic proper list containing no extra stale continuation.

**All empty-side combinations remain uniform**

If the smaller side is empty, `smaller` is `dummySmaller`, so its next pointer is assigned the greater head. If the greater side is empty, `dummyGreater.next` is `None`, and the smaller tail is linked to `None`; `greater` is the dummy and setting its next to `None` is harmless. Empty input returns `None` through the same logic.

## Complexity detail

Let $n$ be the input node count. Every iteration advances to one original successor and performs constant pointer work. Joining and termination are constant, so total time is $O(n)$, matching the manifest.

The method allocates two dummy nodes and stores four node references. This amount does not grow with input size, so auxiliary space is $O(1)$, matching the manifest. All real result nodes are reused from the input.

## Alternatives and edge cases

- **Optimal variant's dummy syntax:** Construct dummies with default values rather than `-1`; behavior is identical because dummy values are ignored.
- **Detach while scanning:** Save the original successor and set each appended node's next to `None`. It prevents temporary cross-links but adds one more pointer variable and assignment.
- **Collect values and rebuild nodes:** This loses original node identity and uses linear extra space.
- **Empty input:** Both dummy chains stay empty, so `None` is returned.
- **All values below `x`:** The greater dummy is empty and the smaller tail is ultimately terminated.
- **All values at least `x`:** The smaller dummy is connected directly to the greater chain.
- **Value exactly `x`:** The `else` branch correctly places it in the greater-or-equal side.
- **Repeated values:** Nodes remain in their original relative order; frequency does not affect classification.
- **Negative threshold and values:** Only the `< x` comparison matters.
- **Temporary cross-links:** They are safe only because `greater.next = None` runs before the result is returned.
- **Termination order:** Joining before clearing is operationally safe here, though clearing first can make the intermediate state easier to reason about.
- **Dummy-node exclusion:** Returning `dummySmaller.next` prevents either artificial node from appearing in the answer.
- **Input mutation:** Original links are deliberately rearranged to satisfy constant-space stable partitioning.
