## General

Maintain a `Map` from each active key to an object containing its value and the timeout handle responsible for expiration. Because expired entries are deleted by their timer callbacks, membership in the map is exactly the condition that the key is currently unexpired. This makes `get` a direct lookup and `count` a read of the map's size.

For `set`, first test whether the key is present. That boolean is the required return value. If an active entry exists, cancel its old timeout before replacing it; otherwise that stale callback could later delete the new value prematurely. Create a new timeout whose callback deletes the key, store the new value and handle, and return the saved presence flag.

The timeout callback closes over the key and the cache instance. Since replacement cancels the prior handle, only the current entry's callback remains able to remove that key. A duration of zero still schedules a future timer task, so the entry exists for the remainder of the current synchronous call sequence.

## Complexity detail

Assuming expected $O(1)$ hash-map operations and constant-time host timer registration, `set`, `get`, and `count` each take expected $O(1)$ time. If $n$ keys are simultaneously active, the map and their timer handles use $O(n)$ space.

The per-operation time is asymptotically optimal because every call must perform at least $\Omega(1)$ work to observe or update state and return a result.

## Alternatives and edge cases

- **Store absolute deadlines:** Checking a deadline during `get` works, but `count` must then remove or scan expired entries unless another cleanup structure is maintained.
- **Periodic cleanup interval:** A global sweep can remove expired entries, but introduces delayed expiration, repeated scanning, and lifecycle management for the interval.
- **Uncancelled replacement timer:** Leaving the old timer active creates a race in which it deletes the replacement before the new duration ends.
- **Zero duration:** The key is inserted synchronously, then expires when the zero-delay timer callback is processed.
- **Expired reinsertion:** Once the timer has removed a key, setting it again returns `false` because no unexpired entry was replaced.
- **Sentinel value:** Values are nonnegative, so `-1` unambiguously represents a missing or expired key.
