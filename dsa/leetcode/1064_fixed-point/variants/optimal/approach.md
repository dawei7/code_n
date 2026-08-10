## General

**Search for where array value meets its index**

A fixed point is an index `i` satisfying `arr[i] == i`. A linear scan would find the smallest one, but the array is strictly increasing because it is sorted and contains distinct integers. That structure makes a logarithmic search possible.

Define the conceptual difference:

```text
g(i) = arr[i] - i
```

A fixed point is exactly an index where `g(i)` is zero.

Because the array values are distinct integers in ascending order:

```text
arr[i + 1] >= arr[i] + 1
```

Therefore:

```text
g(i + 1) = arr[i + 1] - (i + 1) >= arr[i] - i = g(i)
```

So `g` is non-decreasing. It may stay equal across adjacent indices, but it can never move downward. This monotonicity means all negative values come before all non-negative values.

The algorithm finds the first index where `arr[i] >= i`, which is the first index where `g(i) >= 0`. It then checks whether that first non-negative value is exactly zero.

**Use a lower-bound binary search**

The initial boundaries are:

```python
left, right = 0, len(arr) - 1
```

The search interval is closed: both `left` and `right` are possible answers to the lower-bound question. The array is nonempty, so these indices are always valid.

The loop continues until the interval contains one index:

```python
while left < right:
```

Unlike a search that returns immediately when it sees equality, this form deliberately keeps looking left. The problem requests the smallest fixed point, and there may be more than one.

**Choose a midpoint**

The midpoint is:

```python
mid = (left + right) >> 1
```

For non-negative indices, shifting right by one bit is integer division by two. Thus `mid` is the floor of the average of `left` and `right`.

When `left < right`, this midpoint lies inside the interval and is strictly less than `right`. Both update branches therefore make progress.

**Keep the left half when the predicate is true**

The main comparison is:

```python
if arr[mid] >= mid:
    right = mid
```

This says `g(mid) >= 0`. Index `mid` is a valid candidate for the first non-negative position, but an earlier candidate may exist. The update keeps `mid` and discards only positions to its right.

This branch includes equality. If `arr[mid] == mid`, the code does not return immediately because there could be a smaller fixed point. Setting `right = mid` preserves the found fixed point while continuing to search its left side.

If `arr[mid] > mid`, monotonicity says every later difference is also positive or at least non-negative. A zero, if one exists before the first positive region, must be at `mid` or to the left. The same boundary update is correct.

**Discard the left half when the predicate is false**

The other branch is:

```python
else:
    left = mid + 1
```

Here `arr[mid] < mid`, so `g(mid) < 0`. Since `g` is non-decreasing, every index at or before `mid` has difference at most `g(mid)` and is also negative. None can be a fixed point or the first non-negative position.

The algorithm safely discards that complete prefix and starts the remaining interval at `mid + 1`.

**The search invariant**

At the start of every iteration, the interval from `left` through `right` contains the earliest index whose difference is non-negative, if such an index exists. If no non-negative difference exists, the interval is being driven toward the final array index, which will fail the equality check.

The true branch keeps a satisfying midpoint and removes only later positions. The false branch proves the midpoint and everything earlier are negative. Both updates preserve the invariant and shrink the interval.

When `left == right`, that index is the lower-bound candidate: the first position where `arr[i] >= i` when one exists.

**Verify equality after finding the boundary**

The return statement is:

```python
return left if arr[left] == left else -1
```

Binary search found the first non-negative difference, not automatically a zero. The values can jump from negative to positive. For example, `g` could go from minus two to three without ever equaling zero.

If `arr[left] == left`, `left` is a fixed point. Because it is the first non-negative position, every earlier index has a negative difference and cannot be fixed. Thus `left` is the smallest valid answer.

If `arr[left] != left`, the candidate's difference is positive or, in the all-negative case, still negative at the last position. A non-decreasing sequence cannot contain a zero after a positive first candidate, and the all-negative case contains no zero anywhere. Returning minus one is correct.

**A short trace**

For `arr = [-10, -5, 0, 3, 7]`, the first midpoint is index two. Since zero is less than two, indices zero through two are discarded. The remaining search finds index three, where value and index are equal. The final check returns three.

For `arr = [0, 1, 4, 7]`, both indices zero and one are fixed. A search that returned on an arbitrary equality might return one. The lower-bound updates continue left and finish at zero, correctly choosing the smallest.

For `arr = [-10, -5, 3, 4, 7, 9]`, the difference jumps from negative to positive. The lower bound is index two, but `arr[2]` is three rather than two, so the function returns minus one.

## Complexity detail

Let `N` be the length of `arr`.

Every loop iteration reduces the search interval to at most about half its previous size. It takes `O(log N)` iterations to reduce `N` candidates to one. Each iteration performs constant-time indexing, comparison, and arithmetic, so total time is `O(log N)`.

The solution stores only two boundaries and one midpoint. It allocates no auxiliary collection and uses no recursion, so auxiliary space is `O(1)`.

These exact bounds match the manifest.

## Alternatives and edge cases

- **Linear scan:** Visit indices from left to right and return the first equality. This is easy and uses `O(1)` space, but takes `O(N)` time and misses the logarithmic follow-up.
- **Return immediately on equality:** Ordinary binary search may find a fixed point but not necessarily the smallest one. Equality must keep the left half under consideration.
- **Search for zero in a conceptual difference array:** One could describe binary search over `arr[i] - i` directly. Computing the difference on demand avoids allocating that array.
- **One element equal to zero:** The loop is skipped and the final equality check returns index zero.
- **One element not equal to zero:** The loop is skipped and the function returns minus one.
- **Several fixed points:** The lower-bound predicate leads to the first non-negative difference, which is the smallest fixed point.
- **All values below their indices:** The search moves right and the final equality check rejects the last index.
- **All values above their indices:** The search moves left and the final equality check rejects index zero unless its value is zero.
- **Negative values:** They are ordinary values in the comparison and naturally create negative differences at early indices.
- **Large positive jump:** A jump can skip zero, which is why finding `arr[i] >= i` must be followed by exact equality verification.
- **Distinctness is essential:** If duplicates were allowed, `arr[i + 1]` might equal `arr[i]`, making `arr[i] - i` decrease. The binary-search proof would no longer hold.
- **Sorted order is essential:** Without ascending values, the predicate is not monotonic and only a general scan is safe.
- **Input preservation:** The array is read only and remains unchanged.
