## General

Sort a copy of `nums`, then place `left` at the smallest value and `right` at the largest. Sorting does not lose any required information: the task asks only for the number of index pairs, and every original position remains one element in the sorted copy even when values are equal.

When `values[left] + values[right] < target`, every value from position `left + 1` through `right` also forms a valid pair with `values[left]`. Each of those values is at most `values[right]`, so there are exactly `right - left` valid pairs to add at once. After counting them, advance `left`; no pair using that position remains uncounted.

Otherwise, the current sum is greater than or equal to `target`. Pairing `values[right]` with any position from `left` through `right - 1` cannot help: all those values are at least `values[left]`. Therefore no still-unexamined valid pair ends at `right`, and decrementing `right` safely discards it.

These two cases preserve all uncounted candidates inside the active pointer interval while either counting every pair involving its left endpoint or proving that none can involve its right endpoint. The interval shrinks on every iteration. Once the pointers meet, every possible pair has been counted exactly once.

**Why equality moves the right pointer**

The condition is strictly less than `target`. A sum equal to `target` belongs to the failing case, so `right` moves left; counting that range would incorrectly include equality.

## Complexity detail

Let $n$ be the length of `nums`. Sorting the copied values takes $O(n \log n)$ time, and the two pointers make at most $n - 1$ moves, so the total time is $O(n \log n)$. The sorted copy uses $O(n)$ space.

The source contract fixes $n \le 50$, which is too small for a stable measured scaling distinction from pair enumeration. The package therefore uses a bounded-domain certificate backed by exhaustive small-array comparisons and legal boundary cases.

## Alternatives and edge cases

- **Enumerate every index pair:** Two nested loops are simple and correct in $O(n^2)$ time. The small source limit allows this approach to pass, but it does not exploit the ordered range-counting observation.
- **Binary search per left endpoint:** After sorting, search for the first partner that reaches `target` for every left position. This also takes $O(n \log n)$ time but repeats searches that the two pointers share across positions.
- **Strict inequality:** A sum equal to `target` is not valid and must move `right`, not increase the count.
- **Duplicate values:** Equal values at different positions remain separate elements and create separate index pairs.
- **Singleton input:** With fewer than two elements, the pointer loop never runs and the result is zero.
- **Negative values and target:** Sorting and the comparison work unchanged; no positivity assumption is needed.
- **Input preservation:** The app-local reference sorts a copy so a run does not reorder the caller's list.
