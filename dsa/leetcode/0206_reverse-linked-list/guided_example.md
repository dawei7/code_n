# Guided Example: Reverse Linked List

## 1. The Edge-Inversion Task and Its Representative Instance

A singly linked list is a chain of nodes in which each node stores one value and a
single forward reference to its successor, or an empty reference if it is the last
node. Only the head of the chain is reachable from outside; every other node is
found by following forward references. The task is to reverse the direction of every
one of those references, so that traversing from the returned head visits the
original values in the opposite order, while keeping the very same node objects.
No values may be copied into new nodes: node identity must be preserved and every
original node must appear exactly once in the result.

The representative instance uses the five-node chain below, written positionally as
$v_1 \to v_2 \to v_3 \to v_4 \to v_5 \to \text{nil}$ and with the head pointing at
$v_1$.

| Position | Node | Stored `val` | Original successor | Required successor |
|:---:|:---:|:---:|:---:|:---:|
| 1 | $v_1$ | `1` | $v_2$ | nil (it becomes the tail) |
| 2 | $v_2$ | `2` | $v_3$ | $v_1$ |
| 3 | $v_3$ | `3` | $v_4$ | $v_2$ |
| 4 | $v_4$ | `4` | $v_5$ | $v_3$ |
| 5 | $v_5$ | `5` | nil | $v_4$ (it becomes the new head) |

The required traversal order of the returned chain is therefore
`5 → 4 → 3 → 2 → 1`, produced by the returned head $v_5$. The two smaller instances
in the contract are the degenerate cases: a two-node input `[1, 2]` becomes
`[2, 1]`, a one-node input `[1]` stays `[1]` with an unchanged empty successor, and
an empty input returns an empty chain.

## 2. Two Disjoint Segments: The Reversal Invariant

The decisive difficulty is that a singly linked node holds only one outgoing
reference. Overwriting it to point backward destroys the only route to the rest of
the chain, so the reference to the remaining unprocessed nodes must be captured in a
local variable before the overwrite happens. This forces a small, carefully ordered
set of steps per node.

The method maintains exactly two logical segments of the original node set:

- the **reversed segment**, whose head is held in a local reference and whose chain
  ends in an empty reference; and
- the **unprocessed suffix**, whose first node is held in a cursor reference and
  which still retains its original forward references.

Write the processed count after $k$ iterations as $k$ and the cursor as $c$. The
invariant that holds at the start of every iteration is:

> **Reversal invariant.** The reversed segment contains exactly the first $k$
> original nodes in exact reverse original order, its head is the $k$-th node, and
> its chain terminates in an empty reference. The cursor points at the
> $(k+1)$-th original node, which is the head of the unprocessed suffix, and that
> suffix contains the remaining $n - k$ nodes in original order. The two segments
> are disjoint and their union is the whole input.

Two consequences follow immediately. First, the list is never longer or shorter
than at the start: no node is duplicated and none is lost, because the cached
forward reference preserves the suffix across the overwrite. Second, the final
answer is the reversed segment's head once the suffix becomes empty. A dummy node
whose successor field is the reversed head is convenient here: it provides a stable
location to update as the head of the reversed segment changes, and it is never
returned as data.

| Iteration start $k$ | Reversed segment (reverse original order) | Unprocessed suffix (original order) | Union size |
|:---:|:---|:---|:---:|
| 0 | empty | $v_1 \to v_2 \to v_3 \to v_4 \to v_5$ | 5 |
| 1 | $v_1$ | $v_2 \to v_3 \to v_4 \to v_5$ | 5 |
| 2 | $v_2 \to v_1$ | $v_3 \to v_4 \to v_5$ | 5 |
| 3 | $v_3 \to v_2 \to v_1$ | $v_4 \to v_5$ | 5 |
| 4 | $v_4 \to v_3 \to v_2 \to v_1$ | $v_5$ | 5 |
| 5 | $v_5 \to v_4 \to v_3 \to v_2 \to v_1$ | empty | 5 |

## 3. Step-by-Step Trace of Front Insertion

Each iteration performs four ordered actions on the node at the cursor:

1. **Cache the successor** of the cursor node into a local reference, before any
   overwrite, so the unprocessed suffix stays reachable.
2. **Point the cursor node backward** by assigning it the current head of the
   reversed segment. On the first iteration that head is empty, which is precisely
   what makes the original head the eventual tail.
3. **Publish the cursor node as the new head** of the reversed segment. Front
   insertion changes the reversed sequence from $\text{reverse}(k)$ to
   $v_{k+1} + \text{reverse}(k)$, which is exactly $\text{reverse}(k+1)$.
4. **Advance the cursor** to the cached successor, restoring the invariant with
   $k$ increased by one.

Tracing the five-node instance:

| Iteration | Cursor node | Cached successor | New backward reference from cursor | Reversed segment after step 3 | Suffix after step 4 |
|:---:|:---:|:---:|:---:|:---|:---|
| 1 | $v_1$ | $v_2$ | nil | $v_1$ | $v_2 \to v_3 \to v_4 \to v_5$ |
| 2 | $v_2$ | $v_3$ | $v_1$ | $v_2 \to v_1$ | $v_3 \to v_4 \to v_5$ |
| 3 | $v_3$ | $v_4$ | $v_2$ | $v_3 \to v_2 \to v_1$ | $v_4 \to v_5$ |
| 4 | $v_4$ | $v_5$ | $v_3$ | $v_4 \to v_3 \to v_2 \to v_1$ | $v_5$ |
| 5 | $v_5$ | nil | $v_4$ | $v_5 \to v_4 \to v_3 \to v_2 \to v_1$ | empty |

