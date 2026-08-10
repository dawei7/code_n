## General

For every legal `k \times k` window, the source:

1. copies all `k^2` values into a temporary list;
2. sorts that list;
3. checks gaps between adjacent unequal values;
4. stores the smallest gap, or zero when no distinct pair exists.

The key mathematical fact is that after sorting, the minimum difference between any two distinct values must occur between two adjacent **distinct** entries. This reduces a quadratic all-pairs comparison inside each window to one sort plus one linear scan.

**Enumerating every submatrix**

A `k \times k` submatrix is determined by its top-left coordinate `(i,j)`.

Its row start can range from zero through `m-k`, giving `m-k+1` choices. Its column start can range from zero through `n-k`, giving `n-k+1` choices.

The nested loops cover exactly those ranges. The result matrix is allocated with the same dimensions, and `ans[i][j]` corresponds directly to the window beginning at `(i,j)`.

For one start, rows `i` through `i+k-1` and columns `j` through `j+k-1` are visited. Every cell in the square is appended once to `nums`. The source does not try to reuse values between overlapping windows; each window is built independently.

**Why sorting exposes the minimum gap**

Suppose the sorted values are

$$
a_0 \le a_1 \le \cdots \le a_{k^2-1}.
$$

Take any two distinct values `a_p < a_q` with at least one sorted element between them. Then

$$
a_q-a_p
= (a_{p+1}-a_p) + \cdots + (a_q-a_{q-1}).
$$

All terms are nonnegative, and at least one transition between distinct adjacent values occurs along this range. That adjacent positive gap is no larger than the whole difference `a_q-a_p`.

Therefore a globally minimum positive difference cannot require comparing nonadjacent sorted values: some adjacent distinct pair is at least as good. Scanning adjacent pairs is sufficient.

Because the list is sorted, `b \ge a` for each adjacent pair `(a,b)`. The source calls `abs(a-b)`, which equals `b-a` here. The absolute value is correct but not necessary after sorting.

**Why equal adjacent values are skipped**

The problem asks for two **distinct values**, not merely two different cells. If value `3` appears twice, comparing those occurrences gives difference zero but does not satisfy the distinct-value requirement.

The generator therefore includes `if a != b`. Repeated equal values are skipped until the scan reaches a boundary between two different values.

The manifest summary says the method “builds and sorts the distinct values.” The exact source actually sorts all `k^2` occurrences and filters equal adjacent pairs during scanning. The outcome is equivalent, but the temporary list can contain duplicates and its sorting cost is based on all cells.

**Why default zero handles the special case**

If every element in a window has the same value, no adjacent unequal pair exists. This also occurs automatically for `k=1`, where there is only one element and `pairwise(nums)` is empty.

The `min` call uses `default=0`. When the generator supplies no candidate gap, the result is zero, exactly matching the note. If at least two distinct values exist, every candidate difference is positive and ordinary minimum selection is used.

**A representative trace**

For window values `[1,8,3,-2]`, sorting gives `[-2,1,3,8]`. Adjacent distinct gaps are:

- `1-(-2)=3`;
- `3-1=2`;
- `8-3=5`.

The minimum is two, corresponding to values one and three. Comparing all six unordered pairs would find the same result but perform unnecessary work.

For values `[-2,3,3,5]`, sorting leaves the duplicate threes adjacent. The gaps considered are five between `-2` and `3`, then two between `3` and `5`; the equal `3,3` pair is ignored. The answer is two rather than zero.

**Why windows can be solved independently**

The requested answer for one top-left coordinate depends only on values inside that square. Sorting a copied list leaves `grid` unchanged, so processing one window cannot affect another. Overlap in the original matrix creates repeated computation but no correctness dependency.

## Complexity detail

Let

$$
W=(m-k+1)(n-k+1)
$$

be the number of windows. Copying one window takes `O(k^2)` time. Sorting `k^2` elements takes

$$
O(k^2\log(k^2)) = O(k^2\log k),
$$

and scanning adjacent pairs takes `O(k^2)`.

Total time is

$$
O(Wk^2\log k)
= O((m-k+1)(n-k+1)k^2\log k).
$$

The manifest’s `O(RCk^2\log k)` is a looser upper bound when `R` and `C` denote grid dimensions.

The temporary `nums` list holds exactly `k^2` values. The result holds `W` integers. Peak space is `O(k^2 + W)` including output, which is the manifest’s `O(k^2 + RC)` upper-bound form. Excluding required output, auxiliary space is `O(k^2)`; Python’s sort may also use temporary memory within the same linear order.

## Alternatives and edge cases

- **Compare every pair:** Checking all value pairs in one window costs `O(k^4)` time. Sorting reduces the relevant comparisons to adjacent gaps.
- **Build a set before sorting:** Sorting `set(nums)` directly represents distinct values and can reduce work when duplicates are common. The exact source sorts all occurrences and filters equal neighbors instead.
- **Balanced ordered multiset across sliding windows:** One could update value frequencies as a window shifts and maintain adjacent distinct gaps. Extending this efficiently across both row and column movement is more complex, and the small `30 \times 30` limits make independent sorting reasonable.
- **Counting array:** With values bounded to a small dense range, frequency counts could find adjacent distinct values without comparison sorting. The allowed range from `-10^5` to `10^5` is manageable but much larger than a window, and repeated initialization needs care.
- **Window size one:** There is no pair of distinct values, so every output entry is zero.
- **All equal values:** Equal adjacent occurrences are skipped and `default=0` supplies the required result.
- **Duplicates plus other values:** Duplicate copies do not create a zero answer; only boundaries between unequal values are candidates.
- **Negative values:** Sorting and subtraction handle them normally, as shown by a gap such as `1-(-2)`.
- **Exactly two distinct values:** Their difference is the only positive adjacent distinct gap and is returned regardless of duplicate counts.
- **k equals both grid dimensions:** Only one window exists, so the answer has shape `1 \times 1`.
- **Rectangular grid:** Row and column window counts are computed independently, so non-square full grids are handled correctly.
- **Input preservation:** Values are copied before sorting; the original grid order never changes.
- **Absolute value after sorting:** It is redundant but harmless because adjacent sorted values never decrease.
- **Output dimensions:** Allocating `m-k+1` rows and `n-k+1` columns exactly matches the number of top-left positions.
