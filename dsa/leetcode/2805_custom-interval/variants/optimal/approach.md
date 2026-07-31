## General

**Separate public identity from native timer handles**

Node.js returns an object from `setTimeout`, but the public API must return a number. Maintain a module-level counter for custom identifiers and a map from each numeric identifier to its interval state. The state records the number of completed invocations, the current native timeout handle, and whether the interval remains active. Distinct counter values keep concurrently active intervals independent.

**Chain the increasing waits**

A fixed `setInterval` cannot express the required changing gap. Instead, schedule one `setTimeout` at a time. Before any callback has run, `count` is zero, so the first wait is `delay`. When the timeout fires, invoke `fn`, increment `count`, and schedule the next timeout using `delay + period * count`. Therefore the waits are

$$
\texttt{delay},\quad \texttt{delay}+\texttt{period},\quad \texttt{delay}+2\,\texttt{period},\ldots
$$

and the $k$-th cumulative invocation time is

$$
k\,\texttt{delay}+\frac{\texttt{period}\,k(k-1)}{2}.
$$

Each scheduled callback checks the state's active flag. After invoking `fn`, it schedules another timeout only if the state is still active. This extra check makes cancellation safe even when `fn` itself calls `customClearInterval`.

**Cancel exactly one interval**

To clear an interval, find its state by numeric ID, mark it inactive, cancel its current native handle, and remove the map entry. Marking first prevents an executing callback from extending the chain. Clearing one entry cannot affect any other interval because every ID has separate state and a separate timeout handle.

The app-local adapter replaces wall-clock waiting with the same recurrence over cumulative times. It appends a time only when it is strictly earlier than `cancelTime`, matching the rule that cancellation prevents an invocation at or after that instant.

## Complexity detail

Let $k$ be the number of times `fn` runs before cancellation and $a$ the number of active custom intervals. Each firing performs constant scheduler bookkeeping and creates at most one successor timeout, so the total work for one interval is $O(k)$. The registry and one state object per active interval use $O(a)$ space; each interval has only one pending native timeout.

The legal inputs bound the cumulative timer work too tightly for meaningful runtime scaling. With the minimum `delay = 20`, minimum `period = 20`, and `cancelTime = 1000`, nine invocations occur before cancellation and the tenth would be at $1100$ milliseconds. A bounded-concurrency certificate therefore verifies the scheduling contract with a deterministic fake timer rather than extrapolating noisy wall-clock measurements.

## Alternatives and edge cases

- **Use `setInterval`:** A fixed interval repeats at one constant delay and cannot produce the required linearly increasing gaps.
- **Return the `setTimeout` result:** This violates the numeric-ID contract in Node.js because its timer handle is an object.
- **Schedule every timeout in advance:** This creates unnecessary simultaneous handles, makes cancellation more expensive, and complicates cleanup.
- Cancellation before the first timeout must prevent every invocation.
- A timeout scheduled exactly at `cancelTime` does not contribute an invocation because cancellation stops future execution at that boundary.
- Multiple intervals need distinct numeric IDs and independent state even when their delay parameters are identical.
- Clearing an unknown or already-cleared ID should be harmless.
- If `fn` clears its own interval, the active check after `fn` prevents a successor timeout from being scheduled.
