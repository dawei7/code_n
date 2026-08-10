## General

**Turn ordering requirements into two closed gates**

Three threads may begin in any scheduler order, but the callbacks must complete in the sequence first, second, third. There are two dependencies:

- `second` must wait until `first` has finished printing.
- `third` must wait until `second` has finished printing.

The class represents these dependencies with locks `l2` and `l3`. Both are acquired during construction, before worker methods run, so both later stages begin behind closed gates.

**Let the first stage run immediately**

`first` does not acquire a gate. Regardless of when its thread is scheduled, it can call `printFirst`.

Only after that callback returns does it call `self.l2.release()`. This placement is essential. Releasing before the callback would allow the second thread to print while the first callback had not completed, breaking the required output order.

Releasing `l2` opens exactly the gate on which `second` waits.

**Block the second stage until first completes**

`second` begins with `self.l2.acquire()`. Because the constructor already holds that lock, a second thread scheduled too early blocks rather than printing.

After `first` releases the lock, the acquire succeeds. The second callback runs, and only after it returns does `second` release `l3`. This establishes the next happens-before relationship.

The method does not release `l2` afterward. Each of the three methods is called exactly once, so that gate has no future consumer and does not need to be reusable.

**Block the third stage until second completes**

`third` waits on `self.l3.acquire()`. Its lock cannot become available until `second` has acquired the first gate, completed `printSecond`, and released the second gate.

Therefore, when `printThird` runs, both earlier callbacks have completed in order. No final release is necessary because no fourth stage waits.

**Why arbitrary scheduling cannot break the sequence**

If the third thread starts first, it blocks on `l3`. If the second starts first, it blocks on `l2`. The first thread is the only one initially able to pass its method body.

After first prints, exactly the second gate opens. Third remains blocked. After second prints, the third gate opens. Scheduler delays may insert waiting time between stages, but they cannot reverse the callback order.

All six possible method launch permutations therefore converge to `firstsecondthird`.

**A Python lock detail**

The constructor acquires the locks, while worker methods release them from other threads. Python’s primitive `threading.Lock` is not owner-bound: a lock may be released by a thread different from the one that acquired it. That property makes this gate pattern legal.

An owner-tracking reentrant lock would not be an interchangeable choice here because cross-thread release would violate its ownership rules.

**Progress and safety**

Safety means no later callback can run too early, which follows from the two locked gates. Progress means waiting threads eventually continue when the preceding callback completes. Each successful stage releases exactly the next required gate, so no circular wait exists.

The argument assumes the supplied callbacks return normally. If one raised an exception before its release, a later thread could remain blocked; callback failure handling is outside the source contract.

## Complexity detail

The repository classifies this package as bounded concurrency: exactly three calls and all six launch permutations form a fixed legal domain. Each method performs one callback and at most one acquire or release, so total algorithmic work is $O(1)$.

Two lock objects and no input-sized collection are stored, giving $O(1)$ space. A blocked acquire may suspend a thread, but it does not busy-wait or repeatedly scan state.

The important complexity property is constant synchronization work per transition. Wall-clock duration depends on scheduler delays and callback execution time, not on additional algorithmic loops.

## Alternatives and edge cases

- **Semaphores:** Initialize the second and third stage permits to zero, then release them in sequence. This expresses the same two gates and does not rely on lock ownership semantics.
- **Events:** One event can signal completion of first and another completion of second. Events are readable for one-way, one-use notifications.
- **Condition variable with stage counter:** Wait until a shared stage reaches the required number, update it, and notify. It is more general but more code for three fixed stages.
- **Busy waiting on flags:** Repeatedly checking shared booleans wastes CPU and still needs memory-visibility synchronization.
- **Calling methods in apparent input order:** Incorrect because operating-system scheduling, not input presentation, determines actual execution.
- **Third starts first:** It blocks on `l3` until both preceding callbacks finish.
- **Second starts first:** It blocks on `l2` until first finishes.
- **First starts last:** The other two wait safely; once first runs, the gates open in sequence.
- **Release after callback:** Moving either release before its print callback would permit overlapping or reversed output.
- **Exactly one call per method:** The locks are one-use gates and are not reset for repeated cycles.
- **Callback exception:** It can prevent the next release and cause a wait; the contract assumes normal callbacks.
- **No final unlock:** Nothing follows third, so leaving `l3` acquired after the successful wait is harmless.
