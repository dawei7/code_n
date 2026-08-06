## General

**Queue only vectors that still have a turn**

Store a pair `(values, i)` for each nonempty input, where `i` is its next unreturned position. `next()` removes the
front pair, returns `values[i]`, and appends `(values, i + 1)` to the back only when that vector still has another value.

The queue contains each vector with remaining values exactly once, ordered by whose turn comes next. Each stored
position points to that vector's first unreturned value.

**Re-enqueueing creates round-robin order**

Removing the front chooses exactly the vector whose turn is next. Returning its saved value consumes that value once.
If the vector remains active, appending it behind every other active vector schedules its next turn only after theirs;
otherwise omitting it prevents empty turns. Repetition therefore produces the exact zigzag sequence.

## Complexity detail

Each `next()` and `hasNext()` call performs a constant number of deque or indexing operations, so each is $O(1)$
amortized. With two vectors, the iterator stores at most two pairs and therefore uses $O(1)$ auxiliary space, excluding
the referenced inputs.

For the app adapter, let $N = \lvert\texttt{v1}\rvert + \lvert\texttt{v2}\rvert$. Collecting every yielded value takes
$O(N)$ total time and $O(N)$ returned-output space; it does not change the native per-operation bound recorded for the
iterator.

## Alternatives and edge cases

- **Delete or rescan vector prefixes:** repeats linear prefix work and can take $O(N^2)$ total time.
- **One empty vector:** it is omitted initially, so the nonempty vector is yielded in its original order.
- **Unequal lengths:** once the shorter vector is exhausted, only the longer vector remains in the deque.
- **Both vectors empty:** the app-local iterator reports no next value defensively, although the source contract requires
  at least one total element.
- **The $k$-vector follow-up:** enqueue each nonempty vector once; the same rotation keeps each operation $O(1)$ while
  iterator state grows to $O(k)$.
