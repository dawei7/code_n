## General

**Let the smaller current head determine the next output node**

Each input list is already sorted in non-decreasing order. Therefore, among all nodes not yet placed in the merged list, the smallest value must be at `list1`'s current head or `list2`'s current head. No later node can be smaller than its own list's head.

This observation gives a recursive definition. Select the smaller current head as the next node, then merge the unselected list with the remainder after the selected node. The selected source implements exactly that recurrence and reuses the existing nodes rather than copying their values into new nodes.

**Handle exhaustion before reading node values**

The first condition is

```python
if list1 is None or list2 is None:
    return list1 or list2
```

If either list is empty, no comparison is possible or necessary. The other list is already sorted, and every node that preceded this recursive call has a value no greater than its current head. The entire remaining chain can therefore be returned unchanged.

Python's `or` returns an operand, not merely a Boolean. If `list1` is a node, `list1 or list2` returns that node; otherwise it returns `list2`, which may also be `None`. This compact expression consequently handles all three cases: only list 1 remains, only list 2 remains, or both are empty.

Checking exhaustion first also guarantees that both `.val` accesses in the following comparison are safe.

**Choose a head and recursively build its successor**

When both heads exist, the implementation compares their values. If

```python
list1.val <= list2.val
```

then `list1` is safe to place first. The assignment

```python
list1.next = self.mergeTwoLists(list1.next, list2)
```

does two jobs. It removes the chosen node from further consideration by passing its old successor as the new `list1`, and it connects the chosen node to the correctly merged result of everything still unconsumed. Returning `list1` makes that chosen node the head of this recursive subproblem.

The `else` branch is symmetric: when `list2.val` is smaller, it recursively merges `list1` with `list2.next`, assigns that result to `list2.next`, and returns `list2`.

**Why ties may safely come from list 1**

The condition uses `<=`, so equal values select `list1` first. This creates a deterministic and stable preference for the first list across equal heads. Choosing `list2` first would also produce the required non-decreasing sequence because the values are equal, but it would change node identity order. The problem cares about values and sortedness, not which input contributes the first equal node.

The equality choice does not discard the `list2` node. Only `list1` advances in that call; `list2` remains the head of its list and will be compared again in the next recursive subproblem.

**A recursive invariant explains sortedness and completeness**

For any call `mergeTwoLists(a, b)`, the returned chain contains every node reachable from `a` and every node reachable from `b`, exactly once, arranged in non-decreasing order.

The base case satisfies this statement because the sole non-empty remainder is already sorted and is returned intact. For the recursive step, suppose both lists are non-empty and `a.val <= b.val`. Since each list is sorted, `a.val` is no larger than any node later in `a`, and the comparison proves it is no larger than `b.val` or any later node in `b`. Thus `a` is a valid first node. By the recursive hypothesis, merging `a.next` with `b` returns every remaining node once in sorted order. Linking `a.next` to that result creates the complete sorted merge. The other branch follows the same reasoning with `b`.

Each non-base call advances exactly one input head, so it cannot select the same node twice. The base case attaches the one remaining suffix once. This proves node preservation as well as sortedness.

**Trace `[1, 2, 4]` and `[1, 3, 4]`**

At the first comparison, both heads are `1`; `<=` chooses the first list's `1`. The next call compares `2` with the second list's still-unconsumed `1`, so it chooses that second `1`. It then chooses `2`, then `3`, then the first list's `4` on the equal-`4` tie. At that point the first list is exhausted, and the base case returns the second list's final `4` directly.

As recursive calls return, their `next` assignments produce `[1, 1, 2, 3, 4, 4]`. Although it is natural to describe this as unwinding, the nodes were logically chosen on the way down; unwinding completes the links and returns the chosen heads.

**Understand the mutation**

The method splices together original nodes. It overwrites `next` fields on chosen nodes, so the two original list structures should not be expected to remain independently traversable afterward. This is exactly what the description requests: the merged list is made by splicing the input nodes.

No cycle is introduced when the inputs are separate, acyclic linked lists as required. Every recursive call advances one head and only points a chosen node toward a merge of nodes that were still later in the input order.

## Complexity detail

Let $m$ and $n$ be the numbers of nodes initially reachable from `list1` and `list2`.

- **Time complexity: $O(m+n)$.** Each non-base recursive call consumes one node by advancing either `list1` or `list2`. Once one list is exhausted, the other suffix is attached in constant time. There are at most $m+n$ calls and constant work per call.
- **Auxiliary space of the exact selected source: $O(m+n)$ in the worst case.** This implementation is recursive. A call remains on Python's call stack until its recursive merge returns, and as many as $m+n$ nested calls can exist when values interleave or one list's nodes are repeatedly chosen before exhaustion. It allocates no replacement list nodes, but call-stack memory is still auxiliary space.

The manifest states $O(1)$ space, which would describe the iterative two-pointer variant or an analysis that incorrectly ignores recursion. It does not describe the exact Python implementation here. Output storage is not additional allocation because the returned chain reuses the input nodes.

With the supplied limit of at most 50 nodes across both lists, recursion depth is small. For a much larger unrestricted list, Python's recursion limit would make the iterative method operationally safer.

## Alternatives and edge cases

- **Iterative dummy-tail merge:** Maintain a dummy node and append the smaller head in a loop. It preserves $O(m+n)$ time while using $O(1)$ call-stack space and is the appropriate way to meet the manifest's constant-space claim.
- **Create a new list:** Copy values into newly allocated nodes. This preserves the inputs but costs $O(m+n)$ new node storage and does not follow the requested splicing emphasis as directly.
- **Collect and sort all values:** It discards the useful sorted-input structure, takes $O((m+n)\log(m+n))$ time, and either creates new nodes or loses node identity.
- **Both inputs empty:** The base case evaluates `None or None` and returns `None`.
- **Exactly one input empty:** The non-empty list is returned unchanged; no recursion or copying is needed.
- **One list entirely smaller:** Nodes from that list are selected until exhaustion, after which the other suffix is attached at once.
- **Equal values:** `<=` consistently chooses the first list's current node, while retaining every duplicate from both lists.
- **Negative values:** Comparisons work identically; only non-decreasing order matters.
- **Input mutation:** Existing `next` pointers are overwritten. Callers must treat the returned head as the authoritative merged chain.
- **Shared nodes or cyclic inputs:** The contract supplies ordinary independent acyclic lists. Aliasing or cycles could invalidate the progress proof and are outside this implementation's guarantees.
