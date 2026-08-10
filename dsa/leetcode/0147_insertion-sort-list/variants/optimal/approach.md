## General

**Grow a sorted prefix one node at a time**

The algorithm maintains two regions:

- the list from `head` through `pre` is sorted in non-decreasing order;
- `cur` is the first node not yet incorporated into that sorted prefix.

Initially, `pre` is the dummy node and `cur` is `head`. Because the dummy’s stored value equals `head.val`, the first comparison succeeds and advances both pointers. The real sorted prefix then consists of the original head, which is trivially sorted.

Each later iteration either leaves `cur` at the end of the sorted prefix or removes it from there and inserts it earlier.

**Why a dummy node helps**

`dummy.next` points to the current sorted-list head. A node may need to be inserted before the original head, and a singly linked list can insert before a node only through its predecessor.

The dummy is that predecessor for head insertion. After all rearrangements, `dummy.next` is the possibly changed real head returned to the caller.

The dummy constructor receives `head.val` and `head`. Its value is relevant only to the special initial `pre.val <= cur.val` comparison; insertion search compares `p.next.val`, not `p.val`.

**Use a constant-time append fast path**

If `pre.val <= cur.val`, the current node is at least as large as the last node in the sorted prefix. Since the prefix is already sorted and `cur` already follows `pre`, it is already in the correct place.

The method simply advances:

- `pre` to `cur`;
- `cur` to `cur.next`.

This fast path makes an already sorted list linear rather than forcing a scan from the dummy for every node.

After the first iteration, `pre` is always a real node. The special dummy value does not distort later ordering checks.

**Find the insertion predecessor for an inversion**

When `pre.val > cur.val`, the current node belongs somewhere before the sorted tail.

`p` starts at `dummy` and advances while `p.next.val <= cur.val`. Thus it passes every sorted-prefix node whose value is no greater than the current value. When it stops, `p.next` is the first prefix node with a larger value.

The strict inversion at the tail guarantees such a stopping point exists before reaching `cur`: `pre` itself has a value larger than `cur.val`. This is why the loop can read `p.next.val` without a separate null check.

Using `<=` makes the insertion stable. A current node is placed after all equal-valued nodes already processed, preserving their original relative order.

**Splice without losing the unsorted remainder**

The source saves `t = cur.next`, the node that must be processed next after this insertion.

It then performs:

- `cur.next = p.next`, linking the moved node to the first larger prefix node;
- `p.next = cur`, linking the insertion predecessor to the moved node;
- `pre.next = t`, removing `cur` from its old position after the sorted tail;
- `cur = t`, advancing to the next unprocessed node.

`pre` does not move in this case. It remains the final node of the sorted prefix; moving a later node before it does not change that tail’s identity.

For `[4,2,1,3]`, node two moves before four, node one then moves before both, and node three is inserted between two and four. The returned chain is `[1,2,3,4]`.

**Why the maintained prefix remains sorted**

The append branch adds a value no smaller than the current tail.

The insertion branch places `cur` after all values at most `cur.val` and before the first larger value. All other sorted-prefix links keep their relative order. Therefore, either branch extends the sorted prefix by exactly one node while preserving non-decreasing order.

Every iteration advances `cur` to a previously unprocessed node, so eventually all nodes belong to the sorted prefix. Nodes are relinked rather than copied, and values are never modified.

## Complexity detail

Let $n$ be the number of nodes.

The outer loop processes each node once. An insertion search may scan up to the entire sorted prefix. In the worst case, the total comparisons are proportional to:

$$
1+2+\cdots+(n-1)=O(n^2).
$$

Thus worst-case time is $O(n^2)$. An already non-decreasing list takes the append fast path throughout and runs in $O(n)$ time.

The algorithm allocates one dummy node and stores a fixed number of pointers, so auxiliary space is $O(1)$. It reuses every original data node.

## Alternatives and edge cases

- **Always rebuild from a dummy:** Remove each input node and scan a separate sorted result list for insertion. It is simpler but misses the already-sorted-tail fast path.
- **Merge sort:** Linked-list merge sort runs in $O(n\log n)$ time and is generally preferable for large arbitrary inputs, but it does not fulfill the explicit insertion-sort request.
- **Array conversion:** Copy nodes or values into an array, sort, and rebuild links. It uses $O(n)$ extra space and may violate the spirit of in-place node sorting.
- **Empty list:** The early return handles it even though the constraints specify at least one node.
- **One node:** The early return returns it unchanged.
- **Already sorted:** Every iteration after initialization advances in constant time, giving the best-case $O(n)$ behavior.
- **Reverse sorted:** Every new node is inserted near the head; the search itself stops quickly, so this particular linked-list implementation can be faster than the generic worst-case pattern.
- **Equal values:** The `<=` scan places later equal nodes after earlier ones, preserving stability.
- **Head replacement:** The dummy allows a new minimum to become `dummy.next` without a special branch.
- **Runtime dependency:** The platform must supply `ListNode` with a constructor accepting `(val, next)` as shown in the template.
