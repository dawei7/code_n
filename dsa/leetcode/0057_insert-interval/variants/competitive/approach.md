## General

**Use the existing order to split the answer into three regions**

Because `intervals` is already sorted and internally non-overlapping, inserting one interval has a simple structure:

- intervals completely before `newInterval` remain unchanged;
- one consecutive block may overlap `newInterval` and must be merged with it;
- intervals completely after the merged interval remain unchanged.

The source locates these regions with one index `i`, never sorting and never moving backward.

**First loop: copy intervals strictly to the left**

The condition `newInterval[0] > intervals[i][1]` means the old interval ends before the new interval starts. The inequality is strict. If the endpoints are equal, the closed intervals share a point and belong in the merge block.

Each strictly-left interval is added with `result += intervals[i],`. The trailing comma creates a one-element tuple containing the interval, and list `+=` extends by that tuple. In effect, this is an unusual spelling of `result.append(intervals[i])`.

Since input intervals are sorted and non-overlapping, every copied interval is also safely before all later output.

**Second loop: absorb the consecutive overlap block**

After the first loop, either no interval remains or the current interval does not lie strictly left. It overlaps the evolving `newInterval` exactly while `newInterval[1] >= intervals[i][0]`. Equality again counts as overlap.

For each overlap, the source creates a fresh pair whose start is the smaller start and whose end is the larger end. Rebinding `newInterval` to this pair expands the active union. As it expands rightward, it may reach additional intervals that did not overlap the original interval directly. The loop correctly absorbs that entire connected chain.

The original intervals are non-overlapping, so the overlap candidates form one consecutive block. Once an interval starts after the merged end, every later interval starts still farther right and cannot overlap.

**Append the merged interval and untouched suffix**

When the overlap loop ends, `newInterval` is the exact union of the inserted interval and every intersecting old interval. It is appended once. `result.extend(intervals[i:])` then copies references to all strictly-right intervals.

These suffix intervals remain sorted and disjoint. The first suffix start is greater than the merged end, or the overlap loop would not have stopped. Therefore, concatenating the three regions produces a sorted, non-overlapping result.

**The phase invariant**

After the first loop, `result` contains exactly the old intervals ending before the new start, in original order. During the second loop, local `newInterval` equals the union of the original inserted interval and all overlapping intervals processed so far. The unprocessed suffix begins at index `i`.

Each merge preserves a single closed interval because the next candidate intersects the active union. At termination, no unprocessed interval intersects it. Appending the active union and suffix therefore covers every input point and introduces no overlap.

**Example with a chain of overlaps**

For `[[1,2],[3,5],[6,7],[8,10],[12,16]]` and `[4,8]`, `[1,2]` is copied left. The active interval merges successively with `[3,5]`, `[6,7]`, and `[8,10]`, becoming `[3,10]`. The next start 12 lies beyond end 10, so the merge stops and `[12,16]` is appended as suffix.

**Mutation and reference behavior**

The outer input list is not sorted, appended to, or otherwise mutated. Old intervals copied into the prefix or suffix are the same inner list objects, but the method never writes into them.

If at least one overlap occurs, local `newInterval` is rebound to a freshly allocated pair, so the caller's original new-interval list is not mutated. If no overlap occurs, the exact original `newInterval` object is appended to `result`. Later caller mutation of shared inner lists could therefore be visible through both structures, but the method itself performs no inner-list writes.

`intervals[i:]` creates a temporary suffix list of references before `extend`, which contributes linear temporary space in the worst case.

## Complexity detail

Index `i` increases from 0 to at most $n$ across the two while loops. Prefix copying, overlap merging, and suffix extension together process $O(n)$ interval references, so time is $O(n)$, matching the manifest.

The returned list can contain $O(n)$ intervals. The suffix slice may also hold $O(n)$ temporary references. Thus total/result storage is $O(n)$, matching the manifest. Apart from output and that slice, the algorithm uses constant scalar state. The source comment's $O(1)$ is only meaningful if required output and slicing behavior are excluded.

## Alternatives and edge cases

- **Avoid suffix slicing:** Append remaining intervals in a final loop. This preserves $O(n)$ time and avoids the temporary `intervals[i:]` list.
- **Binary-search insertion neighborhood:** It may reduce search for the first relevant interval, but output construction still costs linear time in the worst case.
- **Append then sort and merge:** It is simple but ignores the sorted precondition and costs $O(n \log n)$.
- **Empty interval list:** Both while loops skip, the new interval is appended, and it is the sole result.
- **New interval before everything:** No left interval is copied and no merge occurs unless endpoints overlap; the new interval appears first.
- **New interval after everything:** Every old interval enters the left region, then the new interval is appended.
- **Touching endpoints:** Both phase conditions use strict separation, so touching intervals merge.
- **Contained interval:** Merged min/max bounds reproduce the containing old interval.
- **New interval spans many gaps:** Once it overlaps the next interval, its end may extend and absorb a whole consecutive chain, while genuine gaps beyond the final end remain.
- **Input preservation:** The method itself does not reorder or write into `intervals` or the original `newInterval`.
