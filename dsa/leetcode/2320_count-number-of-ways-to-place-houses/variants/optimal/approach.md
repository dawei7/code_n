## General

**Solve one side of the street**

For a processed prefix, separate arrangements by whether its final plot is
empty or contains a house. An empty plot may follow either state, while a house
may follow only a prefix ending empty. Starting from one empty and one occupied
arrangement at the first plot, these two transitions count every legal pattern
on one side.

**Combine the independent sides**

The adjacency rule never crosses the street. Therefore, every valid pattern on
one side may be paired with every valid pattern on the other side. If
`one_side` is the sum of the two final states, the answer is
`one_side * one_side`.

The recurrence is complete because every one-side arrangement has exactly one
final-plot state, and its permitted extensions are precisely the two
transitions above. Squaring then gives a one-to-one count of ordered pairs of
side patterns.

## Complexity detail

Each of the $n$ plot positions updates two values in constant time, giving
$O(n)$ time. Only the two rolling states are retained, so auxiliary space is
$O(1)$. Arithmetic is reduced modulo $10^9+7$.

## Alternatives and edge cases

- **Enumerate occupancy masks:** Testing every one-side bit mask is correct but takes $O(2^n)$ time.
- **Array dynamic programming:** Storing both states for every position gives the same $O(n)$ time with unnecessary $O(n)$ space.
- **Fast doubling or matrix exponentiation:** Fibonacci structure permits $O(\log n)$ time, but the linear recurrence is simpler within the stated bound.
- **One plot:** Both states are available independently on both sides, producing four placements.
- **Across the street:** Opposite plots may both contain houses; only neighbors on the same side conflict.
- **Empty placement:** The all-empty arrangement is included.
