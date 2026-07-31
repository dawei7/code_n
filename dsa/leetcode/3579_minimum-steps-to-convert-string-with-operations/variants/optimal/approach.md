## General

For one fixed segment, first ignore reversal. Every position where the source and target characters differ contributes a directed mismatch pair $(x,y)$. One swap can fix two positions exactly when their pairs are reciprocal: $(x,y)$ and $(y,x)$. For each unordered pair of distinct letters, the maximum number of useful disjoint swaps is therefore the smaller of the two directed counts. After taking all such swaps, every remaining mismatch is fixed by one replacement. If a segment has $M$ mismatches and $P$ reciprocal pairs, its minimum direct cost is $M-P$.

These quantities can be maintained as a segment grows. When a new mismatch $(x,y)$ is added, it creates another usable swap precisely when its old count is smaller than the existing count of $(y,x)$. Extending every left endpoint to the right computes all direct segment costs in $O(n^2)$ total time.

Reversing a segment changes which source position aligns with each target position, but all reversed costs can also be computed in quadratic time. For an interval $[l,r]$, the reversed alignment pairs `word1[r]` with `word2[l]`, `word1[r - 1]` with `word2[l + 1]`, and so on. Intervals having the same sum $l+r$ share one center. Expanding outward from that center adds only the two new endpoint alignments, so the same mismatch counters yield every reversed conversion cost in $O(n^2)$ total. Choosing this route adds one operation for the reversal.

Finally, let `best[i]` be the minimum cost to transform the first $i$ characters. For every right endpoint and every possible start `left` of its final segment, combine `best[left]` with the smaller of that segment's direct cost and one plus its reversed cost. Every legal partition has a unique last segment, so this transition considers every solution and selects the minimum.

## Complexity detail

There are $O(n^2)$ intervals. Direct extensions, center-based reversed extensions, and partition-DP transitions each do constant work per interval, so total time is $O(n^2)$. The two interval-cost tables occupy $O(n^2)$ space; the DP array and fixed $26\times26$ mismatch counters do not change that bound.

The benchmark uses $S=n$ and strings whose every position requires replacement. The accepted interval precomputation remains $O(S^2)$. The calibrated alternative rebuilds direct and reversed mismatch counts by scanning every candidate segment during the partition DP, taking $O(S^3)$ time while producing identical answers.

## Alternatives and edge cases

- **Recompute every segment:** Scanning each direct and reversed substring independently is easy to reason about but costs $O(n^3)$ time.
- **Try arbitrary swap matchings:** A general matching algorithm is unnecessary because useful swaps only connect reciprocal directed letter pairs; each pair class is independent.
- **Replacement-only strategy:** Replacing every mismatch is always feasible but misses the saving from each reciprocal pair and from a reversal.
- **Reversal alignment:** Reversing changes source-to-target pairings across the entire segment; reusing the direct mismatch counts would be incorrect.
- **Duplicate mismatch pairs:** If one direction occurs more often than its reciprocal, only the matched minimum can become swaps; the excess positions still need replacements.
- **Already equal segment:** Its direct cost is zero, so paying for a reversal cannot improve it.
- **Singleton segment:** It needs zero operations when characters match and exactly one replacement otherwise.
- **Partition boundaries:** Operations never cross segments, so each DP transition must use costs computed for that exact contiguous range.
