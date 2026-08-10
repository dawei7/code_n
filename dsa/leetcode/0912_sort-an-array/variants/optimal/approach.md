## General

The exact solution implements randomized three-way quicksort. It selects a pivot value, partitions the current interval into values smaller than, equal to, and greater than the pivot, then recursively sorts only the smaller and greater regions.

Three-way partitioning is particularly important when many values are equal. An ordinary two-way quicksort may repeatedly include duplicates in recursive calls, while this method finishes the entire equal region in one partition.

For interval `nums[l:r+1]`, choose

```text
x = nums[randint(l, r)]
```

so the pivot is a randomly selected value from the interval.

**Partition pointers and regions.** The code initializes `i = l - 1`, `j = r + 1`, and `k = l`. During the loop:

- `l..i` contains values less than `x`;
- `i+1..k-1` contains values equal to `x`;
- `k..j-1` is unclassified;
- `j..r` contains values greater than `x`.

While `k < j`, inspect `nums[k]`.

**Value smaller than pivot.** Swap it into position `i + 1`. That position is immediately after the known smaller region. Increment both `i` and `k`. The value swapped back to `k` came from the equal region boundary and is already known equal, so advancing is safe.

**Value greater than pivot.** Decrement `j`, then swap `nums[k]` with `nums[j]`. The greater value is now in the right region. Do not increment `k` because the value swapped in from `j` was previously unclassified and still needs inspection.

**Value equal to pivot.** Increment `k`. It extends the middle equal region.

When `k == j`, no unclassified positions remain. The interval is partitioned as:

- less region `l..i`;
- equal region `i+1..j-1`;
- greater region `j..r`.

Only `quick_sort(l, i)` and `quick_sort(j, r)` are needed. The middle already contains identical values and is sorted relative to both outer regions.

**Why partitioning preserves all elements.** Every operation is a swap, so the interval remains a permutation of its original contents. The region invariant proves every final left value is below the pivot, every middle value equals it, and every right value is above it.

As a concrete partition trace, suppose pivot is 3 and the unresolved value is 1. Swapping it with position `i + 1` extends the smaller region, while the displaced value came from the already scanned equal boundary and needs no reclassification. If the unresolved value is 5, swapping it toward `j` fixes 5 on the right but may bring an arbitrary value back to `k`; keeping `k` stationary is what prevents that value from being skipped.
A zero- or one-element interval is already sorted. For a larger interval, partitioning creates three correctly ordered value regions. By induction, recursive calls sort the left and right regions. Concatenating sorted smaller values, equal pivots, and sorted greater values gives a fully ascending interval. The top call therefore sorts the whole array.

**Why randomization helps.** If pivots repeatedly land near the median, recursion is balanced and total work is $O(n\log n)$. Deterministic poor pivots can create one-sided recursion and quadratic time on already ordered or adversarial inputs. Random selection makes such consistently bad splits unlikely independently of input order.

The algorithm uses no built-in sorting function and mutates `nums` in place, satisfying the primary implementation constraint.

Termination follows because the pivot value occurs at least once in the interval and every loop iteration shrinks the unclassified region. After partitioning, the equal region is nonempty, so both recursive intervals are strictly smaller than the caller. Repeated recursion must eventually reach the base case.

## Complexity detail

Let $n$ be the array length.

- **Expected time complexity:** $O(n\log n)$ with randomized pivots.
- **Worst-case time complexity:** $O(n^2)$ if partitions are repeatedly maximally unbalanced.
- **Expected recursion space:** $O(\log n)$ for balanced partitions.
- **Worst-case recursion space:** $O(n)$ for a chain of unbalanced calls.

Partitioning itself uses $O(1)$ extra storage. The manifest's $O(1)$ space describes in-place partition data but does not include the recursive call stack. The exact Python implementation is therefore not literal constant-space overall.

## Alternatives and edge cases

- **Merge sort:** Guarantees $O(n\log n)$ time but needs $O(n)$ merge storage.
- **Heap sort:** Guarantees $O(n\log n)$ time with $O(1)$ auxiliary array storage and avoids recursion, though it is often less cache-friendly.
- **Counting sort:** Values lie in a bounded range, so frequency counting can run in $O(n+K)$ time with $O(K)$ space.
- **Two-way quicksort:** It can perform poorly on many duplicates; three-way partitioning removes the entire equal block.
- **Already sorted input:** Random pivot selection avoids the deterministic first-pivot worst-case pattern in expectation.
- **All values equal:** One partition places the whole interval in the middle, and no nontrivial recursion follows.
- **Duplicate values:** They remain grouped in the equal region and appear with correct multiplicity.
- **Negative values:** Ordinary comparisons partition them correctly.
- **One element:** The base case returns immediately.
- **Pivot by value:** The pivot element may move during swaps, but stored scalar `x` remains the comparison value.
- **Do not advance `k` after a greater swap:** The incoming element is unclassified and must be examined.
- **Input mutation:** The returned object is the now-sorted original list.
- **Random worst case:** Randomization improves expected behavior but does not create a deterministic worst-case guarantee.
