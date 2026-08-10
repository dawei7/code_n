## General

Four threads share one sequence position. At each integer, exactly one thread is responsible for the output token. The challenge is not deciding ordinary Fizz Buzz; it is ensuring that concurrent callbacks run once each, in increasing numerical order, without busy waiting or deadlock.

The solution stores:

- `self.current`, the next integer whose token has not been printed;
- `self.n`, the inclusive final integer;
- one shared `Condition` that protects `current` and lets ineligible threads sleep.

A condition variable combines a lock with a wait-and-notify mechanism. Entering `with self.condition` acquires its lock. Calling `wait()` atomically releases that lock while sleeping and reacquires it before returning. Calling `notify_all()` wakes waiting threads so they can recheck their predicates once the notifier releases the lock.

**Express each thread’s ownership as a predicate**

All four public methods call the same helper, `_run`, with a predicate and an action.

The fizz predicate accepts values divisible by three but not five. The buzz predicate accepts values divisible by five but not three. The fizzbuzz predicate accepts values divisible by 15. The number predicate accepts values divisible by neither three nor five.

These categories are mutually exclusive: one value cannot satisfy two predicates. They are also exhaustive: every positive integer belongs to exactly one. This partition is the foundation for safe coordination because at every `current <= n`, exactly one worker is eligible.

The string-output wrappers adapt callback signatures. `_run` supplies the current integer to every action. Fizz, buzz, and fizzbuzz use lambdas that ignore that argument and call their zero-argument print functions. The number thread passes `printNumber` directly because that callback needs the integer.

**Wait in a loop until this thread owns the current value**

Each worker acquires the condition lock and enters an outer loop while work remains. If its predicate is false for `current`, it executes:

`while self.current <= self.n and not predicate(self.current): self.condition.wait()`.

The inner test is a `while`, not an `if`. A waiting thread can wake because another value was printed even though the new value belongs to a different thread. Condition waits can also wake spuriously. In either case, rechecking under the lock prevents the wrong callback from running.

Waiting releases the condition lock. Therefore, an ineligible thread does not prevent the one eligible worker from acquiring the lock and making progress.

**Print and advance as one protected transition**

Once the predicate is true, the worker still holds the condition lock. It calls `action(self.current)`, increments `current` by one, and calls `notify_all()`.

Holding the lock through the callback and increment gives the operation a clear order. No second worker can inspect the same current value between deciding ownership and advancing it. The callback for value `i` completes before `current` becomes `i + 1`, so output tokens remain in numerical sequence.

Waking every worker is simple and safe. At most one predicate matches the new value; all other awakened workers return to waiting. With exactly four threads, this constant amount of extra wake-up work does not change linear complexity.

**Terminate every worker cleanly**

After the worker responsible for `n` prints, it increments `current` to `n + 1` and notifies all waiters. A waking thread sees that `current <= n` is false, skips the predicate wait, and returns at the explicit `if self.current > self.n` check. The processing thread itself reaches the top of the outer loop, sees that work is finished, and exits the `with` block.

A thread that starts only after completion acquires the lock, finds the outer condition false, and also returns normally. The final notification is important for threads already asleep; without it, they could remain blocked even though no future value would ever satisfy their predicates.

**Why the output is exact**

Initially, `current = 1`. Assume all tokens below `current` have been printed exactly once in order. Exactly one predicate matches `current`. Only its worker can leave the inner waiting loop, and the shared lock prevents any other callback from acting concurrently on that value. That worker invokes the correct callback, increments by exactly one, and notifies the others. The induction statement now holds for the next value.

This continues until `n` is printed. No value can be skipped because `current` advances only after its responsible action. No value can be duplicated because the lock allows only one action before the increment. Predicate definitions produce the correct Fizz Buzz token. Termination occurs only after all values one through `n` have been processed.

The playbook’s scalable workload is terminal integer $n$, with reviewed tiers 1, 10, and 50. The algorithm performs one coordinated state transition per emitted token; it does not rebuild or rescan the preceding output.

## Complexity detail

For each integer from one through $n$, the solution runs one output callback, increments one shared counter, and performs one notification. `notify_all` can wake the other three fixed workers, each of which performs a constant predicate check and may wait again. Because the thread count is fixed at four, total synchronization work is $O(n)$.

Wall-clock waiting time depends on thread scheduling and callback execution. Complexity describes computational and synchronization steps, not a guarantee that the scheduler wakes the eligible thread immediately.

The object stores one counter, one limit, one condition object, and fixed callback/predicate state on four worker stacks. No data structure grows with $n$, so shared auxiliary-space complexity is $O(1)$. The externally captured output contains $n$ tokens, but that required judge output is not stored by this class itself.

## Alternatives and edge cases

- **Four semaphores with explicit handoff:** The current worker could release the semaphore for the next category. This can avoid waking all threads but requires routing logic after every integer and careful termination signaling.
- **Busy-wait on a shared counter:** Repeated predicate checks waste CPU and require additional memory-visibility synchronization. A condition variable provides blocking waits.
- **One worker prints everything:** It would be simpler but violates the required four-method, four-thread interface.
- **Use `if` around `wait`:** This is unsafe because notifications are not promises that the awakened thread’s predicate is now true, and spurious wakeups are permitted. The condition must be rechecked in a loop.
- **`n = 1`:** The number thread prints one, advances to two, and wakes every other worker so all methods terminate.
- **Multiples of 15:** The fizz and buzz predicates explicitly exclude the other divisor, leaving `fizzbuzz` as the sole eligible worker.
- **Scheduler starts threads in any order:** Ineligible starters wait and release the lock. Eventually the worker matching `current` can run.
- **Final notification:** After processing `n`, waking all waiters lets them observe `current > n` and return instead of sleeping forever.
- **Callback executed under the lock:** This preserves token order and single ownership. It assumes callbacks are short and do not recursively require the same coordination object.
- **Spurious wakeup:** The nested predicate loop simply sends the thread back to sleep without producing an incorrect token.
- **Progress assumption:** As with ordinary condition-variable algorithms, a runnable eligible thread must eventually be scheduled. The code introduces no circular lock dependency.
- **No output buffering in the class:** The provided callbacks own printing or capture. The class coordinates when to invoke them and does not accumulate the sequence itself.
