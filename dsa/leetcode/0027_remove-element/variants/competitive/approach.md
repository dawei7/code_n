## General

**Use the permission to change order**

When order does not matter, an unwanted value near the front does not require shifting every later retained value left. It can be replaced by a value from the end of the still-active region. The Competitive solution uses `i` to inspect from the front and `last` to mark the final index still belonging to that region.

At all times, indices greater than `last` are logically discarded. They may contain anything. Indices below `i` are already known not to equal `elem`. The interval `A[i:last + 1]` is the unchecked work remaining.

**Represent an empty active interval cleanly**

Initialization is

```python
i, last = 0, len(A) - 1
```

For an empty array, `last = -1`, so `i <= last` is false and the method returns `last + 1 = 0`. No separate empty-input branch is necessary.

The loop invariant is:

- every index below `i` contains a retained value;
- every index above `last` is outside the logical result; and
- every value whose fate is not yet decided lies between `i` and `last`, inclusive.

**Discard a matching value by shrinking from the right**

When `A[i] == elem`, the source swaps it with `A[last]`:

```python
A[i], A[last] = A[last], A[i]
last -= 1
```

The unwanted occurrence moves to the old active tail, which is then excluded by decrementing `last`. The value moved into `A[i]` came from the unchecked interval, so it still needs classification.

That is why `i` does not advance in this branch. The replacement might also equal `elem`. Rechecking the same index on the next iteration repeatedly removes matching tail values until a retained value arrives or the active interval becomes empty.

Python evaluates the right-hand sides of the multiple assignment before writing either destination, so the two values are genuinely exchanged without a temporary variable.

**Advance only after proving the current value is retained**

If `A[i] != elem`, that position is valid and can join the established prefix. The source performs `i += 1`. This expands the proven-good region by one while leaving `last` fixed.

Each iteration therefore makes progress: either `i` increases or `last` decreases. Since the two bounds begin at opposite ends and the loop runs only while `i <= last`, termination is guaranteed.

**Why the returned length is `last + 1`**

At termination, `i > last`. The invariant says every index below `i` is retained and every index above `last` is discarded. Because the pointers have crossed, the active result occupies exactly indices `0` through `last`. Its length is therefore `last + 1`.

In fact, `i` also equals that length at termination, but the exact source returns the boundary-derived expression.

**Trace a case with repeated removals at the tail**

For `A = [2, 1, 2, 2]` and `elem = 2`, `i = 0` and `last = 3`. The first match swaps equal `2` values and reduces `last` to two; `i` remains zero. The next iteration does the same and reduces `last` to one. Now swapping with `A[1]` moves `1` to index zero and reduces `last` to zero. The same index is checked again, sees `1`, and increments `i` to one. The pointers cross and the method returns one, with meaningful prefix `[1]`.

If the method had incremented `i` immediately after the first swap, a newly moved `2` could have escaped removal.

**Trace the provided mixed example**

For `[0,1,2,2,3,0,4,2]`, the front pointer accepts `0` and `1`. At the first `2`, it swaps in the final `2` and shrinks the boundary, then rechecks and swaps in `4`. The `4` is retained. Later another `2` is replaced from the active tail. The eventual prefix may be `[0,1,4,0,3]`, matching the example's allowed reordered form.

**Why the partition is correct**

Every nonmatching value seen at `i` is permanently placed below the advancing front boundary. Every matching value seen there is swapped to the active tail and permanently excluded when `last` shrinks. A swapped-in value remains unchecked until the same logic classifies it. Thus no unchecked value is silently skipped. When the interval empties, all retained occurrences lie in the prefix and no prefix value equals `elem`; every excluded matching occurrence lies beyond the returned boundary.

## Complexity detail

Let $n$ be the initial array length.

- **Time complexity: $O(n)$.** Every iteration increments `i` or decrements `last`. Each pointer moves at most $n$ times, so at most $n$ active positions are classified. A swap is constant time.
- **Auxiliary space: $O(1)$.** Two indices and temporary references used by Python's assignment are independent of input size.

The number of swaps equals the number of removed occurrences encountered in the active region. This can perform fewer writes than stable compaction when `elem` is rare.

## Alternatives and edge cases

- **Stable write-pointer compaction:** Copy every nonmatching value forward. It preserves order and is often simplest, but writes every retained value even when very few removals occur.
- **Physical deletion:** It changes list length but shifts array suffixes and can become quadratic.
- **Allocate a filtered array:** Easy to express, but violates the $O(1)$ auxiliary-space goal.
- **Empty input:** `last = -1`; the loop is skipped and zero is returned.
- **All values match:** `last` repeatedly shrinks while `i` stays zero, producing an empty prefix.
- **No values match:** `i` crosses the array with no swaps and returns the original length.
- **Replacement also matches:** The unchanged `i` deliberately checks it again.
- **One element:** It returns zero for a match and one otherwise.
- **Order changes:** Moving tail values forward is permitted; consumers must not expect stability.
- **Retained duplicates:** Values unequal to `elem` are preserved with their full multiplicity.
- **Unspecified suffix:** Swapped-out occurrences and other stale values beyond `last` are irrelevant.
- **Judge comparison:** Only `A[:last + 1]` is meaningful; sorting that prefix is sufficient to compare unordered retained values.
