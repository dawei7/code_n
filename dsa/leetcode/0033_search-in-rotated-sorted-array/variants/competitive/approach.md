## General

**Intended algorithm: identify one sorted half at every midpoint**

A rotated distinct sorted array has at most one rotation break. When an active interval is divided at `mid`, at least one side is normally sorted. The intended Competitive logic tests whether the left half is sorted and then uses its value boundaries to decide which half could contain `target`.

`left` and `right` are inclusive. The intended loop checks the midpoint for equality first, then discards one half with `right = mid - 1` or `left = mid + 1`. If implemented with an integer midpoint, this is a standard $O(\log n)$ rotated binary search.

**A material Python 3 defect occurs before that logic can run**

The exact selected source calculates

```python
mid = left + (right - left) / 2
```

In Python 3, `/` always returns a `float`, even when the mathematical result is an integer. Lists require integer or slice indices, so the next expression `nums[mid]` raises `TypeError` on every non-empty legal input before a result can be produced.

The line needs `// 2` (or `>> 1`) to be executable Python 3. The remainder of this explanation describes the intended branch semantics, but the protected source as written does not satisfy the runtime contract. This is not a complexity nuance; it is an operational correctness defect.

**Intended equality check**

If `nums[mid] == target`, returning `mid` is correct because values are unique. Checking equality before classifying halves also makes later interval tests use strict bounds around the midpoint.

Again, this statement assumes `mid` has first been made an integer.

**Recognize when the left half is sorted**

The condition

```python
nums[mid] >= nums[left]
```

means the interval from `left` through `mid` has not crossed the rotation boundary and is sorted. With distinct values, the target lies strictly before `mid` in that half exactly when

```python
nums[left] <= target < nums[mid]
```

If both parts are true, the compound condition moves `right` to `mid - 1`.

**Decode the rotated-left-half clause**

If `nums[mid] < nums[left]`, the rotation boundary lies in the left portion and the right half from `mid` through `right` is sorted. The target belongs strictly after `mid` in that sorted half when

```python
nums[mid] < target <= nums[right]
```

The source places the negation of this condition inside its move-left expression:

```python
nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])
```

When the target is not in the sorted right range, the algorithm must search left, so `right = mid - 1`. Otherwise it falls through to `left = mid + 1`.

The whole large `elif` is therefore two separate reasons to choose the left side: the target is inside a sorted left half, or the target is outside a sorted right half.

**Trace the intended search**

For `[4,5,6,7,0,1,2]` and target zero, an integer midpoint three has value seven. The left half is sorted, but zero is not in `[4,7)`, so the intended algorithm moves `left` to four. Midpoint five then has value one; the left part of the active interval is sorted as `[0,1]`, and zero lies in `[0,1)`, so `right` becomes four. Midpoint four equals the target and is returned.

For target three, the same half-discarding decisions eventually empty the interval and return `-1`.

**Why the intended branch is correct**

If the left half is sorted, its boundary values exactly characterize whether the target can occur there; otherwise it can be discarded. If the left half is rotated, the right half is sorted and its boundaries provide the symmetric decision. Distinctness prevents ambiguous equal plateaus. Every successful iteration removes at least half of the remaining candidates while retaining any existing target.

The exact source cannot realize this proof until its midpoint operator is corrected.

## Complexity detail

For the intended integer-midpoint algorithm:

- **Time complexity: $O(\log n)$.** Each iteration discards one inclusive half.
- **Auxiliary space: $O(1)$.** Only three indices and comparisons are used.

For the exact Python 3 source, execution fails in the first iteration on a non-empty input, so asymptotic successful-search claims do not describe its actual behavior. The manifest records the intended corrected algorithm.

## Alternatives and edge cases

- **Correct `/` to `//`:** This minimal change makes `mid` an integer and activates the intended algorithm.
- **Pivot plus binary search:** Find the smallest element first, then search the appropriate sorted segment; still $O(\log n)$.
- **Optimal anchored variant:** Uses `nums[0]` and `nums[-1]` to classify segments and has executable integer midpoint arithmetic.
- **Single element:** The exact source still creates `mid = 0.0` and fails at indexing; the corrected source would compare index zero.
- **Target at midpoint:** Intended equality returns before half classification.
- **No rotation:** Intended left-half checks reduce to ordinary binary search decisions.
- **Distinctness:** Required by the branch logic; duplicates can make both-half classification ambiguous.
- **Absent target:** The corrected interval eventually becomes empty and returns `-1`.
- **Operator precedence:** `and` binds more tightly than `or`, so the two move-left cases group as intended.
- **Runtime fidelity:** The unused conceptual correctness of the branches must not be mistaken for correctness of the exact `/`-based Python 3 file.
