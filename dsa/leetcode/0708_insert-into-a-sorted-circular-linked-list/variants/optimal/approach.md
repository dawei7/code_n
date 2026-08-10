## General

A sorted circular list has no null end and the supplied `head` may point anywhere, not necessarily at the minimum. Walking once around the cycle shows nondecreasing values except at one wrap from a maximum value back to a minimum value. If all values are equal, even that strict drop is absent.

The solution examines adjacent pairs `prev -> curr` and inserts between a suitable pair.

**Empty-list case**

The new node is allocated before the check.

If `head is None`, the list must become a one-node cycle. Setting `node.next = node` makes the node point to itself, and returning it supplies the only possible head.

No general traversal can handle an empty cycle, so this case is resolved first.

**Two moving pointers**

For a nonempty list:

`prev, curr = head, head.next`.

At every iteration, these pointers describe one existing edge. If that edge is not suitable, both move forward:

`prev, curr = curr, curr.next`.

The loop continues while `curr != head`, checking each edge until it is about to close the cycle back to the supplied head. The closing edge is handled by the fallback after the loop if no earlier edge was selected.

Keeping both pointers is necessary because a singly linked node has no backward link; insertion needs both the predecessor whose `next` will change and the successor the new node must point to.

**Case 1: insertion inside an ascending region**

For an ordinary nondecreasing edge, `prev.val <= curr.val`. The new value fits there when:

$$
\texttt{prev.val}\le\texttt{insertVal}\le\texttt{curr.val}.
$$

The inclusive comparisons allow insertion next to equal values. Since any suitable location is accepted, there is no need to choose a particular side of duplicates.

**Case 2: insertion at the maximum-to-minimum wrap**

The wrap edge is recognized by:

`prev.val > curr.val`.

Here `prev` is at a maximum end of the sorted order and `curr` is at a minimum beginning. A value belongs across this boundary in either extreme:

- `insertVal >= prev.val`, so it extends the maximum end;
- `insertVal <= curr.val`, so it extends the minimum beginning.

The logical `or` combines these two disjoint numeric regions.

A middle value should not be placed across the wrap because it belongs between some ordinary ascending neighbors elsewhere.

**Why the loop can stop at the first match**

The contract accepts any valid insertion position. Once an edge satisfies either case, placing the value there preserves the cyclic sorted order.

There may be several matches because of duplicate values. Choosing the first one encountered from the arbitrary input head is sufficient.

**Fallback after one complete traversal**

If the loop reaches `curr == head` without breaking, it inserts across the current closing edge.

This covers several situations:

- all existing values are equal, so no strict wrap exists and a differing new value may be inserted anywhere;
- the list has one node, so the loop body never runs;
- the only suitable ordinary or wrap edge is the edge returning to the supplied head;
- duplicates make multiple positions equivalent.

Why is arbitrary fallback safe after no earlier match? A sorted cycle partitions possible values among its ordinary gaps and its wrap gap. If none of the checked edges accepts `insertVal`, the unexamined closing edge is the remaining suitable location. In the uniform-value case, every edge is structurally equivalent and placing the value at any one of them creates the single required wrap.

**Performing the insertion**

The pointer changes are:

`prev.next = node`

followed by

`node.next = curr`.

The new edge sequence becomes `prev -> node -> curr`. The rest of the cycle is untouched.

Because `curr` is never null in a valid cycle, the new node remains connected into a closed loop.

The method returns the original `head` for every nonempty input, as required. It does not return the new node even when the new value is the mathematical minimum.

**A trace with an arbitrary head**

For cycle `3 -> 4 -> 1 -> 3` and `insertVal = 2`:

- Edge `3 -> 4` is ordinary, but two is below three, so it does not fit.
- Edge `4 -> 1` is the wrap. Two is neither at least four nor at most one, so it does not fit there.
- The next edge `1 -> 3` satisfies `1 <= 2 <= 3`.
- Insert to obtain `1 -> 2 -> 3` along that portion, while returning the original node `3`.

**A value outside the range**

With the same cycle and `insertVal = 5`, edge `4 -> 1` is the wrap and `5 >= 4`. Inserting there yields cyclic order `3, 4, 5, 1, 3`.

For `insertVal = 0`, the same edge qualifies through `0 <= 1`.

**Why the result remains sorted**

For a normal edge, the explicit double inequality preserves nondecreasing order on both new edges.

For a wrap edge, an above-maximum value makes `prev -> node` nondecreasing and moves the wrap to `node -> curr`. A below-minimum value moves the wrap to `prev -> node` and makes `node -> curr` nondecreasing.

Fallback is reached only when the closing edge is the suitable remaining edge or the cycle is uniform. In every case, exactly one node is inserted and the circular sorted structure is preserved.

## Complexity detail

Let `n` be the number of existing nodes.

The algorithm examines at most one full cycle, doing constant work per edge. Its running time is

$$
O(n).
$$

It often stops earlier when a suitable edge is found.

Aside from the required new output node, it stores only `prev`, `curr`, and `node` references. Auxiliary working space is

$$
O(1).
$$

The traversal is iterative and uses no recursion stack.

## Alternatives and edge cases

- **Find minimum and then insert linearly:** One could first locate the wrap and treat the cycle as a linear sorted list, but that may require extra traversal and is unnecessary.

- **Empty list:** The new node must point to itself; leaving `next` as null would not create a circular list.

- **One-node list:** The main loop does not run, and fallback inserts after the existing node.

- **All values equal:** No strict wrap exists. Any edge is valid, and fallback handles it.

- **Insert another equal value:** The ordinary inclusive condition may accept the first checked edge.

- **New minimum:** Insert at the maximum-to-minimum edge using `insertVal <= curr.val`.

- **New maximum:** Insert at that edge using `insertVal >= prev.val`.

- **Head is not minimum:** Traversal and wrap detection use values, not assumptions about head.

- **Closing edge omitted from loop body:** The fallback deliberately inserts there when no earlier edge matches.

- **Duplicate minima or maxima:** Several valid boundaries may exist; the problem permits any one.

- **Return identity:** Nonempty input must return the original head reference even if insertion changes which node would be considered the smallest.

- **Pointer order:** Both links must be established so the old successor remains reachable and the cycle stays closed.
