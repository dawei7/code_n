## General

**Create a race between work and a deadline**

The limited wrapper must settle according to whichever event occurs first:

- the original function's Promise settles;
- $t$ milliseconds elapse.

`Promise.race` implements exactly this “first settlement wins” rule. The solution races the source Promise against a timer-backed Promise that rejects with the required string.

**Return a reusable wrapper**

`timeLimit(fn, t)` stores `fn` and `t` in a closure and returns an async function accepting `...args`.

No timer starts when the wrapper is created. Each invocation starts its own source call and its own deadline, so separately timed invocations do not share or cancel one another.

Rest syntax collects all invocation arguments in their original order. `fn(...args)` forwards them as positional arguments.

**Build the rejecting timeout Promise**

Inside one invocation, `timeoutId` is declared so it can later be cleared.

The timeout Promise executor calls:

`setTimeout(() => reject('Time Limit Exceeded'), t)`.

It saves the returned handle in `timeoutId`. The Promise remains pending until the timer callback rejects it with the exact string required by the contract.

The unused `resolve` parameter is present only because Promise executors receive both settlement functions.

**Race both outcomes**

The main expression is:

`await Promise.race([fn(...args), timeout])`.

If `fn` fulfills first, the race fulfills with exactly its value. If `fn` rejects first, the race rejects with exactly its error. This preserves normal success and failure semantics.

If the timer fires first, the race rejects with `"Time Limit Exceeded"`. A later settlement of `fn` cannot change the already-settled race.

This behavior matches all four cases in the description, including immediate source rejection.

**Why `await` is inside a `try/finally`**

Whichever competitor wins, the timer is no longer useful:

- if the source settles first, leaving the timer alive would keep unnecessary runtime work scheduled and later trigger an ignored rejection;
- if the timer wins, it has already fired, but clearing its handle is harmless.

The code places the awaited race in a `try` and calls `clearTimeout(timeoutId)` in `finally`.

JavaScript executes `finally` whether the awaited expression fulfills or rejects. Thus cleanup is guaranteed without changing the winning result.

If the race fulfilled, the `return await` value is returned after cleanup. If it rejected, the same rejection propagates after cleanup because `finally` does not return or throw a replacement.

**Trace a timeout**

Suppose `fn(5)` will resolve after 100 milliseconds, while $t=50$.

1. The wrapper schedules the rejecting timer for time 50.
2. It invokes `fn(5)` and races the two Promises.
3. At about time 50, the timer rejects.
4. The race rejects with `"Time Limit Exceeded"`.
5. `finally` clears the now-fired timer handle.
6. The wrapper's returned Promise rejects with that string.

The original function is not forcibly stopped. Its underlying work may continue and resolve around time 100, but that settlement is ignored by the completed race.

**Trace an on-time fulfillment**

If `fn(5)` resolves to 25 at time 100 and $t=150$, the source wins. `Promise.race` fulfills with 25, `finally` cancels the still-pending 150-millisecond timer, and the wrapper fulfills with 25.

Cancelling the timer prevents a needless later callback.

**Source errors remain source errors**

If the async source immediately throws `"Error"`, its returned Promise rejects before the long timer wins. The race adopts that rejection.

The wrapper does not convert all failures into time-limit failures. Only the deadline Promise produces the time-limit string; source errors preserve their identity.

**A settlement argument proves correctness**

For one wrapper invocation, let $S$ be the source settlement time and $T$ the timer settlement time.

- If $S<T$, the race adopts the source's fulfilled value or rejection, satisfying the within-limit rule.
- If $T<S$, the timer's rejection becomes the race result, satisfying the exceeded-limit rule.

Once a Promise settles, later competitor outcomes cannot alter it. The cleanup step affects only the timer's future execution, not the already-chosen result.

**Timing ties**

At an exact nominal tie, event-loop task ordering decides which settlement callback is processed first. Real timer timing is not perfectly exact, and the contract's practical tests schedule distinguishable outcomes.

The implementation correctly uses the runtime's first observed settlement as `Promise.race` specifies.

**Invocation context**

The exact code calls `fn(...args)` without forwarding the wrapper's dynamic `this`. This is correct for the provided standalone async functions.

A general method utility could use `fn.apply(this, args)`, but that is not what the stored solution executes.

## Complexity detail

Let $a$ be the number of arguments. Rest collection and spreading take $O(a)$ time and $O(a)$ temporary space. Timer creation, Promise creation, racing two Promises, and cleanup use constant additional work.

Thus computational complexity is $O(a)$ time and $O(a)$ space per invocation, matching the manifest. The elapsed waiting time is at most approximately $t$ before a timeout result, or less if the source settles first.

The underlying source may continue consuming its own resources after losing the race.

## Alternatives and edge cases

- **Wrap everything in one manually settled Promise:** Correct but requires explicit success, failure, timeout, and cleanup wiring that `Promise.race` already provides.
- **Race without clearing the timer:** Returns correctly but leaves unnecessary timer callbacks after fast source completion.
- **AbortController:** Can cooperatively cancel supported underlying work, but the problem only asks to time-limit the wrapper result.
- **`t = 0`:** The timer is scheduled immediately, though an already-settled source Promise may compete through event-loop ordering.
- **Source rejects before deadline:** Its original rejection propagates.
- **Source fulfills before deadline:** Its exact value is returned.
- **Source finishes after deadline:** The wrapper rejects, but underlying work is not physically cancelled.
- **Multiple wrapper calls:** Each owns an independent timer and race.
- **Several arguments:** Rest and spread preserve their order.
- **Cleanup on every path:** `finally` runs after both fulfillment and rejection.
