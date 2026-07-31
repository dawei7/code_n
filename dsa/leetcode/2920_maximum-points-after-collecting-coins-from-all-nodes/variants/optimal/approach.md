## General

**The ancestor effect is a small state.** Root the undirected tree at node 0.
For a node $u$, only the number $h$ of second-method choices made by its
ancestors affects its current coins; that value is
$\lfloor\texttt{coins[u]}/2^h\rfloor$. Choices made in one child subtree do
not affect a sibling, so subtrees become independent once $u$'s method and
$h$ are fixed.

Let `dp[u][h]` be the maximum score obtainable from the entire subtree of
$u$ after $h$ inherited halvings. The first method contributes
`(coins[u] >> h) - k` and leaves every child at state $h$. The second
contributes `coins[u] >> (h + 1)` and sends every child to state $h+1`.
Therefore each state is the larger of

$$
\left(\left\lfloor\frac{\texttt{coins[u]}}{2^h}\right\rfloor-k\right)
+\sum_{v\text{ child of }u}\texttt{dp[v][h]}
$$

and

$$
\left\lfloor\frac{\texttt{coins[u]}}{2^{h+1}}\right\rfloor
+\sum_{v\text{ child of }u}\texttt{dp[v][h+1]}.
$$

**Stop after every coin value becomes zero.** Since
$\texttt{coins[u]}\le10^4<2^{14}$, state 14 has zero current coins
everywhere. From there, repeatedly choosing the second method gives zero
rather than a negative penalty, so every `dp[u][14]` is zero and no larger
state is needed.

**Evaluate children before parents.** Build parent pointers and a root-first
order iteratively, then process that order in reverse. At each node, compute
states 13 down to 0, so both child states referenced by the recurrence are
already available. The recurrence considers both legal methods and adds the
independently optimal result from every child. Induction from the leaves
therefore proves each state optimal, including `dp[0][0]`, the answer with no
inherited halving.

## Complexity detail

Let $n=\lvert\texttt{coins}\rvert$ and
$C=1+\max_i\texttt{coins[i]}$. There are $O(\log C)$ effective halving
states per node. Each edge is examined a constant number of times per state,
so the time complexity is $O(n\log C)$. The rooted tree data and dynamic
programming table use $O(n\log C)$ auxiliary space. Under the given
$10^4$ coin bound, there are at most 15 states.

## Alternatives and edge cases

- **Enumerate both methods at every node:** Exploring all $2^n$ choice assignments repeats identical subtree states and is exponential.
- **Recursive memoization:** Memoizing `(node, inherited_halvings)` has the same asymptotic bounds, but a path of $10^5$ nodes can exceed the language's call-stack limit; iterative postorder avoids that risk.
- **Copy and halve entire subtrees:** Mutating descendant coin arrays for each second-method choice repeats work; the inherited shift represents all such mutations without copying.
- **Negative first-method score:** Collecting by the first method is still legal when the current coins are below `k`, but the second method may avoid that loss.
- **Zero coins:** The second method awards zero and propagates another harmless halving, so a subtree never has to accept a negative score once all values are zero.
- **Zero penalty:** The first method collects each current value without loss and no halving choice can improve the total.
- **Sibling subtrees:** A second-method choice affects only its own rooted subtree, never a sibling, which is why child optima can be summed independently.

