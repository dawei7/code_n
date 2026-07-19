## General
**The sorted input splits into left, overlap, and right regions**

Copy every interval ending strictly before the new interval starts. Because intervals are closed, `end < new_start` is the strictly-left condition; equality means the intervals touch and must merge.

Then consume intervals whose start is at most the working end. Absorb each one by taking the minimum start and maximum end. Extending the end may cause a later interval to overlap even if it did not overlap the original insertion, so the overlap test must use the growing interval.

**Emit the merged insertion once, then preserve the suffix**

Once an interval starts after the merged end, no later interval can overlap because starts are sorted. Append the merged interval once, then copy the untouched suffix.

**The working interval represents the complete overlap component so far**

Before the overlap loop, the output contains exactly the disjoint prefix lying left of the insertion. During the loop, the working interval equals the union of the original insertion and every consumed overlapping interval. The unprocessed suffix remains sorted and disjoint.

**Trace transitive overlap growth**

For `[[1,2],[3,5],[6,7],[8,10],[12,16]]` and `[4,8]`, copy `[1,2]`. Absorb `[3,5]`, `[6,7]`, and `[8,10]`, growing the insertion to `[3,10]`. Append it, then copy `[12,16]`.

**Three ordered regions exhaust the interval list**

Any interval ending before the new interval starts is disjoint on the left and can be copied unchanged. Once overlap begins, every interval whose start is at most the growing merged end belongs to the same connected union and must expand that union's endpoints.

At the first start greater than the merged end, sorted order guarantees that interval and all later ones are disjoint on the right. Copying the left region, emitting the single merged middle interval, and copying the right region therefore covers every input interval exactly once and preserves the required union and order.

## Complexity detail
Each original interval is examined and copied at most once, giving $O(n)$ time. The returned list uses $O(n)$ storage; only the merged endpoints and index are auxiliary state.

## Alternatives and edge cases
- **Append, sort, then run Merge Intervals:** is correct but discards the useful precondition and costs $O(n \log n)$ time.
- **Repeated pairwise merging:** can require quadratic comparisons and list shifts.
- **Modify the original list in place:** can reduce allocations in some environments but violates this contract's nonmutation requirement.
- Empty input produces a list containing only the new interval. An insertion entirely before or after the input is handled by an empty left or overlap region.
- Copy endpoints into a working interval if the input must remain unchanged; mutating `new_interval` or an original interval would violate the stated contract.
