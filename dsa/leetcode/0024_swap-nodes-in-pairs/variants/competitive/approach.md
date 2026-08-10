## General

**Keep a pointer immediately before the pair being swapped**

Swapping two adjacent linked-list nodes requires changing three connections: the preceding chain must point to the second node, the second node must point to the first, and the first must point to the node after the pair. The competitive implementation performs those changes iteratively.

The important cursor is `current`. At the start of each iteration, `current` points to the node immediately before the next unswapped pair. After the swap, it moves to the tail of that pair, which is again immediately before the following pair.

**Use a dummy predecessor for the first pair**

The source creates

```python
dummy = ListNode(0)
dummy.next = head
current = dummy
```

Without `dummy`, the first pair would have no real predecessor, and swapping it would require a special update to the external head variable. The dummy supplies a uniform predecessor. Its value `0` is never inspected and the dummy is excluded by returning `dummy.next`.

This also handles an empty list naturally: `dummy.next` is `None`, the loop does not run, and the return is `None`.

**Enter the loop only for a complete pair**

The condition

```python
while current.next and current.next.next:
```

requires both the first node after `current` and that node's successor. Python short-circuits `and`, so `current.next.next` is not evaluated when `current.next` is `None`.

If no nodes remain, the algorithm is finished. If exactly one remains, it is the required unpaired final node and must keep its current link. The loop condition therefore encodes both termination cases without separate branches.

**Save all three relevant positions before mutation**

Inside the loop, the exact source assigns

```python
next_one, next_two, next_three = (
    current.next,
    current.next.next,
    current.next.next.next,
)
```

These names mean the first node of the pair, the second node, and the node immediately after the pair. `next_three` may be `None`. Python evaluates all right-hand expressions before binding the left-hand names, so all three references describe the original local structure before any link is overwritten.

Saving `next_three` is crucial. Once `next_two.next` points backward to `next_one`, following the old forward chain through `next_two` would no longer reach the remainder safely.

**Perform the three-link rotation**

The assignments are

```python
current.next = next_two
next_two.next = next_one
next_one.next = next_three
```

The first connects the already processed prefix to the new head of the pair. The second puts the original first node after it. The third reconnects that original first node—the pair's new tail—to the untouched remainder.

Before the change, the local chain is

```text
current -> next_one -> next_two -> next_three
```

After all three assignments, it is

```text
current -> next_two -> next_one -> next_three
```

Values are never assigned, so the node objects truly exchange positions as required.

There may be a brief intermediate state that is not a valid complete list while these statements execute. Correctness concerns the state after all saved references have been used; saving the nodes first makes each update independent of that transient shape.

**Advance to the next pair's predecessor**

After swapping, `next_one` is the tail of the processed pair. The source sets

```python
current = next_one
```

Its `next` is `next_three`, the first unprocessed node. Thus the loop invariant is restored: `current` again sits immediately before the next possible pair.

Advancing to `next_two` instead would be wrong because `next_two` is the pair's new head; the next iteration would overlap the pair just processed. Advancing directly to `next_three` would also lose the predecessor needed to attach the next swapped pair.

**Trace `[1, 2, 3, 4]`**

Initially `current` is the dummy. The saved nodes are `1`, `2`, and `3`. Rewiring produces `dummy -> 2 -> 1 -> 3 -> 4`, then `current` becomes node `1`.

The next saved nodes are `3`, `4`, and `None`. Rewiring produces `dummy -> 2 -> 1 -> 4 -> 3 -> None`, and `current` becomes node `3`. It has no successor, so the loop ends. Returning `dummy.next` gives `[2, 1, 4, 3]`.

For `[1, 2, 3]`, the first swap produces `2 -> 1 -> 3` and moves `current` to `1`. Now `current.next` exists but `current.next.next` does not, so node `3` is left untouched.

**The loop invariant proves correctness**

At each iteration start, every node through `current` is already arranged as correctly swapped pairs, `current` is the processed prefix's tail, and the suffix beginning at `current.next` remains in original order. The three-link rotation correctly swaps the first two suffix nodes without changing any later node. Moving `current` to the pair's new tail extends the processed prefix by exactly two and restores the invariant.

When the loop stops, fewer than two nodes remain. A zero-node suffix needs no work; a one-node suffix is correctly unpaired. The entire chain after the dummy therefore satisfies the requested transformation.

## Complexity detail

Let $n$ be the number of input nodes.

- **Time complexity: $O(n)$.** Each iteration processes exactly two previously unprocessed nodes and performs a fixed number of reference reads and assignments. There are $\lfloor n/2\rfloor$ iterations.
- **Auxiliary space: $O(1)$.** The implementation allocates one dummy node and holds a constant number of node references. It uses no recursion and no collection whose size grows with the input. The returned list consists of the original nodes.

The method mutates the list in place. Constant auxiliary space does not mean the operation is non-mutating; it means no input-sized additional storage is used.

## Alternatives and edge cases

- **Recursive pair processing:** Recursively swap the suffix and attach the current reversed pair. It is concise but consumes $O(n)$ call-stack space in the exact Python implementation.
- **Value swapping:** Exchanging `val` fields would leave nodes in place and violates the explicit requirement.
- **Allocate a replacement chain:** It avoids link mutation but requires $O(n)$ new nodes and changes node identity.
- **Empty list:** The first `and` operand is false, so the loop is skipped safely.
- **Single node:** The second link does not exist; the node remains the returned head.
- **Two nodes:** One iteration swaps them, with `next_three = None` terminating the new tail.
- **Odd node count:** The last node remains after `current`; the loop condition deliberately leaves it unchanged.
- **Even node count:** Every node belongs to exactly one processed pair.
- **Equal values:** Nodes are swapped by position regardless of equal values, fulfilling the structural contract.
- **Dummy value collision:** Input nodes may also have value zero; the dummy's value is never compared and never returned, so this is irrelevant.
- **Assignment order:** The three nodes are saved before any mutation. Recomputing `next_three` after reversing a link could lose the suffix or create a cycle.
- **Use the return value:** The first pair's second node becomes the new head, so the original `head` reference is generally no longer the correct starting point.
- **Cyclic lists outside the contract:** The loop could fail to terminate; the proof assumes the supplied finite acyclic chain.
