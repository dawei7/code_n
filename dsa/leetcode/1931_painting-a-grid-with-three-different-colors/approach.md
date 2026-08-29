## General

**Compress one narrow column into one state**

The grid has only $m\le5$ rows but may have up to $1000$ columns. Instead of making a state for the entire painted prefix, the solution remembers only the colors in its final column. Future legality depends only on that column because a new cell is adjacent horizontally only to the cell in the immediately previous column.

Encode red, green, and blue as ternary digits $0$, $1$, and $2$. An $m$-cell column is then represented by an integer from $0$ through $3^m-1$. Leading zero digits are significant colors, not missing positions; both helper functions explicitly extract exactly $m$ digits, so an integer with fewer written ternary digits is automatically padded with color zero at the top.

**Keep only vertically valid column states**

`f1(x)` extracts $m$ ternary digits from `x`. It remembers the previous extracted digit in `last` and rejects the state if the next digit is equal. Consecutive extracted digits represent vertically adjacent grid cells, so accepted states have no equal vertical neighbors.

The initial `last = -1` cannot equal a real color from zero through two, which lets the first digit pass without a special branch. The set

`valid = {i for i in range(mx) if f1(i)}`

contains every legal single-column coloring. There are actually $S=3\cdot2^{m-1}$ such states: the first cell has three choices, and each later cell has two choices different from the previous one.

**Precompute horizontally compatible columns**

Two vertically valid states may be placed next to one another only if their corresponding cells have different colors. `f2(x, y)` extracts one ternary digit from each state for each of the $m$ rows and rejects the pair if any two corresponding digits match.

For every valid ordered pair, the code appends `y` to `d[x]`. Compatibility is symmetric, although the dictionary stores directed adjacency entries. Precomputing it once avoids repeating $m$ digit comparisons during every one of the up to $999$ column transitions.

**Dynamic programming across columns**

The array `f` represents the number of valid colorings of the processed columns ending in each state. For the first column, every valid state has exactly one way to occur and every invalid state has zero ways, so `f[i] = int(i in valid)` is the correct base case.

For each remaining column, the solution creates a zero-filled `g`. For every possible current valid state `i`, it loops through `d[i]`. Each `j` in that list is compatible with `i` and can be the previous column. Therefore

`g[i] = sum(f[j] for j compatible with i)`.

The code applies the modulus after every addition. Once the whole transition is finished, `f = g` advances the DP by one column. Only the immediately previous array is needed; older columns cannot affect future compatibility except through their already-counted ways.

After $n-1$ transitions, `f[i]` counts full-grid colorings ending in state `i`. Every finished grid has exactly one final-column state, so `sum(f) % mod` gives the total without overlap.

**Why the recurrence is correct**

For the base column, `f1` guarantees vertical legality and there are no horizontal neighbors, so every valid state represents exactly one legal coloring.

Assume `f[j]` correctly counts all legal colorings of the first $k$ columns ending with `j`. Appending current state `i` is legal exactly when `i` is vertically valid and `f2(i, j)` says every horizontal pair differs. Each earlier coloring has one unique previous state, so adding `f[j]` over compatible states counts every legal $(k+1)$-column coloring once. No incompatible coloring is added. This proves the transition, and induction proves the final total.

## Complexity detail

Let $K=3^m$, let $S$ be the number of vertically valid states, and let $P$ be the number of compatible ordered state pairs.

Testing all ternary masks costs $O(mK)$. Testing every pair of valid states costs $O(mS^2)$ because `f2` examines $m$ digits. Each of the $n-1$ DP transitions visits the $P$ precomputed compatibility entries, costing $O(nP)$ time. The precise combined bound is $O(mK+mS^2+nP)$. Since $P\le S^2$ and $m\le5$ is a small fixed constraint, this is commonly summarized as $O(nS^2)$.

The compatibility lists store $P$ entries. The valid set uses $O(S)$ space, and each DP array has $K$ entries. Peak auxiliary space is $O(P+K)$, bounded by $O(S^2+3^m)$ and summarized as $O(S^2)$ for this state family. Only two DP layers exist at once.

## Alternatives and edge cases

- **Cell-by-cell DP:** A state can track the last $m$ cell colors while scanning cells. It reaches similar state compression but is harder to visualize than whole-column transitions.
- **Recursive generation of valid states:** Generate only the $3\cdot2^{m-1}$ vertically valid columns rather than scanning all $3^m$ masks. This reduces preprocessing constants while preserving the same DP.
- **Matrix exponentiation:** The compatibility graph is a fixed transition matrix, so exponentiation can reduce dependence on very large $n$ to logarithmic. For $n\le1000$ and a small state set, ordinary DP is simpler and efficient.
- **Brute force all cells:** Trying $3^{mn}$ colorings is exponential in the entire grid and infeasible.
- **One row:** Every ternary state is a single color and vertically valid. Adjacent columns must differ, giving $3\cdot2^{n-1}$ colorings.
- **One column:** No transition runs. Summing the initialized valid states returns $3\cdot2^{m-1}$.
- **Leading ternary zeroes:** They represent real red cells. Extracting exactly $m$ digits ensures those cells participate in all adjacency checks.
- **Current-versus-previous orientation:** The code stores `d[i]` as compatible `j` values and sums `f[j]` into `g[i]`. Symmetry makes the orientation natural, but the recurrence still explicitly treats `i` as current.
- **Modulo arithmetic:** Applying the remainder after every addition prevents counts from growing unnecessarily; the final sum is reduced once more.
- **Only horizontal and vertical adjacency:** Diagonal cells are not compared, exactly matching the problem.
- **State count:** The full arrays have length $3^m$, while loops over transitions use only `valid` states. Invalid entries remain zero.
