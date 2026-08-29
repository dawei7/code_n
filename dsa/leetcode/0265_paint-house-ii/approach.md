## General

The adjacency rule couples one house only to the color of the immediately previous house. Dynamic programming can therefore summarize every valid painting of a processed prefix by its final color.

The list `f` has one entry per color. After processing some house `i`,

```text
f[j] = minimum cost to paint houses 0..i validly
       when house i uses color j
```

The exact solution initializes `f = costs[0][:]`. For the first house, choosing color `j` costs exactly `costs[0][j]`, and there is no previous house to restrict it. The slice creates a copy, so later dynamic-programming work does not mutate the input row.

**Transition to the next house**

For each later house `i`, the solution begins with `g = costs[i][:]`, another copy of the raw painting costs. To finish a valid prefix at current color `j`, the previous house may use any color `h` except `j`. Therefore,

$$
g[j]=\text{costs}[i][j]+\min_{0\le h<k,\ h\ne j}f[h].
$$

The generator expression

```text
min(f[h] for h in range(k) if h != j)
```

computes exactly that legal predecessor cost. Adding it to `g[j]` converts the raw cost for the current house into the best full-prefix cost ending at that color.

After all `k` current colors are calculated, `f = g` advances the DP layer. Older rows are no longer needed because the next transition depends only on the immediately preceding house.

**Why `f` and `g` must be separate during a row**

Every `g[j]` must read predecessor costs from the same completed previous row. If the implementation overwrote `f[j]` in place and then used `f` for later colors, some transitions would mix costs ending at the current house with costs ending at the previous house. That could effectively select two colors for one house or skip the adjacency boundary.

Keeping `f` unchanged while filling `g` gives a clean layer boundary. Only after every current state is complete does the assignment `f = g` replace the old row.

**Trace through the first example**

For

```text
costs = [[1, 5, 3], [2, 9, 4]]
```

the first row initializes

```text
f = [1, 5, 3]
```

For the second house:

- Current color `0` cannot follow previous color `0`, so choose `min(5, 3) = 3`; `g[0] = 2 + 3 = 5`.
- Current color `1` cannot follow previous color `1`, so choose `min(1, 3) = 1`; `g[1] = 9 + 1 = 10`.
- Current color `2` cannot follow previous color `2`, so choose `min(1, 5) = 1`; `g[2] = 4 + 1 = 5`.

The completed row is `[5, 10, 5]`. The smallest value is `5`, representing either colors `2 -> 0` or colors `0 -> 2`, exactly as in the example.

**Why one cheapest predecessor per ending color is enough**

Many different prefix paintings may end in the same previous color `h`. Only their cheapest cost matters. Every future choice sees the same restriction—current color may not equal `h`—regardless of how the earlier houses were painted. A more expensive prefix with the same ending color can never become better after both alternatives add identical future costs.

The DP must still retain all `k` ending colors because each current color excludes a different predecessor. Keeping only one overall previous minimum would fail when that minimum uses the same color as the current state.

**Why the recurrence is correct**

For house zero, `f[j]` is clearly the cheapest valid one-house painting ending in color `j`. Assume `f` has the stated meaning through house `i - 1`. Any valid painting ending with color `j` at house `i` must have some previous color `h != j`. Its prefix through `i - 1` costs at least `f[h]` by the inductive meaning, so the cheapest such painting costs the raw current price plus the minimum legal `f[h]`.

Conversely, choosing the predecessor color attaining that minimum and appending current color `j` produces a valid painting with exactly the computed cost. Thus every `g[j]` is optimal for its ending color. By induction, after the last house, `f` contains the optimal full costs for all possible final colors, and `min(f)` is the global minimum.

The constraint $k\ge2$ ensures that for every excluded color `j`, at least one different predecessor remains. The generator passed to `min` is never empty.

## Complexity detail

Let $n$ be the number of houses and $k$ the number of colors. There are $n-1$ transition rows. For each row, the outer color loop runs $k$ times, and each `min` scans $k-1$ predecessor colors. The exact running time is therefore

$$
O(nk^2).
$$

Copying each current cost row adds $O(nk)$ work, which is dominated by the repeated minimum scans.

At any moment the algorithm retains `f` and `g`, each of length $k$, plus scalar loop variables. Auxiliary space is $O(k)$. The input matrix is preserved.

This differs from the manifest summary, which describes caching the smallest and second-smallest prior totals to make each transition $O(1)$ and the full runtime $O(nk)$. That optimized transition is not present in the protected source; the approach and bounds here follow the actual nested scans.

## Alternatives and edge cases

- **Track the minimum and second minimum:** Find the cheapest prior total, its color, and the second-cheapest total once per row. A current color uses the cheapest unless it has the same color, in which case it uses the second cheapest. This achieves the follow-up's $O(nk)$ time and is the algorithm described by the manifest.
- **Top-down memoization:** Cache `(house, previous color)` states and try all legal next colors. It has the same $O(nk^2)$ time as the exact source, plus recursion and a larger cache.
- **Full two-dimensional DP:** Store all $n\cdot k$ states. It can help reconstruct the color assignment but uses $O(nk)$ space when only the previous row is needed for the minimum cost.
- **One house:** No transition runs. `min(costs[0])` returns the cheapest available color.
- **Two colors:** Each current color has exactly one legal predecessor, so the generator's minimum contains one value and paintings must alternate.
- **Tied predecessor costs:** `min` needs only the numeric total. Any tied legal predecessor yields the same optimum, and no path reconstruction is requested.
- **Positive costs:** Positivity is guaranteed but not required for the recurrence; optimal substructure still holds with arbitrary additive costs.
- **Input preservation:** Both `f` and each `g` are slices, so no row in `costs` is overwritten.
- **`k = 1` outside the constraints:** With multiple houses, no valid painting exists and the generator would be empty. The documented $k\ge2$ avoids this undefined case.
- **Empty matrix outside the constraints:** The source accesses `costs[0]`, so it relies on $n\ge1$. A broader API would need an early empty-input decision.
- **Recovering chosen colors:** The rolling rows discard predecessor identities. Returning the actual plan would require back-pointers or recomputation and additional space.
