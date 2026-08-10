## General

**Keep bars whose right boundary is not known yet**

The stack stores indices of bars that have not yet encountered a shorter-or-equal bar to their right. A sentinel index `-1` sits at the bottom. It is never used to read `heights`; it represents the imaginary position just before the histogram and makes the width formula uniform.

As real indices are processed, stack heights are increasing under the source's `>=` pop rule. A new shorter-or-equal height proves that a top bar can extend no farther right than the position immediately before the new index. That bar's maximal candidate area can now be calculated and forgotten.

**Pop and calculate with the new stack top**

When index `i` blocks the top bar, `stk.pop()` yields the height index whose area is being finalized. After that pop, `stk[-1]` is the nearest remaining smaller-height index to its left under the tie convention.

The rectangle spans from `stk[-1] + 1` through `i - 1`, inclusive. Its width is

`(i - 1) - stk[-1]`,

which is algebraically `i - stk[-1] - 1`. Multiplying by the popped height produces a feasible rectangle because every intervening bar was tall enough to let the popped index remain on the stack until now.

The source updates `result` at every pop. A bar needs no later reconsideration: both its blocking boundaries are now known.

**Why the current index may pop several bars**

One low bar can end the possible spans of many taller bars. For `[1, 5, 6, 2]`, height 2 pops height 6 and then height 5. Each pop exposes a different left boundary and therefore a different width. The loop continues until the stack sentinel is reached or the top height is strictly lower than the current height.

After popping, the current index is pushed. It becomes a possible height for future rectangles. Because greater-or-equal tops were removed, the real bar heights in the stack are strictly increasing.

**Use a virtual end position to flush remaining bars**

The outer loop runs through `range(len(heights) + 1)`. The extra index `i == len(heights)` is not a real bar. The while condition treats it as a blocker for every remaining real height through `i == len(heights) or ...`.

Short-circuit `or` is essential: at the virtual index, the code does not evaluate `heights[i]`, which would be out of bounds. It simply pops until only `-1` remains. Those bars had no real blocker to the right, so using the virtual end as `i` gives them a rightmost included position of `len(heights) - 1`.

After flushing, the source appends the virtual index to the stack. It is never read or used again, so this harmless append avoids a special branch around the common push statement.

**Equal heights and the `>=` rule**

When an equal-height bar arrives, the older equal index is popped and receives a rectangle ending immediately before the new one. The new equal index is then pushed with the older bar's smaller left boundary exposed beneath it.

This does not lose the widest equal-height rectangle. A later representative can extend left across the earlier equal bars and right until a lower blocker or the virtual end. For `[2,2]`, the first 2 produces area two when the second arrives, and the second produces area four during the final flush.

Using `>` instead could keep equal indices together and also be correct with consistent boundaries, but the stack invariant and which representative receives the full width would differ.

**A stack invariant and correctness argument**

Before processing an index, real stack indices are increasing and their heights are strictly increasing. For each stacked bar, every processed position after its previous smaller boundary is at least its height, and no right blocker has yet appeared.

When a new bar is shorter or equal, popping exactly those blocked heights preserves the invariant. The new stack top after each pop is their nearest valid smaller boundary, so the computed width is maximal under the tie convention. Pushing the current index restores increasing heights.

Every bar is eventually popped either by a real blocker or by the virtual end. Its feasible maximal candidate is therefore considered. Every possible histogram rectangle has some minimum-height bar, and the candidate finalized for an appropriate representative spans at least that rectangle's interval. Taking the maximum of all feasible candidates returns the global largest area.

**Trace the maximum in the standard example**

For `[2,1,5,6,2,3]`, index four with height 2 pops index three with height 6, calculating width one and area six. It then pops index two with height 5. The new top is index one, so width is `3 - 1 = 2` in the source's `(i - 1) - stack_top` form, producing area ten. No later pop exceeds this result.

## Complexity detail

Every real index is pushed once and popped once at most. The extra virtual iteration causes only the remaining total pops, so aggregate time is $O(n)$, matching the manifest despite the nested while loop.

In an increasing histogram, the stack can hold all `n` real indices plus the sentinel. Its size is therefore $O(n)$, matching the manifest. Other state is scalar, and `heights` is not modified.

## Alternatives and edge cases

- **Precompute left and right boundaries:** Store both blockers for every bar and calculate areas afterward. It is equally linear but uses two extra arrays in addition to the stack.
- **Append a real zero sentinel:** Temporarily add height zero and run an ordinary loop. It simplifies the condition but mutates the input and must restore it if preservation matters.
- **Brute-force intervals:** Maintain minimum height for every pair of endpoints, requiring $O(n^2)$ time.
- **Single bar:** It remains stacked until the virtual end, where width one is calculated.
- **Zero-height bars:** They flush positive heights; their own area is zero.
- **Increasing input:** All bars wait for the virtual end, yet each is popped only once.
- **Decreasing input:** Each new bar immediately finalizes the preceding top, still linear overall.
- **Equal bars:** The `>=` condition replaces older equals, and the later representative captures the plateau width.
- **Sentinel safety:** The condition checks `stk[-1] != -1` before any height access using that index.
- **Virtual-index safety:** `i == len(heights)` short-circuits before `heights[i]` is evaluated.
- **Empty input outside the contract:** The virtual iteration leaves result zero and returns zero.
- **Large heights:** Python integer multiplication does not overflow; fixed-width translations should use a sufficiently wide area type.
- **Input preservation:** The source never appends to or edits `heights`.
