## General

Use a shared `nextIndex` to identify the first asynchronous function that has not started. Create $c = \min(m,n)$ workers, where $m$ is the number of functions. Each worker repeatedly claims the current index, increments the shared counter, starts that function, and awaits its promise before returning to claim another.

JavaScript runs the index read and increment synchronously before the worker reaches `await`. Consequently, two workers cannot claim the same function: each receives a unique increasing index. Starting the workers in a loop makes the first $c$ functions begin in array order without waiting for one another.

**Awaiting inside each worker enforces one pending promise per slot**

A worker cannot claim its next index until its current promise resolves, so it contributes at most one pending promise. With at most $c \le n$ workers, the pool limit is never exceeded. Conversely, whenever a worker's promise resolves and unstarted work remains, that worker synchronously claims the next index, so an available slot is refilled without waiting for unrelated promises.

Every claim advances `nextIndex`, and every claimed function is awaited. Eventually all $m$ indices are claimed exactly once. `Promise.all(workers)` resolves only after every worker has exhausted the queue and its final promise has resolved, which is exactly when all input work is complete. For an empty input, no workers are created and `Promise.all([])` resolves immediately.

## Complexity detail

Let $m$ be the number of functions and $c = \min(m,n)$. Excluding the functions' own asynchronous durations and work, the pool performs constant scheduling work for each function, for $O(m)$ total overhead. It retains $c$ worker promises and at most $c$ active async call stacks, so auxiliary scheduling space is $O(c) = O(\min(m,n))$.

The legal domain caps both $m$ and $n$ at ten. Runtime scaling cannot honestly distinguish scheduler classes at those sizes, and wall-clock duration is chosen by the input promises. The `bounded_concurrency` certificate therefore replaces scaling with bounded-work, schedule-stress, semantic-safety, and termination evidence.

## Alternatives and edge cases

- **`Promise.race` active-set loop:** Track active promises and race them before launching replacements. It is correct, but needs careful settled-promise removal and more bookkeeping than fixed workers.
- **Launch batches with `Promise.all`:** Waiting for an entire batch leaves slots idle when one fast promise finishes before a slow batch mate, violating the requirement to start new work as soon as possible.
- **Run every function immediately:** `Promise.all(functions.map(fn => fn()))` preserves completion but violates the pending-promise limit when $m > n$.
- **Serial loop:** One worker is correct only when `n = 1`; larger limits must start multiple initial functions.
- **Empty function array:** Create zero workers and resolve immediately.
- **Limit above work count:** Start every function once and create no unnecessary idle workers.
- **Equal resolution times:** Shared index claiming remains unique and ordered even when multiple workers resume in the same microtask turn.
- **No rejections:** The source guarantees every promise resolves, so rejection recovery and cancellation are outside the contract.
