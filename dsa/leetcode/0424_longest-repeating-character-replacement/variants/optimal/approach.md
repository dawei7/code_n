## General
**Express feasibility as a frequency deficit**

Within a window, keep the most frequent letter unchanged and replace every other character with it. If the window length is `L` and its largest frequency is `F`, exactly $L - F$ replacements are necessary and sufficient. The window is feasible precisely when this deficit is at most `k`.

**Maintain the longest feasible sliding window**

Move the right boundary across the string and increment that letter's frequency. While the current deficit exceeds `k`, remove the leftmost letter and advance the left boundary. Recompute the maximum across the fixed 26-letter table after each boundary change, then record the largest feasible length.

**Why discarding the left boundary is safe**

When a window is infeasible, extending it cannot reduce the number of nonmajority characters enough to make that same left boundary produce a longer feasible window before some prefix is removed. Shrinking only until feasibility returns preserves every candidate that could improve the answer. Each right boundary is therefore paired with its longest relevant feasible suffix, and the maximum recorded length is globally optimal.

## Complexity detail
Each boundary advances at most `n` times. Finding the maximum scans 26 counters, a fixed alphabet, so time is $O(26n) = O(n)$. The 26-element frequency table uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Monotone historical maximum:** never decrease the largest frequency seen while expanding; this yields the same $O(n)$ result with fewer constant-time scans but has a subtler correctness argument.
- **Enumerate every start and end:** count each substring independently in $O(n^2)$ time.
- **No replacements:** the answer is the longest existing run of one letter.
- **Budget covers the string:** if `k` can replace every nonmajority character, the whole string is feasible.
- **Several equally frequent letters:** choosing any maximum-frequency target gives the same replacement count.
