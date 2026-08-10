## General

**Use a fixed number of long-lived workers**

The pool must start functions in array order while never allowing more than $n$ returned promises to remain pending.

The solution creates at most one asynchronous worker per available pool slot. Each worker repeatedly:

1. claims the next unstarted function index;
2. starts that function;
3. waits for its Promise to resolve;
4. returns to claim another index.

Because a worker never claims its next task before its current `await` finishes, each worker contributes at most one pending task. With at most $n$ workers, the concurrency limit follows automatically.

**One shared index distributes work**

`nextIndex` begins at zero and is captured by every worker.

At the top of the worker loop, a worker checks whether an unstarted function remains. It then performs:

`const index = nextIndex`

followed by:

`nextIndex += 1`.

The local `index` permanently identifies this worker's current task. Incrementing the shared pointer makes the following worker claim the next array position.

No function is removed from the input array, and no queue shifting is needed.

**Why workers cannot claim the same index**

JavaScript executes synchronous statements on one event-loop thread. A worker runs from the loop condition through reading and incrementing `nextIndex` before it reaches:

`await functions[index]()`.

Only at that await can control yield to other asynchronous work. Consequently, another worker cannot interleave between the read and increment and capture the same value.

This atomicity is based on JavaScript's run-to-completion semantics for synchronous code, not on locks or threads.

**Why function start order is preserved**

Workers are created in a normal loop. Calling `worker()` begins executing that async function synchronously until its first await.

The first worker claims index zero and starts `functions[0]`. The second worker then claims index one, and so on. Later, whichever worker finishes first claims the current `nextIndex`, which is the smallest unstarted position.

Completion order may differ, but start order remains:

$$
0,1,2,\ldots,m-1.
$$

That is exactly what the contract requires.

**Why the pool remains full when work is available**

Initially:

`workerCount = Math.min(n, functions.length)`.

Therefore, if at least $n$ functions exist, $n$ workers immediately start the first $n$ tasks. If fewer exist, every function starts and no useless extra worker is created.

Whenever one task resolves, its worker resumes, loops, and immediately claims the next index if one remains. Other workers continue awaiting their own tasks. Thus a newly available pool slot is refilled without waiting for unrelated promises.

The number of active tasks can drop below the limit only when fewer unstarted-or-pending tasks remain than the limit.

**Await one task per worker**

Inside the loop, `await functions[index]()` pauses only that worker. It does not pause other workers or the JavaScript runtime.

For pool size two and durations 300, 400, and 200:

- workers zero and one start tasks zero and one at time zero;
- at time 300, worker zero resumes and starts task two;
- task one resolves at time 400;
- task two resolves around time 500;
- only then are both worker Promises complete.

The third task starts at the first available slot, not after all initially started tasks finish.

**Wait for all workers, not all raw tasks**

Every call to `worker()` returns a Promise representing that worker's entire loop, including all tasks it will claim.

The solution collects these worker Promises and awaits `Promise.all(workers)`. When all workers have finished, no worker is awaiting a task and no unstarted index remains. Therefore, every input function has resolved.

The returned async `promisePool` function then resolves with undefined, an allowed result.

**Empty input resolves immediately**

When `functions.length` is zero, `workerCount` is zero. No worker starts, and `Promise.all([])` returns an already-fulfilled Promise.

The async pool therefore resolves without invoking anything. No special empty branch is required.


At every suspension point:

- indices below `nextIndex` have each been claimed exactly once;
- indices at or above `nextIndex` are unstarted;
- each worker has at most one claimed function currently pending;
- a worker claims another function only after its prior one resolves.

Initialization satisfies this invariant. Synchronous claim increments preserve uniqueness and order, while awaiting enforces one active task per worker.

At most `workerCount <= n` tasks can be pending. When all workers finish, their loop conditions prove `nextIndex >= functions.length`, so every function was claimed; their resolved Promises prove every claimed task resolved.

**Failure behavior under the stated assumption**

The contract guarantees input functions never reject. If one did reject, that worker Promise and then `Promise.all` would reject, while other workers could continue their already-started work. The exact implementation does not add custom error recovery because it is unnecessary for valid inputs.

## Complexity detail

Let $m=\texttt{functions.length}$. Each function index is claimed and invoked exactly once, so scheduler work is $O(m)$, excluding time spent inside the asynchronous functions.

At most $\min(m,n)$ worker Promises and active async worker states exist. Scheduler auxiliary space is $O(\min(m,n))$. The input array itself is not copied or modified.

Wall-clock completion time depends on task durations and dynamic worker assignment, not merely on $m$.

## Alternatives and edge cases

- **Launch every Promise with `Promise.all`:** Violates the pool limit when $m>n$.
- **One recursive launcher per slot:** Equivalent in principle, but the worker loop avoids recursive chaining.
- **Shift from an array queue:** Works but mutates or copies input and repeated shifting can be inefficient.
- **`n = 1`:** One worker executes every function sequentially.
- **`n >= m`:** Every function begins immediately, and completion waits for the slowest.
- **Empty function array:** Zero workers are created and the pool resolves immediately.
- **Different completion order:** Allowed; only start order and concurrency are constrained.
- **Fast synchronous fulfillment:** Await still resumes through Promise scheduling, and the worker then claims the next index.
- **Rejection:** Outside the stated input guarantee, it propagates through the worker and `Promise.all`.
- **Shared index safety:** Claims contain no await between reading and incrementing `nextIndex`.
