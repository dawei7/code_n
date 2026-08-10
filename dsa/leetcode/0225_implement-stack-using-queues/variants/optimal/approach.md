## General

**Make the queue front behave like the stack top**

A stack removes the most recently pushed element, while a queue removes the
earliest enqueued element. The exact solution reconciles these opposite orders
by doing the reordering during `push`. Between public operations, queue `q1`
stores every stack element from logical top to logical bottom, in front-to-back
queue order. Queue `q2` is empty and serves as temporary storage for the next
push.

For a logical stack whose top-to-bottom order is `[c, b, a]`, `q1` has front
`c`, followed by `b`, then `a`. With that representation, both `pop` and `top`
can use the queue's front directly in constant time.

**Push the new value before all older values**

Suppose `q1` already contains the existing stack in top-to-bottom order. A new
value `x` must become the new top, so the desired new queue order is `x`
followed by all of `q1`'s old contents.

`push` first appends `x` to the back of the empty `q2`. Because it is currently
the only element, it is also at `q2`'s front. The method then repeatedly removes
the front of `q1` with `popleft()` and appends that value to the back of `q2`.
The old elements leave `q1` in their existing top-to-bottom order, so appending
them preserves that relative order behind `x`.

After the transfer, `q2` has exactly the desired sequence and `q1` is empty.
The simultaneous assignment `self.q1, self.q2 = self.q2, self.q1` swaps the
deque objects. The newly ordered deque becomes the permanent `q1`, and the
emptied old deque becomes scratch `q2` for the next call. Swapping references
avoids copying elements back a second time.

**Trace several pushes**

Initially both queues are empty. Pushing 1 appends it to `q2`; there is nothing
to transfer, and the swap leaves `q1 = [1]` and `q2 = []`.

Pushing 2 starts with `q2 = [2]`. Moving the one old element appends 1, giving
`q2 = [2, 1]`. After the swap, the front of `q1` is 2, which is the correct
stack top.

Pushing 3 starts with `q2 = [3]` and transfers 2 followed by 1. The resulting
`q1 = [3, 2, 1]` directly represents last-in-first-out order. A pop removes 3,
the next top is 2, and no further reorganization is necessary.

**Pop, top, and empty become direct queue operations**

Because the representation keeps the stack top at `q1`'s front:

- `pop` calls `q1.popleft()`. It removes and returns the top element. The
  remaining queue already begins with the next-most-recent pushed element, so
  the representation remains valid.
- `top` returns `q1[0]`. This reads the front without removing it. Index zero
  is just a peek at a standard queue endpoint; the implementation never uses
  arbitrary interior removal.
- `empty` tests `len(q1) == 0`. All logical elements live in `q1` between
  calls, while `q2` is empty, so this is exactly the stack's emptiness.

The contract guarantees that every `pop` and `top` call is valid. Therefore the
source does not need to catch the error that `popleft()` or `[0]` would raise on
an empty deque.

**Why the representation remains correct**

Initially `q1` is empty, matching an empty stack, and `q2` is empty. Assume
before an operation that `q1` lists the logical stack from top to bottom and
`q2` is empty.

For `push(x)`, placing `x` first and transferring every old element in order
creates exactly the stack after pushing `x`; swapping also restores an empty
`q2`. For `pop`, removing the represented first element removes the logical
top, and the suffix remains in correct order. `top` and `empty` do not mutate
either deque. Thus every supported operation preserves the representation, and
their returned values match a real stack.

**The exact source uses two queues, not the manifest's one-queue rotation**

The manifest summary says this branch rotates one queue after each push. The
executable solution instead keeps `q1` as the main queue and uses `q2` to place
the new value before transferring old elements. It then swaps the two queues.
Both designs make pushes linear and other operations constant, but they are
not the same data flow. This document follows the two-queue source.

The class relies on `collections.deque`, but the source file does not include
the import and assumes the execution environment supplies `deque`.

## Complexity detail

Let $n$ be the number of elements already in the stack before an operation.
`push` performs one append for the new value, then $n$ front removals and $n$
back appends while transferring the old contents. Its time is $O(n)$. Swapping
the two deque references is $O(1)$.

`pop`, `top`, and `empty` each take $O(1)$ time. A sequence of $m$ pushes with
no intervening pops can take $1+2+\cdots+m = O(m^2)$ total transfer work, which
is the tradeoff chosen to make every removal immediate.

Across both deques, the structure stores exactly the logical elements after an
operation and at most the new total during a push, so persistent space is
$O(n)$. The second deque is empty between calls but may temporarily hold all
elements while a push is in progress; it does not change the overall linear
bound.

## Alternatives and edge cases

- **One-queue rotation:** Append `x` to the only queue, then move each older front element to the back so `x` rotates to the front. It satisfies the follow-up, has the same $O(n)$ push and $O(1)$ pop behavior, and matches the manifest summary rather than the exact source.
- **Cheap push, expensive pop with two queues:** Always append to the main queue in $O(1)$; for pop, transfer all but its last element to the second queue. It shifts the linear cost to removals and may be preferable when pushes greatly outnumber pops.
- **Ordinary list as a stack:** Python could append and pop at the same end in amortized $O(1)$ time, but that would evade the requirement to implement the behavior using queue operations.
- **First push:** With no old values to transfer, the new element becomes the front after a constant-time swap.
- **Pop down to empty:** Removing the sole element leaves `q1` empty and `q2` already empty, so `empty()` returns true.
- **Alternating push and pop:** Every push reorders only the current stack contents; every pop immediately removes the new front. The representation does not depend on batching operations.
- **Repeated values:** Position determines stack order. Equal integers remain separate deque entries and are popped once per push.
- **Maximum operation count:** At most 100 calls are made, but the complexity reasoning remains valid for larger sequences.
- **Invalid empty access:** The reference guarantees it does not occur. A reusable production class might raise a documented exception or return a sentinel, but adding that behavior is outside this contract.
- **Queue-operation restriction:** The implementation uses append-to-back, remove-from-front, front peek, size, and emptiness only. The reference swap exchanges queue identities and does not violate FIFO access.
