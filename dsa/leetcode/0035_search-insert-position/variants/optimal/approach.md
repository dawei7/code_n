## General

**Search for the first value that is not smaller than the target**

The requested answer has one unified definition whether or not `target` exists:

> Return the first index `p` for which `nums[p] >= target`, or `len(nums)` if every value is smaller.

If target exists in this distinct sorted array, that position is its index. If it does not exist, inserting it there places it after all smaller values and before all larger values. This is commonly called a lower-bound search.

**Use a half-open candidate interval**

The exact source initializes

```python
l, r = 0, len(nums)
```

and treats `[l, r)` as the interval in which the lower boundary may lie. Unlike an inclusive-right binary search, `r` is allowed to equal `len(nums)`. That past-the-end position is a valid answer when target belongs after every element.

The invariant is:

- every index before `l` has a value strictly less than target; and
- every real index at or after `r` has a value greater than or equal to target.

Initially there is no index before zero, and there is no real index at or after `len(nums)`, so both statements hold vacuously.

**Choose an integer midpoint inside the interval**

While `l < r`, at least one candidate position remains. The midpoint is

```python
mid = (l + r) >> 1
```

For nonnegative indices, right shifting by one is floor division by two. Because `mid < r <= len(nums)`, `nums[mid]` is always a valid element access while the loop runs.

**Keep the midpoint when it could be the first legal position**

If `nums[mid] >= target`, `mid` satisfies the lower-bound value condition. It might be the first satisfying index, but an earlier one might also qualify. The update

```python
r = mid
```

keeps `mid` inside the half-open candidate interval while discarding everything strictly after it. Setting `r = mid - 1` would mix inclusive and half-open conventions and could skip the correct boundary.

If `nums[mid] < target`, `mid` cannot be the insertion position, and neither can any earlier index because the array is ascending. The source uses `l = mid + 1`, discarding the entire proven-smaller prefix.

**Why equality searches left rather than returning immediately**

The contract says values are distinct, so returning immediately on equality would also give the right index. The exact source nevertheless uses lower-bound behavior and moves `r = mid`. This formulation remains correct even if duplicates are later allowed: it would return the first equal value.

More importantly, one consistent predicate handles both presence and absence without a separate equality branch.

**Trace insertion between values**

For `nums = [1,3,5,6]` and target two, the initial midpoint is two with value five. Since five is at least two, `r` becomes two. The new midpoint is one with value three, so `r` becomes one. Midpoint zero has value one, which is smaller, so `l` becomes one. Now `l == r == 1`, and index one is returned: inserting two there yields `[1,2,3,5,6]`.

For target seven, every inspected value is smaller, so `l` advances until it equals `len(nums) = 4`. Returning four correctly means append at the end.

**Why convergence returns the answer**

Each iteration shrinks `[l, r)`: either `r` moves down to `mid` or `l` moves above `mid`. The invariant is preserved by sortedness. At termination `l == r`, leaving one boundary between the proven-smaller prefix and the proven-not-smaller suffix. That boundary is exactly the lower bound and therefore the required existing or insertion index.

**Why returning `len(nums)` is not an out-of-bounds mistake**

An insertion position is a boundary between elements, not necessarily the index of an existing element. An array of length $n$ has $n+1$ insertion boundaries: before index zero, between each adjacent pair, and after index `n - 1`. The final boundary is numbered `n`.

This function never evaluates `nums[l]` after the loop, so returning `l == n` is safe. It tells the caller to append the target conceptually. Confusing “valid element index” with “valid insertion index” is a common reason implementations incorrectly clamp the answer to `n - 1`.

**Do not mix interval conventions**

In this half-open version, `r` itself is excluded and a qualifying midpoint is retained with `r = mid`. In an inclusive version, the comparable update is `right = mid - 1`, with the possible midpoint remembered indirectly by the eventual crossed boundary. Either convention works when used consistently. Combining `r = len(nums)` with `right = mid - 1` can create gaps or invalid midpoint access.

## Complexity detail

Let $n$ be the number of elements.

- **Time complexity: $O(\log n)$.** Every iteration reduces the candidate interval to at most about half its previous length.
- **Auxiliary space: $O(1)$.** Only the two boundaries and midpoint are stored; the loop is iterative.

## Alternatives and edge cases

- **Python `bisect_left`:** It implements this same lower-bound operation directly.
- **Inclusive interval search:** Use `[left, right]` and return `left` after the pointers cross. Correct, but its updates differ from this half-open form.
- **Linear scan:** Easy but violates the requested logarithmic runtime.
- **Target equals an element:** The boundary converges to that element's index.
- **Target below all elements:** `r` repeatedly moves left and the result is zero.
- **Target above all elements:** `l` reaches `n`, representing insertion after the array.
- **Single element:** The one comparison returns either zero or one as appropriate.
- **Distinctness:** Not required by the lower-bound mechanics, but guaranteed by the problem.
- **No mutation:** The method returns an index and leaves `nums` unchanged.
