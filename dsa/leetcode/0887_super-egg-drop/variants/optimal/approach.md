## General

The exact solution uses minimax dynamic programming. “Minimax” is necessary because every drop has two possible outcomes, and the strategy must succeed with certainty in the worse of those outcomes.

Define `dfs(i, j)` as the minimum number of additional moves needed when there are `i` candidate floors in the current unknown interval and `j` unbroken eggs available. The actual floor labels do not matter; only the number of consecutive possibilities matters.

**Base cases.**

- If `i < 1`, there are no floors left to distinguish, so zero moves are needed.
- If `j == 1`, only one egg remains. The safe guaranteed strategy is to test floors from bottom to top, requiring `i` moves in the worst case. A higher first drop could break the last egg and leave unresolved lower possibilities.

**Drop at relative floor `mid`.** There are two outcomes:

1. The egg breaks. The threshold lies below that floor. There are `mid - 1` lower floors to resolve and only `j - 1` eggs, costing `dfs(mid - 1, j - 1)` further moves.
2. The egg survives. The threshold is at or above that floor. There are `i - mid` higher floors still to resolve and all `j` eggs remain, costing `dfs(i - mid, j)` further moves.

The strategy must cover both outcomes, so a drop at `mid` costs

$$
1+\max\bigl(
\text{dfs}(\text{mid}-1,j-1),
\text{dfs}(i-\text{mid},j)
\bigr).
$$

The leading one counts the current drop. The best drop minimizes this worst-case quantity.

**Why binary search can locate the best drop.** As `mid` moves upward, the break-side subproblem contains more floors, so

$$
A(\text{mid})=\text{dfs}(\text{mid}-1,j-1)
$$

is nondecreasing. At the same time, the survive-side subproblem contains fewer floors, so

$$
B(\text{mid})=\text{dfs}(i-\text{mid},j)
$$

is nonincreasing.

The maximum of these two functions is minimized near the place where they cross. Far below the crossing, the survive case dominates and moving upward can reduce it. Far above the crossing, the break case dominates and moving farther upward can only worsen it.

The loop searches for the largest `mid` at which `A(mid) <= B(mid)`. It uses an upper midpoint so that assigning `l = mid` always makes progress. When the condition reverses, it moves `r` left. At convergence, `l` lies at the balance boundary, and the solution returns one plus the worse of its two outcome costs.

**Memoization is what makes recursive evaluation practical.** Many candidate drops ask about identical pairs of remaining floors and eggs. The `@cache` decorator stores every computed `dfs(i,j)` result. Later requests for the same state reuse it rather than rebuilding an exponential decision tree.

**Why the recurrence determines the global guarantee.** For each possible first drop, the maximum chooses the more expensive physical outcome, modeling the certainty requirement. The binary-searched choice selects the first drop with the smallest such worst case. By induction, recursive values already use optimal guaranteed strategies for the smaller subproblems. Therefore the full `dfs(n,k)` is the minimum number of moves sufficient in the worst case.

For one egg and two floors, the base directly returns two. For two eggs and six floors, a balanced sequence can resolve the threshold in three moves, and the recurrence finds that no two-move decision tree can cover all seven possible threshold values $f=0$ through $6$.

**Distinguish this code from the mathematical editorial method.** Another formulation asks how many floors can be distinguished with a fixed number of moves and eggs. Its recurrence can be compressed to $O(k)$ storage and reaches $O(k\log n)$ time. The local manifest's $O(k\log n)$ time and $O(1)$ space describe that style at a high level.

The exact `solution.py` instead memoizes floor-count/egg-count states and performs a binary search inside each visited state. Its complexity must be reported from that executed recurrence, not from the separate mathematical solution.

## Complexity detail

There are at most $nk$ meaningful cached states $(i,j)$. For each non-base state, the internal binary search performs $O(\log i)$ cached recursive queries and comparisons.

- **Time complexity of the exact solution:** $O(kn\log n)$ in the standard worst-case state accounting.
- **Space complexity of the exact solution:** $O(kn)$ for memoized results, plus recursion stack space.

The manifest's $O(k\log n)$ time and $O(1)$ space do not match this cached minimax implementation. A moves-based coverage recurrence is required to obtain the advertised faster bound; depending on its implementation, it normally uses at least $O(k)$ working storage rather than literal constant space when $k$ is variable.

## Alternatives and edge cases

- **Moves-versus-eggs coverage DP:** After $m$ moves with $e$ eggs, compute how many floors can be distinguished and stop once coverage reaches `n`. This is the common $O(k\log n)$ approach and avoids the $n\times k$ memo table.
- **Try every drop floor in every state:** The direct minimax recurrence is correct but costs $O(kn^2)$ time. Binary search exploits the opposing monotonic branches.
- **Naive recursion without cache:** Repeated subproblems create exponential work.
- **Ordinary binary search with unlimited eggs:** Breaking an egg reduces future options, so simple halving is not always achievable when eggs are scarce.
- **One egg:** Floors must be tested sequentially from bottom upward, giving exactly `n` moves.
- **One floor:** One drop distinguishes whether the threshold is below or at that floor.
- **More eggs than useful levels:** Extra eggs cannot reduce the information-theoretic decision depth below what the outcome tree allows.
- **Break outcome:** The tested floor itself is known to be above `f` and is excluded; only `mid - 1` lower floors remain.
- **Survive outcome:** The tested floor is known safe and is excluded; only `i - mid` higher floors remain.
- **Worst-case guarantee:** Taking the minimum of the two outcomes would model luck, not certainty. The recurrence must take their maximum.
- **Manifest mismatch:** The approach should not label cached interval-state execution as $O(k\log n)$ or constant-space merely because a different editorial method achieves those bounds.
