## General

**Represent only currently active keys**

The class stores a `Map` named `cache`. Every present entry has:

- `value`: the value returned by `get`;
- `timeout`: the timer handle responsible for expiring this exact entry.

An expired key is physically deleted from the map when its timer fires. This design gives a strong invariant:

> A key is present in `cache` exactly while it is considered unexpired.

Because the map contains no stale records, both `get` and `count` can answer directly without comparing timestamps.

**Construct an empty independent cache**

`TimeLimitedCache` is a constructor function. Calling it with `new` creates an instance, and the constructor assigns a new `Map` to `this.cache`.

Each cache instance therefore owns separate entries and timer handles. Setting key one in one instance does not affect key one in another instance.

The public operations are installed on `TimeLimitedCache.prototype`, so all instances share the same method functions while using their own `this.cache` state.

**Set a new key**

At the beginning of `set(key, value, duration)`, the code evaluates:

`const existed = this.cache.has(key)`.

By the class invariant, this Boolean says exactly whether the same key currently has an unexpired value. It is saved before any overwrite so the method can return the required historical fact.

For a new key, no old timer needs cancellation. The method schedules a callback that deletes the key after `duration` milliseconds, stores the new value and timer handle, and returns false.

**Replace an active key safely**

If `existed` is true, the old entry already has an expiration timer. Merely overwriting the map value would not cancel that timer.

Suppose the old timer was due at time 50 and a replacement should remain active until time 140. If the old timer were left running, it would execute at time 50 and call `delete(key)`, accidentally deleting the replacement 90 milliseconds early.

The solution prevents this race by retrieving the old handle and calling:

`clearTimeout(this.cache.get(key).timeout)`.

It then creates a fresh timer and stores both the new value and the new handle. The replacement gets a completely new duration measured from the replacement call.

This explains why the timer handle must be stored alongside the value rather than discarded.

**Expire through the timer callback**

The new timer uses:

`setTimeout(() => this.cache.delete(key), duration)`.

The arrow function captures the method's lexical `this` and the current `key`. When it eventually runs, it deletes that key from the correct cache instance.

An arrow function is convenient here because it does not receive a new dynamic `this` from the timer system. A normal unbound callback using `this.cache` would not reliably refer to the cache instance.

After deletion, `has` becomes false, `get` returns `-1`, and `size` decreases automatically.

**Read a value**

`get(key)` asks whether the map contains the key. If so, it returns the entry's `value`; otherwise it returns `-1`.

The method cannot use a value truthiness test because zero is a permitted cached value. It also cannot use `Map.get(key) ?? -1` as a general design because a cached value could in other contracts be nullish. Membership is the right way to distinguish absence.

Under this problem's integer constraints, the explicit `has` check remains clear and exact.

**Count active keys**

`count()` returns `this.cache.size`. Since expiration callbacks delete records and replacement does not change the number of keys, map size is always the number of active keys.

No scan is needed. This is one main advantage of eager deletion by timers compared with keeping expired records and cleaning them lazily.

**Trace replacement timing**

At time zero, setting key one to 42 for 50 milliseconds finds no entry, schedules timer A, stores the pair, and returns false.

At time 40, setting key one to 50 for 100 milliseconds finds the active entry:

- `existed` becomes true;
- timer A is cancelled;
- timer B is scheduled for about time 140;
- the map entry becomes value 50 with handle B.

At times 50 and 120, the key is still active and `get` returns 50. At time 140, timer B deletes it. A later `get` returns `-1` and `count` returns zero.

**Why asynchronous ordering matters**

Timer callbacks run through the event loop. A duration of zero schedules expiration as soon as the runtime can run the timer task; it does not execute the deletion in the middle of `set`.

The `set` call first stores the entry and returns. Subsequent scheduled actions in the challenge's timeline observe the runtime's timer ordering.

The design assumes the normal single-threaded JavaScript execution model: `set` and an expiration callback do not interleave halfway through one synchronous method body.

**Class invariant proves all methods**

Initially the map is empty, so it contains exactly the active keys.

- Setting a new key adds one active record and schedules its future removal.
- Replacing a key cancels the only callback that could remove the old generation, then stores the new generation.
- A current timer removes its key when the duration ends.
- Get and count do not alter membership.

Thus the invariant is preserved over every operation, and all three public return values follow directly from it.

## Complexity detail

`Map.has`, `Map.get`, `Map.set`, `Map.delete`, and `Map.size` are expected $O(1)$ operations. Timer registration and cancellation are treated as $O(1)$ runtime operations, so each `set`, `get`, `count`, and expiration callback takes expected $O(1)$ time.

If $n$ keys are active, the map stores $n$ values and $n$ timer handles, and the runtime holds up to $n$ active timers. Space is $O(n)$.

Replacing a key cancels its previous timer, so obsolete generations do not accumulate as live timers.

## Alternatives and edge cases

- **Store expiration timestamps:** Check time during `get` and `count`; this avoids one timer per key but makes accurate count require cleanup or scanning.
- **Priority queue of expirations:** Efficiently expire keys in chronological order, but replacement generations need validation and the implementation is more complex.
- **Overwrite without `clearTimeout`:** Incorrect because the old timer can delete the new value early.
- **New key:** `set` returns false and increases active count.
- **Unexpired replacement:** `set` returns true, preserves key count, and restarts duration.
- **Expired replacement:** The old callback has removed the key, so `set` returns false.
- **Cached value zero:** Membership, not truthiness, ensures it is returned correctly.
- **Duration zero:** Expiration is timer-scheduled after the synchronous call rather than performed inline.
- **Repeated `get`:** Reads do not extend the expiration time.
- **Separate instances:** Each constructor call owns its own map and timers.
