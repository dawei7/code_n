## General

**Store the minimum for every stack prefix**

Represent each entry as `(value, prefix_minimum)`, where `prefix_minimum` is the smallest value from the bottom of
the stack through that entry. The first pushed value is its own prefix minimum. Every later push stores the smaller
of the new value and the previous top entry's prefix minimum.

This representation makes each query local. `top` reads the value in the final pair, while `getMin` reads its
prefix minimum. A pop removes one complete pair, exposing an earlier pair whose stored minimum is already correct
for the shortened stack. Repeated minimum values are safe because each depth carries its own snapshot.

The prefix property holds after every push by construction. A pop cannot invalidate it for any remaining entry, so
the final pair always describes both the current top and the minimum of the entire live stack.

The app-local `solve` function adapts the operation stream to the same `MinStack` methods used by the native source
and records one output for each operation.

## Complexity detail

Every class operation performs a constant number of list accesses, comparisons, or updates, so `push`, `pop`,
`top`, and `getMin` each take $O(1)$ time. For $n$ live values, the stored pairs use $O(n)$ space. Processing a
sequence of $q$ operations consequently takes $O(q)$ total time.

## Alternatives and edge cases

- **Compute the minimum on demand:** `min(stack)` makes each `getMin` call take $O(n)$ time and violates the
  per-operation contract.
- **Separate value and minimum stacks:** has the same asymptotic bounds but must keep duplicate minima synchronized
  correctly during pushes and pops.
- **Encode the minimum through arithmetic differences:** can store one integer per depth, but is less direct and can
  overflow in fixed-width languages.
- Equal minimum values need independent snapshots so one copy remains available after another is popped.
- Values may be negative or at either 32-bit boundary; comparisons require no sentinel.
- The contract guarantees that `pop`, `top`, and `getMin` are never called on an empty stack.
