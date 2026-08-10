## General

**Viewing the rope as maximal same-color runs**

The rope is invalid wherever two adjacent balloons have the same color. Instead of deciding about every adjacent pair separately, the implementation groups consecutive equal colors into maximal runs. A run begins at index `i` and extends through every following index whose color equals `colors[i]`. The first different color, at index `j`, ends that run, so the run occupies the half-open interval `[i, j)`.

This grouping turns the global-looking deletion task into independent local decisions. A run of length one already causes no duplicate-color adjacency. A run of length $L>1$ must lose enough balloons that only one of those $L$ balloons remains. Keeping two balloons from the same original run would leave them adjacent after the balloons between them were removed, and their colors would still match.

Because every removal time is positive, there is no benefit to deleting the final balloon of a run as well. One balloon is sufficient to represent that color without causing an internal conflict, and retaining it avoids an additional positive cost. Therefore, every nontrivial run has one precise optimization problem: choose which single balloon to keep.

**Why the most expensive balloon is kept**

Suppose the removal times in one run sum to `s`. If the balloon with removal time `t` is kept, every other balloon in the run is removed, for a cost of `s - t`. Since `s` is fixed for that run, minimizing `s - t` is equivalent to maximizing `t`. The optimal choice is therefore to keep a balloon whose removal time is the run maximum `mx` and pay `s - mx`.

This explains both accumulators in the inner loop. For every position in the run, the code adds `neededTime[j]` to `s`. It also updates `mx` when the current removal time is larger. Once `j` reaches a different color or the end of the string, `s - mx` is exactly the minimum necessary cost for this run.

The branch `if j - i > 1` adds that amount only for a run containing at least two balloons. For a singleton, `s` and `mx` are equal, so `s - mx` would already be zero. The branch is not required mathematically, but it makes the intention explicit: only repeated-color runs need removals.

**How the two pointers cover the input**

The outer pointer `i` marks the first unprocessed balloon. At the start of each outer iteration, `j` is initialized to `i`, and `s` and `mx` are reset to zero. The inner loop advances `j` while `colors[j] == colors[i]`, so it consumes exactly one maximal run.

After charging that run’s optimal deletion cost, the assignment `i = j` moves directly to the first balloon of the next run. No index is skipped: `j` stops precisely at the first unprocessed different color. No index is processed twice by the inner loops: once `i` moves to `j`, the completed run is never revisited.

For example, consider colors `"abaac"` with removal times `[1, 2, 3, 4, 5]`. The first run is the single `a` at index zero and costs zero. The next is the single `b` and also costs zero. The run `"aa"` has total time seven and maximum time four, so removing the time-three balloon costs three. The final `c` costs zero. The total answer is three.

For a longer run such as color sequence `"bbbb"` with times `[4, 1, 7, 3]`, the total is fifteen and the maximum is seven. The algorithm keeps the time-seven balloon and removes the other three for eight. Any other retained balloon costs more: keeping time four costs eleven, keeping time three costs twelve, and keeping time one costs fourteen.

**Why different runs can be optimized independently**

A potential concern is that deleting balloons might bring formerly separated balloons together. For maximal runs, that does not create a hidden interaction. Two consecutive runs have different colors by definition. The algorithm keeps exactly one balloon from each run. After internal deletions, the kept balloon from one run may become adjacent to the kept balloon from the next run, but their colors are different, so that boundary remains valid.

Runs that are farther apart cannot become adjacent without deleting every balloon from an intervening run. The optimal rule never deletes an entire run because removal times are positive and keeping one balloon is both valid and cheaper. Thus the original sequence of run colors remains present in the same order.

Every valid final rope must remove at least $L-1$ balloons from a run of length $L$, so it must pay the sum of all run times except the time of at most one retained balloon. The largest possible saving is the maximum removal time. The algorithm attains that lower bound independently in every run. Adding those per-run minima therefore gives the minimum total time for the entire rope.

**What the variables mean**

The variable `ans` accumulates the optimal costs of fully processed runs. The outer-loop invariant is that all indices before `i` have been resolved into a valid colorful prefix at minimum possible removal cost, while index `i` begins the next maximal run. During the inner loop, `s` is the sum and `mx` is the maximum over precisely the portion `[i, j)` already scanned. When the loop ends, those summaries cover the whole run, so adding `s - mx` preserves the invariant for the expanded processed prefix.

This formulation needs no mutation of `colors` or `neededTime`. It calculates the cost alone, which is all the problem requests.

## Complexity detail

Let $N$ be the number of balloons. Although there is a loop nested inside another loop, the execution is linear. The pointer `j` moves forward across each balloon once while discovering its run. The outer pointer `i` then jumps to `j`; it does not cause those balloons to be scanned again. Each index contributes one addition, one maximum comparison, and constant-time color comparisons.

The total time complexity is therefore $O(N)$. Thinking of it as $O(N^2)$ merely because the loops are syntactically nested would ignore that their pointer ranges do not restart over the same suffix for each index.

The algorithm uses a fixed collection of scalar variables: `ans`, `i`, `j`, `s`, `mx`, and `n`. It creates no array, stack, map, or modified copy proportional to the input. Its auxiliary space complexity is $O(1)$. The input string and list are read-only and are not counted as newly allocated auxiliary storage.

## Alternatives and edge cases

- **Greedy deletion of the cheaper adjacent balloon:** Scanning adjacent conflicts and removing the cheaper of the two can also be made linear, provided the surviving balloon’s time is carried forward correctly across a long run. The run-sum formulation is often easier to verify because it handles the entire group with the direct formula `sum - maximum`.
- **Physically deleting from arrays:** Removing characters or list elements while scanning complicates indices and can make an implementation quadratic because later elements shift. Only the minimum cost is required, so physical simulation is unnecessary.
- **Dynamic programming:** A state describing which previous balloon was kept can solve the problem, but maximal runs eliminate the need for cross-position state. Each run has the closed-form optimum `s - mx`.
- **Sorting each run:** Sorting could identify the largest removal time, but a single scan finds both the sum and maximum. Sorting adds $O(L\log L)$ time and storage for a run of length $L$ without improving the decision.
- **All colors distinct:** Every maximal run has length one. The algorithm adds zero for each and returns zero, as no deletion is necessary.
- **All colors identical:** There is one run spanning the whole rope. The answer is the total of all removal times minus the largest time, which keeps exactly the most expensive balloon.
- **Equal maximum times inside a run:** Any balloon tied for the maximum can be kept. The cost `s - mx` is the same, and the method does not need to remember which index wins.
- **Two-balloon run:** The formula removes the cheaper balloon because the sum minus the larger time equals the smaller time.
- **Positive removal times:** Positivity justifies keeping one balloon per run. If negative costs were permitted, deleting extra balloons could change the optimization, but that case is outside the contract.
- **Run boundary at the final index:** The inner loop stops when `j == n`, and the completed run is charged normally. The next assignment makes `i == n`, cleanly ending the outer loop.
- **Singleton run branch:** The explicit `j - i > 1` condition skips adding zero. Removing it would not change the numerical result because a singleton has `s == mx`.
- **No cross-run conflict after deletion:** Adjacent maximal runs always have different colors, and one balloon remains from each, so their new boundary cannot violate the colorful-rope condition.
