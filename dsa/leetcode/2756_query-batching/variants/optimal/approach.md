## General

**What the class must coordinate**

Each call to `getValue(key)` must eventually receive the value for that particular key, but the class should combine waiting keys into calls to `queryMultiple`. The timing rule is the important part: a request may be dispatched immediately when no cooldown is active, and after a dispatch the next batch may not be dispatched until `t` milliseconds have elapsed. The exact solution separates those two responsibilities with two pieces of state:

- `queue` contains records for requests that have arrived but have not yet been dispatched. Each record stores both the requested `key` and the Promise's `resolve` function.
- `throttled` says whether the cooldown following the most recent dispatch is still active.

The queue is not merely a collection of keys. Keeping the resolver beside its key is what allows one batched response to settle many independently returned Promises later.

**What happens when a caller asks for a value**

`getValue` constructs and immediately returns a new Promise. The Promise executor runs synchronously, so its `{ key, resolve }` record is appended to `queue` before `getValue` returns. It then calls `flush()`.

`flush` has two guard conditions. If `throttled` is true, another dispatch would be too early, so the queued request is left in place. If the queue is empty, there is nothing to send. Otherwise, this request is allowed to start a batch immediately. This explains why the first request after an idle period is not delayed by `t`: no cooldown exists yet, and the call to `flush` proceeds at once.

**Why the queue is detached before asynchronous work starts**

An allowed flush executes:

1. Set `throttled` to true.
2. Save the current array in `batch`.
3. Replace `queue` with a new empty array.
4. Schedule a timer for the end of the cooldown.
5. Call `queryMultiple` with the keys in `batch`.

The assignment `const batch = this.queue; this.queue = [];` is crucial. `batch` is a stable snapshot of exactly the requests covered by this one external query. Calls arriving afterward append to a different array, so they cannot accidentally become associated with the already-dispatched result.

For example, suppose key `A` arrives while idle. It forms a one-key batch immediately. If `B` and `C` arrive during the next `t` milliseconds, their calls to `flush` see `throttled === true`, so both records remain in the new queue. When the timer fires, it clears the flag and invokes `flush` again. That second flush snapshots `B` and `C` together.

**The cooldown is based on dispatch time, not response time**

The timer is scheduled when a batch is sent, before the Promise returned by `queryMultiple` settles. When it fires, it sets `throttled` to false and tries another flush. The earlier external query does not have to be finished. Consequently, two calls to `queryMultiple` may be in flight simultaneously if an earlier query takes longer than `t`.

That behavior is intentional in the exact implementation. This is rate spacing, not a concurrency limit. Waiting for the earlier query to resolve before starting the timer would implement a different contract and would make slow network responses postpone later batches unnecessarily.

If the timer fires while no requests are queued, `flush` simply returns. The object remains unthrottled. The next call to `getValue` can therefore dispatch immediately; the implementation does not create empty batches or periodic polling.

**Returning the right value to every Promise**

`queryMultiple` receives `batch.map(item => item.key)`, preserving queue order. The contract guarantees that the returned values use the corresponding order. The `then` callback walks those values by index and calls `batch[index].resolve(value)`. Thus the record at batch position zero gets response position zero, and so on.

The keys are guaranteed to be unique, but the solution does not need a key-to-resolver map. Positional association is simpler and exactly matches the API. It also avoids assuming that a returned value can identify its own key.

The reference contract states that `queryMultiple` never rejects. That guarantee matters because the exact code installs only a fulfillment callback. In a more general API, rejection handling would be required to reject every Promise in the affected batch; here, omitting it is safe under the given contract.

**Why no request is lost**

Every request is in exactly one of three stages: it is in the current queue, it belongs to a detached batch whose query is in flight, or its resolver has already been called. Detaching a batch moves records from the first stage to the second without copying or discarding them. New arrivals cannot enter an old batch, and a timer always attempts to dispatch whatever accumulated during the cooldown. Once a result arrives, the fixed index mapping settles each Promise from that batch exactly once.

This lifecycle is the core correctness argument. The boolean prevents dispatches that are too close together, while the two distinct arrays prevent temporal mixing between requests on opposite sides of a dispatch.

## Complexity detail

Let `c` be the total number of `getValue` calls and let `b` be the number of non-empty batches. Across the lifetime of the object, each request record is created once, appended once, included in one key-mapping pass, and resolved once. The class therefore performs `O(c)` total bookkeeping work, in addition to the external work and latency of `queryMultiple`. Each `getValue` does `O(1)` immediate work. A particular `flush` that dispatches a batch of size `q` spends `O(q)` time building the key array and later `O(q)` time resolving its values.

There are `b` timers and `b` external calls. Timer scheduling itself is `O(1)` per batch. The elapsed completion time cannot be expressed only in terms of `c` because it depends on `t`, when calls arrive, and how long `queryMultiple` takes. The first batch is immediate, while consecutive non-empty dispatches are spaced by at least `t` according to the event loop's timer behavior.

The request records can collectively occupy `O(c)` space in the worst case. A large number may wait in `queue` during a cooldown, and records in detached in-flight batches remain reachable until their queries resolve. The object also has `O(1)` scalar state, and each scheduled callback closes over one batch. If one measures only the currently waiting queue, its size is the number of requests since the last dispatch; the safe whole-execution peak bound is `O(c)`. The result arrays owned by `queryMultiple` and the JavaScript Promise runtime are external/API storage, but the solution's resolver records are part of its own auxiliary state.

## Alternatives and edge cases

- **Delay-first debounce:** Waiting `t` milliseconds before the first dispatch could collect a larger initial batch, but it violates the required behavior because an idle batch must start immediately.
- **Wait for query completion before unlocking:** This would cap concurrency at one, yet it would measure the gap from response completion rather than dispatch time. A slow query would incorrectly delay later work beyond the stated throttle interval.
- **One timer per incoming request:** Repeatedly scheduling timers complicates ordering and can produce duplicate flush attempts. The single cooldown timer established by the dispatch is sufficient.
- **Key-to-resolver map:** A map can associate results by key, but it is unnecessary because the API guarantees aligned result order and keys are unique. The positional batch array is both smaller conceptually and faithful to the contract.
- **Calls arriving synchronously:** The first synchronous call dispatches immediately and turns on throttling. Further synchronous calls in the same JavaScript turn enter the next batch rather than the first one.
- **`t = 0`:** The timer still runs asynchronously through `setTimeout`. Requests arriving before that callback executes may batch together; the implementation does not recursively spin.
- **A timer finds an empty queue:** It clears `throttled` and `flush` returns. No external query is made, and a future request starts immediately.
- **Slow external queries:** Multiple batches may be in flight, but each callback closes over its own detached `batch`, so responses that finish out of order still resolve the correct Promises.
- **Rejected external queries:** The local reference promises this cannot happen. Without that guarantee, the exact implementation would leave the affected Promises pending because it has no rejection callback.
- **Mutable or repeated keys:** The contract guarantees unique keys. The implementation forwards each stored key value as received and relies only on response position, not object identity or a deduplication rule.
