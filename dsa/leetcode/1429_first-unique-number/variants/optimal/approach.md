## General

**Track frequency and arrival order separately.** A value is eligible only while its total frequency is one, but the answer must also respect when values arrived. Store total frequencies in a hash map and append a value to a deque exactly when its first occurrence is processed. Feed the constructor's entire `nums` array through the same `add` operation used for later arrivals, so initialization and updates share one state transition.

**Retain stale entries until they reach the front.** When a deque member appears again, its frequency rises above one and it can never become unique later because the stream only grows. Removing that member from the middle of a deque would be expensive, so `add` leaves it in place. Before answering a query, discard front entries whose frequencies exceed one. This cleanup is safe because each discarded value is permanently ineligible.

The deque preserves first-occurrence order. After cleanup, every earlier deque entry has been proved non-unique, and the surviving front has frequency one. It is therefore the earliest currently unique value. If cleanup empties the deque, every value that has ever appeared is non-unique, so the required result is `-1`.

## Complexity detail

Let $n$ be the initial array length and $q$ the number of later operations. Each value's first occurrence is appended once, and each deque entry is removed at most once. `add` takes expected $O(1)$ time. A single `showFirstUnique` call may remove several stale entries, but over the complete lifecycle all cleanup costs $O(n+q)$, making each operation amortized expected $O(1)$ and the full trace $O(n+q)$ expected time. The frequency map and deque use $O(n+q)$ space in the worst case.

## Alternatives and edge cases

- **Doubly linked list plus node map:** Keep only currently unique values in arrival order and delete a node on its second occurrence. This gives expected $O(1)$ updates and queries but requires more pointer bookkeeping than lazy deque cleanup.
- **Insertion-ordered map of current uniques:** An ordered hash map can express the same immediate-deletion strategy compactly where insertion order and constant expected-time deletion are guaranteed.
- **Heap or ordered set:** Pair frequencies with an order-aware structure for $O(\log(n+q))$ operations. This is correct but weaker than the required linear total bound.
- **Rescan the arrival history:** Recounting or searching from the beginning at every query is correct, but alternating additions and queries can make the full trace quadratic.
- **No current unique value:** Lazy cleanup may empty the deque, in which case return `-1`.
- **Frequencies above two:** Once a value is stale, further copies only increase its count; they neither append a new deque entry nor restore uniqueness.
- **Repeated queries:** A query that finds a valid front does not mutate it, so consecutive queries return the same value until a relevant addition occurs.
- **Single initial value and numeric limits:** The same transitions handle the minimum array length and values at either allowed endpoint without special cases.
