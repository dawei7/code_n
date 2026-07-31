## General

**Turn equal values into one decision**

Selecting by row makes the value-uniqueness rule awkward because a value chosen now may occur in many later rows. Reverse the viewpoint: process each possible value once, and decide either to skip it or assign it to one row that contains it. Processing a value only once makes duplicate selection impossible by construction.

For every value that occurs, record the rows in which it appears. Repeated copies within one row add that row only once. A bitmask represents rows already used by the partial selection.

Memoize `search(value_index, used_rows)`, the best additional score obtainable from the remaining distinct values. One branch skips the current value. Every other branch assigns it to one row that contains it and whose bit is absent from `used_rows`; that branch sets the row bit, adds the value, and advances to the next value. Advancing on every branch ensures that the same value cannot be assigned twice.

Inductively, every state represents selections with unique processed values and unique rows. A skip preserves those properties, and an assignment adds the current value once to one unused row. Conversely, every valid selection either omits the current value or chooses it from exactly one available row, so one of these branches constructs it. Memoization solves each pair of value position and used-row mask once, and the initial state therefore returns the best valid score.

## Complexity detail

There are $2^m$ row masks at each of at most $V$ value positions. A state may inspect up to $m$ candidate rows, giving $O(Vm2^m)$ time. The memoized states and recursion use $O(V2^m)$ space; the value-to-row mapping is smaller than that bound.

## Alternatives and edge cases

- **Backtrack row by row:** Trying every cell choice and an optional skip is correct, but repeats equivalent subproblems and can grow exponentially in both row and column choices.
- **Choose each row's maximum:** Two rows can share that maximum, and resolving the collision greedily may sacrifice a better global assignment.
- **Track used values directly:** A 100-bit value mask is much larger than the row mask; processing values as stages keeps the exponential dimension at $m \le 10$.
- Duplicate occurrences of a value within one row should create only one transition.
- If every cell has the same value, exactly one occurrence can contribute to the score.
- A row may remain unused when all of its values conflict with more profitable choices.
- Equal values in different rows remain one global choice, not separate selectable items.
- All values are positive, so the final optimum is nonzero even though the empty state initializes the dynamic program.
- A one-row grid reduces to selecting its largest value.
