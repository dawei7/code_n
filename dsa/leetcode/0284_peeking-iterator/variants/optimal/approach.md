## General

**Why peeking requires one saved value**

The underlying iterator exposes only `next()` and `hasNext()`. Calling its `next()` is destructive from the caller's perspective: it returns the current element and advances the underlying position. There is no method for moving that iterator backward.

To implement `peek()`, the wrapper must learn the next value without advancing its own logical position. The only available way to learn that value is to call the underlying `next()`, so the wrapper must save the returned element and give it back later when its own `next()` is called.

Only one value of lookahead is required. `peek()` asks about the immediate next element, not an arbitrary future offset. The exact source stores that one possible value in `peeked_element` and records whether the cache is occupied in `has_peeked`.

**Use a flag instead of treating `None` as the state**

The constructor initializes

```text
has_peeked = False
peeked_element = None
```

The Boolean is the authoritative state. `peeked_element` is meaningful only when `has_peeked` is true. This separation is stronger than checking whether the cached value is `None`: in a generic iterator, `None` might itself be a legitimate element. A separate occupancy flag distinguishes “a cached value whose value happens to be `None`” from “there is no cached value.”

Although the current problem uses positive integers, the exact design already contains the key mechanism needed by the generic follow-up.

**Two logical states describe the wrapper**

When `has_peeked` is false, no element is buffered. The wrapper's next logical value is still the underlying iterator's next value.

When `has_peeked` is true, `peeked_element` is the wrapper's next logical value. The underlying iterator has already advanced one position beyond it, but that advancement is hidden from users until the wrapper's `next()` consumes the cache.

This distinction between physical underlying position and logical wrapper position is the heart of the design. A peek may advance the wrapped object internally, yet the public sequence does not advance because the fetched value remains pending in the cache.

**Implement the first `peek()` by filling the cache**

If no value is cached, `peek()` calls `self.iterator.next()`, stores the returned value, and sets `has_peeked` to true. It then returns the cached value.

If a value is already cached, `peek()` returns it directly and makes no underlying call. Consequently, any number of consecutive peeks returns the same element:

```text
peek() -> x
peek() -> x
peek() -> x
```

The underlying iterator advances only during the first call. Later peeks observe the saved value, so the wrapper's logical position remains unchanged.

The constraints guarantee that every `peek()` call is valid, so the source does not separately call the underlying `hasNext()` before fetching. Under the contract, a nonempty next value exists whenever this branch runs.

**Implement `next()` differently in the two states**

If `has_peeked` is false, no lookahead has occurred. The wrapper delegates directly to `self.iterator.next()` and returns that value. The underlying iterator advances exactly once, as an ordinary iterator should.

If `has_peeked` is true, the underlying iterator has already advanced past the logical next value during the earlier peek. Calling it again would skip an element. Instead, the wrapper copies `peeked_element` into `result`, clears `has_peeked`, resets `peeked_element` to `None`, and returns `result`.

Clearing the state makes the cached value consumable exactly once. The following operation again sees the next value from the underlying iterator. Resetting the value field is not required for correctness once the flag is false, but it removes a stale reference and makes the inactive state explicit.

**Make `hasNext()` account for buffered data**

The correct condition is

```text
has_peeked or iterator.hasNext()
```

If a value is cached, the wrapper definitely has a next element even if the underlying iterator now reports false. This situation occurs when `peek()` fetched the underlying iterator's final element: physically, the wrapped iterator is exhausted, but logically, the wrapper still owes that cached element to its caller.

Python's `or` short-circuits. When `has_peeked` is true, `iterator.hasNext()` is not called because the answer is already known. When the cache is empty, the wrapper's availability exactly matches the underlying iterator's availability.

**A sequence-preservation invariant**

At all times, the sequence of elements still observable through the wrapper equals:

- `[peeked_element]` followed by the underlying iterator's remaining sequence when `has_peeked` is true; or
- exactly the underlying iterator's remaining sequence when `has_peeked` is false.

The constructor establishes the second case. Filling the cache removes the first underlying element but places that same element in front of the remaining sequence, preserving the wrapper-visible sequence. Repeated peeks do not change either component. A cached `next()` removes the cached first element; a direct `next()` removes the underlying first element. Both operations therefore return and consume exactly the wrapper-visible next value.

This invariant proves that peeking never changes the order, duplicates an element, or loses an element.

**Trace the example**

Start with underlying values `[1,2,3]` and an empty cache:

| Operation | Returned value | Cache afterward | Underlying remainder |
|---|---:|---|---|
| `next()` | 1 | empty | `[2,3]` |
| `peek()` | 2 | contains 2 | `[3]` |
| `next()` | 2 | empty | `[3]` |
| `next()` | 3 | empty | `[]` |
| `hasNext()` | false | empty | `[]` |

The peek physically fetched 2 from the wrapped iterator, but caching made the following wrapper `next()` return 2 rather than skipping to 3.

If the operations instead call `peek()` twice before `next()`, both peeks return 2, the underlying remainder stays `[3]` after the first peek, and the later `next()` consumes the single cached 2 once.

## Complexity detail

Each wrapper method performs a constant number of flag checks, assignments, and at most one underlying iterator call. Assuming the supplied iterator's `next()` and `hasNext()` are $O(1)$, constructor, `peek()`, `next()`, and `hasNext()` each take $O(1)$ time.

The wrapper stores one iterator reference, one Boolean, and one cached element. Its additional space is $O(1)$ regardless of the length of the underlying sequence. It does not copy or materialize the sequence, preserving the streaming benefits of the iterator abstraction.

Across a complete traversal of $n$ values, every underlying element is fetched exactly once—either by a direct wrapper `next()` or by the first `peek()` before its cached consumption. Repeated peeks add only constant work each and do not increase underlying consumption.

## Alternatives and edge cases

- **Prefetch in the constructor:** Always store the next element immediately and refill after every `next()`. This can simplify method branches, but construction must handle an empty iterator and performs work even if no method is called. The exact source fetches lazily.
- **Copy all remaining values:** Materializing the iterator into a list makes peeking easy but uses $O(n)$ space, fails for infinite streams, and defeats the iterator abstraction.
- **Use `None` as the only sentinel:** This works only if `None` can never be a real element. The explicit `has_peeked` flag is safer and supports generic value types.
- **Repeated peeks:** Only the first fills the cache. Every later peek returns the same pending value without advancing anything further.
- **Peek at the final element:** The underlying iterator becomes physically exhausted, but `hasNext()` remains true because the cached final element is still logically available.
- **Next after peek:** It must return the cache and must not call the underlying iterator again, or the peeked value would be skipped.
- **Next without peek:** Direct delegation is correct because no buffered value stands between the wrapper and the underlying sequence.
- **Valid-call guarantee:** The source assumes `peek()` and `next()` are never requested when no logical element remains. It does not define a custom exception path for invalid calls.
- **Empty iterator outside current constraints:** Construction remains safe because it does not prefetch. `hasNext()` delegates and returns false; invalid `peek()` or `next()` would rely on the underlying iterator's behavior.
- **Generic values:** Replacing integer-specific annotations with a type parameter is sufficient for storage and returns. The existing Boolean occupancy flag already permits falsey values such as `0`, `False`, empty strings, and even `None`.
- **External use of the wrapped iterator:** The wrapper assumes exclusive control of the supplied iterator after construction. Advancing it separately would desynchronize the cached logical view and is outside the intended design.
- **Thread safety:** Concurrent method calls could race on the cache fields. The interview design is single-threaded; a shared concurrent wrapper would need synchronization.
