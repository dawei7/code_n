## General
**Separate frequency from arrival order.** Maintain a hash map from each value to its total frequency and a queue containing values when they first become unique. During construction, feed every initial value through the same `add` logic used for later updates.

**Append only on the first occurrence.** When `add(value)` changes the frequency from zero to one, append the value to the queue. If its frequency becomes two or more, leave any earlier queue entry in place. Removing an arbitrary middle entry would complicate updates; instead, defer cleanup until the front matters.

**Clean stale candidates lazily.** For `showFirstUnique()`, repeatedly discard the queue front while its stored frequency exceeds one. Every discarded value is permanently non-unique because frequencies only increase. Therefore the first surviving entry has appeared exactly once and arrived before every other surviving entry. If the queue empties, no unique value remains and the result is `-1`.

## Complexity detail
Building from $n$ initial values and processing $q$ later calls takes $O(n+q)$ expected time because each hash-map operation is expected $O(1)$ and each queued value is appended and removed at most once. The frequency map and queue together store at most $O(n+q)$ values.

## Alternatives and edge cases
- **Rescan the whole stream:** Count frequencies and search from the beginning for every query. It is correct but repeated queries can make total time quadratic.
- **Ordered map of unique values:** Removing a value when its second occurrence arrives also supports constant expected-time operations, but it requires an insertion-ordered map with deletion.
- **No unique values:** After stale queue entries are removed, return `-1`.
- **Repeated additions:** Frequencies above two require no extra queue entries or special transitions.
- **Initially empty array:** The first added value becomes the first unique value.
- **Reappearance after duplication:** A non-unique value can never become unique again because the stream only gains occurrences.
