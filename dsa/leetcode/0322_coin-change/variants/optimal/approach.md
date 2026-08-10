## General

**Why this is an optimization problem, not a greedy counting problem.**

For a target `amount`, many different combinations of denominations may produce the same total, and the task asks for the combination with the fewest coins. Taking the largest coin whenever possible is not reliable for arbitrary denominations. With `coins = [1,3,4]` and `amount = 6`, greedy selection takes `4 + 1 + 1`, which uses three coins, while `3 + 3` uses only two. A correct method must compare the possibilities created by every denomination.

The problem has useful optimal substructure. If an optimal combination for total $j$ uses a coin worth $x$, removing one copy of that coin leaves a combination for $j-x$. That remaining combination must itself use the minimum possible number of allowed coins. If it did not, replacing it with a better combination would improve the solution for $j$, contradicting optimality.

The exact source turns this observation into a two-dimensional dynamic program. The extra dimension makes the unlimited-use rule explicit and also gives a clean way to prove that every denomination choice has been considered.

**Define the state precisely.**

Let $c$ be the number of denominations and let $A$ be `amount`. The table `f` has `c + 1` rows and `A + 1` columns. Its state means:

$$
f[i][j] = \text{the minimum number of coins needed to make total } j
\text{ using only the first } i \text{ denominations}.
$$

The word “only” is essential. Row `i` may use `coins[0]` through `coins[i - 1]`, each any number of times, but it may not use later denominations. When the algorithm finishes row $i$, it has solved every target from `0` through $A$ under exactly that set of allowed coin types.

Every cell initially contains infinity. Infinity is a sentinel meaning “this total has not been shown reachable.” With zero denominations, total zero is possible using zero coins, so the source sets

$$
f[0][0] = 0.
$$

Every positive total in row zero correctly remains unreachable because no coins are available. As later rows are filled, column zero is copied forward as zero: the empty selection always makes amount zero, regardless of how many denominations are allowed.

**Derive the two choices for one cell.**

When row $i$ is being processed, let `x` be its newly available denomination, `coins[i - 1]`. Any combination counted by `f[i][j]` falls into exactly one of two groups.

First, the combination may use no copy of `x`. Then it uses only the previous $i-1$ denominations, and its best coin count is already stored in `f[i - 1][j]`. The source begins by copying that value:

$$
f[i][j] = f[i-1][j].
$$

Second, the combination may use at least one copy of `x`. Remove one such copy. The remaining coins must make total $j-x$ while still being allowed to use all first $i$ denominations, including `x` again. Its candidate count is therefore

$$
f[i][j-x] + 1.
$$

This choice is legal only when $j \ge x$. The transition takes the smaller of the exclude and include candidates:

$$
f[i][j] = \min\bigl(f[i-1][j],\ f[i][j-x]+1\bigr).
$$

Notice that the include candidate reads from the current row, not the previous row. This is exactly how the source represents an unlimited supply. After using one `x`, the subproblem may use `x` again. If the transition used `f[i - 1][j - x]`, each denomination could be selected at most once, which would solve a different problem.

**Why totals are processed from small to large.**

For a positive coin value $x$, the dependency $j-x$ is strictly smaller than $j$. The inner loop visits `j` in increasing order from `0` to $A$, so `f[i][j - x]` is already final for the current row by the time it is read. This permits repeated copies: `f[i][x]` can use one `x`, `f[i][2x]` can build on that state to use two, and so on.

If the current-row loop ran backward, `f[i][j-x]` might not yet include the current denomination, and the behavior would resemble a one-use, zero-one knapsack update. Loop direction is therefore part of the algorithm's meaning, not merely an implementation preference.

Infinity also behaves safely in the recurrence. If `j - x` is unreachable, then adding one to its infinity sentinel still does not form a finite candidate. The algorithm cannot accidentally claim that an unreachable remainder becomes reachable.

**Walk through the target `11`.**

