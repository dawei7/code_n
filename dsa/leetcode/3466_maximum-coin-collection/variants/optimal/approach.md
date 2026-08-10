## General

**Represent every future choice with three state values.** The protected source defines `dfs(i, j, k)` as the maximum total obtainable when Mario is at mile `i`, is currently positioned in lane `j`, and has `k` switches remaining. Lane zero means `lane1` and lane one means `lane2`. The initial calls always use lane zero and two remaining switches because Mario enters on lane 1.

The state does not store the entry mile or accumulated total. Once Mario reaches the same mile, lane, and remaining switch count, the best future earnings are identical regardless of the earlier path. Returning a future total makes those equivalent suffixes shareable through `@cache`.

When `i >= n`, no miles remain, so the suffix contributes zero. For an in-range state, `x` is the coin gain or toll at the current mile in the current lane.

**Driving the current mile offers an immediate stopping choice.** The first recurrence is

`ans = max(x, dfs(i + 1, j, k) + x)`.

The `x` option drives this one mile and exits. It is essential when every continuation is negative, and it guarantees that a chosen trip need not continue to the freeway's end. The second option drives the mile, remains in the same lane, and considers mile `i+1` with the same switch budget.

This is the Kadane-style part of the recurrence: at each state, either stop the current contiguous trip or extend it. It never skips an interior mile. The outer loop, rather than the recurrence, chooses where the trip begins.

**A switch can occur on either side of the current mile.** If `k > 0`, the code considers two more transitions:

`dfs(i + 1, j ^ 1, k - 1) + x`

drives mile `i` in the current lane, then reaches the next mile in the other lane. In contrast,

`dfs(i, j ^ 1, k - 1)`

switches immediately and evaluates the same mile in the other lane. `j ^ 1` toggles zero and one.

Both forms are needed to express the statement's boundary timing cleanly. The same-mile switch allows Mario to enter the freeway on lane 1 and immediately switch before collecting the first chosen mile in lane 2. It also permits a switch at any boundary before the current mile. The after-driving form attaches the current mile to the old lane before changing the lane for what follows.

The switch budget strictly decreases on same-mile transitions, so recursion cannot alternate lanes forever without advancing. It may represent two immediate switches at the same location, but that returns to the original lane after wasting the budget and cannot improve over simply not taking those switches. Such redundant paths do not affect the maximum.

**Try every legal entry mile.** The outer loop computes `dfs(i, 0, 2)` for every `i` and keeps the maximum. Thus Mario may begin at any mile while satisfying the rule that his initial lane state is lane 1. From that state he can immediately switch to lane 2 if beneficial, as in the all-negative-lane-1 example.

Initializing the global answer to negative infinity matters. Mario must travel at least one mile, so returning zero merely because every option is negative would be wrong. Every in-range `dfs` path eventually includes some `x` before it can stop; therefore, the final answer is the best nonempty trip. For `lane1 = [-10]` and `lane2 = [-2]`, the start state can immediately switch and take $-2$, which correctly beats taking $-10$ but does not invent an empty zero-profit trip.

For the first example, a represented optimal path starts with `dfs(0, 0, 2)`, collects $1$ in lane 1, changes to lane 2 for miles one and two, then changes back to lane 1 for mile three. The recurrence totals $1+10+0+3=14$. Stopping alternatives at every occupied state ensure it exits exactly where continuing would cease to help.

**Why every valid trip appears in the recurrence.** A legal trip chooses a starting mile, a lane for each mile of one contiguous interval, and at most two boundaries where that lane changes. The outer loop enumerates its start. At each driven mile, the recurrence can stay in the same lane or use one switch to change before the next mile; an immediate first switch covers a lane-2 start. At the trip's final mile, the `x` branch exits. Therefore, the recursion contains a transition sequence matching every legal trip.

Conversely, every recurrence path starts from lane 1, consumes at least one mile before producing a final value, advances through consecutive miles, toggles lanes only while decrementing `k`, and uses no more than two switches. It therefore represents a legal trip. Maximizing over exactly this set proves the returned coin total is optimal.

**The protected source differs materially from the manifest summary.** The manifest describes an iterative three-state Kadane recurrence with $O(1)$ space. The protected code is a top-down cached search over mile, lane, and remaining-switch states. Its recurrence captures the same optimization idea, but caching and recursion consume linear memory. More importantly, a path can recurse through up to $n$ miles, while Python's default recursion limit is far below the stated $n=10^5$. Without an external recursion-limit change that is not present in this source, sufficiently long inputs can raise `RecursionError`. This is a genuine operational defect in the protected implementation even though the recurrence is mathematically correct.

## Complexity detail

There are at most $n\cdot2\cdot3=6n$ distinct tuples `(i, j, k)`, plus constant-size base states. Caching computes each state once, and each computation performs a constant number of comparisons and recursive lookups. The outer loop's calls reuse that cache. Total algorithmic time is $O(n)$, matching the manifest's time bound.

The cache stores $O(n)$ values. The recursion stack can also reach $O(n)$ depth when a path continues through many miles, with at most two additional same-index switch frames. Exact auxiliary space is therefore $O(n)$, not the manifest's $O(1)$.

An iterative formulation can maintain only the constant number of lane/switch totals needed at the current mile and would achieve the advertised $O(1)$ auxiliary space while avoiding recursion depth. That is a different implementation; it should not be attributed to this protected file.

## Alternatives and edge cases

- **Ordinary one-lane Kadane:** It cannot represent gains obtained by moving between the two lane arrays.
- **Enumerate both switch positions:** Trying all start, end, and switch boundaries leads to a prohibitively large polynomial search.
- **Iterative constant-state DP:** This is the safer production approach for $n=10^5$ and matches the manifest summary, but it is not what the protected source executes.
- **Always continue when a suffix is positive overall:** The recurrence must compare stopping now with continuing because the next segment can reduce the total.
- **Immediate switch at entry:** The same-index lane-toggle transition permits beginning the driven portion in lane 2 while still modeling entry on lane 1.
- **At most two switches:** The trip may use zero, one, or two; no transition forces the budget to be exhausted.
- **Switch just before exit:** Such a switch changes no collected mile and cannot improve the sum, so omitting a special exit-only action does not change the optimum.
- **All values negative:** Negative-infinity initialization and the one-mile `x` option return the least harmful legal mile rather than zero.
- **Single mile:** The recursion chooses the better of driving it in lane 1 or switching immediately and driving it in lane 2.
- **Ties and zero values:** `max` may choose any equal-valued path; only the maximum coin count is returned.
- **Large coin magnitudes:** Python integers do not overflow when totals exceed fixed-width integer ranges.
- **Recursion depth:** The stated maximum length can exceed Python's call-stack limit, so the exact protected source is not robust over the full declared domain without an iterative rewrite or environment adjustment.
- **Input preservation:** The arrays are read but never mutated; cached states store totals only.
