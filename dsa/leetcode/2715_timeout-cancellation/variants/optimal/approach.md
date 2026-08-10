## General

**Schedule once and return control over that schedule**

`cancellable(fn, args, t)` immediately registers one timer:

`setTimeout(() => fn(...args), t)`.

The returned value from `setTimeout` is stored in `timer`. That handle identifies the pending callback to the JavaScript timer system.

The function then returns a cancellation closure rather than waiting for the timeout itself.

**Why the callback is wrapped in an arrow function**

`setTimeout` needs a zero-argument callback to run later.

The arrow function captures `fn` and `args` from `cancellable`'s lexical scope. When the timer expires, it invokes the target with:

`fn(...args)`.

Spreading passes the array elements as separate positional arguments in their original order.

**The returned closure captures the timer handle**

The cancel function executes `clearTimeout(timer)`.

Although `cancellable` has already returned, closure semantics retain access to its local `timer` binding.

The caller does not need to know or store the environment-specific handle; invoking the returned function is enough.

**Cancellation before the deadline**

If `clearTimeout` runs while the timer is still pending, the timer system removes that scheduled callback.

The arrow function never runs, so `fn` is never invoked and produces no result.

This is the second example's behavior when cancellation occurs at 50 ms and execution was scheduled for 100 ms.

**Cancellation after execution**

If the timeout has already fired, `fn` has already been called. Clearing the old handle cannot undo a completed function call or retract its return value.

The cancellation closure is still safe to invoke, but it has no effect on past execution.

This explains why a cancel scheduled at 50 ms does not prevent an `fn` timer that ran at 20 ms.

**Trace argument forwarding**

Suppose `fn` multiplies two parameters, `args = [2, 4]`, and `t = 30`.

At the timer event, spread syntax calls `fn(2, 4)` rather than `fn([2, 4])`. The result is eight.

If cancellation occurs only at 100 ms, the 30 ms callback has already executed.

**Only one execution can occur**

`setTimeout` schedules a one-shot callback, not an interval.

If not canceled, it fires at most once. The returned cancel function does not create, restart, or reschedule any timer.

Repeated calls to the cancel function therefore cannot cause extra target executions.

**Repeated cancellation is harmless**

Calling `clearTimeout` more than once with the same handle is safe.

After the pending timer has been removed, later clear calls simply have no scheduled callback to remove. No explicit `cancelled` Boolean is necessary for the required behavior.

**Timer delay is a minimum scheduling delay**

JavaScript timers arrange for the callback to become eligible after approximately `t` milliseconds.

The event loop may run it slightly later if other work is active. The algorithm guarantees scheduling and cancellation relationships, not real-time precision to the exact millisecond.

The challenge harness accounts for ordinary timer behavior.

**Boundary-time ordering**

If cancellation and target execution are both scheduled for the same effective time, event-loop queue order determines which callback runs first.

The implementation does not add a timestamp comparison. Whichever timer task acts on the pending handle first determines whether `fn` executes.

This is standard `setTimeout` and `clearTimeout` behavior.

**Receiver semantics**

The target is called as `fn(...args)`, not with `apply` and a captured receiver.

The contract supplies a function and arguments but no requested `this` context. Regular functions therefore receive the environment's ordinary standalone-call receiver semantics, while arrow functions keep their lexical receiver.


The one timeout schedules exactly one future invocation of `fn` with the supplied arguments.

The returned closure holds the exact timer handle. Invoking it before dispatch removes that pending invocation; invoking it afterward cannot affect the already completed call.

These are precisely the two cases required by the contract, so the result is correct.

**Why no promise is needed**

The interface is callback-based and asks only for a cancel function.

Wrapping the timer in a Promise would not make native promise execution cancelable and would require additional state. Direct access to the timeout handle is the proper mechanism.

## Complexity detail

Registering or clearing one timer is treated as $O(1)$ time and the closure stores $O(1)$ persistent state. The target function's own runtime is excluded.

With $a$ arguments, spreading them at execution takes $O(a)$ call-setup time. The solution stores a reference to the existing `args` array rather than copying it, so its own additional space remains $O(1)$ under the bounded-argument contract.

## Alternatives and edge cases

- **Boolean cancellation flag:** The timer can check a flag before calling `fn`, but the callback still wakes; `clearTimeout` removes it directly.
- **Promise wrapper:** Does not inherently cancel the underlying timer.
- **`setInterval`:** Incorrect because it can call `fn` repeatedly.
- **Cancel before `t`:** Prevents the target invocation.
- **Cancel after `t`:** Cannot undo an invocation that already ran.
- **Repeated cancel calls:** Harmless for the same timer handle.
- **Several arguments:** Spread preserves order and positional calling.
- **Mutable `args` array:** The callback reads its contents at execution time because the reference is captured.
- **Target throws:** The exception occurs asynchronously in the timer task; cancellation no longer applies after dispatch.
- **Event-loop delay:** Execution may occur later than nominal `t`.
- **Equal scheduling boundary:** Task ordering decides the race.
- **Exactly one timer:** The implementation never reschedules or repeats.
