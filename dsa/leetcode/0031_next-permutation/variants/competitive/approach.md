## General

**Find the longest suffix that cannot be increased internally**

The selected Competitive method scans adjacent pairs from right to left. It searches for the first `k` such that `nums[k] < nums[k + 1]`. All positions after `k` form a non-increasing suffix.

That suffix is already its lexicographically greatest arrangement. If the prefix through `k` were kept unchanged, no rearrangement of later elements could produce a larger permutation. Therefore position `k` is the rightmost place where the next permutation can begin to differ.

**Understand Python's `for`–`else` control flow**

The source writes

```python
for i in reversed(range(len(nums)-1)):
    if nums[i] < nums[i+1]:
        k = i
        break
else:
    nums.reverse()
    return
```

The `else` belongs to the `for`, not to the `if`. It executes only if the loop finishes without `break`. That means no pivot exists and the entire array is non-increasing—the maximum permutation. `nums.reverse()` then mutates it into non-decreasing order, the minimum permutation, and the function returns.

For an empty pivot range such as a one-element array, no break occurs, so the same branch safely leaves the array unchanged after reversal.

**Choose the smallest suffix value strictly above the pivot**

When a pivot exists, the array must increase at index `k`, but by as little as possible. The source scans the suffix from the end toward `k + 1` and stops at the first value greater than `nums[k]`.

Because the suffix is non-increasing from left to right, scanning from its right end encounters smaller values first. The first one satisfying strict `>` is therefore the smallest value that can make the pivot position larger. Equal values are skipped because they would leave the first changed position unchanged.

The swap installs that successor at the pivot and moves the old pivot into the suffix.

**Reverse the suffix with a compact slice expression**

The source uses

```python
nums[k+1:] = nums[:k:-1]
```

With a negative step, `nums[:k:-1]` begins at the array's final element and stops just after index `k`. It is exactly the suffix `nums[k+1:]` in reverse order. Assigning it to the left-hand suffix replaces that section while preserving the identity of the original list object.

After the successor swap, the suffix remains non-increasing. Values before the chosen successor were at least as large as it, and values after it were no greater than the old pivot. Reversal therefore makes the suffix non-decreasing, which is its minimum lexicographic arrangement.

**Why this is the immediate next permutation**

Any greater permutation must differ at or before `k`, since the old suffix is maximal. Changing an earlier position would create a larger jump than changing `k`, so the next permutation preserves all indices before `k`. At `k`, the algorithm chooses the smallest available strictly greater value. Once that minimal increase is fixed, it arranges every later value as small as possible. No valid permutation can fall lexicographically between the original and the result.

If no `k` exists, no greater arrangement exists at all, and the `for`–`else` branch correctly wraps to the minimum.

**Trace `[1, 2, 3]`**

The reverse scan begins at index one and immediately sees `2 < 3`, so `k = 1`. The successor scan begins at index two; `3 > 2`, so `l = 2`. Swapping produces `[1,3,2]`. The suffix after `k` has one element, so reverse-slice assignment changes nothing. This is the next permutation.

For `[3,2,1]`, neither adjacent pair is an ascent. The loop ends without `break`, its `else` reverses the full list, and the result is `[1,2,3]`.

**Trace duplicates with `[1, 1, 5]`**

The pivot is the second `1` at index one because `1 < 5`. The rightmost greater value is `5`, so swapping gives `[1,5,1]`; the one-element suffix stays as is. The equal first `1` causes no ambiguity because lexicographic comparison is positional and the strict inequalities prevent a no-op successor.

**Why initialization values do not leak into valid paths**

The source initializes `k = -1` and `l = 0`. If no pivot is found, the `for`–`else` branch returns before either is used in the normal path. If a pivot is found, the non-increasing suffix must contain at least `nums[k + 1]`, which is greater than the pivot by definition, so the successor loop is guaranteed to assign `l` before the swap.

## Complexity detail

Let $n$ be the number of array elements.

- **Time complexity: $O(n)$.** The first reverse scan, the successor scan, and suffix reversal each touch at most a linear number of values. `nums.reverse()` is also linear in the no-pivot case.
- **Auxiliary space on the normal slice path: $O(n)$ worst case.** `nums[:k:-1]` constructs a temporary reversed list proportional to the suffix. In the no-pivot path, `nums.reverse()` itself is in-place with $O(1)$ auxiliary storage. Because worst-case space considers all valid paths, the exact method is $O(n)$ auxiliary, despite its source comment and manifest saying $O(1)$.

Replacing slice assignment with endpoint swaps would make the entire implementation genuinely constant-space.

## Alternatives and edge cases

- **Manual in-place reverse:** Swap `k + 1` with the last position, then move inward. This meets the constant-memory contract exactly.
- **Optimal variant's generator search:** It expresses the same pivot and successor selection with `next`; algorithmic behavior is equivalent.
- **Sort the suffix:** Produces the same minimum suffix but increases time to $O(n\log n)$.
- **No pivot:** The `for`–`else` syntax triggers full in-place reversal and immediate return.
- **One element:** The empty loop reaches `else`; reversal is harmless.
- **Duplicate successor candidates:** The rightmost scan chooses the smallest strictly larger value in the ordered suffix.
- **Zeros and repeated values:** Only ordering comparisons matter; no sentinel is used.
- **Suffix of length one:** Reverse-slice assignment writes an identical one-element list.
- **Output contract:** The method returns `None` implicitly and mutates the supplied list.
- **Slice notation:** With step `-1`, the stop index `k` is excluded, so the pivot itself is not accidentally reversed.
