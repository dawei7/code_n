## General

**Use the original first value as a segment anchor**

A rotated distinct sorted array consists of two increasing segments: a high-valued segment beginning at index zero and, if rotation occurred, a low-valued segment ending at index `n - 1`. Every value in the first segment is at least `nums[0]`; every value in the second segment is less than `nums[0]`.

The selected implementation uses this fact to identify which segment contains `nums[mid]` and whether `target` belongs on the same searchable side. It does not find the rotation pivot separately.

Distinctness is essential. With duplicate values equal to `nums[0]`, the comparison could no longer identify a segment unambiguously.

**Maintain one inclusive candidate interval**

`left` and `right` delimit an interval that still contains the target if the target exists. The loop runs while `left < right`, so at least two candidates remain. The midpoint

```python
mid = (left + right) >> 1
```

uses a right shift to perform nonnegative integer floor division by two. Since indices are nonnegative, it is equivalent to `(left + right) // 2`.

Updates use either `right = mid` or `left = mid + 1`. The first retains `mid` when it might be the answer; the second discards it only when the branch proves the target must be strictly to its right. Every update shrinks the interval, guaranteeing termination.

**When `mid` lies in the first sorted segment**

The test

```python
if nums[0] <= nums[mid]:
```

means `mid` belongs to the high segment that starts at index zero. Values from `nums[0]` through `nums[mid]` are in ascending order. If

```python
nums[0] <= target <= nums[mid]
```

then the target's value belongs in that sorted range, so `right = mid` keeps the left portion including `mid`. Otherwise, the target cannot be in that high-segment prefix: it is either larger than `nums[mid]` or belongs to the low segment. The source sets `left = mid + 1`.

The upper comparison is inclusive because `nums[mid]` has not been checked separately; retaining `mid` is how equality survives.

**When `mid` lies in the second sorted segment**

If `nums[mid] < nums[0]`, `mid` is in the low segment. The range from `mid` through `n - 1` is increasing. The condition

```python
nums[mid] < target <= nums[n - 1]
```

identifies a target strictly to the right of `mid` in that segment, so the method uses `left = mid + 1`.

If the condition is false, the target might equal `nums[mid]`, might lie earlier in the low segment, or might belong to the high segment. All of those possibilities are at or left of `mid` within the current candidate interval, so `right = mid` is safe.

Notice the strict lower comparison. Equality with `nums[mid]` must retain `mid`, not discard it.

**Trace the search for zero**

For `[4,5,6,7,0,1,2]`, `nums[0] = 4`. Initially `mid = 3` with value seven, which is in the high segment. Target zero is not between four and seven, so `left` becomes four.

The remaining interval is indices four through six. `mid = 5` has value one in the low segment. The condition `1 < 0 <= 2` is false, so `right` becomes five. Then `mid = 4` has value zero; the strict test `0 < 0` is false, retaining index four as `right`. The pointers meet at four, and the final equality returns it.

**Why one final comparison is sufficient**

The loop invariant ensures any existing target remains inside `[left, right]`. Each iteration strictly reduces its size. When `left == right`, exactly one possible index remains. The return

```python
return left if nums[left] == target else -1
```

distinguishes presence from absence. The Reference guarantees a non-empty array, so `nums[left]` is safe. An empty array outside the contract would not be handled.

**Why the method never discards the target**

At each midpoint, one segment relative to the fixed anchors is known. Boundary comparisons determine whether the target's value can lie in the sorted portion being retained or discarded. Because values are distinct and both segments preserve original ascending order, membership in the corresponding value interval is exact. Thus every branch keeps the target when it exists. Interval convergence plus the final equality proves correctness.

## Complexity detail

Let $n$ be the array length.

- **Time complexity: $O(\log n)$.** Each iteration reduces the inclusive candidate interval to at most roughly half its former size.
- **Auxiliary space: $O(1)$.** The method stores only lengths and indices and uses no recursion or auxiliary collection.

## Alternatives and edge cases

- **Find pivot, then ordinary binary search:** Two logarithmic searches are easier to separate conceptually but have the same asymptotic bounds.
- **Determine the sorted half using `nums[left]`:** The editorial's common formulation updates bounds with `mid - 1` and `mid + 1`; it is equivalent under distinctness.
- **Linear scan:** Simple but violates the required $O(\log n)$ runtime.
- **No rotation:** Every midpoint belongs to the first segment, reducing behavior to ordinary binary search.
- **Single element:** The loop is skipped and the final comparison decides the result.
- **Target at `mid`:** Inclusive/strict inequalities retain it until convergence.
- **Target absent:** Bounds still converge, and the final equality returns `-1`.
- **Distinct values:** Required for unambiguous segment classification; duplicates need additional handling.
- **Non-empty guarantee:** The exact final index access relies on it.