For `coins = [1,2,5]`, the row for denomination `1` can make every total $j$ using exactly $j$ coins. When denomination `2` is introduced, even totals improve by using twos, while odd totals use some twos plus one `1`. For example, total `6` becomes three coins: `2 + 2 + 2`.

When denomination `5` is processed, the cell for total `10` can build from the current-row cell for total `5`, producing `5 + 5` with two coins. Then total `11` considers using one more `5` on top of the best solution for `6`. At this point `f[i][6]` is two coins, `5 + 1`, so the include candidate for `11` is three coins, `5 + 5 + 1`. The table compares that against the best result without denomination `5` and keeps three.

**Why the final value is correct.**

Use induction over rows and, within a row, increasing totals. The base row is correct: only total zero can be made with no denominations. Assume the earlier row is correct and the smaller totals of the current row are correct. Every combination for `f[i][j]` either uses no current coin, placing it in the exclude case, or uses at least one, placing it in the include case after one copy is removed. The transition evaluates the optimum of both exhaustive, disjoint cases. Its referenced states are correct by the induction assumptions, so the chosen minimum is correct.

After all $c$ rows, `f[c][A]` allows every supplied denomination and therefore represents the requested optimum. If it is still infinity, no combination exists and the method returns `-1`; otherwise, it returns the finite minimum coin count.

## Complexity detail

Let $c$ be `len(coins)` and $A$ be `amount`. The algorithm fills $(c+1)(A+1)$ table cells, and each cell performs only constant-time comparisons, indexing, and arithmetic. Its time complexity is $O(cA)$.

The exact optimal source allocates the complete two-dimensional table, so its auxiliary space complexity is $O(cA)$. Each of the $c+1$ rows contains $A+1$ values. The variant manifest lists $O(A)$ space, which would describe the standard one-dimensional compression, but that compression is not present in this source. An explanation of the checked-in implementation must therefore distinguish its actual $O(cA)$ allocation from the manifest's tighter claim.

No recursion is used. The infinity sentinel is a constant representation detail and does not alter the asymptotic bounds.

## Alternatives and edge cases

- **One-dimensional bottom-up DP:** Keep `dp[j]` as the best count for total `j`, then for each denomination scan `j` upward from that coin value to $A$. This uses $O(A)$ space and the same $O(cA)$ time. It is a valid optimization because the current row only needs the previous-row value at `j` and the current-row value at `j-x`; however, it is not what the exact source allocates.

- **Amount-first one-dimensional DP:** For every total from `1` through $A$, try each denomination as the final coin. This also takes $O(cA)$ time and $O(A)$ space. It derives directly from the last-coin recurrence and allows unlimited reuse because all smaller totals are already known.

- **Top-down memoization:** Recursively try subtracting each coin and cache the answer for each remaining amount. It has the same $O(cA)$ state-transition bound, but adds recursion overhead and can create a deep call stack when small denominations are present.

- **Breadth-first search over totals:** Treat each reachable total as a node and adding one coin as an edge. BFS reaches the target with the fewest edges, hence the fewest coins. It is correct but usually less direct than the array DP and still explores up to $A+1$ totals with $c$ outgoing choices each.

- **Greedy largest denomination:** This is correct for some specially structured currency systems but not for arbitrary input denominations. The `[1,3,4]`, target `6` counterexample shows why the dynamic program is needed.

- **`amount = 0`:** The empty collection uses zero coins. Column zero remains `0` through every row, so the function returns `0` without a special branch.

- **Unreachable target:** With `coins = [2]` and `amount = 3`, no transition reaches total `3`. The final cell remains infinity and is converted to `-1`.

- **Coin larger than the target:** If `x > A`, the condition `j >= x` is never true. Its entire row simply copies the preceding row, correctly showing that this denomination cannot participate.

- **Repeated denominations:** Duplicate coin values may repeat a row's work but do not change the minimum. Unlimited copies were already available when that value first appeared.

- **Positive denominations:** The contract guarantees every coin is at least `1`. This ensures `j-x < j`, makes the increasing-order dependency well founded, and avoids a zero-value coin that could be selected infinitely without changing the total.
