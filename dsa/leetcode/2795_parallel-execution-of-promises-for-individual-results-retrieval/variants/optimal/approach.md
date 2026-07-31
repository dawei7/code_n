## General

**Separate aggregate settlement from individual rejection**

Create one outer promise whose executor invokes every input function during the same synchronous loop. No invocation waits for an earlier promise, so all asynchronous operations begin in parallel. Allocate a result array with one slot per function and keep a counter of how many operations have settled.

For each returned promise, install both a fulfillment handler and a rejection handler. A fulfillment writes `{ status: "fulfilled", value }` at the function's original index. A rejection writes `{ status: "rejected", reason }` at that same index. Both branches then increment the shared settlement counter.

**Resolve only after the final record**

When the counter reaches $n$, every result slot has been written exactly once, so resolve the outer promise with the array. Writing by index rather than appending preserves input order independently of settlement order. Because rejection handlers create ordinary result objects and do not reject the outer promise, any mixture of outcomes still produces one fulfilled aggregate.

Invoke each function inside `try`/`catch` and pass returned values through `Promise.resolve`. The promised contract supplies promises, but these two steps also assimilate thenables and turn an unexpected synchronous throw into the same rejected-record form without preventing later functions from starting.

## Complexity detail

Let $n$ be the number of functions. The implementation invokes each function once, attaches one pair of settlement handlers, and writes one result record, so its bookkeeping takes $O(n)$ total time. The result array, callbacks, and fixed counters use $O(n)$ space. Wall-clock completion is determined by the last promise to settle, not by the sum of delays.

Since $1 \le n \le 10$ and correctness depends on parallel scheduling and settlement evidence rather than an unbounded workload, the package uses a bounded-concurrency certificate instead of runtime scaling tiers.

## Alternatives and edge cases

- **Built-in `Promise.allSettled`:** It provides the desired behavior directly but is explicitly excluded by the task.
- **Sequential `await` loop:** This can build the correct records but delays later invocations and makes elapsed time additive instead of parallel.
- **`Promise.all` over raw promises:** It rejects on the first failure, whereas this aggregate must resolve after every promise settles.
- **Append records on settlement:** This orders records by completion time rather than by input index.
- Every function must be invoked once even if an earlier operation rejects.
- The aggregate waits for the slowest settlement, including when a rejection happens before a later fulfillment.
- Fulfillment values and rejection reasons must be preserved without coercion.
- A single function follows the same indexing and counter logic without a special case.
- Several promises may settle at the same time; their result positions still come from input indices.

