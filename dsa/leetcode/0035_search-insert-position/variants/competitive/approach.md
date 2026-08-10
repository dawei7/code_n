## General

**Intended method: an inclusive lower-bound binary search**

The Competitive source aims to return the first index whose value is at least `target`. It keeps an inclusive undecided interval `[left, right]`. Values before `left` are known to be smaller than target. When the interval becomes empty, `left` is the insertion boundary, including the possible past-the-end value `len(nums)`.

This is the same mathematical lower bound as the Optimal variant but expressed with an inclusive right endpoint.

**The exact Python 3 source has a midpoint defect**

It calculates

```python
mid = left + (right - left) / 2
```

In Python 3, `/` returns a floating-point number. Even `0 / 2` becomes `0.0`. The following `nums[mid]` access therefore raises `TypeError` because list indices must be integers or slices.

The operator must be `// 2` for this implementation to run. The logic below explains the intended corrected algorithm, but the exact selected file fails on every legal non-empty input before it can return an answer. The manifest's complexity describes that intended algorithm, not actual successful Python 3 execution.

**Intended invariant and updates**

With integer `mid`, the test is

```python
if nums[mid] >= target:
    right = mid - 1
else:
    left = mid + 1
```

When the middle value is at least target, `mid` is a possible lower bound, but an earlier index may be the first. Moving `right` to `mid - 1` searches earlier positions. Although `mid` leaves the active interval, its position remains represented by the boundary that `left` will eventually reach if nothing earlier qualifies.

When the middle value is smaller, sortedness proves every index through `mid` is also too small, so `left = mid + 1` safely discards them.

**Why the crossed pointer is the insertion position**

The loop runs while `left <= right`. On exit, all real indices before `left` have been proven smaller than target, and any real index at or after `left` is not smaller. Therefore `left` is exactly where target belongs.

If target exists, its distinct existing index is the first not-smaller position. If it is absent, this boundary lies between the smaller and larger neighbors. If every value is smaller, `left` becomes `len(nums)`.

**Trace the intended search for target five**

For `[1,3,5,6]`, integer midpoint one has value three, so `left` becomes two. Midpoint two has value five, so `right` becomes one. The pointers cross with `left = 2`, returning the existing target index.

For target two, midpoint one has value three and moves `right` to zero. Midpoint zero has value one and moves `left` to one. The returned insertion position is one.

**Why no immediate equality return is needed**

Equality enters the `>=` branch and continues left. With distinct values this still returns the one equal index. This predicate-oriented form also generalizes to arrays with duplicates, where it would return the first occurrence rather than an arbitrary equal position.

**Operational truth versus intended proof**

The invariant proves the version using integer floor division. It cannot prove the behavior of the literal file under Python 3 because indexing fails before either update. A beginner implementing this pattern must regard midpoint type as part of correctness, not as cosmetic syntax.

**Why `left` remembers a discarded qualifying midpoint**

When `nums[mid] >= target`, the inclusive algorithm removes `mid` from the active interval by setting `right = mid - 1`. It may look as though a correct answer at `mid` has been lost. It has not: the search is trying to prove whether any earlier qualifying index exists. If one does, `left` will converge there. If none does, all earlier positions will eventually be proven smaller, causing `left` to advance back to `mid`. The returned crossed boundary therefore recovers the smallest qualifying position without storing a separate answer variable.

**Past-the-end is a legitimate boundary**

When every value is below target, every comparison takes the `left = mid + 1` branch. `left` finally becomes `len(nums)`. The method does not index at that value after the loop; it returns it as the position immediately after the final element. An insertion index ranges from zero through `n`, even though existing element indices stop at `n - 1`.

**The midpoint correction must preserve integer floor behavior**

Changing `/ 2` to `int((right - left) / 2)` would happen to work for these nonnegative differences, but `// 2` states the integer-search intent directly and avoids creating a float at all. `left + (right - left) // 2` also keeps the midpoint inside the active inclusive interval.

## Complexity detail

For the corrected integer-midpoint algorithm:

- **Time complexity: $O(\log n)$.** Each iteration removes at least half of the remaining inclusive interval.
- **Auxiliary space: $O(1)$.** Only three scalar indices are used.

For the exact `/`-based Python 3 source, non-empty inputs terminate with `TypeError` in the first iteration, so successful-search complexity is not applicable.

## Alternatives and edge cases

- **Replace `/` with `//`:** This is the required minimal correction.
- **Half-open interval:** Initialize `right = len(nums)` and retain `mid` with `right = mid`; this is the Optimal source's convention.
- **Built-in `bisect_left`:** Directly returns the same boundary in Python.
- **Target below all values:** The corrected algorithm returns zero.
- **Target above all values:** The corrected algorithm returns `len(nums)`.
- **Existing target:** Equality continues left and returns its index.
- **One-element input:** The exact source fails with float index; the corrected source returns zero or one.
- **Empty input outside the stated lower bound:** The loop would be skipped and return zero even in the exact source.
- **Distinct values:** Guaranteed, though lower-bound logic would also handle duplicates.
- **No mutation:** Only an index should be returned.
