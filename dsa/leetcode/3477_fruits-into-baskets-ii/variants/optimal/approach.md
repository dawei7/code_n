## General

**The placement rule is deterministic, so simulate it in the stated order.** Fruit types must be processed from left to right, and each one must use the leftmost still-available basket whose capacity is at least its quantity. There is no optimization choice to make once those rules are fixed.

The protected source creates Boolean list `vis` with one entry per basket. `vis[i]` is false while basket $i$ is unused and becomes true after a fruit type is placed there. Keeping availability separate lets the code preserve the original capacity array.

The answer begins as `ans = n`, treating every fruit type as unplaced. Whenever a placement succeeds, the source decrements `ans`. This is equivalent to starting from zero and incrementing on failures, but it lets successful placement update the count at the exact moment a basket is consumed.

**Search baskets from index zero for every fruit type.** For current quantity `x`, the inner loop enumerates `baskets` in increasing index order. A basket is usable exactly when both conditions hold:

- `y >= x`, so its capacity is sufficient; and
- `not vis[i]`, so no earlier fruit type has consumed it.

The first basket satisfying both is necessarily the leftmost available sufficient basket. The code marks it visited, decrements the unplaced count, and immediately executes `break`. Breaking is essential: one fruit type may occupy only one basket, and no later suitable basket should also be marked.

If the loop reaches its end without a match, no basket is changed and `ans` is not decremented. That fruit type remains unplaced exactly as required.

For `fruits = [4,2,5]` and `baskets = [3,5,4]`, quantity four skips basket zero and consumes basket one. Quantity two then starts searching from the left again and consumes basket zero. Quantity five finds basket one already used and basket two too small, so the initial count of three has been decremented twice and the returned answer is one.

Restarting from basket zero for each fruit is correct. A low-index basket skipped earlier because it was too small for a large fruit may still be the leftmost valid choice for a later smaller fruit. Maintaining one monotonically advancing basket pointer would miss this possibility.

For `fruits = [3,6,1]` and `baskets = [6,4,7]`, the first fruit consumes index zero. The second skips used index zero and insufficient index one, then consumes index two. The final quantity one returns to the beginning, skips used index zero, and consumes index one. All three placements succeed.

**Why capacity alone cannot mark usage in this source.** A used basket might retain a large original capacity, so the inner condition must consult `vis`. The local editorial shows another legal implementation that overwrites a used positive capacity with zero, but the protected source deliberately avoids mutation and therefore requires the separate flag.
Before processing fruit position $p$, `vis` marks exactly the baskets used by fruit types $0$ through $p-1$, and `ans` equals $n$ minus the number of successful placements so far. The inner loop inspects baskets in left-to-right order and accepts the first one that is both unused and large enough, so it performs exactly the mandated placement for fruit $p$. If none qualifies, leaving all flags unchanged exactly represents an unplaced fruit. The successful branch marks one and only one basket and updates the count once. Thus the invariant holds for the next fruit.

After all fruits have been processed, every placement agrees with the deterministic rule, no basket has been used twice, and `ans` counts precisely the fruit types for which no placement occurred.

This is not a matching problem where rearranging choices could improve a global objective. The word “leftmost” fixes the required allocation even if choosing a later basket would leave more options for future fruit. The simulation must follow that rule rather than substitute a capacity-based greedy strategy.

**The protected space use differs from the manifest.** The manifest and local editorial state constant auxiliary space for an implementation that consumes a basket by overwriting its capacity. The protected source leaves `baskets` unchanged and allocates `vis` of length $n$. Its actual auxiliary space is therefore linear.

## Complexity detail

There are $n$ fruit types. In the worst case, each scans all $n$ baskets—for example, when no capacity is sufficient or only the last available basket qualifies. Total time is $O(n^2)$, matching the manifest.

The visited array contains $n$ Booleans, so auxiliary space is $O(n)$, not the manifest's $O(1)$. The remaining variables are scalars. No output array is created.

Because $n\le100$, at most ten thousand fruit-basket checks occur, making direct simulation entirely appropriate for this version of the problem.

An in-place variant can mark a used basket by assigning zero because all fruit quantities are positive and a zero-capacity basket can never qualify later. That would achieve $O(1)$ auxiliary space but would mutate the input; it is not the protected implementation.

## Alternatives and edge cases

- **Sort fruits or baskets:** Sorting destroys the required original left-to-right order and changes which basket is considered leftmost.
- **Use the smallest sufficient basket:** Capacity best-fit is a different policy; the problem requires the lowest available basket index.
- **Maintain one forward-only basket pointer:** A basket too small for one fruit may fit a later fruit, so earlier indices must be reconsidered.
- **Segment tree over maximum capacity:** It can find the leftmost sufficient unused basket in $O(\log n)$ per fruit for larger constraints, but is unnecessary for $n\le100$.
- **Overwrite used capacities with zero:** This is a valid constant-space alternative under positive quantities, but it mutates `baskets` and differs from the source.
- **Capacity exactly equal to quantity:** The `>=` condition correctly accepts the basket.
- **Several sufficient baskets:** The scan and immediate `break` choose only the leftmost one.
- **Previously used large basket:** `not vis[i]` prevents it from being selected again.
- **No sufficient basket:** No decrement occurs, so that fruit remains included in `ans`.
- **All fruits placed:** `ans` is decremented $n$ times and returns zero.
- **No fruits placed:** `ans` remains its initial value $n$.
- **Duplicate fruit quantities or capacities:** Positions remain distinct, and visited flags track each basket separately.
- **Input preservation:** The capacity list retains all original values because usage is recorded only in `vis`.
