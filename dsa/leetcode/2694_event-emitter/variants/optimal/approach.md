## General

Maintain a `Map` from each event name to an array of callbacks. An array records exactly the listeners currently active for that event, and appending new callbacks naturally preserves subscription order. Different map keys isolate unrelated events.

**Return a subscription-specific closure**

After appending a callback, `subscribe` returns an object whose `unsubscribe` closure captures both that callback and its listener array. Because callbacks are referentially unique, `indexOf` identifies the intended entry. Remove it with `splice`, and delete the map entry when the array becomes empty. A captured `active` flag makes cleanup safe if the returned method is called again, although valid traces unsubscribe existing subscriptions only once.

For `emit`, look up the requested name. A missing entry immediately yields `[]`. Otherwise copy the listener array and map over that snapshot, invoking every callback with `...args` and collecting its result. The snapshot fixes the set and order for the current emission even if a callback changes subscriptions while it runs. Thus every listener active at the start is called once in subscription order, and the returned array has the corresponding results in the same order.

## Complexity detail

Let $k$ be the number of listeners for the emitted event, $a$ the number of forwarded arguments, and $s$ the total number of active subscriptions. Subscription takes $O(1)$ expected time. Unsubscription takes $O(k)$ time for search and array removal. Emission takes $O(1 + k(a + 1))$ time, excluding the callbacks' own work, because it copies $k$ references, invokes $k$ callbacks, and forwards $a$ arguments to each. Persistent listener storage is $O(s)$; one emission additionally uses $O(k)$ space for its snapshot and result.

The source permits at most ten actions in a trace, so $k$ and $s$ are too tightly bounded for an honest listener-scaling benchmark. The certificate instead verifies the bounded management work and the required per-listener argument delivery.

## Alternatives and edge cases

- **One global listener array:** Filtering it by event name on every emission works but scans unrelated subscriptions and makes event isolation less direct.
- **Set per event:** A `Set` preserves insertion order in JavaScript, but the returned unsubscription closure still needs careful identity handling and the problem explicitly guarantees unique callbacks.
- **Doubly linked listeners:** Nodes can make unsubscription $O(1)$, but snapshot semantics and ordered traversal require more state than the tiny source domain warrants.
- Emitting an unknown event or an event whose last listener was removed must return `[]`.
- Omitted `args` means an empty array, not one `undefined` argument.
- Preserve callback results and subscription order exactly; do not sort or discard duplicates in returned values.
- Unsubscribing from one event must not modify listeners stored under another name.
- Copy the listener list before invoking callbacks so subscription changes during an emission do not skip or duplicate calls in that emission.
