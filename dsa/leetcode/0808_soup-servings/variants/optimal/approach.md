## General

**What probability are we trying to compute?**

There are initially `n` milliliters of soup A and `n` milliliters of soup B. At every serving step, exactly one of four operations is chosen, each with probability `0.25`:

- serve 100 milliliters from A and 0 from B;
- serve 75 milliliters from A and 25 from B;
- serve 50 milliliters from A and 50 from B;
- serve 25 milliliters from A and 75 from B.

If an operation asks for more soup than remains, all of the remaining soup is served. The process ends as soon as A or B becomes empty. The requested result is

$$
\Pr(\text{A becomes empty first})
+ \frac{1}{2}\Pr(\text{A and B become empty together}).
$$

The extra one-half is important. A simultaneous finish is not counted as a complete win for A or as a complete loss; it contributes exactly half of its probability.

**Why the amounts can be measured in units of 25**

Every amount removed by every operation is a multiple of 25. Therefore, the exact milliliter value is more detailed than the recurrence needs. We can measure both soups in 25-milliliter units:

$$
m=\left\lceil\frac{n}{25}\right\rceil.
$$

The implementation computes this ceiling using `(n + 24) // 25`. Adding 24 before integer division ensures that any positive remainder rounds upward. For example, 50 becomes 2 units, while 51 becomes 3 units.

Rounding upward is faithful to the problem's “serve everything that remains” rule. Suppose only 1 milliliter remains. It is represented as one positive unit. Any serving operation that removes at least one 25-milliliter unit changes that state to zero or below, exactly representing that the final 1 milliliter has been exhausted. We do not need to remember whether the last unit contains 1, 7, or 25 milliliters because every nonzero serving amount removes all of it in any case.

After scaling, the four operations remove the following pairs of units:

- `(4, 0)`;
- `(3, 1)`;
- `(2, 2)`;
- `(1, 3)`.

This compression reduces the number of meaningful starting levels by a factor of 25 without changing the answer.

**The meaning of one dynamic-programming state**

Define `dfs(i, j)` as the required probability score when A has `i` units remaining and B has `j` units remaining. This definition already includes the half credit for a tie. Because the state stores the complete information needed to determine future behavior, its value depends only on `i` and `j`, not on the sequence of operations that reached it.

The terminal conditions follow directly from the scoring rule:

- If `i <= 0` and `j <= 0`, both soups became empty on the same operation, so the state returns `0.5`.
- If only `i <= 0`, A became empty first, so the state returns `1`.
- If only `j <= 0`, B became empty first, so the state returns `0`.

The order of these checks matters. The simultaneous-empty condition must be tested before the separate A-empty and B-empty conditions. Otherwise, a tie would accidentally receive either full credit or no credit.

For a nonterminal state, each operation is equally likely. The recurrence is therefore the average of the four possible next-state answers:

$$
\begin{aligned}
\operatorname{dfs}(i,j)=\frac14(&\operatorname{dfs}(i-4,j)
+\operatorname{dfs}(i-3,j-1)\\
&+\operatorname{dfs}(i-2,j-2)
+\operatorname{dfs}(i-1,j-3)).
\end{aligned}
$$

This is an exact application of total probability: first condition on which of the four operations is selected, then use the correct probability for the resulting state. Each branch has weight one-quarter, so their weighted sum is their arithmetic average.

**Why memoization is essential**

A plain recursive computation would revisit the same remaining amounts many times. For instance, different orders of serving operations can lead to the same pair `(i, j)`. Once the process reaches that pair, its future probability is identical regardless of the earlier order.

The `@cache` decorator stores the answer after a state is computed for the first time. Every later request for the same pair returns the stored value immediately. This changes the computation from an exponentially branching recursion into a dynamic program with at most one real calculation per reachable state.

The recursion always terminates. In each operation, A loses at least one unit, so `i` strictly decreases along every recursive edge. B never increases either. Consequently, no state can lead back to itself or form a cycle.

**A small trace for `n = 50`**

Fifty milliliters becomes `m = 2` units, so the answer starts at `dfs(2, 2)`. Consider the four equally likely operations:

- `dfs(-2, 2)`: only A is empty, contributing `1`.
- `dfs(-1, 1)`: only A is empty, contributing `1`.
- `dfs(0, 0)`: both are empty, contributing `0.5`.
- `dfs(1, -1)`: only B is empty, contributing `0`.

Their average is

$$
\frac{1+1+0.5+0}{4}=0.625.
$$

This example exposes why overshooting below zero is harmless: any nonpositive amount simply means that soup was exhausted by the latest serving. It also shows why the joint base case must return one-half.

**Why large inputs can return 1**

Every operation removes at least as much from A as from B, and three of the four operations remove strictly more from A. Over many steps, A therefore has a strong tendency to empty before B. As the equal starting amount grows, the desired probability approaches 1.

