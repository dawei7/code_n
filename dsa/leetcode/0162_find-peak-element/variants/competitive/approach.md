## General

**Binary-search for an uphill destination**

The intended competitive algorithm keeps an inclusive interval
`[left, right]` containing at least one peak. It compares the midpoint only
with its right neighbor and preserves the side toward which a peak is
guaranteed.

This works even though the array is not sorted. A strict upward step cannot
continue beyond the right boundary without ending at a peak, because the
imaginary value after the array is negative infinity. A strict downward step
similarly guarantees a peak at the midpoint or somewhere to its left.

The adjacent-elements-unequal guarantee ensures every inspected step is either
strictly rising or strictly falling.

**Interpret both interval updates**

The intended midpoint is
`left + (right - left) // 2`. While `left < right`, this midpoint is less than
`right`, so `nums[mid + 1]` exists.

If `nums[mid] > nums[mid + 1]`, the source sets `right = mid`. The midpoint
must remain because it may already be a peak. If it is not greater than its
left neighbor, then moving left from it goes uphill and must eventually reach a
peak within the retained interval.

If `nums[mid] < nums[mid + 1]`, the source sets `left = mid + 1`. The midpoint
is certainly not a peak because a larger right neighbor exists. Beginning at
that neighbor and following rises as needed guarantees a peak on the retained
right side.

The method is searching for any valid peak, not for a specific numeric target.
Its invariant is existential: some peak remains inside the current interval.

**Why arbitrary hills and valleys do not break it**

The retained side need not be globally monotone. There may be another valley,
rise, or peak within it. The proof needs only the immediate slope plus the
finite boundary.

On a rising step, imagine walking right while each next value is larger. Either
a fall appears, making the value just before it a peak, or the walk reaches the
last element, which is greater than the imaginary outside neighbor. A falling
step has the symmetric leftward argument.

Thus discarding the opposite half cannot eliminate every possible peak, even
when that discarded half also contains valid peaks. Returning any one is
allowed.

**Trace the intended execution**

For `[1,2,3,1]`, the first midpoint is one. Since two is less than three, the
left boundary moves to two. The next midpoint is two; three is greater than
one, so the right boundary becomes two. The shared index two is returned.

For a strictly increasing array, every comparison follows the right side until
the last index remains. For a strictly decreasing array, every comparison
retains the midpoint on the left side until index zero remains.

For `[1,2,1,3,5,6,4]`, there are two peaks. The midpoint slope determines
which candidate region survives; either acceptable peak can be returned. The
method is not computing the global maximum.

**Termination and correctness**

Every intended update strictly shortens the interval. The rising case excludes
`mid`; the falling case retains `mid` but moves `right` down to it. Because the
interval always contains a peak, when `left == right` that single index must be
a peak.

Only cursor variables change. The input is read-only.

**Python 3 defect in the exact selected source**

The source calculates:

`mid = left + (right - left) / 2`

In Python 3, `/` returns a floating-point number even when both operands are
integers. Accessing `nums[mid]` then raises `TypeError`, because list indices
must be integers. Under Python 2 integer operands produced the intended floor
result.

Replacing `/ 2` with `// 2` is required for Python 3 compatibility and yields
the algorithm analyzed above. It does not change the interval rules or
asymptotic complexity.

## Complexity detail

With integer midpoint division, each iteration halves the candidate interval,
so intended time is $O(\log n)$. Only `left`, `right`, and `mid` are stored,
giving intended auxiliary space $O(1)$. These match the manifest.

The source exactly as stored under Python 3 fails at its first float-index
access and does not complete the search. Complexity claims describe the
intended one-character repair.

## Alternatives and edge cases

- **Optimal variant in this package:** Uses a right shift to compute an integer midpoint and otherwise applies the same slope decisions.
- **Linear first-drop scan:** Return the first value greater than its successor, or the last index; it costs $O(n)$ time.
- **Recursive binary search:** Preserves the same invariant but uses logarithmic call-stack space.
- **One element:** No midpoint access occurs and zero is returned.
- **Increasing order:** The intended method reaches the last index.
- **Decreasing order:** It reaches the first index.
- **Several peaks:** The retained side may choose any one, as the contract permits.
- **Equal adjacent values outside the contract:** The source has no equality branch, and a plateau would weaken the slope proof.
- **`mid + 1` bounds:** It is safe only because the loop condition is `left < right`.
- **Python division:** `/` is a runtime defect for indexing; `//` is mandatory.
