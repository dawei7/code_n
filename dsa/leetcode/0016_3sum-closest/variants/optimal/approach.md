## General

**Sort so changing one pointer changes the sum predictably**

Fix one value `v = nums[i]`. The remaining task is to choose two distinct later indices whose pair sum comes as close as possible to `target - v`. After sorting, pointer `j` starts at `i + 1` and `k` at the final index.

The current triplet sum is

$$
t = v + \texttt{nums[j]} + \texttt{nums[k]}.
$$

Increasing `j` keeps or raises `t`; decreasing `k` keeps or lowers it. This monotonic behavior lets the search discard many pairs without measuring each one.

Sorting mutates `nums`, but only values and the returned sum matter. Original indices are not part of the output, and `i < j < k` still guarantees three distinct positions.

**Initialize the best sum with infinity**

`ans = inf` means no real triplet has been considered. The comparison

```python
abs(t - target) < abs(ans - target)
```

must succeed for the first candidate because its finite distance is less than infinity. From then on, `ans` is always the closest evaluated triplet sum.

The contract guarantees at least three elements, so at least one inner-loop iteration occurs and infinity cannot be returned.

**An exact match is immediately optimal**

If `t == target`, the absolute difference is zero. No other sum can be closer than zero, so the method returns `t` without continuing. The unique-solution guarantee is not even needed for this early return; exact equality is an absolute lower bound on distance.

**Update only on a strict improvement**

When no exact match exists, compare distances:

```python
if abs(t - target) < abs(ans - target):
    ans = t
```

The strict inequality leaves `ans` unchanged on a tie. The Reference guarantees a unique closest answer, so a final unresolved tie cannot occur for legal input. Strict comparison also prevents unnecessary replacement.

**Why the pointer direction is safe for closeness**

Suppose `t < target`. For the same `i` and `j`, replacing `k` with any smaller index chooses a value no greater than `nums[k]`. That new sum is at most `t`, hence even farther below the target. None of those skipped pairs can improve on the current `t`, which has already been compared with `ans`. The only useful direction is `j += 1`, which may raise the sum toward the target.

If `t > target`, keeping `i` and `k` while increasing `j` can only keep or raise the excessive sum. Those pairs cannot be closer than the current one. Decreasing `k` is the only move that may lower the sum toward the target.

This is stronger than merely saying “move toward the target.” It proves that every pair skipped by a pointer move lies on the wrong side and is no closer than a candidate already evaluated.

**Trace the example**

Sort `[-1,2,1,-4]` into `[-4,-1,1,2]`, with `target = 1`.

- Pivot `-4`, pointers `-1` and `2`: sum `-3`, distance `4`; save `-3` and move the left pointer.
- Same pivot with `1` and `2`: sum `-1`, distance `2`; save `-1`.
- Pivot `-1`, pointers `1` and `2`: sum `2`, distance `1`; save `2` and move the right pointer, ending that search.

No later candidate is closer, so the result is `2`.

**Why every possible optimum survives elimination**

For each pivot, pointers begin at the widest remaining pair. A move discards only pairs whose sums are provably at least as far from the target on the same side as the current evaluated sum. Therefore a strictly better pair cannot be discarded unseen. Pointer crossing means every undominated pair for that pivot has been evaluated.

The outer loop uses every array value as a pivot; iterations near the end simply have no pair and do nothing. Consequently the unique globally closest triplet is evaluated or an exact match returns earlier, and `ans` holds its sum.

## Complexity detail

Let $n$ be the array length.

- **Time complexity: $O(n^2)$.** Sorting costs $O(n\log n)$. For each pivot, `j` and `k` move inward at most $O(n)$ combined steps. The nested two-pointer work dominates sorting.
- **Space complexity: $O(n)$ under conservative accounting for Python sorting.** The pointer scan uses $O(1)$ scalar state. The sorting implementation may use input-dependent temporary storage; the manifest records $O(n)$. No output collection is built because only one sum is returned.

## Alternatives and edge cases

- **Binary search for the third value:** Fix two indices and binary-search the remaining suffix near the desired complement. It costs $O(n^2\log n)$, slower than two pointers.
- **Brute-force triples:** Examines $O(n^3)$ combinations and ignores sorted monotonic elimination.
- **Skip duplicate pivots:** This can reduce repeated work, but is not required for correctness or the $O(n^2)$ bound; the exact source processes them.
- **Exact target exists:** Return immediately with distance zero.
- **All values equal:** Repeated searches compute the same sum; the first candidate initializes `ans` correctly.
- **Target outside all attainable sums:** Pointer movement reaches the extreme attainable triplet closest to that target.
- **Negative target and values:** Only numerical order and differences matter; sign requires no special branch.
- **Distinct indices:** `j = i + 1` and `j < k` maintain `i < j < k`.
- **Input mutation:** In-place sorting changes the caller's list order.
