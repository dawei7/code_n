## General

**Sleeping in JavaScript means postponing completion**

JavaScript should not block the execution thread for the requested number of milliseconds. A busy loop would prevent other work, timers, and callbacks from running.

Instead, `sleep(millis)` returns a Promise whose settlement is scheduled for the future. Callers can either:

- use `await sleep(millis)` inside an asynchronous function, or
- attach a continuation with `sleep(millis).then(...)`.

In both cases, the caller receives an asynchronous pause while the JavaScript runtime remains free to process other work.

**Create a Promise that starts pending**

The expression

`new Promise(r => setTimeout(r, millis))`

constructs a Promise and immediately invokes its executor function. The parameter `r` is the Promise's resolver.

The executor does not call `r` immediately. It passes that resolver to `setTimeout` with delay `millis`. Therefore, the Promise remains pending after construction.

Once the timer becomes eligible and the runtime executes its callback, `r` is called. That resolves the Promise. The resolver receives no argument, so the resolved value is `undefined`, which is allowed because the contract says the Promise may resolve any value.

**What `setTimeout` actually guarantees**

`setTimeout(callback, millis)` schedules the callback no earlier than approximately the requested delay. It does not reserve the JavaScript thread or guarantee execution at an exact wall-clock instant.

After the delay expires, the callback becomes eligible to run. It may wait until:

- the current call stack is empty;
- earlier queued work has completed;
- the runtime's timer resolution and scheduling permit it.

That is why minor positive deviation is acceptable. The solution promises a minimum-style asynchronous delay, not a hard real-time deadline.

For the challenge's values from one through 1000 milliseconds, ordinary timer scheduling directly models the requirement.

**Why the function is declared `async`**

An `async` function always returns a Promise. Here, the body explicitly returns another Promise.

JavaScript's async return semantics adopt the returned Promise's state rather than immediately wrapping it as an already-resolved nested Promise. The Promise returned to the caller therefore remains pending until the timer-backed Promise resolves.

The `async` keyword is not strictly necessary: a normal function returning `new Promise(...)` would behave equivalently for this contract. It does, however, make the asynchronous interface explicit.

**Follow one call through the event loop**

Suppose code records the current time and calls `sleep(100)`.

1. `sleep` constructs a pending Promise.
2. Its executor registers the resolver with a timer for approximately 100 milliseconds later.
3. `sleep` returns a Promise immediately; the JavaScript thread does not wait synchronously.
4. Other synchronous code may continue.
5. After at least the requested delay, the timer callback enters the task queue.
6. When the call stack becomes free, the callback invokes the resolver.
7. Promise continuations become eligible as microtasks and observe the elapsed time.

This sequence explains why the example prints about 100 rather than why the function itself spends 100 milliseconds executing instructions.

**Why resolving is enough**

A Promise has two terminal states: fulfilled and rejected. Sleeping is not a computation that needs to produce data, so fulfillment with `undefined` is sufficient.

The solution does not need an explicit `return` inside the timer callback. Passing the resolver itself is equivalent to using `() => r()` because `setTimeout` invokes it as a function when the timer fires.

Calling the resolver exactly once settles the Promise exactly once. No cleanup handler is necessary; the runtime discards the completed timer registration.

**Concurrent sleeps stay independent**

Each call constructs a new Promise and registers a new timer. Calling `sleep(50)` and `sleep(100)` creates two independent pending operations.

The shorter timer can resolve first even if both were started in immediate succession. Neither call stores state in a global variable or cancels the other.

This is different from debounce, where a later invocation deliberately cancels a prior timer. Sleep has no shared timer handle because every requested delay must complete.

**Why a busy wait is incorrect**

A loop that repeatedly checks `Date.now()` until enough time passes could approximate the elapsed duration, but it would monopolize the single JavaScript thread.

During that loop:

- user-interface events could not be handled;
- other timers could not fire;
- Promise continuations could not run;
- CPU time would be wasted.

The timer-and-Promise solution yields control to the runtime and is the intended asynchronous design.

**The returned value and chaining**

When a caller writes `await sleep(100)`, the surrounding async function suspends and later resumes with `undefined` as the awaited value.

When a caller writes `sleep(100).then(callback)`, `callback` runs after fulfillment. Its scheduling as a Promise continuation occurs after the timer resolver runs, so the observed elapsed time can be slightly larger than the timer delay.

No rejection path exists in the exact solution under the provided valid input.

## Complexity detail

The function performs constant computational work: it creates one Promise, registers one timer, and later invokes one resolver. Computational time is $O(1)$, excluding time spent waiting.

If $m=\texttt{millis}$ represents elapsed wall-clock delay, the operation remains pending for approximately $O(m)$ time, which is the convention reflected by the manifest.

The function retains one Promise, timer registration, and resolver closure while pending, all $O(1)$ space per call. With $q$ simultaneous calls, runtime-held pending state would total $O(q)$.

## Alternatives and edge cases

- **Normal function returning a Promise:** Removing `async` preserves behavior because the body already returns a Promise.
- **Callback-only API:** A timer callback can delay work, but it does not provide the requested awaitable Promise interface.
- **Busy waiting:** It blocks the event loop and wastes CPU, so it is not an acceptable asynchronous sleep.
- **Exact timing expectation:** The callback may run later than requested because `setTimeout` specifies an earliest eligible time.
- **Several concurrent calls:** Each receives an independent Promise and timer.
- **Ignored resolved value:** The Promise fulfills with undefined, which the contract permits.
- **Very busy event loop:** Completion may be delayed beyond `millis` but cannot run synchronously before timer scheduling.
- **Positive delay:** Constraints exclude negative values and require at least one millisecond.
- **No cancellation:** Sleep always resolves; the returned API exposes no timer handle.
- **No thread blocking:** Other JavaScript work can run while the Promise is pending.
