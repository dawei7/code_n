## General

**Track only distance and remaining steps**

Absolute positions are unnecessary. From any current position, future possibilities depend only on its distance from `endPos` and how many steps remain. Shifting the entire number line does not change the number of left/right step sequences.

The initial distance is:

$$
d=\lvert\texttt{startPos}-\texttt{endPos}\rvert.
$$

The helper `dfs(i, j)` returns the number of step sequences that reach distance zero after exactly `j` more steps when the current distance is `i`.

**Describe both one-step choices by distance**

When `i > 0`, one physical direction moves toward the target and changes distance to `i - 1`; the other moves away and changes it to `i + 1`.

The transition uses:

```python
dfs(i + 1, j - 1) + dfs(abs(i - 1), j - 1)
```

The absolute value is important at `i = 0`. From the target, a left step and a right step both create distance one. They are still two different ways because their step directions differ. At `i = 0`, both recursive terms become `dfs(1, j - 1)`, so the addition counts the two distinct physical moves separately.

This distance compression does not accidentally merge their multiplicity; identical next states appear twice in the sum.

**Reject states that cannot close the distance**

If `i > j`, fewer steps remain than the current distance. Even moving toward the target on every step cannot reach zero, so the helper returns zero immediately.

The check `j < 0` is a defensive invalid-state boundary. Normal transitions from a positive `j` reach zero exactly before going negative, but the condition makes the helper definition complete.

When `j == 0`, exactly zero steps remain. There is one valid continuation—the empty step sequence—if and only if `i == 0`. Otherwise, there is no way to change position, so the count is zero.

**Why exact steps differ from shortest distance**

Reaching the target early is not enough. If extra steps remain, the walker must spend them in pairs that leave and return. The recurrence continues from distance zero rather than treating it as an immediate success, correctly counting those detours.

For example, from position one to two in three steps, initial distance is one. One step could reach the target, but two steps still remain. The distance-zero transition counts a left-right or right-left excursion as distinct sequences where appropriate.

**Memoize repeated states**

Many direction prefixes lead to the same pair `(i, j)`. From that point onward, their number of valid completions is identical. `@cache` stores each state result, converting an exponential recursion tree into a dynamic program.

Counts are added modulo:

$$
10^9+7
$$

at every transition. Modular addition preserves the final required remainder and prevents intermediate counts from growing unnecessarily large.

**Trace the three-step example**

Starting at one and targeting two gives distance one with three steps. Valid direction sequences contain two moves toward the right overall and one left move. The left move can appear first, second, or third, producing three orders.

The distance recursion discovers the same multiplicity through its branches. Whenever distance reaches zero with steps remaining, its two equal-distance outgoing states are added separately, preserving different directions.

**Why the recurrence is correct**

Every valid length-`j` sequence from distance `i` begins with exactly one of two physical directions. Those choices lead to distances `i+1` and `abs(i-1)` and leave `j-1` steps. The two sets of sequences are disjoint because their first directions differ, even if their next distance is equal at zero. Adding recursive counts therefore counts every valid sequence exactly once.

The base case correctly recognizes exact completion, and impossible-distance pruning removes no feasible sequence. Induction on remaining steps proves `dfs(i,j)` is exact. Calling it with the initial absolute distance and `k` yields the requested count.

**Exact source versus the manifest formula**

The manifest describes solving for the required number of right steps and evaluating a binomial coefficient in $O(k)$ time. The source instead explores cached distance-step states. Both methods are correct, but their runtime and state are different. The binomial method is presented as an alternative rather than attributed to this recursion.

## Complexity detail

For remaining steps `j`, only distances `0` through `j` survive the `i > j` check. Across `j = 0` through `k`, there are $O(k^2)$ relevant cached pairs. Each does constant work beyond cached calls, so exact time is $O(k^2)$.

The cache stores $O(k^2)$ integers, and recursive depth is at most $k$. Exact auxiliary space is $O(k^2)$, not the manifest's $O(1)$ combinatorial bound.

The initial distance can exceed `k`, but that root returns immediately. Otherwise, all explored feasible distances remain bounded by remaining-step layers.

## Alternatives and edge cases

- **Binomial coefficient:** Let displacement be `endPos - startPos`. Solve `R + L = k` and `R - L = displacement`, then return $\binom{k}{R}$ when `R` is an integer in range. This achieves $O(k)$ time and $O(1)$ extra space with iterative combinations.
- **Bottom-up DP by position:** Update counts across reachable positions for each step. It avoids recursion but still uses $O(k^2)$ work.
- **Distance greater than `k`:** The target is unreachable and the first pruning check returns zero.
- **Parity mismatch:** If distance and `k` have different parity, no exact-step path exists; recursion derives zero even without an explicit parity test.
- **Start equals end:** Extra steps must cancel in pairs; at distance zero the two physical directions are counted separately.
- **Exactly shortest-path steps:** All moves must head toward the target, giving one way.
- **Negative number-line positions:** Absolute distance makes translation and sign irrelevant.
- **Modulo:** Every addition is reduced, so the cached counts already store required remainders.
