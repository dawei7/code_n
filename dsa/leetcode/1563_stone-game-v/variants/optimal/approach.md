## General

**Treat every surviving row as an interval**

After any round, the remaining stones are still contiguous in the original array. A game state is therefore completely identified by inclusive endpoints `i` and `j`.

`dfs(i, j)` returns the maximum additional score Alice can obtain when the current row is `stoneValue[i:j+1]`.

If `i >= j`, at most one stone remains. No split into two nonempty rows is possible, so the additional score is zero.

The `@cache` decorator memoizes each interval result because many different first-split choices can lead to the same surviving interval.

**Compute split sums incrementally**

Prefix sums `s` are built with an initial zero. The total value of interval `[i,j]` is `s[j+1] - s[i]`.

At the start of a state, `l = 0` and `r` is the whole interval sum. As split index `k` moves from `i` through `j-1`, the source adds `stoneValue[k]` to `l` and subtracts it from `r`.

After those updates:

- `l` is the sum from `i` through `k`.
- `r` is the sum from `k+1` through `j`.

Both sides are nonempty because the final possible `k` is `j-1`.

**Follow Bob's forced choice**

If `l < r`, Bob discards the larger right row. Alice gains `l`, and the next state is the retained left interval `dfs(i, k)`.

The candidate total is `l + dfs(i, k)`.

If `l > r`, Bob discards the left row. Alice gains `r` and continues with `dfs(k+1, j)`.

If the sums are equal, Alice may choose which row survives. The source evaluates both candidates and keeps the larger:

`max(l + dfs(i, k), r + dfs(k + 1, j))`.

The state answer is the maximum candidate over all legal first split positions.

**Why this recurrence is complete**

Every strategy from interval `[i,j]` begins by selecting one of the split indices enumerated by the loop.

Once that split is chosen, Bob's rule uniquely determines the survivor unless sums tie. In a tie, evaluating both allowed survivors covers Alice's freedom.

The future game depends only on the surviving interval, and `dfs` supplies its optimal continuation. Thus each candidate is the best score conditional on that first split, and maximizing over splits gives the optimal state value.

Induction on interval length proves correctness from the one-stone base case upward.

**Understand the continue pruning**

All stone values are positive. The maximum future score obtainable from an interval of total value `l` is bounded above by `l`: every future gain comes from nested retained portions whose scoring potential is limited by the current retained mass.

Therefore a left-retained candidate `l + dfs(i,k)` is at most `2*l`.

When `l < r` and current `ans >= l * 2`, this particular split cannot improve the answer, so the source skips its recursive call with `continue`.

It cannot stop the loop entirely because `l` increases as `k` moves right. Later left-side upper bounds may be larger.

**Understand the break pruning**

When `l > r`, the right side is retained. Its candidate is at most `2*r`.

As `k` moves farther right, positive values transfer from `r` to `l`, so `r` only decreases. Once `ans >= r * 2`, neither this split nor any later right-retained split can beat `ans`.

The source can safely `break` out of the remaining split loop.

These tests reduce many recursive evaluations and loop iterations in practice without changing the set of candidates capable of improving the answer.

**Tracing the first decision in the example**

For values six, two, three, four, five, five, splitting after the third stone gives left sum eleven and right sum fourteen.

The left side is smaller, so Bob removes the right side. Alice scores eleven and continues on interval six, two, three.

The recurrence adds that interval's optimal future score, eventually reaching the stated total eighteen.

Other split positions are evaluated or pruned according to the same exact upper bounds.

**The custom max function**

The file defines a two-argument `max(a,b)` helper that returns the larger integer. Calls inside the solution therefore use this custom function rather than Python's variadic built-in.

Every call supplies exactly two arguments, so behavior matches the needed pairwise maximum. Nested calls handle the equal-sum comparison of two continuation candidates.

**Why prefix sums still matter**

The source already updates `l` and `r` incrementally within one interval. Prefix sums provide the initial interval total in constant time for every memoized state.

Without them, each state would first rescan its stones merely to initialize `r`, adding avoidable work.

## Complexity detail

There are $O(N^2)$ distinct intervals, and caching ensures each is solved at most once. However, the exact source may scan $O(N)$ split positions within one interval.

Its safe worst-case upper bound is therefore $O(N^3)$ time. The `continue` and `break` pruning can greatly reduce actual work, but they do not establish that every one of the $O(N^2)$ states examines only constant amortized splits for all inputs.

The manifest's $O(N^2)$ time describes the stronger optimized Stone Game V interval DP that maintains prefix and suffix best values to avoid scanning every split for every interval; it is not the plain worst-case bound of this exact memoized loop.

The cache can store $O(N^2)$ state values. Prefix sums use $O(N)$, and recursion depth is at most $O(N)$. Total auxiliary space is $O(N^2)$, matching the manifest's space bound.

## Alternatives and edge cases

- **Bottom-up cubic interval DP:** Fill the same recurrence by increasing interval length; it has the same safe $O(N^3)$ time without recursion.
- **Quadratic optimized DP:** Maintain best attainable prefix and suffix expressions around each balance point to realize the manifest's $O(N^2)$ time.
- **Enumerate complete game trees:** It repeats overlapping intervals exponentially and is infeasible.
- **One stone:** No split exists, so score is zero.
- **Two stones:** There is one split; Alice gains the smaller value, or that value when equal.
- **Equal side sums:** Alice chooses the continuation with the larger future score.
- **Strictly smaller left side:** Only the left interval may survive under Bob's rule.
- **Strictly smaller right side:** Only the right interval may survive.
- **Positive values:** They make `l` increase and `r` decrease, which is essential for the pruning arguments.
- **Continue versus break:** A pruned left split cannot justify stopping because later `l` grows; a pruned right split can stop because later `r` shrinks.
- **Cached intervals:** Repeated requests return immediately, but the first computation still loops over splits.
- **Prefix-sum initial zero:** It makes inclusive interval total `s[j+1]-s[i]` work at every boundary.
- **Runtime imports:** The exact source expects `cache`, `accumulate`, and `List` to be supplied by its execution environment.
