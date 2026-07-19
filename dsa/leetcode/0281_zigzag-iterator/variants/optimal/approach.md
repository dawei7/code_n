## General
**Queue only vectors that still have a turn**

Store a pair `(vector, next_index)` for each nonempty input. `next()` removes the front pair, returns its indexed value, and appends the pair to the back only when that vector still has another value.

The queue contains each vector with remaining values exactly once, ordered by whose turn comes next. Each stored index points to that vector's first unreturned value.

**Re-enqueueing creates round-robin order**

Removing the front chooses exactly the vector whose turn is next. Returning its indexed value consumes that value once. If the vector remains active, appending it behind every other active vector schedules its next turn only after theirs; otherwise omitting it prevents empty turns. Repetition therefore produces the exact zigzag sequence.

## Complexity detail
Each operation performs a constant number of deque actions, so it is $O(1)$ amortized. With two vectors, iterator state is $O(1)$ excluding the referenced inputs.

## Alternatives and edge cases
- **Delete index zero from lists:** repeatedly shifts remaining values and can take $O(n^2)$.
- Empty vectors are omitted initially, and unequal lengths naturally leave one active vector.
