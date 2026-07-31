## General

**Start every operation before waiting**

Create the combined promise and iterate through `functions` synchronously inside its executor. Invoke every function during that loop and attach fulfillment and rejection handlers immediately. No handler awaits another promise and no invocation is delayed until an earlier operation settles, so all asynchronous work begins in parallel.

Allocate a result array with one slot per input function. A fulfillment handler writes its value at the function's original index rather than appending in completion order, then increments a completion counter. When that counter reaches $n$, every promise has fulfilled and the combined promise resolves with the completed array.

Attach the combined promise's rejection callback to every returned promise. The first rejection call settles the combined promise with that reason; later fulfillments or rejections cannot change an already settled promise. If no rejection occurs, each function fulfills exactly once, the counter eventually reaches $n$, and every result slot has been written. This proves both settlement branches while preserving input order without `Promise.all`.

## Complexity detail

Let $n$ be the number of functions. Invoking the functions, installing handlers, and processing their settlements takes $O(n)$ total bookkeeping time. The indexed result array and attached callbacks use $O(n)$ auxiliary space. Actual elapsed time is governed by the slowest fulfillment or first rejection, not the sum of durations. Since $1 \le n \le 10$ and parallel scheduling semantics cannot be established by asymptotic wall-clock tiers, the package uses a bounded-concurrency certificate with deterministic schedule evidence.

## Alternatives and edge cases

- **Sequential `await` loop:** Awaiting each function before invoking the next preserves value order but violates the requirement that all operations execute in parallel and makes elapsed time additive.
- **Append on fulfillment:** Pushing values as promises settle loses input order whenever a later-indexed promise finishes first.
- **Built-in `Promise.all`:** It provides the required semantics directly but is explicitly prohibited by the problem.
- A rejection must settle the combined promise immediately with that exact reason.
- Fulfillment order can differ arbitrarily from input order.
- Every function must be invoked once even when one returned promise will reject later.
- With one function, the combined promise mirrors that function's settlement.
- Multiple settlement attempts are harmless because a JavaScript promise changes state only once.
