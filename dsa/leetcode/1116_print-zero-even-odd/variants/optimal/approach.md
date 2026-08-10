## General

**Model the next allowed callback with three permits**

The required sequence alternates zero with the integers one through `n`:

`0, 1, 0, 2, 0, 3, ...`.

Three threads own different callback types, so a semaphore for each role represents whether that role may print.

`z` starts with one permit, allowing zero to begin. `o` and `e` start at zero, forcing both number threads to wait. At every later moment, the thread that just printed releases exactly the role that should run next.

**The zero thread chooses odd or even**

The zero loop has `n` iterations, one for every integer that must follow a zero. It first acquires `z`, consuming the only zero permit, and calls `printNumber(0)`.

Loop index `i` is zero-based, while the next actual integer is `i + 1`. When `i` is even, `i + 1` is odd, so the code releases `o`. When `i` is odd, the next number is even, so it releases `e`.

The release occurs only after the zero callback returns. Therefore, the chosen number cannot print before its preceding zero has completed.

**The odd and even threads print disjoint sequences**

The odd loop visits one, three, five, and so on through `n`. Before each value, it acquires `o`. Only the zero iteration immediately preceding that odd value can supply the permit.

After printing, odd releases `z`, allowing the next zero.

The even loop is symmetric: it visits two, four, six, and so on, waits on `e`, prints its current value, and returns permission to zero.

Because the loops generate their own values, neither number thread needs a shared counter. Their ranges are disjoint and together contain every integer from one through `n` exactly once.

**The handoff invariant**

Initially, only zero has one permit. After zero prints for iteration `i`, only the semaphore matching parity of `i + 1` receives a permit. After that number prints, only zero receives a permit again.

Thus the permitted roles cycle:

`zero -> correct number -> zero -> correct number`.

No thread can print twice consecutively. Zero consumes its permit before printing and cannot continue until a number releases it. A number thread consumes its parity permit and cannot continue until a later zero releases another.

**Why arbitrary scheduling is harmless**

Odd or even may start first, but each blocks on a zero-count semaphore. If zero receives repeated CPU time, it still blocks at its next `z.acquire()` after handing control away. If the wrong number thread is scheduled, its semaphore remains zero.

The operating system controls when runnable threads execute, but the permit state controls which role is runnable. Delays may slow output, but they cannot reorder it.

**Progress and termination**

There is always one logical next role. Zero enables exactly one number thread, and every enabled number thread returns permission to zero. There is no circular dependency in which all three wait without an available permit during normal execution.

The zero loop executes $n$ times. Odd and even loop counts add to $n$, so every zero handoff has exactly one consuming number iteration. After the final integer prints, it releases a zero permit that is no longer needed because the zero loop is complete; this harmless leftover permit cannot produce extra output.

The callbacks are assumed to return normally. An exception before the next release could strand another thread, which is outside the contract.

## Complexity detail

There are $n$ zero callbacks and $n$ number callbacks. Every callback is surrounded by a constant number of semaphore operations, so total algorithmic work is $O(n)$.

The reviewed complexity criterion is constant synchronization work per emitted value. The implementation does not rescan previous output or retain a growing history.

Three semaphore objects, the stored limit, and loop variables use $O(1)$ space. Output is emitted through callbacks rather than buffered by the class.

Scheduler waiting affects elapsed time but does not add algorithmic iterations. Semaphore acquire blocks rather than busy-spinning.

## Alternatives and edge cases

- **Condition variable with next-role state:** Store whether zero, odd, or even should run and notify after each callback. It is flexible but requires guarded wait loops.
- **Locks as gates:** Three one-use handoff locks can implement the same cycle, though semaphores express repeatable permits naturally.
- **Busy-wait flags:** Polling wastes CPU and still requires synchronization for visibility.
- **One shared number counter:** Zero could inspect a shared next integer and wake parity accordingly. The separate ranges here avoid extra shared mutation.
- **`n = 1`:** Zero prints, releases odd, odd prints one, and all loops finish.
- **Even `n`:** The final number callback belongs to the even thread.
- **Odd `n`:** The final number callback belongs to the odd thread.
- **Number thread starts first:** It blocks safely until zero releases its permit.
- **Zero scheduled repeatedly:** It cannot pass its next acquire without a number handoff.
- **Wrong parity thread scheduled:** Its semaphore remains zero, so it cannot print out of turn.
- **Release after callback:** Moving a release before printing would permit overlap and break the completed-output order.
- **Leftover final zero permit:** No zero-loop iteration remains, so it creates no extra output.
- **Callback exception:** Normal completion is assumed for progress.
