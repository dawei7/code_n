## General

**View every bar as a possible rectangle height**

Any rectangle covering consecutive histogram bars is limited by the shortest bar in its interval. Turn that statement around: choose a bar at index `i` with height `h`, and ask how far a rectangle of height `h` can extend left and right before meeting a blocking bar.

If the nearest blocking positions are known, the width is the number of indices strictly between them. The source stores one boundary in `left[i]` and one in `right[i]`, then evaluates

`h * (right[i] - left[i] - 1)`.

The outside sentinel positions `-1` and `n` allow a bar to extend to the physical beginning or end without separate width formulas.

**Maintain indices of increasing heights**

`stk` stores indices whose heights are strictly increasing from bottom to top after each iteration. When a new height `h` arrives, every stack-top height greater than or equal to `h` is popped. Once those bars see this new shorter-or-equal bar, they cannot extend through index `i` under the source's tie convention, so `right[popped] = i` is recorded.

After all such pops, any remaining top has height strictly smaller than `h`. It is the nearest surviving smaller bar to the left, so `left[i] = stk[-1]`. If the stack is empty, no smaller bar exists to the left and the initialized `-1` remains.

Finally, index `i` is pushed. Because all greater-or-equal heights were removed, strict height increase is restored.

**Why popping reveals the nearest right blocker**

Consider a bar index `p` that is popped when processing `i`. It stayed on the stack through every index between `p` and `i`, so none of those earlier positions caused its removal. Therefore no intervening height was less than or equal to `heights[p]` under this pop rule. The current index is the first such blocker to its right.

Bars that never get popped have no blocking height at or below them on the right. Their `right` entries keep the initialized sentinel `n`, allowing their rectangles to reach the histogram end.

**Understand the asymmetric treatment of equal heights**

The pop condition is `heights[stk[-1]] >= h`, not just `>`. Consequently the remaining left boundary for a newly pushed bar is strictly lower, while a popped older bar may receive an equal-height bar as its right boundary.

This can make an earlier member of an equal-height plateau receive a narrower interval than its true maximal geometric span. Correctness is still preserved because the later equal bar replaces it after the pop and inherits the earlier bar's strictly lower left boundary. The rightmost relevant representative of a plateau can span across the equal bars until a genuinely lower boundary appears or the array ends.

For `[2, 2]`, index zero is popped when index one arrives and gets width one. Index one receives left boundary `-1` and right sentinel 2, so its width is two and area four. The maximum considers the full plateau even though the first bar's individual interval was shortened.

**Trace the example boundaries**

For `[2,1,5,6,2,3]`, height 1 at index one pops height 2 and gives it right boundary one. Indices two and three, heights 5 and 6, form an increasing stack above index one. Height 2 at index four pops 6 and then 5, assigning both right boundary four. The nearest smaller index remaining for height 2 is index one.

For height 5 at index two, `left[2] = 1` and `right[2] = 4`. Its rectangle covers indices two and three, width `4 - 1 - 1 = 2`, and area 10. The final maximum recognizes this as the answer.

**Why checking every bar boundary is complete**

Take any maximum rectangle and choose a bar of minimum height within it. A rectangle using that height can extend at least across the chosen interval. The boundary process associates an equal-height representative with the maximal interval allowed before a lower or tie-handled blocker. Its calculated area is at least the maximum rectangle's area over that interval, and cannot exceed what the histogram supports.

Conversely, every calculated rectangle lies between boundaries that guarantee all included bars are at least the chosen height under the monotonic-stack construction. Each candidate area is therefore feasible. Taking the maximum over all indices yields exactly the largest feasible area.

**Why the arrays are initialized before scanning**

`left = [-1] * n` and `right = [n] * n` encode absence of blockers. The scan overwrites only discovered boundaries. This avoids a cleanup pass over remaining stack indices: an unpopped bar's correct right boundary is already `n`.

The constraints guarantee at least one bar, so the final `max(...)` generator is nonempty. An empty input outside the contract would raise `ValueError` rather than return zero.

## Complexity detail

Each index is pushed once and popped at most once. Although the pop loop is nested inside the scan, its total iterations across the whole algorithm are $O(n)$. Computing all final areas also takes $O(n)$, so total time is $O(n)$, matching the manifest.

The stack, `left`, and `right` can each contain $O(n)$ entries. Exact auxiliary space is $O(n)$, matching the manifest. The input heights are read without modification.

## Alternatives and edge cases

- **Compute areas during pops:** A sentinel index or appended zero can finalize width immediately, avoiding the two boundary arrays while retaining $O(n)$ stack space.
- **Quadratic expansion:** For each bar, scan left and right until a shorter bar. It is easy to derive but can take $O(n^2)$ time on monotone histograms.
- **Divide and conquer:** Split at a minimum-height bar. Without fast range-minimum queries, sorted inputs cause quadratic time.
- **Segment tree:** It accelerates range-minimum queries but adds substantial structure and usually $O(n\log n)$ total time.
- **Single bar:** Both sentinel boundaries give width one and return its height.
- **Zero-height bar:** Its area is zero and it pops all positive stack heights, correctly finalizing their right boundaries.
- **Strictly increasing heights:** Nothing pops during the scan; right sentinels let each bar extend to the end.
- **Strictly decreasing heights:** Each new bar pops prior bars immediately; total work remains linear.
- **Equal-height plateau:** Earlier equals are popped, while a later representative inherits the full left reach.
- **Maximum length:** Amortized push/pop analysis avoids the quadratic behavior of repeated outward scans.
- **Nonempty guarantee:** The final `max` depends on at least one candidate.
- **Input preservation:** Only boundary and stack arrays are mutated.
