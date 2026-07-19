## General
**Preserve each suspended list position**

Flattening everything in the constructor is simple, but it performs all work and stores all integers even if the caller consumes only a prefix. A genuinely lazy iterator should remember where traversal paused and descend only far enough to locate the next integer.

Represent each active nesting level by an iterator over that list. The stack begins with an iterator over the outermost list. To prepare the next value, inspect the iterator at the top:

- If that level is exhausted, pop it and resume its parent.
- If its next element is another list, push an iterator for the child list.
- If its next element is an integer, cache that integer and stop.

**Separate lookahead from consumption**

`hasNext()` performs this preparation only when no integer is already cached. Repeated calls therefore return `True` without advancing again. `next()` first ensures a value is ready, returns the cached integer, and clears the cache so the following call can continue the traversal.

**Trace the iterator stack**

For `[1, [4, [6]]]`, the outer iterator first yields `1`. It next yields a list, so its child iterator is pushed and yields `4`; another child is then pushed for `6`. Exhausted child iterators are popped in reverse order until the outer level is exhausted.

**Why the flattened order is exact**

The stack always describes one path from the outer list to the current traversal position, and each iterator points just after the last element taken from its level. Pushing a child before resuming its parent enforces depth-first order; retaining the parent iterator preserves the exact position to return to. Since an integer is cached at most once and is not removed by `hasNext()`, every integer is returned exactly once in left-to-right order.

## Complexity detail
Across a complete traversal, every nested entry is pulled from one level iterator once and every list iterator is pushed and popped once, for $O(N)$ total time. A particular `hasNext()` call may cross several empty or nested lists, but that work is not repeated, so iterator advancement is amortized $O(1)$ per entry. The stack contains at most one iterator per active nesting level and therefore uses $O(D)$ auxiliary space. Construction itself is $O(1)$.

## Alternatives and edge cases
- **Eager depth-first flattening:** takes $O(N)$ time but stores all `I` integers and performs work even when the caller consumes only a prefix.
- **Restart from the root for each value:** can take $O(N^2)$ over complete consumption.
- **Recursive list concatenation:** risks quadratic copying as increasingly large partial results are combined; one shared result avoids the copies but remains eager.
- Empty and arbitrarily nested empty lists must be skipped without making `hasNext()` return `True`.
- Repeated `hasNext()` calls must be idempotent and must not consume the cached integer.
- Zero and negative integers are values, not exhaustion markers.