After the fifth iteration the cursor is empty, so the loop stops. The reversed
segment now holds all five nodes, its head is $v_5$, and the answer is that head's
chain, which reads `5 → 4 → 3 → 2 → 1`.

| Termination check | Value at loop exit | Meaning |
|:---|:---|:---|
| Cursor | empty reference | The unprocessed suffix holds no nodes |
| Reversed head | $v_5$ | The returned entry point of the final chain |
| Reversed chain length | 5 nodes | Equal to the original node count |
| Original head's successor | empty reference | $v_1$ is the new tail, so the chain is acyclic |

## 4. Why the Reasoning Is Correct

**Ordering is what avoids node loss.** Assigning the backward reference before
caching the successor would sever the only route to the suffix and make the
remaining nodes unreachable from any local reference. The fixed action order —
cache, rewire, publish, advance — is therefore not stylistic; it is the correctness
condition that keeps the two segments' union equal to the whole input.

**Soundness by induction on $k$.** The base case $k = 0$ holds because nothing has
been processed: the reversed segment is empty and the cursor is the original head.
For the step, assume the invariant at the start of iteration $k$. The cached
successor is exactly the head of the suffix, so the suffix minus its first node is
still wholly reachable and in original order. Front insertion places $v_{k+1}$ before
every node of the already reversed segment, so the new segment is
$v_{k+1} + \text{reverse}(k) = \text{reverse}(k+1)$ in exact reverse original order.
Advancing the cursor to the cached successor restores the invariant with $k$
increased by one, and the two segments remain disjoint because $v_{k+1}$ was moved
out of the suffix and into the reversed segment exactly once.

**Termination is exact.** The cursor advances one original node per iteration and
the suffix strictly shrinks, so after $n$ iterations the suffix is empty and the loop
stops. By the invariant the reversed segment then contains all $n$ original nodes in
exact reverse original order, so its head is the correct returned chain.

**No cycle can form.** The first iteration sets the original head's reference to
empty, creating the new tail. Every later processed node points only into the
already reversed segment, whose chain ends in that empty reference, and no reversed
node ever points forward into the suffix. Caching a forward reference in a local
variable does not create a list edge, so the result is one acyclic chain.

**Node identity and values are preserved.** Only successor references change. No
value is read, written, or copied, and no node is allocated except the never-returned
dummy holder, so equal values in different nodes remain distinct entities and every
original node appears exactly once.

## 5. Traps and Alternatives This Instance Exposes

| Trap or alternative | Description | Consequence |
|:---|:---|:---|
| Overwriting before caching | Assigning the backward reference while the forward reference has not yet been saved | The suffix becomes unreachable; all nodes after the cursor are lost |
| Initialising the old tail's new reference wrongly | Leaving the original head pointing at its old successor instead of an empty reference | The chain becomes cyclic and traversal never terminates |
| Treating the holder node as data | Returning the dummy holder rather than its successor | An extra node with no meaningful value appears in the output |
| Three-reference iterative variant | Track previous, current, and cached next explicitly, without a dummy holder | Correct and equivalent; uses one more local reference but performs the same front insertion |
| Recursive variant | Reverse the suffix first, then point the successor back at the current node and clear the current node's old forward reference | Correct and elegant, but consumes $O(n)$ stack space and risks a stack-depth limit on long inputs |
| Copying values into fresh nodes | Building a new chain with the values in reverse order | Produces the right traversal but violates the constant-space and node-identity requirements |
| Two-node input | One iteration creates the new tail, the next makes the old tail the new head | Handled by the general method with no special branch |
| One-node or empty input | The cursor is empty immediately, or the single node's cached successor is empty | The holder's successor is the correct (possibly empty) answer with no special branch |

## 6. Complexity Derivation

Let $n$ be the number of nodes in the input chain.

- **Time.** The loop body executes exactly once per node, because the cursor moves
  to the cached successor each iteration and the suffix shrinks by one. Each body
  performs a constant number of reference reads and writes — one cache, one
  assignment into the node, one assignment to the holder, one cursor advance — and
  no traversal of the segments takes place. The total is therefore
  $\Theta(n)$, i.e. $O(n)$ time, and it is asymptotically optimal because every one
  of the $n$ references must be rewritten for the reversal to be complete.
- **Auxiliary space.** The method stores a fixed number of local references plus a
  single holder node, independent of $n$, so auxiliary space is $O(1)$. The output
  reuses the input nodes and is the same object set, so it is not additional
  storage. The recursive alternative instead uses $O(n)$ auxiliary space for its
  call stack, which is the decisive practical difference between the two correct
  approaches.
- **Derivation from the invariant.** The reversed segment grows by exactly one node
  per iteration and the union of the two segments is always the whole input, so the
  number of iterations is exactly $n$ rather than something that depends on the
  values stored. The bound is therefore tight in the input size and independent of
  the value range, of duplicate values, and of whether the chain is sorted.
