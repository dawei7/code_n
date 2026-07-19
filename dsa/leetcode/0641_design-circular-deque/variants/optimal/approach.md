## General
**Represent the occupied circular segment**

Allocate exactly `k` array slots. Track `front`, the index of the first live value, and `size`, the number of live values. Empty means `size = 0`, while full means `size = k`, so wrapped indices never make those states ambiguous.

**Derive both insertion positions**

For a front insertion, decrement `front` modulo `k` and write there. The next rear insertion belongs at `(front + size) % k`, immediately after the current occupied segment. Increment `size` only after a successful insertion.

**Delete by moving boundaries**

Deleting the front advances `front` modulo `k`; deleting the rear only decrements `size`. Existing values outside the live segment need not be erased. When nonempty, the rear value is at `(front + size - 1) % k`.

**Why both endpoint orders remain correct**

The live deque is always `size` consecutive circular positions beginning at `front`. Front operations extend or shrink that segment at its first position, while rear operations extend or shrink its other boundary. Each successful operation preserves this representation, so the derived endpoint indices always identify the logical first and last values.

## Complexity detail
Every one of the `Q` method calls performs a constant number of state checks, modular arithmetic operations, or array accesses, giving $O(Q)$ total time and $O(1)$ time per call. The fixed backing array uses $O(k)$ space.

## Alternatives and edge cases
- **Doubly linked list with head and tail:** supports every operation in $O(1)$ time and tracks capacity with a count, but allocates nodes individually.
- **Singly linked list without a tail:** front operations remain constant-time, but rear insertion or deletion requires traversal and can make a trace quadratic.
- **Dynamic language deque:** provides the operations directly, but the exercise requires implementing the bounded behavior and failure conditions.
- Capacity one must distinguish empty and full even though front and rear refer to the same slot.
- Insertion on a full deque returns false without overwriting an endpoint.
- Deletion on an empty deque returns false, and endpoint queries return `-1`.
- Repeated deletions and insertions must wrap indices and reuse freed slots.
