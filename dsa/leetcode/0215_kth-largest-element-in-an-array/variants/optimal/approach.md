## General

**Convert the requested rank into one array index**

The problem gives `k` as a one-based rank counted from the largest value. The
partition routine in the exact source arranges values in ascending relation to
a pivot and reasons with ordinary zero-based indices. For an array of length
$n$, the $k$th largest value occupies ascending sorted index $n-k$.

For example, in an array of six elements, the second largest is at ascending
index `6 - 2 = 4`: four elements occupy indices 0 through 3 before it. The
source therefore executes `k = n - k` before selection. From that point onward,
the local variable `k` means a fixed zero-based target index, not the original
one-based rank. Duplicates remain separate positions; no distinct-value set is
created, exactly as the contract requires.

**Selection needs only the side containing the target**

Sorting establishes the order of every element, but the method needs only the
value at one position. Quickselect partitions the active interval so that a
boundary separates values on the low side from values on the high side. Once
the target index is known to lie on one side, the other side can be discarded
without being internally sorted.

The nested function is named `quick_sort`, but it is a selection routine: after
each partition it recurses into only one subinterval. That one-branch behavior
is the difference between Quickselect and Quicksort.

The active range uses inclusive boundaries `l` and `r`. If `l == r`, only one
candidate remains, so `nums[l]` is returned. Otherwise the pivot value `x` is
read from the middle position `nums[(l + r) >> 1]`. The bit shift by one is
integer division by two for these nonnegative indices.

**Hoare partition uses two inward scans**

The exact source applies Hoare's two-pointer partition scheme. Pointer `i`
starts one position before the interval at `l - 1`, and `j` starts one position
after it at `r + 1`. Each pass does the following:

- Increment `i` at least once, then continue moving it right while values are
  strictly less than the pivot. It stops at a value `nums[i] >= x`, which is
  potentially misplaced on the low side.
- Decrement `j` at least once, then continue moving it left while values are
  strictly greater than the pivot. It stops at a value `nums[j] <= x`, which
  is potentially misplaced on the high side.
- If `i < j`, swap those two stopped values. The smaller-or-equal value moves
  left, and the greater-or-equal value moves right.
- When `i >= j`, the scans have crossed, and `j` is returned implicitly as the
  partition boundary used by the following recursion decision.

The pivot is a value from inside the active range. Therefore the left scan must
encounter at least that pivot value, which is not less than itself, and the
right scan must encounter one, which is not greater than itself. These built-in
stopping points keep both scans inside the interval without explicit boundary
checks in the inner loops.

After crossing, every position from `l` through `j` contains a value no greater
than every value that has been forced to the right partition in the needed
partition sense, and every position from `j + 1` through `r` lies on the high
side. Neither side is fully sorted. Equal-to-pivot values may appear on both
sides, which is permitted and important for making progress when duplicates
are common.

**Choose the one interval that can contain the target rank**

The target `k` remains an index in the original array throughout recursion;
the routine never slices the array or renumbers positions. If `j < k`, the
target position lies strictly to the right of the boundary, so the method calls
`quick_sort(j + 1, r)`. Otherwise `k <= j`, so it calls
`quick_sort(l, j)`.

All values in the discarded left partition are on the lower side when the
target is right, so none can occupy target index `k`. Symmetrically, when the
target lies left, values in the discarded right partition cannot change the
value belonging at that lower index. Repeating this argument preserves the
answer while shrinking the active interval. Eventually `l == r`, and the one
remaining value is exactly the value that would occupy index `k` in fully
sorted order.

**Trace the rank conversion and first partition idea**

For `nums = [3, 2, 1, 5, 6, 4]` and original `k = 2`, the target becomes
`6 - 2 = 4`. The desired value is the one that would appear at ascending index
4. Partitioning the full range chooses its middle-position value as pivot and
moves low values toward the left and high values toward the right. If the
crossing boundary is below index 4, only the right interval can contain that
rank. A later partition may discard another low interval. The process ends
when index 4 is isolated, returning 5 without requiring indices 0 through 3 or
5 to be mutually sorted.

The physical sequence of swaps depends on the current array arrangement, but
the decision needs only the boundary relative to target index 4. This is why
selection can do less work than complete sorting.

