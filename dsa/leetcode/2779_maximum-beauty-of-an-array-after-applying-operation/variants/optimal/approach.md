## General

**Turn each number into an interval of reachable values**

One array value `x` can be replaced by any integer in `[x - k, x + k]`. A collection of elements can all become equal exactly when their reachable intervals share at least one common integer. The maximum beauty is therefore the maximum number of these intervals covering the same point.

The exact solution computes that maximum overlap with a difference array. It does not sort `nums`, despite the Optimal manifest describing a sorted sliding window.

**Shift every interval to avoid negative coordinates**

The direct reachable interval for `x` begins at `x - k`, which can be negative. Instead of allocating negative array indices, add `k` to every possible target coordinate. The interval becomes

$$
[x,\ x + 2k].
$$

Shifting every interval by the same amount does not change how many overlap at any point. If original intervals share target `t`, shifted intervals share `t + k`, and the converse is also true.

This explains the seemingly unusual updates at `x` and `x + 2k + 1`. They describe the shifted interval, not an asymmetric operation range.

**Mark an inclusive interval with two events**

Array `d` is a difference array. For each input value `x`:

- `d[x] += 1` starts one interval at coordinate `x`;
- `d[x + 2 * k + 1] -= 1` ends its contribution immediately after the inclusive right endpoint `x + 2k`.

When prefix sums are later computed, that interval contributes one at every coordinate from `x` through `x + 2k` and zero elsewhere.

The extra `+1` on the closing event is essential. Placing the decrement at `x + 2k` would make the right endpoint exclusive and lose valid overlaps where two ranges only meet at a boundary.

**Choose an array long enough for every closing event**

`m = max(nums) + k * 2 + 2`.

The largest possible closing index is `max(nums) + 2k + 1`. A Python list of length `m` has that as its final valid index, because `m - 1` equals the same expression. Every update is therefore in bounds.

The constraints keep `max(nums)` and `k` at most `10^5`, so this coordinate array has at most about 300,002 entries and is practical.

**Recover overlap counts through prefix accumulation**

`accumulate(d)` yields running sums. At a coordinate `q`, its value is:

the number of intervals whose start event has occurred minus the number whose end-after event has occurred.

That is exactly the number of shifted reachable intervals containing `q`. Each covering interval represents one input element that can be changed to the corresponding original target `q - k`.

Taking `max(accumulate(d))` selects the target reachable by the greatest number of elements. Those elements, in their original index order, form an equal-valued subsequence of that length after modification. Order imposes no further restriction because any chosen set of indices is a subsequence when listed in increasing order.

**A walkthrough**

For `nums = [4, 6, 1, 2]` and `k = 2`, original intervals are:

- 4 reaches `[2, 6]`;
- 6 reaches `[4, 8]`;
- 1 reaches `[-1, 3]`;
- 2 reaches `[0, 4]`.

After shifting by two, they are `[4, 8]`, `[6, 10]`, `[1, 5]`, and `[2, 6]`. Coordinate six is covered by the intervals for 4, 6, and 2, a maximum overlap of three. It corresponds to original target four. The prefix sum reaches three there, so the method returns three.

**Why pairwise overlap is not the argument**

For arbitrary intervals, pairwise overlap does not always imply one common point. Here the algorithm avoids that trap by directly counting coverage at each coordinate. A prefix value of `b` certifies one concrete target contained in all `b` corresponding intervals.

Equivalently, because these are intervals on a line, the maximum beauty can also be characterized by a sorted window whose largest and smallest original values differ by at most `2k`. The line sweep computes the same optimum through coordinates rather than ordering.

**Why the returned overlap is achievable and maximal**

At any coordinate with prefix count `c`, exactly `c` elements have reachable ranges containing the associated target, so all `c` can be changed to that target. Thus every candidate count is achievable.

Conversely, if a solution makes `c` elements equal to some target `t`, all their original reachable intervals contain `t`. After shifting, all cover `t + k`, so the prefix count there is at least `c`. The maximum prefix count cannot be smaller than any achievable beauty. Both directions prove equality.

**The manifest describes a different implementation**

The branch manifest says the source sorts values and uses a sliding window with `O(n log n)` time and `O(n)` space. The exact solution instead allocates a coordinate array and performs a line sweep. Its cost depends on the largest coordinate and `k`, not only on `n`. The explanation and bounds below follow the actual code.

## Complexity detail

Let

$$
M = \max(\text{nums}) + 2k + 2.
$$

Finding `max(nums)` and writing two events for each of `n` values costs `O(n)` time. `accumulate(d)` scans all `M` coordinates, and `max` consumes that stream in the same pass. Total time is `O(n + M)`.

The difference list contains `M` integers, so auxiliary space is `O(M)`. `accumulate` is lazy and does not create another length-`M` list. The manifest's `O(n log n)` time and `O(n)` space belong to a different sorting solution and are not the exact implementation's bounds.

## Alternatives and edge cases

- **Sorted sliding window:** Sort values and maintain the longest interval with endpoint difference at most `2k`. It costs `O(n log n)` and avoids dependence on coordinate magnitude.
- **Binary search per left endpoint:** Sorting plus upper-bound queries also costs `O(n log n)` but repeats searches that two pointers avoid.
- **Use original intervals directly:** Negative starts require an offset or map. Shifting all intervals by `k` produces nonnegative indices cleanly.
- **Forget the closing `+1`:** That would make intervals right-exclusive and miss boundary overlaps.
- **`k = 0`:** Each shifted interval is a single coordinate; prefix counts become ordinary value frequencies.
- **All values equal:** Their intervals all overlap, so the maximum prefix count is `n`.
- **Intervals meet only at one endpoint:** Inclusive event placement counts that shared target correctly.
- **One-element input:** Its interval produces maximum overlap one.
- **Large gaps:** Disjoint shifted ranges never contribute simultaneously, so they cannot inflate the result.
- **Large coordinate domain:** The exact array approach is practical only because constraints bound values and `k`; sorting is preferable for unbounded sparse coordinates.
- **Input mutation:** The line sweep reads `nums` without sorting or modifying it.
- **Subsequence order:** Once equalizable indices are selected, their natural increasing index order forms the required subsequence automatically.
