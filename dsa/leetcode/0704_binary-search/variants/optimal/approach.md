## General

The exact solution implements a lower-bound binary search: it finds the first index whose value is greater than or equal to `target`, then checks whether that value is exactly the target.

This differs slightly from the template that returns immediately on equality, but it has the same logarithmic efficiency and a clean invariant.

**Initial search interval**

`l = 0` and `r = len(nums) - 1` describe an inclusive interval of real array indices.

The source guarantees that `nums` is nonempty, so both boundaries are valid. The loop runs while `l < r`, meaning more than one candidate remains.

**The lower-bound goal**

Conceptually, the desired index is the smallest position `p` such that

$$
\texttt{nums}[p]\ge\texttt{target}.
$$

If every value is smaller than the target, the algorithm converges to the final array index even though that position does not truly satisfy the conceptual condition. The final equality check safely rejects it. Within the nonempty-array contract, this avoids using a virtual index `n`.

**Choosing the midpoint**

`mid = (l + r) >> 1` computes the floor of the average.

When `l < r`, this midpoint satisfies `l <= mid < r`. That strict inequality on the right is important: setting `r = mid` will always shrink the interval.

**When `nums[mid] >= target`**

If the midpoint value is at least the target, every index strictly to the right of `mid` is unnecessary for finding the first adequate position.

However, `mid` itself may be the answer. The code keeps it by setting:

`r = mid`.

Using `mid - 1` would be unsafe because it could discard an exact target or the correct lower-bound index.

**When `nums[mid] < target`**

Sorted order implies that `nums[l]` through `nums[mid]` are all below the target. None can be a match or a lower-bound position.

The update:

`l = mid + 1`

discards that entire left portion.

Both branches eliminate at least one candidate, so the loop terminates.

**A useful interval invariant**

Throughout the loop:

- no discarded index left of `l` can contain the target because its value was proven smaller;
- if an exact target exists in the original array, its index remains in `[l, r]`.

Initially the second statement is obvious because the interval covers the array. In the first branch, an exact target cannot lie right of a midpoint already at least as large when values are strictly increasing; retaining `mid` and the left side preserves it. In the second branch, every discarded value is too small.

When `l == r`, any existing target must be at that sole remaining index.

**Why the final comparison is required**

Convergence identifies the position where the target would belong under this bounded lower-bound search, not proof that the target exists.

For `nums = [-1, 0, 3, 5]` and target `2`, the interval converges to index `2`, whose value is `3`. That is the first value above `2`, but `2` is absent. The expression

`l if nums[l] == target else -1`

distinguishes insertion position from exact membership.

If the target is greater than every value, convergence reaches the last index. Its value fails equality, also yielding `-1`.

**A successful trace**

Search `9` in `[-1, 0, 3, 5, 9, 12]`.

- Start `[0, 5]`, midpoint `2` has `3 < 9`, so move `l` to `3`.
- Interval `[3, 5]`, midpoint `4` has `9 >= 9`, so move `r` to `4`.
- Interval `[3, 4]`, midpoint `3` has `5 < 9`, so move `l` to `4`.
- Boundaries meet at index `4`, and equality succeeds.

**Why strict uniqueness simplifies the proof**

All array values are unique, so there is at most one exact target position. The lower-bound method would also work with duplicates and return the first occurrence, but no tie behavior is needed for this contract.

**Why the algorithm is correct**

Every update preserves any possible target index and removes only indices proven unable to match. Interval length strictly decreases until one index remains.

If a target exists, the invariant forces that remaining index to be its location, so equality returns it. If equality fails, the only remaining candidate is not the target and all discarded indices were ruled out by sorted comparisons, so `-1` is correct.

## Complexity detail

Let `n = len(nums)`.

Each iteration reduces the inclusive interval to roughly half its prior size. After `t` iterations its size is at most about `n/2^t`, so only `O(\log n)` iterations are needed to reach one index.

Time complexity is

$$
O(\log n).
$$

The method stores three integer indices and does not use recursion or allocate data proportional to the input. Auxiliary space is

$$
O(1).
$$

## Alternatives and edge cases

- **Immediate-return binary search:** Compare midpoint with the target using three branches and return on equality. It has the same bounds but a different loop invariant.

- **Half-open lower bound:** Search `[0, n)`, allowing `n` as the insertion position. This makes “target greater than all values” explicit but requires checking `l < n` before indexing.

- **Built-in `bisect_left`:** It performs lower-bound search, followed by the same equality check. Manual implementation exposes the reasoning expected by the exercise.

- **Single-element array:** The loop does not run; the final comparison returns zero or `-1`.

- **Target smaller than every value:** The search retains left candidates and converges to index zero; equality rejects when absent.

- **Target larger than every value:** The search moves right and converges to the final index; equality rejects.

- **Target at either endpoint:** The invariant keeps the endpoint until convergence and returns it.

- **Nonempty-array guarantee:** The final `nums[l]` access is safe only because at least one element exists.

- **Sorted-order requirement:** Discarding half the interval would be invalid for an unsorted array.

- **Unique values:** The returned match is unique; with duplicates this version returns the leftmost occurrence.

- **Keeping `mid` in the greater-or-equal branch:** `r = mid` is required because `mid` may be the exact target.

- **Using floor midpoint:** Together with `l < r`, it ensures both branches make progress and prevents an infinite loop.
