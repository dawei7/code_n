## General

Choosing the second collection method at a node halves every coin value in its subtree. Therefore a descendant's effective value depends on how many ancestors used that method. That count is the only information from above the subtree that affects later decisions.

The memoized state `dfs(i, fa, j)` is the maximum score from the subtree rooted at `i` when all original coin values there have already been halved $j$ times. `fa` is the parent, used to orient the undirected adjacency list and avoid walking back upward.

After $j$ halvings, node $i$ contains

$$
\left\lfloor\frac{\texttt{coins}[i]}{2^j}\right\rfloor,
$$

which right shift computes as `coins[i] >> j`.

**Option one: pay the fixed penalty**

The first collection method contributes `(coins[i] >> j) - k`. It does not cause another halving, so every child remains in state $j$:

$$
a=(\texttt{coins}[i]\mathbin{\texttt{>>}}j)-k
 +\sum_c\texttt{dfs}(c,i,j).
$$

The current contribution may be negative, as the contract permits. The algorithm compares complete subtree totals instead of greedily deciding from the current coin alone.

**Option two: halve this subtree**

The second method contributes `coins[i] >> (j + 1)`. Every child inherits the extra halving:

$$
b=(\texttt{coins}[i]\mathbin{\texttt{>>}}(j+1))
 +\sum_c\texttt{dfs}(c,i,j+1).
$$

The state returns `max(a,b)`. Once the current method fixes the inherited count, child subtrees are independent, so their optimal scores may be added.

**Why counts through fourteen are sufficient**

The maximum coin value is $10^4<2^{14}$. After fourteen halvings, every effective coin is zero.

The exact source computes option-two child states only when `j < 14`. At `j == 14`, choosing the second method yields zero at the current node and would pass zeros throughout the descendants. Every descendant can also choose its zero-yielding second method, so the optimal omitted child contribution is zero.

Option one is still evaluated at `j == 14`, but it pays `-k` at zero-valued nodes and cannot beat the available zero option. The fixed cutoff bounds the state dimension.

**Why the recurrence is optimal**

Fix state $(i,j)$. Every valid strategy must use one of the two methods at node $i$. If it uses the first, the current reward and child states are exactly those in $a$. If it uses the second, they are exactly those in $b$.

For either fixed choice, different child subtrees have no shared nodes. Replacing a child's decisions with its memoized optimum cannot harm any other child. Thus $a$ and $b$ are the best totals under the two exhaustive first choices, and their maximum is exact. Induction from leaves to root proves `dfs(0,-1,0)` is the global answer.

The ancestor-order rule is respected naturally: recursion reaches a node only through its parent state. Every node's coins are collected exactly once within one of the two branches.

**Adjacency and cache mechanics**

Each edge is stored in both directions. The `c != fa` check roots the traversal without a separate parent array. `@cache` memoizes node, parent, and halving count. A rooted-tree node has one parent, so there are at most about $15n$ meaningful states.

After obtaining the integer answer, `dfs.cache_clear()` releases cached references. It does not change the result.

## Complexity detail

Let $C=\max(\texttt{coins})$. There are $O(\log C)$ relevant halving counts, bounded by 15 here. Each node-state scans its child adjacency, giving $O(n\log C)$ time.

The adjacency list uses $O(n)$ space. The cache stores $O(n\log C)$ results, and recursion can reach $O(n)$ depth on a path. Overall auxiliary space is $O(n\log C)$.

The manifest summary describes an iterative evaluation, but the exact source is recursive. On a legal path-shaped tree, Python's default recursion limit can be exceeded. This is a genuine robustness defect even though the recurrence and asymptotic DP bounds are correct.

## Alternatives and edge cases

- **Greedy per node:** Comparing only `coins[i]-k` with `coins[i]//2` ignores the second method's effect on descendants.
- **Iterative postorder DP:** Root with a stack and fill the same states bottom-up. This avoids the source's recursion-limit risk.
- **No memoization:** Recomputing subtree states across ancestral choices can grow exponentially.
- **$k=0$:** The first method has no penalty and keeping full current values is at least as good as halving.
- **Zero coins:** The second method yields zero safely; the first may lose $k$, so the maximum chooses correctly.
- **Leaf:** Both formulas have empty child sums and reduce to comparing two current-node rewards.
- **Hard-coded cutoff:** Fourteen relies on the stated $10^4$ bound. A larger domain should derive it from $C$.
- **Parent in the cache key:** It is redundant under fixed rooting but harmless in a tree.
- **Deep path:** The mathematical DP remains valid, but the recursive Python source may raise `RecursionError`.
- **All-zero effective subtree:** Once $j=14$, repeatedly choosing the second method yields zero everywhere and proves that omitting its child calls cannot discard positive score.
