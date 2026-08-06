## General

**Keep exactly one value ahead of the public cursor**

During construction, consume the underlying iterator's first value when one exists. `peek()` returns the cache.
`next()` returns that cached value and immediately refills from the underlying iterator when another value exists.

When `has_next` is true, the cache contains exactly the next value in the wrapper's public sequence. When false, both
the wrapper and underlying iterator are exhausted.

**Peek observes the cache; next advances it**

`peek()` never touches the underlying iterator, so any number of peeks returns the same next value. `next()` returns
that cached value and refills once, advancing the public sequence by exactly one element. When no refill is possible,
both layers are exhausted, making `hasNext()` accurate.

The candidate's offline `Iterator` uses `i` as its cursor. The adapter executes each requested operation against the
same `PeekingIterator` class and collects the observed results without changing the native state machine.

## Complexity detail

Every public method makes at most one underlying iterator call and constant local work, so `peek()`, `next()`, and
`hasNext()` are each $O(1)$. The wrapper stores one cached value, one availability flag, and one iterator reference, so
its auxiliary space is $O(1)$.

If the app adapter executes $q$ requested operations, the complete adapter run takes $O(q)$ time and $O(q)$ returned
output space; these aggregate costs do not change the native per-method bounds.

## Alternatives and edge cases

- **Copy all remaining values:** uses $O(n)$ space.
- **Delete the first list item repeatedly in an adapter:** can take $O(n^2)$ due to shifting.
- **Repeated peeks:** are idempotent because they never refill or otherwise mutate the cache.
- **Consume the final value:** `next()` returns it, finds no underlying successor, and leaves `hasNext()` false.
- **Valid-call guarantee:** `peek()` and `next()` need no empty-state exception path because the source promises that
  every such call is valid.
- **Generic follow-up:** parameterize the wrapped iterator and cached value by an element type; the state machine and
  bounds remain unchanged.
