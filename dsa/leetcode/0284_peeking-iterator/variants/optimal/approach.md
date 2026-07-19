## General
**Keep exactly one value ahead of the public cursor**

During construction, consume the underlying iterator's first value when one exists. `peek()` returns the cache. `next()` returns it and immediately refills from the underlying iterator.

When `has_next` is true, the cache contains exactly the next unconsumed underlying value. When false, both the wrapper and underlying iterator are exhausted.

**Peek observes the cache; next advances it**

`peek()` never touches the underlying iterator, so any number of peeks returns the same next value. `next()` returns that cached value and refills once, advancing the public sequence by exactly one element. When no refill is possible, both layers are exhausted, making `hasNext()` accurate.

## Complexity detail
Every method makes at most one underlying iterator call and constant local work, using one cached value and one boolean.

## Alternatives and edge cases
- **Copy all remaining values:** uses $O(n)$ space.
- **Delete the first list item repeatedly in an adapter:** can take $O(n^2)$ due to shifting.
- Repeated peeks are idempotent, and consuming the final value makes `hasNext()` false.
