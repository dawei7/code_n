## General

Checking every pair `(i, j)` directly would require quadratic time. The merge-sort approach gains speed by dividing pairs into three categories:

1. both indices lie in the left half;
2. both indices lie in the right half;
3. `i` lies in the left half and `j` lies in the right half.

Recursive calls count the first two categories. The current call counts the cross-half pairs, then merges the halves so its parent can use the same reasoning.

`merge_sort(l, r)` returns the number of reverse pairs whose two indices were originally inside the inclusive range `[l, r]`. As a side effect, it sorts `nums[l : r + 1]` in non-decreasing order. That sorted-side-effect contract is essential: cross pairs can be counted with two pointers only because both child ranges are already sorted.

**Base interval.** If `l >= r`, the range contains zero or one value. It cannot contain two different indices, so its reverse-pair count is zero. Such a range is already sorted.

For a longer range, `mid = (l + r) >> 1` splits it into `[l, mid]` and `[mid + 1, r]`. The code first adds the recursive counts from both halves. At that moment, every pair entirely inside one half is counted exactly once, and both halves are sorted.

**Count cross pairs without changing index order.** Every original index in the left half is less than every original index in the right half. Sorting values within each half does not destroy this cross-half fact: any left-half value still represents an earlier original index than any right-half value. Therefore the cross counting only needs to test the inequality

$$
\texttt{nums}[i] > 2\texttt{nums}[j]
$$

between sorted values.

Pointers `i = l` and `j = mid + 1` begin at the smallest values of their halves. There are two cases.

If `nums[i] <= 2 * nums[j]`, the current left value does not form a reverse pair with `nums[j]`. It also cannot form one with any later right value, because later right values are at least as large and multiplying by positive two preserves order. Thus `nums[i]` has no remaining cross pair, and advancing `i` is safe.

If `nums[i] > 2 * nums[j]`, the current pair is valid. More importantly, every value from `i` through `mid` is at least `nums[i]` because the left half is sorted. All `mid - i + 1` of those values also satisfy the strict inequality with this same `nums[j]`. The code adds that whole block at once and advances `j` to test the next right value.

This pointer process counts every valid cross pair exactly once. A right value is advanced only after all qualifying remaining left values have been counted for it. A left value is advanced only after monotonicity proves it cannot qualify with any remaining right value.

Negative values do not invalidate the argument. Multiplication by `2` is order-preserving for all integers, and both halves are sorted numerically. For instance, a negative left value can still be greater than twice a more negative right value. The exact arithmetic comparison handles that naturally.

The use of `<=` in the failing branch also handles strictness correctly. If `nums[i] == 2 * nums[j]`, the pair is not valid because the contract requires `>`, so `i` must advance without adding a count.

**Merge after counting.** The counting pass does not reorder values. A second two-pointer pass merges the two sorted halves into `t`. When `nums[i] <= nums[j]`, the left value is appended; otherwise the right value is appended. Once one half is exhausted, the two `extend` calls append the remaining suffix of the other half.

Finally, `nums[l : r + 1] = t` replaces the original interval with its sorted version. The current count is returned to the parent. By induction, every call both returns the correct count for its range and leaves that range sorted.

For `[1, 3, 2, 3, 1]`, recursive calls count pairs confined to smaller ranges. At merge boundaries, the sorted halves allow the final `1` in a right half to be compared against entire qualifying suffixes such as values `3` and `3` on the left. Those block additions produce the two required pairs without examining every original pair individually.

The algorithm modifies `nums` by sorting it. The method's public result is only the count, so this does not affect the returned value, but callers that expect the input list to remain in original order would need to pass a copy.

## Complexity detail

Let $n$ be the array length. Merge sort has $O(\log n)$ recursion levels. At each level, the disjoint intervals together perform $O(n)$ cross-counting and merging work. Total time is $O(n\log n)$.

Temporary merge lists across calls at the same instant use $O(n)$ peak space, and the recursion stack uses $O(\log n)$. The dominant auxiliary-space bound is $O(n)$. Slice assignments and suffix slices also allocate linear total temporary data within a merge, remaining inside that bound.

Python integers do not overflow when evaluating `2 * nums[j]`. In a fixed-width language, the multiplication should be promoted to a wider integer type because input values may be 32-bit extremes.

## Alternatives and edge cases

- **Quadratic pair enumeration:** It directly checks the definition but takes $O(n^2)$ time, too slow for fifty thousand values.
- **Fenwick tree or segment tree:** Coordinate-compress values and count previously seen elements greater than twice the current value. This also achieves $O(n\log n)$ but requires careful threshold and compression handling.
- **Balanced search tree:** Maintain ordered counts while scanning, then query how many prior values exceed twice the current value. The asymptotic bound is similar where such a structure is available.
- **Equality at twice the right value:** It is not a reverse pair. The counting branch deliberately uses `<=` for rejection.
- **Negative numbers:** Comparisons must use the full expression rather than assumptions based on positivity. The sorted two-pointer proof still holds.
- **Integer overflow:** `2 * nums[j]` can exceed a signed 32-bit range. Python is safe; other languages need wider arithmetic.
- **One or zero elements:** The base case returns zero and performs no merge.
- **Input mutation:** The algorithm leaves `nums` sorted. Copy the array first if preserving its order is part of a surrounding caller's needs.
