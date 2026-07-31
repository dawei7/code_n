## General

The class needs two independent pieces of state: a queue of unresolved requests and a boolean indicating whether the cooldown after the latest bulk-query start is still active. Query completion is deliberately absent from the throttle state.

**Dispatch the first available batch**

Every `getValue` call creates a promise and appends its key and resolver to the queue. If no cooldown is active, detach the entire queue immediately, mark the batcher throttled, and invoke `queryMultiple` with those keys. The first request after an idle period is therefore dispatched synchronously rather than waiting for a timer.

When the bulk promise fulfills, its value at index $i$ resolves the request stored at index $i$ of the detached batch. Keeping the request records and key array in identical order proves that batching does not mix up values.

**Open the next window by timer**

At each dispatch, schedule one timer for $t$ milliseconds. When it fires, clear the cooldown and attempt another flush. If requests accumulated, they leave as one batch immediately; otherwise the batcher stays idle until a future request triggers a flush.

The timer is registered from the query's start, not from its fulfillment. Therefore a query whose latency exceeds $t$ does not block the next batch. At most one cooldown timer governs queued work, and every queued request is eventually detached and resolved because `queryMultiple` never rejects.

## Complexity detail

Let $c$ be the number of `getValue` calls in the complete schedule. Each request enters and leaves a queue once, contributes one key to a batch, and receives one result, so total JavaScript bookkeeping is $O(c)$ time. The queue and detached in-flight batches hold at most $O(c)$ request records. Host-managed waiting time and the supplied query's own runtime are excluded.

The contract caps $c$ at ten. Timing behavior and overlap are more material than asymptotic runtime over that bounded domain, so a bounded-concurrency certificate supplies scheduler, semantic, and completion evidence instead of an artificial scaling benchmark.

## Alternatives and edge cases

- **Wait for query fulfillment before starting the cooldown:** This incorrectly throttles completion-to-start time and prevents legal overlap.
- **One timer per request:** Multiple timers can race to dispatch partial queues and make the minimum start spacing difficult to preserve.
- **Polling the clock:** Busy waiting blocks the event loop and is unnecessary when one host timer defines the next legal window.
- A first request after an idle period must dispatch immediately.
- With $t=0$, later queued work may dispatch on the next timer turn without an artificial positive delay.
- An empty schedule performs no query.
- Preserve queue order so each returned value resolves the promise for the key at the same batch index.
- A slow large batch may resolve after a later small batch; resolution order is not request order.
