## General

**Walk two concatenated views of the lists**

The competitive implementation uses cursors `curA` and `curB`. `curA` first
walks list A and then list B; `curB` first walks list B and then list A. They
advance in lockstep until their references are equal.

The switch occurs only after a cursor has become `None`:
`curA = curA.next if curA else headB`, with the symmetric update for `curB`.
No link inside either list is changed.

The purpose is to cancel unequal private prefix lengths. If A is longer, the
A cursor reaches its switch later, but the B cursor then traverses A on its
second route. Each cursor ultimately covers the same combined amount of list
structure in opposite order.

**Separate node identity from stored value**

The comparison `curA != curB` compares node references under the platform node
semantics. Two different nodes can both store the value one and still be
unequal. Returning either merely because `curA.val == curB.val` would fail the
custom judge, which constructs one actual shared tail object and may place
duplicate values in private prefixes.

When `curA == curB` at a non-null reference, both paths have reached the same
memory object. Because every node has a single successor, everything after
that object is shared as well.

**Derive why switching aligns the paths**

Let the list portions before the intersection have lengths $a$ and $b$, and
let the shared suffix have length $c$. The full lengths are $a+c$ and $b+c$.

The A-first cursor travels:

$$
(a+c)+b
$$

steps before arriving at the intersection through its second list. The B-first
cursor travels:

$$
(b+c)+a.
$$

Both totals equal $a+b+c$. Their initial mismatch has disappeared because each
one has now traversed both private prefixes and one copy of the shared suffix.

This is equivalent to computing the length difference and skipping extra nodes
from the longer list, but it obtains the alignment implicitly through the two
head switches.

**Follow a concrete pointer sequence**

Suppose A is `A1 -> A2 -> C1 -> C2` and B is
`B1 -> B2 -> B3 -> C1 -> C2`, where `C1` and `C2` are shared objects.

Initially the pointers are offset because B has one more private node. The
A-first cursor reaches `None`, jumps to `B1`, and begins B. The B-first cursor
reaches its own `None` one iteration later, jumps to `A1`, and begins A.

After passing through the opposite private prefixes, both references become
`C1` together. The loop stops before either pointer advances to `C2`, so the
first shared node—not merely some later shared node—is returned.

If both lists have equal-length private prefixes, the cursors reach the
intersection during their first traversal and never need to switch.

**Handle disjoint lists with the same mechanism**

For disjoint acyclic lists, both concatenated routes still have $m+n$ nodes.
Neither cursor finds an equal non-null object. After walking its two routes,
each becomes `None` on the same comparison.

Because the loop condition regards the two null references as equal, it ends
and returns `curA`, which is `None`. The code does not loop forever and does not
need to know in advance whether an intersection exists.

**Why first equality is the answer**

Both cursors take one transition per loop, so they are always at equal traveled
distances within routes of equal combined length. Any unequal-prefix offset is
removed once the routes cross list heads.

If a shared suffix exists, the earliest common object on either list is its
first node. Once the cursors are aligned by remaining distance, that object is
the first possible non-null equality. If it does not exist, null termination
is the only equality. Therefore returning `curA` covers both outcomes.

The no-cycle guarantee ensures every first traversal reaches `None` and every
combined route is finite. A cyclic version would need cycle detection and a
more involved definition of the first shared node.

**Input structure remains unchanged**

Although the code makes each cursor “jump” to the opposite head, that jump is
only a variable assignment. It does not write `curA.next` or `curB.next`.
Every node and link remains unchanged for the caller.

The competitive file includes a `ListNode` class as top-level harness
scaffolding. The native judge normally provides compatible nodes. The method
needs reference equality and `.next`; it does not allocate replacement nodes.

## Complexity detail

With lengths $m$ and $n$, neither cursor makes more than $m+n$ node
transitions before equality. The combined running time is $O(m+n)$.

Only the two cursor references are additional state, so auxiliary space is
$O(1)$. The method leaves all input nodes in place. These bounds agree with the
manifest and the source comments.

## Alternatives and edge cases

- **Explicit length alignment:** Compute both lengths, advance the longer head by their difference, then compare nodes in parallel. It makes the alignment visible but requires separate counting code.
- **Node-reference set:** Expected $O(m+n)$ time, but storing one list requires linear auxiliary memory.
- **Brute-force pair comparisons:** Uses constant space but may inspect $mn$ pairs.
- **Different nodes with the same value:** Reference equality correctly rejects them.
- **Both heads identical:** The loop is skipped and the shared head is returned.
- **Intersection at the final node:** Switching still aligns both cursors before that shared tail node.
- **No intersection:** Both concatenated routes end at `None` together.
- **Unequal lengths:** Each cursor traverses both lengths, canceling the offset.
- **Structure preservation:** No `.next` assignment occurs.
- **Cycles outside the contract:** A cursor might not reach its head switch, invalidating the finite-route proof.
