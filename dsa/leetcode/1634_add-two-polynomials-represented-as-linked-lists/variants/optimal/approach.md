## General

**Merge two already sorted term streams**

Each input list is in strictly descending power order. This is the same structure that makes merging two sorted lists efficient: at any moment, the largest unprocessed power must be at the head of one or both remaining lists.

The source keeps `poly1` and `poly2` as traversal pointers. A dummy node simplifies output construction, and `curr` always points to the last node currently attached to the result. The true head is returned as `dummy.next`, so no special branch is needed for the first output term or for an entirely zero result.

While both input pointers are non-null, the algorithm compares their powers. Exactly one of three cases applies.

**The first polynomial has the larger current power**

If `poly1.power > poly2.power`, no later node in `poly2` can match `poly1.power` because powers in `poly2` only decrease. The term is unique to the first polynomial and passes unchanged into the sum.

The source attaches the existing node with `curr.next = poly1`, advances `poly1` to its saved next node, and advances `curr` to the attached node. Reusing the node avoids an allocation.

The corresponding reasoning applies symmetrically when `poly1.power < poly2.power`: the current `poly2` term cannot have a later match in `poly1`, so the existing second-list node is attached and only `poly2` advances.

**Equal powers combine**

When powers match, the polynomial terms are like terms. Their coefficients are added:

`c := poly1.coefficient + poly2.coefficient`.

The walrus operator both assigns this sum to `c` and uses its truth value. If `c` is nonzero, the source creates a new `PolyNode(c, poly1.power)` and appends it. If `c` is zero, it appends nothing, which enforces the standard-form rule that zero-coefficient terms are omitted.

Both input pointers advance in either case because both terms have been fully consumed. A new node is used for a nonzero combination because neither original node has the combined coefficient.

**Append the remaining suffix**

When the main loop ends, at least one input pointer is null. Every node in the other list has a power smaller than all terms already emitted, and there is no opposing term left with which it could combine. Its whole suffix can therefore be attached in one operation:

`curr.next = poly1 or poly2`.

Python's `or` returns `poly1` if it is non-null, otherwise `poly2`. If both are null, it assigns `None` and correctly terminates the list.

Splicing the suffix is more efficient than visiting it only to recreate identical nodes. It also means the returned list may share nodes with and mutate links from the input lists. The problem asks for the sum list and does not require the two original list structures to remain independently reusable afterward.

**Why reusing an input node does not leave a wrong tail**

When an unequal-power node is attached, that node initially still points to its original successor. On the next output append, `curr.next` is overwritten with whichever term should actually follow in the merged order. Thus the merge gradually repairs the links.

If the loop ends immediately after such an attachment, the final suffix assignment connects `curr` to the remaining correct list. If the attached node's original suffix is itself the remaining suffix from the same input, the assignment simply preserves the appropriate link.

The dummy node guarantees that even if leading equal-power terms cancel, `curr` remains a valid place from which to attach the first later term.

**A cancellation trace**

For

`poly1 = [[2,2],[4,1],[3,0]]`

and

`poly2 = [[3,2],[-4,1],[-1,0]]`,

the power-2 terms match and create a new term with coefficient 5. The power-1 terms sum to zero, so no node is appended. The power-0 terms match and create coefficient 2. The output is `[[5,2],[2,0]]` and remains strictly descending by power.

If `[[1,2]]` is added to `[[-1,2]]`, the only coefficient sum is zero. Nothing follows the dummy node, both pointers become null, and `dummy.next` is `None`, representing the empty list.

**Why the merge is correct**

Maintain this invariant: before every iteration, the output contains the correct sum of all already consumed powers, in strictly descending order, and both pointers identify the greatest unprocessed power in their respective polynomials.

If one current power is larger, that term cannot match anything later in the other list, so copying it is required and preserves order. If powers match, coefficient addition is the definition of polynomial addition; emitting the sum only when nonzero gives standard form. Advancing exactly the consumed pointer or pointers restores the invariant.

After one list ends, no cross-list matches remain, so the other sorted suffix is already the correct rest of the sum. The final list therefore contains exactly one nonzero term for every power whose combined coefficient is nonzero, in strictly descending order.

## Complexity detail

Let $n$ and $m$ be the input list lengths. Every main-loop iteration advances at least one pointer, and no node is revisited. Attaching the remainder is constant time rather than a suffix traversal. Total time complexity is $O(n+m)$.

The dummy node is one allocation. A new result node is allocated only for a matching-power pair whose coefficient sum is nonzero. There can be at most $\min(n,m)$ such pairs, so the exact additional allocation bound is $O(\min(n,m))$; unequal terms and the remaining suffix reuse input nodes.

If all nodes reachable in the returned output are counted as result space regardless of reuse, the output can contain $O(n+m)$ nodes, which is the broader bound recorded in the manifest. The algorithm's auxiliary pointer storage is $O(1)$, while newly allocated auxiliary/output nodes are $O(\min(n,m))$.

This space behavior comes with aliasing: callers should not assume input links remain untouched after the merge.

## Alternatives and edge cases

- **Allocate every output node:** This preserves both input lists and still takes $O(n+m)$ time, but uses $O(n+m)$ fresh space.
- **Accumulate coefficients in a map:** Traverse both lists into a power-to-coefficient dictionary, remove zero sums, sort powers, and build output. It is simpler without sorted inputs but costs $O((n+m)\log(n+m))$ time.
- **Recursive merge:** It mirrors the three comparison cases but can require $O(n+m)$ call-stack depth, which is risky for lists up to $10^4$ nodes.
- **One input is empty initially:** The loop is skipped and the final suffix assignment returns the other polynomial directly.
- **Both inputs are empty:** `poly1 or poly2` is null, so `dummy.next` remains null and the empty polynomial is returned.
- **Equal powers cancel:** Both nodes are consumed and no zero-coefficient node is created.
- **Equal powers do not cancel:** A fresh node stores the combined coefficient because neither input node has that value.
- **Disjoint powers:** All terms are reused and merged in descending order without allocating term nodes beyond the dummy.
- **Very large power gaps:** Only relative ordering matters; the algorithm never iterates through missing exponent values.
- **Negative coefficients:** Addition and the zero test work unchanged.
- **Strictly descending input powers:** This guarantee is essential. If an input were unsorted or repeated a power internally, the two-pointer proof would fail.
- **Input mutation and sharing:** Reused nodes have their `next` links integrated into the result. Copy nodes instead if preserving original list topology were a separate requirement.
