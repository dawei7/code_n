## General

**Two reversals reconcile stack order with queue order**

A queue must return the oldest element, but a stack exposes the newest element.
The exact solution separates queued values into two phases:

- `stk1` is the incoming stack. Every `push` appends the newest value here.
- `stk2` is the outgoing stack. Its top, `stk2[-1]`, is the oldest value still
  in the queue and therefore the queue front.

Values enter `stk1` in arrival order, with the newest on top. When `stk2` needs
values, repeatedly popping `stk1` and appending to `stk2` reverses that order.
The value that arrived earliest was at the bottom of `stk1`, so it moves last
and ends on top of `stk2`, ready to leave first.

**Push never performs a transfer**

`push(x)` simply executes `stk1.append(x)`. This is a standard push-to-top
stack operation and takes constant time. The method does not try to place `x`
directly behind values already in `stk2`; the division between stacks already
encodes the needed chronology.

If `stk2` contains elements, all of them were pushed before every value still
in `stk1`. They must therefore be popped first. New pushes can accumulate in
`stk1` without disturbing the established front order in `stk2`.

**Transfer only when the outgoing stack is empty**

Both `pop` and `peek` call `move`. That helper first checks `if not self.stk2`.
Only when no already-reversed values remain does it move every element from
`stk1` to `stk2`.

Avoiding a transfer while `stk2` is nonempty is essential. Suppose older values
are already waiting in `stk2` and newer pushes are in `stk1`. Moving those new
values onto `stk2` would place them above the older front and violate FIFO
order. Waiting until `stk2` empties ensures one complete older batch is served
before the next batch is reversed.

After a transfer, `stk1` is empty. The oldest value in that batch is at
`stk2[-1]`, the next-oldest is directly below it in pop order, and the newest is
at the bottom. Repeated pops naturally produce arrival order without further
movement.

**Pop and peek share preparation but differ in mutation**

After `move` establishes an outgoing top:

- `pop` returns `stk2.pop()`, removing the oldest queued value.
- `peek` returns `stk2[-1]`, reading that same value without removal.

The contract guarantees that both operations are called only on a nonempty
queue. Thus, after `move`, `stk2` is guaranteed to contain a value, and the
source needs no empty-access branch.

Calling `peek` repeatedly does not repeatedly transfer values. The first call
may fill `stk2`; later calls see it nonempty and perform only constant work.

**Trace interleaved operations**

After `push(1)`, `push(2)`, and `push(3)`, `stk1` is `[1, 2, 3]` from bottom to
top, and `stk2` is empty. The first `peek` triggers a transfer: 3 moves first,
then 2, then 1, leaving `stk2 = [3, 2, 1]`. Its top is 1, the queue front.

If `push(4)` now occurs, 4 goes into `stk1`, while `stk2` still contains the
older values 3, 2, and 1 in reverse storage order. Pops return 1, then 2, then
3. Only after `stk2` becomes empty does a later pop transfer 4 and return it.
This demonstrates why the two batches need not be merged eagerly.

**Empty must inspect both stacks**

At different moments, queued values may reside entirely in `stk1`, entirely in
`stk2`, or across both. The queue is empty only when both are empty, which the
source expresses as `not self.stk1 and not self.stk2`. Checking just one stack
would misclassify a valid intermediate state.

**Why the representation always produces FIFO order**

Within `stk2`, top-to-bottom pop order is oldest to newest for the transferred
batch. Every value in `stk2` is older than every value in `stk1`, because no
new transfer occurs until `stk2` empties. Therefore the top of `stk2`, whenever
present, is the oldest value in the entire queue.

If `stk2` is empty, reversing all of `stk1` places that stack's oldest value on
top and establishes the same property. `push` adds only a new newest value,
`peek` observes the oldest, and `pop` removes it. These operations preserve the
representation after every call.

## Complexity detail

`push` and `empty` take $O(1)$ time. A particular `pop` or `peek` can take
$O(n)$ worst-case time when `move` transfers $n$ values. However, each queued
value is pushed onto `stk1` once, popped from `stk1` once, pushed onto `stk2`
once, and eventually popped from `stk2` once. It is never transferred back.

Across any sequence of operations, total stack work is linear in the number of
pushes and pops. Consequently `pop` and `peek` have amortized $O(1)$ time, and
the manifest's $O(1)$ operation claim must be understood as amortized rather
than worst-case for each individual call.

If the queue contains $n$ values, the two stacks contain $n$ entries in total,
so space is $O(n)$. A transfer changes which list owns each reference but does
not duplicate all values simultaneously.

## Alternatives and edge cases

- **Expensive push, cheap pop:** Move all existing values around every new value so one stack's top is always the queue front. Pop becomes worst-case $O(1)$, but each push costs $O(n)$ and a long push sequence becomes quadratic.
- **One stack plus recursion:** Temporarily pop values recursively to reach the oldest element, then restore newer ones. It uses call-stack space, repeats work across removals, and is less efficient than two persistent phases.
- **Ordinary deque:** It directly supports queue operations in constant time, but using it would avoid the exercise's two-stack constraint.
- **First pop after many pushes:** This is the expensive operation that transfers the whole incoming batch, but later pops from that batch are constant time.
- **Peek before pop:** A transfer performed by `peek` is useful preparation, not wasted work; the following `pop` reuses the outgoing order.
- **Push while `stk2` is nonempty:** The new value waits in `stk1` because every outgoing value is older and must leave first.
- **Pop the last outgoing value while incoming values wait:** That pop returns the correct older value. The next `pop` or `peek` triggers transfer of the waiting newer batch.
- **Repeated values:** Stack positions preserve arrival order even when values are equal; each pushed occurrence is stored and removed separately.
- **Valid-access guarantee:** Empty `pop` and `peek` do not occur. A production queue might raise an explicit exception, but the challenge requires no additional policy.
- **Stack-operation restriction:** Python list `append`, `pop`, `[-1]`, and truth testing correspond to push, pop, top, and empty checks. No bottom or interior element is accessed.
