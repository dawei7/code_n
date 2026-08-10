## General

**Search for insertion boundaries instead of individual matches**

All copies of `target` are contiguous because `nums` is non-decreasing. The desired range can therefore be described by two boundaries:

- `l` is the first index whose value is at least `target`; and
- `r` is the first index whose value is strictly greater than `target`.

If target occurrences exist, they occupy exactly the half-open interval `[l, r)`, so the requested inclusive result is `[l, r - 1]`.

The selected implementation obtains both boundaries with Python's `bisect_left`, a library binary search that returns the first insertion position at which its argument can be placed without disturbing sorted order.

**What `bisect_left(nums, target)` guarantees**

The first call is

```python
l = bisect_left(nums, target)
```

Every index before `l` contains a value strictly less than `target`. If `l < len(nums)`, then `nums[l]` is at least `target`. Therefore, if target exists, `l` is its earliest occurrence. If every value is smaller, `l` is `len(nums)`; if the array is empty, it is zero.

The function does not promise that `nums[l]` equals the searched value. It returns an insertion boundary even when the value is absent. The second boundary and equality-of-boundaries test resolve that distinction.

**Use `target + 1` to express a strict upper boundary for integers**

The source computes

```python
r = bisect_left(nums, target + 1)
```

All array values and `target` are integers. There is no integer strictly between `target` and `target + 1`. Consequently, the first value at least `target + 1` is exactly the first integer value strictly greater than `target`.

Thus `r` lies immediately after the final target occurrence. This is equivalent to `bisect_right(nums, target)` for integer data.

The integer-domain fact is important. For arbitrary real values, searching for `target + 1` would skip values between those numbers and would not define the strict target boundary.

Python integers do not overflow when one is added. Under the stated target bound of $10^9$, `target + 1` would also fit comfortably in ordinary wider fixed-width types.

**Why `l == r` means the target is absent**

The interval `[l, r)` contains exactly values `x` satisfying

$$
\texttt{target}\le x<\texttt{target}+1.
$$

For integer `x`, the only possible value in this interval is `target` itself. Its length `r - l` therefore equals the number of target occurrences.

If `l == r`, the interval is empty and the method returns `[-1, -1]`. If `l < r`, at least one target exists, the first index is `l`, and the last included index is `r - 1`.

This reasoning avoids a separate potentially unsafe `nums[l]` access when the array is empty or when `l == len(nums)`.

**Trace `[5,7,7,8,8,10]` for target eight**

`bisect_left(nums, 8)` returns three because indices zero through two contain values below eight and index three is the first eight. `bisect_left(nums, 9)` returns five because index five contains ten, the first integer at least nine. The half-open block is `[3,5)`, so the inclusive answer is `[3,4]`.

For target six, the insertion position of six is one, immediately before the first seven. The insertion position of seven is also one. Equal boundaries prove that no integer six occurs, so the result is `[-1,-1]`.

**Why duplicates do not damage binary search**

Ordinary binary search may stop at any equal element. Boundary binary search changes the equality rule: `bisect_left` continues conceptually toward the left whenever a value is equal to the query. This converges to the first legal insertion index. Running it on the next integer creates the symmetric boundary after all equal copies.

**Why the answer is correct**

Sortedness guarantees all values before `l` are below target and all values from `r` onward are above target. Every integer between those boundaries must equal target. Hence a non-empty boundary interval contains all and only target occurrences, and converting its exclusive end to `r - 1` gives the requested final index. An empty interval proves absence.

## Complexity detail

Let $n$ be `len(nums)`.

- **Time complexity: $O(\log n)$.** Each `bisect_left` halves its search interval until an insertion boundary is found. Two logarithmic searches remain $O(\log n)$.
- **Auxiliary space: $O(1)$.** The library searches are iterative in CPython and the source stores only two indices plus the fixed two-element result. No slice or input-sized structure is created.

## Alternatives and edge cases

- **`bisect_right(nums, target)`:** It directly returns the upper boundary and avoids the integer-successor trick.
- **Custom lower-bound helper:** Search once with predicate `nums[i] >= target` and once with `nums[i] > target`; this is the Competitive variant.
- **Find one match then scan:** It can degrade to $O(n)$ when many values equal target.
- **Empty array:** Both boundaries are zero, yielding `[-1,-1]` safely.
- **One matching value:** Boundaries differ by one and both reported indices are the same.
- **All values equal target:** `l = 0` and `r = n`.
- **Target below every value:** Both insertion boundaries are zero.
- **Target above every value:** Both boundaries are `n`.
- **Integer requirement:** The `target + 1` equivalence relies on there being no legal value between consecutive integers.
- **No mutation:** Both searches read `nums` and return a new two-integer result list.
