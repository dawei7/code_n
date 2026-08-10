## General

**Map each event name to an ordered listener list**

`EventEmitter` stores `this.events` as a `Map`. Each key is an event-name string, and its value is an array of callbacks in subscription order.

A Map cleanly separates event names and avoids special object-property names such as `constructor` or `__proto__`.

Arrays are used because order matters: emission must call listeners in exactly the sequence in which they subscribed.

**Subscribe by appending**

When `subscribe(eventName, callback)` sees a new event, it first stores an empty array for that name.

It obtains the array, pushes the callback at the end, and captures that exact `listeners` array inside the returned unsubscribe closure.

Appending preserves chronological registration order. The contract guarantees callbacks supplied to subscriptions are not referentially identical, which makes later identity lookup unambiguous.

**Return a subscription handle**

The method returns an object with one `unsubscribe` arrow function.

The closure retains:

- the callback to remove;
- the event name;
- the listener array in which it was registered;
- Boolean `active`, initially true;
- lexical access to the emitter through the arrow function's `this`.

The caller does not need to pass the event or callback again. The returned handle identifies one particular subscription.

**Make unsubscription idempotent**

The first unsubscribe call changes `active` to false. Later calls see it false and return immediately.

On the first call, `indexOf(callback)` locates the callback by identity. `splice(index, 1)` removes exactly that one entry and shifts later listeners left while preserving their relative order.

No explicit value is returned, so JavaScript returns `undefined` as required.

**Remove empty event entries**

After removal, if `listeners.length === 0`, the emitter deletes `eventName` from the Map.

This cleanup prevents empty arrays and unused event names from accumulating.

The subscription closure may still reference the old array, but its `active` flag prevents a later unsubscribe from affecting a newly created listener array for the same event name.

**Emit an unknown event**

`emit` retrieves the listener array with `this.events.get(eventName)`.

If no entry exists, it returns `[]` immediately. No callback is called, and the optional argument array is irrelevant.

This also covers an event whose final listener was unsubscribed and whose Map entry was deleted.

**Snapshot listeners before invoking them**

For an existing event, the exact code uses `listeners.slice()` before `map`.

The slice is a shallow copy of callback references in their current order. It defines which subscriptions belong to this emission before any callback executes.

This protects iteration if a callback subscribes or unsubscribes during its own execution. Such changes update the live listener array, but they do not distort the snapshot currently being mapped.

**Invoke callbacks and collect results**

`map(callback => callback(...args))` visits the snapshot from index zero upward.

Each callback receives the optional arguments as separate positional values, not as one array parameter. Its return value becomes the corresponding element of the result array.

Thus callback order and result order are identical to subscription order.

**Trace subscription and removal**

Suppose callbacks `first` and `second` subscribe to event `score` in that order.

Emitting with `[5]` snapshots `[first, second]` and returns their results in that order.

If the first subscription's handle unsubscribes, `splice` removes index zero. The live array now contains only `second`, so the next emission invokes it alone and returns a one-element result.

**Optional arguments**

The signature `emit(eventName, args = [])` supplies an empty array when the caller omits the second argument.

Callbacks are then invoked with no positional arguments. An explicitly supplied array such as `[1, 2, 3]` is spread so a variadic callback receives three values.

The default prevents trying to spread `undefined`.

**Why snapshot behavior is a deliberate strength**

Imagine the first callback unsubscribes the second while an emission is already running.

Because the snapshot already contains both callbacks, both are invoked in that current emission; the removal affects future emissions. Similarly, a newly subscribed callback waits until the next emission.

The problem does not spell out reentrant changes, but snapshotting gives deterministic and robust behavior.


Appending stores every active callback under its event in registration order. Unsubscription removes exactly the callback captured by its handle and does not reorder survivors.

Emission snapshots precisely the active array at its start, invokes each callback once in stored order with the requested arguments, and `map` places each return value at the matching position. Missing events return an empty list.

Therefore every public method meets its specified subscription, ordering, removal, argument, and result behavior.

## Complexity detail

Let $k$ be the number of listeners for the relevant event and $a$ the number of emitted arguments. Subscription is amortized $O(1)$. Unsubscription uses `indexOf` and `splice`, so it is $O(k)$ in the worst case.

Emission copies $k$ references and calls $k$ callbacks. Excluding callback bodies, spreading $a$ arguments into each call gives $O(k(a+1))$ time. Persistent storage is $O(E+S)$ for $E$ event names and $S$ total active subscriptions; one emission additionally uses an $O(k)$ snapshot and result.

## Alternatives and edge cases

- **Set per event:** Offers expected constant-time deletion, but array order and snapshot semantics are more explicit here.
- **Linked list per event:** Can support constant-time removal with stored nodes, but emission and implementation become more complex.
- **Map callback to index:** Splicing shifts indices, so maintaining them correctly adds bookkeeping.
- **No listeners:** Returns a fresh empty array.
- **Several listeners:** Invoked and reported in subscription order.
- **Repeated unsubscribe:** The `active` flag makes later calls harmless.
- **Last listener removed:** The event key is deleted from the Map.
- **Optional argument array omitted:** Each callback receives zero arguments.
- **Callback returns undefined:** That undefined value occupies its position in the result array.
- **Callback throws:** The exact synchronous `map` stops and propagates the exception.
- **Subscribe during emit:** New listener is absent from the current snapshot and appears next time.
- **Unsubscribe during emit:** Current snapshot remains stable; future emissions use the updated live list.
