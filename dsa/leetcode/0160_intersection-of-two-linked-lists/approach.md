## General

**Intersection means shared identity**

Two singly linked lists intersect only when both paths reach the very same
`ListNode` object. Equal values are not sufficient. In the first example, the
separate nodes whose values are one do not intersect, while the node whose
value is eight is shared in memory by both lists.

Once two acyclic singly linked lists share a node, every later node is also
shared. A node has only one `next` pointer, so the paths cannot separate again.
The common part is therefore a suffix, and the task is to return its first
node.

The challenge is that the private prefixes can have different lengths. Two
pointers started together may pass corresponding positions at different times,
even though they eventually traverse the same shared suffix.

**Equalize the traveled distances by switching heads**

The source initializes `a` at `headA` and `b` at `headB`. While they are not
the same object, each pointer advances one step. When `a` reaches `None`, it
continues from `headB`; when `b` reaches `None`, it continues from `headA`.

This makes the routes:

- `a`: all of list A, followed by all of list B;
- `b`: all of list B, followed by all of list A.

Let $m$ and $n$ be the two complete lengths. Each route has total length
$m+n$. The first pointer initially experiences A's length difference, and the
second experiences B's; switching heads causes them to exchange those
differences. By the time they enter the possible shared region on their second
route, they are aligned by distance remaining.

This is the length-alignment method without explicitly counting lengths or
choosing which list is longer.

**See the algebra around a shared suffix**

Suppose list A has a private prefix of length $x$, list B has a private prefix
of length $y$, and the shared suffix has length $c$.

Pointer `a` reaches the intersection after traveling A's private prefix and
shared suffix, switching lists, and then traveling B's private prefix:

$$
x+c+y.
$$

Pointer `b` reaches the same node after:

$$
y+c+x.
$$

The sums are equal. The order differs, but addition does not. Thus both
pointers arrive at the first shared node after the same number of updates.

Another view is that after each pointer has traversed its original list and
switched, the longer original prefix has been exactly compensated by starting
the other route later. Both pointers then have equal distance to the tail.

**Trace an unequal-prefix example**

In Example 1, A's private part is `[4,1]`, B's is `[5,6,1]`, and the shared
suffix begins at the node eight.

The pointers do not meet during their initial simultaneous walk because B has
one additional private node. Pointer `a` reaches the end of A first and
switches to B's head. Pointer `b` later reaches the end of B and switches to
A's head. After each has absorbed the other list's prefix difference, both
references become the shared node eight on the same iteration.

The loop condition is checked before advancing. If the two heads are already
the same object, the loop does not run and that head is returned immediately.

**Why the no-intersection case terminates**

If the lists are disjoint, there is no shared non-null node at which the
pointers can meet. Nevertheless, both routes have exactly $m+n$ nodes. After
traversing A then B and B then A, both pointers reach `None` together.

`None == None`, so the loop ends and returns `None`. No special disjoint-list
test is required.

The no-cycle guarantee is important. With cycles, a pointer might never reach
`None`, and intersection semantics would require additional cases. Under the
given contract, both finite routes terminate.

**Preserve the lists**

The method changes only local references `a` and `b`. It never assigns a
node's `next` field. Switching from `None` to the other head changes where a
local cursor points; it does not connect the lists or create a cycle.

Therefore both original structures remain exactly as they were, satisfying the
explicit preservation note.

**State the meeting argument precisely**

At each iteration, both pointers have taken the same number of steps along
their respective concatenated routes. If an intersection exists, the route
suffix beginning at the first common node is identical for both pointers, and
the equal route-length calculation aligns their entry into it. Their first
equal non-null reference is therefore the first shared node.

If no intersection exists, their only equal reference is the common terminal
`None`. In either case, the value returned after the loop is exactly the
required result.

**Harness-provided node type**

The selected source annotates `ListNode` but keeps its definition commented as
platform documentation. A standalone environment must provide that class, as
the native judge does. The algorithm relies on reference comparison and the
`next` attribute, not on any particular node value.

## Complexity detail

Let $m$ and $n$ be the lengths of lists A and B. Each pointer traverses at most
both lists, so the number of updates is bounded by $m+n$. Time is
$O(m+n)$.

The method stores two node references and no input-sized collection.
Auxiliary space is $O(1)$. It does not copy or mutate either list. These bounds
match the manifest and the follow-up requirement.

## Alternatives and edge cases

- **Measure lengths first:** Count both lists, advance the pointer on the longer list by the length difference, then walk together. It has the same $O(m+n)$ time and $O(1)$ space but more explicit passes.
- **Hash set of nodes:** Store every node from one list and scan the other. It is straightforward but uses $O(m)$ or $O(n)$ additional space.
- **Nested scans:** Compare every A node with every B node by identity; this can take $O(mn)$ time.
- **Equal values in separate nodes:** They must not be returned; intersection uses object identity.
- **Shared head:** The initial pointers are equal, so that head is returned.
- **No intersection:** Both pointers eventually become `None` together.
- **One list shorter:** Head switching automatically compensates for the difference.
- **Shared tail:** After the first shared node, all successors are necessarily shared in a singly linked structure.
- **No mutation:** Only cursor variables change, preserving both input lists.
- **Cycle outside the contract:** The route-length and termination proof relies on acyclic lists.
