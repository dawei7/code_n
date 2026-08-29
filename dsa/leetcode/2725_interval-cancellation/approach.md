## General

**The schedule has one immediate call and one repeating timer**

The required timeline begins at time zero, but `setInterval` schedules its first callback only after roughly `t` milliseconds. Therefore the exact solution separates the immediate execution from the repeating schedule.

It first calls `fn(...args)` synchronously. The spread syntax expands the array so that each entry becomes a positional argument, matching calls such as `fn(2, 5)` rather than passing one array argument.

Only after that first call returns does the code create the interval.

**Create the repeating callback**

`setInterval(() => fn(...args), t)` registers an arrow-function callback with the host timer system. After at least approximately `t` milliseconds, the event loop may run that callback, which invokes `fn` with the same arguments. The timer continues requesting another callback at each interval until cleared.

The arrow function is necessary because passing `fn` alone would not supply `args`. It also delays the call: `fn(...args)` is executed only when the timer callback runs.

**Keep the interval handle**

`setInterval` returns an interval identifier. The code stores it in `intervalId`. That handle identifies this particular repeating schedule among every timer the environment may be managing.

Without preserving the handle, the returned cancel function would have no reliable way to tell the host which interval to stop.

**Return a closure as the cancellation capability**

The returned function is:

`() => clearInterval(intervalId)`.

Although `cancellable` has already returned, this arrow function retains access to `intervalId` through a closure. Calling it later asks the timer system to remove future callbacks for that interval.

The caller therefore receives a small capability: it does not need access to the timer ID or the internal setup. It simply invokes `cancelFn` at `cancelTimeMs`.

**Trace the first example**

For `t = 35`, `cancellable` invokes `fn(4)` immediately at about zero milliseconds. It then establishes an interval.

If cancellation occurs at 190 milliseconds, callbacks are eligible around 35, 70, 105, 140, and 175 milliseconds. Each calls `fn(4)`. The next nominal occurrence would be 210 milliseconds, but cancellation at 190 clears the interval first, so it is not scheduled to execute.

Together with the time-zero call, this produces the six invocations shown in the example.

**What cancellation does and does not do**

`clearInterval` prevents future callbacks associated with the handle. It cannot undo calls that have already completed. It also cannot interrupt `fn` in the middle if a callback is currently executing; JavaScript normally runs that callback to completion on its event-loop turn.

Calling the cancel closure more than once is harmless in ordinary timer APIs. Once the interval is cleared, clearing the same handle again has no additional effect.

**Timer delays are not exact deadlines**

The value `t` is a minimum scheduling delay, not a guarantee that callbacks run at mathematically exact timestamps. A busy event loop, timer clamping, or a long-running callback can delay execution.

The algorithm nevertheless expresses the intended semantics: request recurring execution every `t` milliseconds and stop future requests when cancellation occurs. The examples use idealized times for clarity.

**Why setup order matters**

The immediate `fn(...args)` appears before `setInterval`. If the initial function call throws synchronously, `cancellable` exits by throwing and never creates an interval, avoiding a hidden repeating timer after failed setup.

If the first call succeeds, the interval is created and the cancel function is returned. This order exactly matches “call immediately and then every `t` milliseconds.”

**Why the approach is correct**

The direct call supplies the mandatory time-zero invocation with the given argument list. The interval callback supplies all later periodic invocations using the same function and arguments. The saved handle uniquely identifies that schedule, and the returned closure clears it when invoked, preventing later interval callbacks. Therefore `fn` runs immediately and repeatedly until cancellation, exactly as required.

**The return values of fn are not accumulated**

The wrapper neither stores nor returns individual invocation results. The judging harness observes calls and their returned values externally. The contract asks `cancellable` to return the cancel function, so retaining an ever-growing history inside this function would be unnecessary.

## Complexity detail

Let $k$ be the number of times `fn` is invoked before cancellation, including the immediate call, let $A=\lvert\texttt{args}\rvert$, and let $F$ represent the cost of one execution of `fn`.

The wrapper performs argument spreading and one function invocation $k$ times, so total work is $O(k(A+F))$. When treating the supplied function and the constraint-bounded argument list as external constant-cost work, this is summarized as $O(k)$, matching the manifest. Setup and cancellation themselves are $O(1)$ host timer operations.

The wrapper retains one timer ID, one closure, and references to `fn` and `args`, so auxiliary space is $O(1)$ with respect to the number of invocations. It does not accumulate callback records in application memory. The argument array is supplied input rather than a new copy retained per tick.

Elapsed time is governed by the caller's cancellation time, not conventional algorithmic input size.

## Alternatives and edge cases

- **Recursive `setTimeout`:** Can schedule the next callback after each execution and may avoid interval backlog, but requires explicit rescheduling and a stored timeout handle or cancellation flag.
- **Call only through `setInterval`:** Incorrect because the first invocation would be delayed by `t` instead of occurring immediately.
- **Lose the interval ID:** Makes precise cancellation impossible.
- **Cancel before the first interval tick:** The immediate call still occurs, while all delayed repetitions are prevented.
- **Cancel exactly near a tick:** Actual ordering depends on which event-loop task runs first; timer timestamps are not strict simultaneous guarantees.
- **Repeated cancellation:** Clearing an already-cleared interval is harmless.
- **Long-running fn:** A cancellation request cannot preempt a callback already executing.
- **Thrown initial call:** No interval is created because setup has not reached `setInterval`.
- **Thrown later call:** The exception belongs to the timer callback; the wrapper does not catch it or automatically clear the interval.
- **Argument identity:** The same values from `args` are spread on every call; nested objects are passed by reference.
