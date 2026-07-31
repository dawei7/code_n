## General

Record the free gaps before the first meeting, between consecutive meetings, and after the last meeting. Moving one meeting can pack it against a neighbor and combine the free time on its two sides. More generally, moving a consecutive block of `k` meetings can pack those meetings to one side of their original span, merging the block's `k + 1` surrounding gaps into one continuous interval.

The meeting durations do not contribute to the merged free interval and never change. Therefore, for each possible block, its achievable free time is exactly the sum of the corresponding `k + 1` consecutive gaps. Conversely, any newly joined free interval can cross only meetings that were moved; its crossed meetings form a consecutive block, so it cannot contain more than `k + 1` original gaps. This establishes that the largest such gap sum is both achievable and optimal.

Compute the first window sum, then slide it across the gap array by adding the entering gap and subtracting the leaving gap. The maximum window sum is the answer. Using exactly `k` positions in the window is safe even though the operation permits at most `k`: all gaps are nonnegative, and a smaller window can be extended without reducing its sum.

## Complexity detail

Let $n$ be the number of meetings. Constructing the $n+1$ gaps and scanning them both take $O(n)$ time. The gap array uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Recompute every window sum:** Summing `k + 1` gaps for each block costs $O(nk)$ time.
- **Move the largest individual gaps:** The gaps must be consecutive to merge into one continuous free interval, so independently selecting them is invalid.
- **No existing free time:** Every gap is zero and the answer remains zero regardless of how meetings move.
- **Move all meetings:** All free time can be consolidated at one event boundary.
- **Boundary gaps:** Free time before the first and after the last meeting participates exactly like every internal gap.