Computing the full two-dimensional dynamic program for an arbitrarily large `n` would waste time on a result that is already indistinguishable from 1 within the problem's accepted numerical tolerance. The exact implementation uses a reviewed cutoff: when `n > 4800`, it immediately returns `1`. At and below 4800, it evaluates the memoized recurrence. Because

$$
\left\lceil\frac{4800}{25}\right\rceil=192,
$$

the recursive state grid remains small. The cutoff is not part of the recurrence's mathematical definition; it is a safe numerical approximation based on the convergence of the answer toward 1. Keeping the exact comparison `n > 4800` also means that `n = 4800` still follows the recurrence, exactly as the solution specifies.

**Why the computed result is correct**

For any terminal state, the base cases return precisely the score required by the problem: one for A first, zero for B first, and one-half for a simultaneous finish. Now consider any nonterminal state. Its first random choice must be exactly one of the four listed operations. After that choice, the remaining process is the same problem on the corresponding smaller pair of amounts. By averaging the correct smaller-state values with their equal probabilities, the recurrence obtains the correct value of the current state.

Because every recursive transition decreases A, repeatedly applying this reasoning eventually reaches a terminal state. Thus, working backward from the correct base cases proves every computed state correct. Memoization changes only whether a previously computed result is reused; it does not change the recurrence or any probability. Finally, for values above the cutoff, returning 1 is within the required tolerance because the true probability has already converged sufficiently close to 1.

## Complexity detail

Let

$$
s=\min\left(\left\lceil\frac{n}{25}\right\rceil,192\right).
$$

For inputs that use the recurrence, a state is identified by a pair of remaining unit counts. There are at most `O(s^2)` relevant pairs, and memoization computes each pair only once. Each computed state performs four constant-time cache lookups and a constant amount of arithmetic. The time complexity is therefore `O(s^2)`.

The cache can store `O(s^2)` state values, so the memoization space complexity is `O(s^2)`. The active recursion depth is `O(s)` because A decreases by at least one unit on each recursive call. That call-stack cost is smaller than the quadratic cache bound, so the total auxiliary space remains `O(s^2)`.

When `n > 4800`, the early return does not construct or evaluate any recursive state. That particular execution uses `O(1)` time and `O(1)` extra space. The bounded definition of `s` captures why the implementation's worst-case work remains constant with respect to arbitrarily large input values, although the dynamic-programming portion is naturally described as quadratic in the scaled amount before the cutoff.

The arithmetic uses floating-point numbers because the answer is a probability. Every transition combines only four values by multiplication with `0.25` and addition. The accepted error tolerance, together with the large-input cutoff, makes ordinary floating-point precision sufficient.

## Alternatives and edge cases

- **Bottom-up dynamic programming:** The same recurrence can be filled iteratively in a two-dimensional table. It avoids recursion but requires careful ordering and explicit handling of negative successor indices. Top-down memoization is simpler here because it naturally visits only reachable states and maps the terminal rules directly to base cases.

- **Uncached recursion:** Recursing over the four operations without `@cache` is mathematically correct but computationally impractical. Many operation sequences merge into the same remaining-amount pair, so recomputing those states causes exponential repetition.

- **Tracking exact milliliters:** A state table indexed by individual milliliters would produce the same result, but 24 out of every 25 distinctions are irrelevant because all serving amounts are multiples of 25. Scaling by 25 is the key reduction that makes the recurrence compact.

- **Simulation:** Randomly simulating many serving sequences can estimate the probability, but its answer varies between runs and requires many trials for dependable accuracy. The memoized recurrence deterministically evaluates the probability represented by all possible operation sequences.

- **Removing the cutoff:** The recurrence remains conceptually valid for larger inputs, but its state count and recursion depth continue growing even though the answer is already extremely close to 1. The `n > 4800` shortcut gives the required accuracy with a firm practical bound on work.

- **Using an earlier arbitrary cutoff:** Returning 1 too soon can exceed the allowed error. The cutoff must be justified by the convergence tolerance; it should not be chosen merely because a round number looks convenient.

- **`n = 0`:** The scaled starting state is `dfs(0, 0)`. Both soups are already empty, so the answer is `0.5`. The joint base case handles this directly.

- **Amounts not divisible by 25:** Ceiling division is necessary. Flooring would turn a positive remainder into zero units and could falsely claim that a soup is empty before any operation occurs.

- **Serving more than remains:** Negative state coordinates are expected and valid. They mean that the operation exhausted the available soup. The `<= 0` base checks correctly treat zero and every negative value as empty.

- **A simultaneous finish:** The condition where both coordinates are nonpositive must be checked first and must contribute `0.5`. Testing A alone first would incorrectly turn every tie into a full A-first result.

- **The cutoff boundary:** The implementation returns 1 only when `n > 4800`. For exactly `n = 4800`, it deliberately computes `dfs(192, 192)`. Preserving this strict comparison keeps the explanation aligned with the exact solution.

- **No independence assumption:** The events “A becomes empty” and “B becomes empty” are linked by the same serving choices. The recurrence handles their joint evolution explicitly; multiplying separate marginal probabilities would be invalid.
