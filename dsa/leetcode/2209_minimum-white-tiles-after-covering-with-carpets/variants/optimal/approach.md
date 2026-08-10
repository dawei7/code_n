## General

The exact solution considers the floor from left to right. Its memoized state `dfs(i, j)` means:

> the minimum number of visible white tiles in suffix `floor[i:]` when at most `j` carpets remain available.

At the first relevant white tile, either leave it visible or start a carpet there. Memoization prevents the same suffix-and-carpet situation from being solved repeatedly.

The manifest describes a prefix DP with linear space, but the protected source is a top-down recursion whose cache can contain $O(n\cdot\texttt{numCarpets})$ states.

**Build white-tile prefix sums**

Array `s` has length `n + 1` and satisfies

`s[i + 1] = s[i] + int(floor[i] == "1")`.

Thus `s[p]` is the number of white tiles before index `p`.

The number of whites in suffix starting at `i` is `s[-1] - s[i]`. This supports an immediate base case when no carpets remain.

**Finish beyond the floor**

If `i >= n`, no tiles remain, so zero white tiles can be visible in the empty suffix.

A carpet may jump `i` beyond `n`. The same base case handles that without clipping the endpoint.

**Skip a black tile**

If `floor[i] == "0"`, the tile contributes no visible white count. The recurrence returns `dfs(i + 1, j)`.

Starting a carpet on this black tile is never necessary for optimality. Shifting such a carpet right until it begins at the next relevant white tile cannot uncover any white tile to its left—the skipped position was black—and covers at least as useful a suffix region.

Therefore the direct skip does not omit a better placement.

**Handle no remaining carpets**

If the current tile is white and `j == 0`, every white tile in the remaining suffix must stay visible.

The prefix-sum expression `s[-1] - s[i]` returns that count in constant time, avoiding a suffix scan in every state.

**Choose at a white tile**

When `floor[i]` is white and a carpet remains, there are two meaningful choices.

Leaving the tile uncovered costs one visible white plus the optimum for the next position:

`1 + dfs(i + 1, j)`.

Placing a carpet starting at `i` covers positions `i` through `i + carpetLen - 1`. No tile under it contributes, so the next uncovered position is `i + carpetLen` and one fewer carpet remains:

`dfs(i + carpetLen, j - 1)`.

Taking the minimum selects the better decision.

**Why overlap and unused carpets need no extra branch**

Overlapping a previously placed carpet covers no new tile in the overlap. Any useful portion can be represented by placing a later carpet when its first uncovered white is reached.

The recurrence may reach the end while `j > 0`, effectively leaving carpets unused. If the problem is interpreted as placing all available carpets, extra carpets can overlap already covered regions without changing visibility. Therefore “at most `j` useful carpets” has the same optimum.

**Why the recurrence is complete**

Consider an optimal arrangement for suffix `i`. If the current tile is black, its visibility cost is zero and delaying decisions is safe.

If it is white, either no carpet covers it, producing the leave-visible branch, or some carpet covers it. That carpet can be shifted so its left edge is at `i` without losing coverage of any earlier relevant suffix tile, producing the carpet branch.

These cases cover every optimum. Each branch adds the exact immediate cost and delegates the independent remaining suffix, so their minimum equals the state optimum.

**Use caching and then release it**

`@cache` keys results by both `i` and `j`. Each state is computed once; later recursive calls reuse it.

After obtaining `ans`, `dfs.cache_clear()` releases references held by this local cached function. This reduces retained memory after the call, but it does not change peak memory while the computation runs.

## Complexity detail

Let $n$ be floor length and $c$ be `numCarpets`. There are at most $O(nc)$ meaningful `(i,j)` states, and each performs constant work after prefix-sum construction. Time is $O(nc)$.

The prefix array uses $O(n)$ space. The exact memoization cache can store $O(nc)$ results, and recursion depth can reach $O(n)$. Peak auxiliary space is therefore $O(nc)$, not the manifest's $O(n)$ bound.

A bottom-up DP with rolling carpet layers can achieve $O(n)$ space. Clearing the cache after computing the answer frees cached states only after peak usage has occurred.

## Alternatives and edge cases

- **Bottom-up rolling DP:** Iterate carpet counts and floor positions with two length-$n$ rows to match the manifest's $O(n)$ space.
- **Full two-dimensional table:** It mirrors the recursive states and also uses $O(nc)$ space without recursion.
- **Greedy cover the densest window:** Locally covering the most whites can conflict with later carpet placement, so dynamic programming is needed.
- **All black tiles:** Every state skips forward and returns zero.
- **Enough total carpet length:** Carpets can cover the whole relevant floor and the answer becomes zero.
- **Carpet longer than remaining suffix:** The jump passes `n` and the base case returns zero.
- **Black starting position:** The exact recurrence never places a carpet there because shifting right is no worse.
- **No carpets left:** Prefix sums count every remaining white immediately.
- **Overlapping allowed:** It does not create a lower cost than the represented useful placements.
- **Unused carpets:** They can be ignored or placed redundantly without changing visible whites.
- **White tile decision:** The two branches exhaust covered versus uncovered outcomes.
- **Recursion depth:** With length 1000, Python's recursion limit can be close to the worst chain; an iterative version avoids that runtime concern.
- **Input preservation:** The string and carpet parameters are read only.
- **Manifest discrepancy:** The source is memoized top-down DP with $O(nc)$ peak cache space, not a linear-space rolling formulation.
