## General

**Turn boundary finding into a monotone Boolean search**

The selected Competitive entry point defines a reusable `binarySearch(n, check)` helper. It assumes `check(i)` is false for an initial portion of indices and true for every index after one transition. The helper returns the first index where the predicate becomes true, or `n` when it never does.

This lower-bound abstraction solves both requested endpoints by changing only the predicate:

- `nums[i] >= target` finds the first target-or-larger position;
- `nums[i] > target` finds the first position after all target copies.

**Maintain an inclusive undecided interval**

The helper starts with

```python
left, right = 0, n - 1
```

Indices before `left` are known false. Indices after `right` are known true candidates or the sentinel boundary `n`. While `left <= right`, it chooses an integer midpoint with floor division.

If `check(mid)` is true, the first true index might be `mid` or somewhere earlier, so the source sets `right = mid - 1`. If it is false, every earlier position is also false by monotonicity, so `left = mid + 1`.

When the interval becomes empty, `left` is exactly the first true position. If the predicate was false everywhere, repeated rightward movement leaves `left == n`.

**Find the first occurrence candidate**

The first call is

```python
left = binarySearch(len(nums), lambda i: nums[i] >= target)
```

Sortedness makes the predicate monotone: values below target come first, followed by values equal to or greater than it. If target exists, the first true position is its first occurrence. If target is absent, the position may instead hold a greater value or may be the past-the-end sentinel.

The source validates both possibilities safely:

```python
if left == len(nums) or nums[left] != target:
    return [-1, -1]
```

Short-circuit `or` prevents `nums[left]` from being evaluated when `left` is out of bounds.

**Find the exclusive upper boundary**

Once presence is proven, the second call searches with `nums[i] > target`. Every value through the final target makes this predicate false; the first larger value makes it true. If no larger value exists, the helper returns `len(nums)`.

The returned `right` is therefore exclusive. Subtracting one converts it to the last included target index:

```python
return [left, right - 1]
```

Because presence was already established, `right` must be at least `left + 1`, so `right - 1` is a valid target index.

**Trace the duplicate block**

For `[5,7,7,8,8,10]` and target eight, the first predicate is false at indices zero through two and true from three onward. The helper returns three. Equality confirms presence.

The second predicate is false through index four and true at index five because ten is greater than eight. It returns five, so the inclusive answer is `[3,4]`.

For target six, the first predicate transitions at index one because seven is the first value at least six. Validation finds `nums[1] != 6` and returns absence without running the second search.

**Only one of four local helpers is actually selected**

The source also defines `binarySearch2`, `binarySearch3`, and `binarySearch4` as alternative interval conventions. They are never called by `searchRange`. Their definitions do not change the executed algorithm, runtime, or result.

This explanation follows `binarySearch`, whose interval is `[0, n - 1]`. Mixing its updates with one of the other helpers' half-open or sentinel invariants would create off-by-one errors.

**Why the two boundaries prove correctness**

The first monotone search returns the earliest index not below target. Validation proves this is the first target rather than merely its insertion position. The second returns the earliest index strictly above target, so the preceding index is the last target. Sortedness guarantees no target lies outside those boundaries and every value between them equals target.

## Complexity detail

Let $n$ be the array length.

- **Time complexity: $O(\log n)$.** Each helper call halves an inclusive interval. At most two calls run, and $2\log n$ is $O(\log n)$.
- **Auxiliary space: $O(1)$.** The helper is iterative. Four helper function objects and two short-lived lambda closures are a fixed amount of storage independent of input length. The result has exactly two integers.

## Alternatives and edge cases

- **Python `bisect_left` and `bisect_right`:** Library boundary searches express the same two transitions concisely.
- **Two specialized binary searches:** Separate first-position and last-position loops can be easier to teach but duplicate control flow.
- **One match plus outward scans:** Correct but can become linear for a large duplicate block.
- **Empty input:** `right = -1`, the helper returns zero, and the sentinel check returns absence.
- **Target at both ends:** Boundaries may be zero and `n`; both sentinel values are handled.
- **One occurrence:** The strict-greater boundary is exactly one position after the lower boundary.
- **Target missing between values:** The lower-bound result points to the next larger value and validation rejects it.
- **Target larger than all values:** The lower bound is `n`, and short-circuiting avoids invalid indexing.
- **Monotonic predicate requirement:** The helper is correct because `nums` is sorted; it is not a general search for arbitrary Boolean patterns.
- **Unused helpers:** Their presence is educational source material, not additional searches performed at runtime.
