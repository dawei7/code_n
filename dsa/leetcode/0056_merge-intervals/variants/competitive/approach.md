## General

**Sort by start so only the last merged interval matters**

`intervals.sort()` orders interval pairs by start and then by end. Once starts are non-decreasing, a new interval can overlap only the last merged interval in `result`. Any earlier result interval ended before that last interval began and has already been separated by a proven gap.

The algorithm therefore needs no nested comparisons. It walks the sorted intervals once and either appends a new group or extends the end of the current last group.

**The two cases for one interval**

If `result` is empty, the first interval starts the first group. Otherwise, compare the new start `interval[0]` with the last merged end `result[-1][1]`.

When the new start is greater than the last end, there is a strict gap. The source appends the interval as a new result group. When the new start is less than or equal to the last end, the intervals overlap under closed-endpoint semantics, and the last end becomes the maximum of the two ends.

The start of the last result never needs modification. It is at most the new start because the input was sorted. If the new interval is contained inside the last group, the maximum leaves the end unchanged. If it reaches farther right, the end expands.

**Closed intervals make equality an overlap**

For `[1,4]` followed by `[4,5]`, the test `4 > 4` is false. Both intervals contain point 4, so their union is continuous and the algorithm produces `[1,5]`. A condition using `>=` would incorrectly separate them.

**The result invariant**

After processing a prefix of the sorted input, `result` contains non-overlapping intervals whose union equals that prefix's union. They appear in increasing start order, and only the final interval can potentially overlap the next input.

Appending after a strict gap preserves non-overlap. Extending the final end after overlap preserves the union and cannot create an overlap with an earlier result interval, because increasing the right edge of the last group moves only farther away from earlier groups. Induction proves the invariant through the full scan.

At completion, the result covers every input interval and contains no pair that should have been merged. Therefore, it is the required non-overlapping cover.

**Why a later interval cannot reconnect an older group**

Suppose an earlier group ends at `a`, the current last group begins after `a`, and a future interval is being processed. Its start is at least the current group's start because of sorting. It cannot start before or at `a` and bridge backward. This monotonicity is what makes comparison with only `result[-1]` safe.

**Exact aliasing and mutation behavior**

The source appends `interval` itself, not a copy. Each result entry is therefore the same inner list object that appears in the sorted input. When an overlap later executes `result[-1][1] = ...`, it mutates that original input interval object.

For example, after appending input object `[1,3]`, merging `[2,6]` changes that same first object to `[1,6]`. The outer input list has also been reordered by `.sort()`. This is accepted by typical judge contracts, but a caller should not expect `intervals` or all its inner lists to remain unchanged.

Intervals that are merged into the tail but not appended remain separate input objects with their old contents; the output tail aliases whichever object originally began that group.

**Empty input behavior**

Although the official constraint guarantees at least one interval, this loop naturally handles `[]`: no iteration runs and an empty result is returned. No special indexing is used.

## Complexity detail

Sorting dominates at $O(n \log n)$. The scan is $O(n)$ with constant work per interval, so total time is $O(n \log n)$.

The `result` outer list can hold $n$ references and is the required output, giving $O(n)$ result space. The algorithm otherwise stores constant local state, but Python's in-place sort may allocate $O(n)$ temporary workspace. Thus the manifest's $O(n)$ storage bound is appropriate. The source comment's $O(1)$ can only describe extra scalar merge state while excluding output and sort implementation workspace.

## Alternatives and edge cases

- **Copy intervals before appending:** Use `[interval[0], interval[1]]` to prevent output-tail updates from mutating input inner lists.
- **Separate active endpoints:** Keep scalar `start` and `end`, append fresh pairs when gaps occur, and avoid aliasing altogether.
- **Non-mutating outer sort:** Iterate over `sorted(intervals)` to preserve outer order, though inner-list aliasing still requires copies if tails are modified.
- **Sweep line:** Endpoint events can compute the union but add event bookkeeping without improving the sorting bound.
- **No overlaps:** Every input object is appended; result entries alias all original inner lists.
- **Complete containment:** The maximum end remains unchanged, so the contained interval adds no new coverage.
- **Touching endpoints:** They merge because the strict-gap condition uses `>`.
- **Equal starts:** Sorting by end as a tiebreaker does not affect correctness; repeated tail extensions reach the largest end.
- **Empty input outside the primary contract:** The implementation returns `[]` safely.
- **Caller-visible mutation:** Both outer ordering and some inner endpoints can change, which is the central tradeoff of reusing interval objects.
