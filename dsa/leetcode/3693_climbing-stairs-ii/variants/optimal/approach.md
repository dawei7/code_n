## General

The staircase forms a directed acyclic graph. Step $i$ can be reached only from earlier steps $i-1$, $i-2$, or $i-3$, so the cheapest way to reach steps can be computed in increasing order.

The exact source uses a dynamic-programming array:

`f[i]` = the minimum total cost required to reach conceptual step $i$.

Step zero is the starting point, so:

`f[0] = 0`

Every other entry begins at infinity because no route has been considered yet.

**Reconciling conceptual and Python indices**

The statement describes `costs` as one-indexed: `costs[j]` is the landing cost of step $j$. The Python list is zero-indexed, so list element `costs[j - 1]` represents that value.

The loop:

`for i, x in enumerate(costs, 1):`

starts enumeration at one. Consequently:

- `i` is the conceptual stair number;
- `x` is the Python element at position `i - 1`, which is the cost of landing on conceptual step `i`.

This alignment prevents an off-by-one lookup and lets the transition use `x` directly.

The method parameter `n` is immediately replaced by `len(costs)`. The contract guarantees these values agree, so the overwrite does not change the intended destination. The source relies on the actual list length for allocating and returning the DP state.

**Considering every legal predecessor**

To land on step $i$, the previous step $j$ must satisfy:

$$
i-j\in\{1,2,3\}.
$$

Equivalently, $j$ is one of $i-3,i-2,i-1$. The source enumerates:

`for j in range(i - 3, i):`

For the first few steps, this range contains negative indices that do not represent real stairs. The guard:

`if j >= 0:`

discards them before using `f[j]`. This is especially important in Python because a negative list index would otherwise refer to an element at the end of the list rather than raising an error.

**Cost of extending one best route**

Suppose the route's final jump is from $j$ to $i$. Everything before that jump must form some route from zero to $j$. The cheapest such prefix costs `f[j]`.

Landing on $i$ adds:

$$
\texttt{costs}[i]+(i-j)^2,
$$

which the aligned Python variables express as:

`x + (i - j) ** 2`.

Therefore, the candidate total through predecessor $j$ is:

`f[j] + x + (i - j) ** 2`.

The recurrence is:

$$
f[i]=
\min_{\substack{j<i\\1\le i-j\le3}}
\left(f[j]+\texttt{costs}[i]+(i-j)^2\right).
$$

The source evaluates each legal $j$ and retains the smallest candidate in `f[i]`.

**Why already computed predecessor costs are enough**

Every route to step $i$ has exactly one final predecessor among $i-1,i-2,i-3$. Once that predecessor is fixed, choosing a more expensive route to $j$ can never improve the final total because the landing cost and jump penalty depend only on $i$ and $j$, not on the earlier route.

Thus an optimal route to $i$ can always use an optimal route to its final predecessor. Taking the minimum over the three possible final jumps covers every valid route and chooses the least expensive one.

The loop processes `i` from one upward, so all needed `f[j]` entries have already reached their final minimum before `f[i]` is computed. No backward edge or cycle can later improve an earlier state.

**Tracing the first example**

For `costs = [1, 2, 3, 4]`:

- Step one can be reached only from zero: $f[1]=0+1+1^2=2$.
- Step two compares a two-step jump from zero, costing $0+2+2^2=6$, with a one-step jump from step one, costing $2+2+1=5$. Hence $f[2]=5$.
- Step three compares routes from zero, one, and two.
- Step four compares predecessors one, two, and three. The route through step two costs $f[2]+4+2^2=5+4+4=13$ and is optimal.

This corresponds to path $0\to1\to2\to4$.

For `costs = [9, 8, 3]`, the direct jump from zero to three costs $3+3^2=12$. The recurrence includes predecessor zero when `i = 3`, so it naturally finds that direct route.

**Why infinity initialization is safe**

Every destination step is reachable because jumps of length one are always allowed. Therefore, each `f[i]` receives at least one finite candidate from `f[i-1]`.

Infinity is used only as an initial value larger than every real route cost. It never survives in the returned state under valid input.

## Complexity detail

Let $n$ be `len(costs)`.

The outer loop processes $n$ destination steps. For each one, the inner range contains exactly three candidate integers, with negative candidates skipped near the beginning. Each valid transition performs constant arithmetic and one comparison. Total time is $O(3n)=O(n)$.

The exact source allocates `f` with $n+1$ entries, so its auxiliary space complexity is $O(n)$.

This is a source/manifest mismatch. The manifest summary describes retaining only a rolling three-step frontier and reports $O(1)$ space, but `solution.py` keeps the full DP array. A rolling implementation is possible because each state reads only the previous three entries, yet it is not the checked-in implementation documented here.

The returned answer is one integer, and the input list is not modified.

## Alternatives and edge cases

- **Rolling three-value DP:** Since `f[i]` depends only on `f[i-1]`, `f[i-2]`, and `f[i-3]`, these values can be rotated in $O(1)$ space. This matches the manifest description but not the exact source.
- **Recursive search without memoization:** Exploring all jump sequences repeats the same subproblems and grows exponentially.
- **Memoized recursion:** This reaches $O(n)$ time but uses $O(n)$ memo storage and potentially an $O(n)$ recursion stack. Bottom-up iteration avoids recursion depth.
- **Dijkstra's algorithm:** The staircase is a weighted graph, but all edges move forward and each vertex has only three predecessors. Topological-order DP is simpler and linear.
- **`n = 1`:** Only jump $0\to1$ is legal, so the answer is `costs[0] + 1`.
- **Destination within three steps:** Step zero appears among the predecessor candidates, allowing a direct jump and its squared-length penalty.
- **Negative Python indices:** The `j >= 0` guard is mandatory; otherwise, Python would silently read unrelated DP cells from the array's end.
- **Landing cost charged once:** `x` is added for the destination of each jump. Step zero has no entry and no starting cost.
- **Large total cost:** Up to $10^5$ landings with positive costs can exceed small integer ranges, but Python integers handle the accumulated value safely.
- **Parameter overwrite:** The method ignores the passed numerical `n` after assigning `len(costs)`. This is harmless only because the function contract guarantees equality.