**Duplicates are rankings, not special values**

Suppose several entries equal the pivot. The left scan stops on an equal value,
and the right scan also stops on an equal value. They may be swapped even though
their values are the same, but both pointers have already advanced inward.
Thus the partition continues rather than becoming stuck.

More importantly, equal values occupy multiple ranks. In
`[3,2,3,1,2,4,5,5,6]`, both copies of 5 count, so they are the second and third
largest positions. Converting the requested fourth-largest rank to one target
index and partitioning the full multiset naturally returns 4. No deduplication
step should be added.

**The exact source differs materially from its manifest summary**

The manifest describes “randomized median-of-three pivots” and “three-way
partitioning.” The exact solution does neither. It deterministically chooses
the middle-position value and uses two-way Hoare partitioning. This affects the
performance guarantee.

For reasonably balanced partitions, the total examined sizes form a decreasing
geometric series and expected or typical time is $O(n)$. A deterministic middle
position can nevertheless be forced to choose repeatedly poor pivot values on
adversarial arrangements, leaving an interval only one element smaller at each
level. The worst-case time is then $O(n^2)$.

The partition itself uses constant extra variables and mutates `nums` in place,
but the implementation is recursive. Its call stack is typically
$O(\log n)$ for balanced partitions and can become $O(n)$ in the worst case,
so the exact source does not have unconditional $O(1)$ auxiliary space as the
manifest claims. An iterative loop would remove call-stack growth but would
not fix deterministic pivot worst-case time. The approach documentation must
describe these source-level facts rather than silently attributing a different
algorithm's guarantees to this code.

## Complexity detail

Let $n$ be the number of elements. One partition of an active interval of size
$m$ takes $O(m)$ time because `i` and `j` move only inward. With balanced or
average partitions, the work is
$n + n/2 + n/4 + \cdots = O(n)$. With repeatedly extreme partitions, it is
$n + (n-1) + (n-2) + \cdots = O(n^2)$. Thus the exact deterministic source has
average or typical $O(n)$ time and worst-case $O(n^2)$ time.

Swapping occurs inside `nums`, and each partition uses $O(1)$ local storage.
Recursive depth is $O(\log n)$ for balanced partitions and $O(n)$ in the worst
case, so auxiliary stack space has those corresponding bounds. No copied
subarrays are allocated. The input array is permanently reordered.

## Alternatives and edge cases

- **Randomized in-place Quickselect:** Choose a uniformly random pivot before the same one-sided recursion. It retains $O(n^2)$ theoretical worst-case time but gives expected $O(n)$ time independent of a fixed adversarial input pattern.
- **Three-way partitioning:** Separate values less than, equal to, and greater than the pivot. If the target falls in the equal block, return immediately; this is especially effective with many duplicates and matches part of the manifest description, but it is not the exact source.
- **Median of medians:** A carefully selected deterministic pivot guarantees $O(n)$ worst-case selection, but its implementation and constant factors are substantially more involved.
- **Min-heap of size `k`:** Keep the largest `k` values seen, with the heap root as the answer. It offers deterministic $O(n\log k)$ time and $O(k)$ space without mutating the input.
- **Counting frequencies:** The narrow guaranteed value range from $-10^4$ through $10^4$ allows $O(n+R)$ time and $O(R)$ space for range width $R$. It is deterministic and attractive here, though it depends on the numeric-domain constraint.
- **Full sorting:** Sorting and indexing is concise and deterministic but takes $O(n\log n)$ time and does more ordering work than selection requires.
- **`k = 1`:** The converted target is `n - 1`, the last ascending position, so selection returns the maximum.
- **`k = n`:** The converted target is 0, so selection returns the minimum.
- **All values equal:** Inner scans stop on equal values from both sides, swap or cross, and shrink the interval. The answer is that repeated value for every legal rank.
- **Negative values:** Partition comparisons work directly on signed integers; no offset or special case is needed.
- **One element:** The converted target is 0, the initial call satisfies `l == r`, and that element is returned without partitioning.
- **Mutation of `nums`:** Swaps change the caller-provided list's order. This is acceptable to the platform contract, but callers that require preservation must pass a copy, adding $O(n)$ time and space.
