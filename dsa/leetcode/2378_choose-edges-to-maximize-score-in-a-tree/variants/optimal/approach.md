## General

**Recognize a maximum-weight matching on a tree**

Two chosen edges may not share a node. Thus, every node can be incident to at most one chosen edge. This is precisely a matching constraint, with edge weights contributing to the objective.

The tree structure makes the global choice decomposable. Child subtrees do not interact except through their common parent. The only information a subtree must expose upward is whether its root is already occupied by the edge to its parent.

**Build children from the parent representation**

For each non-root node `i`, `edges[i] = [p, w]` gives its parent and the connecting edge's weight. The solution creates `g[p]` entries `(i, w)`. Because the input is already rooted, it stores only parent-to-child directions. DFS therefore never needs a visited set or parent argument.

The root's sentinel `[-1, -1]` is skipped by enumerating `edges[1:]` starting at index one.

**Meaning of the two returned states**

`dfs(i)` returns a pair `(a, b)`:

- `a` is the best score inside node `i`'s subtree when the edge from `i` to its parent is selected. Node `i` is already occupied, so no edge from `i` to a child may be selected.
- `b` is the best score inside the subtree when the parent edge is not selected. Node `i` is available, so zero or one child edge may be selected.

The root has no parent edge, so the requested answer is its available state, `dfs(0)[1]`.

**Compute the occupied state**

Suppose child `j` returns `(x, y)`. Here, `x` is the child's state when edge `i-j` is selected, and `y` is its state when that edge is not selected.

If node `i`'s own parent edge is selected, no `i-j` edge can be chosen. Every child must therefore contribute `y`. The code accumulates:

```python
a += y
```

Different child subtrees are disjoint, so their optimal scores add independently.

**Compute the available state**

When `i`'s parent edge is absent, a baseline solution selects no edge between `i` and any child. It again receives `y` from every child. This is why `b` also begins by adding every `y`.

Node `i` can additionally choose at most one child edge. If it chooses edge `i-j` of weight `w`, child `j` must switch from its baseline state `y` to occupied state `x`, and the chosen edge adds `w`. Relative to the baseline, the gain is:

$$
x-y+w.
$$

The variable `t` tracks the largest such gain across children:

```python
t = max(t, x - y + w)
```

It begins at zero. Therefore, if every possible child edge has negative or zero net benefit, no edge is selected at `i`. Finally, `b += t` adds the one best profitable option.

**Why only one gain may be added**

All child edges of `i` share node `i` and are pairwise adjacent. Selecting two would violate the constraint even though their child subtrees are otherwise independent. Taking the maximum single gain rather than summing positive gains enforces this exactly.

**Trace the first example**

Node `2` has child edges of weights `6` and `4`. Its children are leaves, so each has `x = y = 0`. The available state at node `2` takes the maximum gain `6`.

At root `0`, choosing edge `0-2` of weight `10` would occupy node `2` and lose its internal gain of `6`, giving a net comparison of `10` versus keeping that subtree's `6`. Choosing edge `0-1` of weight `5` does not disturb node `2`'s internal edge. The best combination becomes weight `5` plus `6`, totaling `11`.

This demonstrates why greedily selecting the heaviest edge `10` is not optimal: an edge's opportunity cost includes matchings it blocks inside the child subtree.

**Why the recurrence is correct**

For occupied state `a`, every child edge is forbidden by adjacency at `i`. Child subtrees have no other cross-connections, so independently taking each child's free state `y` is both feasible and optimal.

For available state `b`, every feasible matching either selects no child edge or selects exactly one `i-j`. The baseline represents the first case. For the second, replacing `y` by `x` and adding `w` gives the exact score change for that child; all other children remain at `y`. Taking the largest nonnegative gain examines every possible selected child and the no-selection option.

By induction from leaf nodes upward, both states are optimal for their conditions. The root is available and has no parent edge, so its `b` value is the global maximum matching weight.

Negative weights require no special case beyond `t = 0`. Since choosing no edges is allowed, a harmful edge is never forced.

## Complexity detail

Let $n$ be the number of nodes. Building `g` processes the $n-1$ non-root entries once. DFS visits every node once and processes every parent-child edge once. All calculations per edge are constant time, giving $O(n)$ total time.

The adjacency mapping stores $n-1$ child records, and recursion can reach depth $O(n)$ in a chain. Total auxiliary space is $O(n)$. A very deep tree may exceed Python's default recursion limit in practice; an iterative postorder implementation avoids that issue.

## Alternatives and edge cases

- **Iterative postorder DP:** Build an order of nodes and evaluate the same two states bottom-up. It preserves $O(n)$ bounds and avoids recursive depth limits.
- **Greedy by largest edge weight:** It fails because choosing one heavy edge can block a more valuable combination in neighboring subtrees.
- **General graph matching algorithm:** Unnecessary here; the rooted tree permits a simple two-state recurrence.
- **Leaf node:** It has no children, so both returned states are zero.
- **All edge weights negative:** Every gain remains below zero, `t` stays zero, and the answer is zero.
- **Zero-weight edge:** Selecting it is never necessary for score and may block alternatives; the zero baseline is at least as good.
- **Star-shaped tree:** The root can choose at most one incident edge, so the answer is the largest positive edge weight.
- **Chain:** Alternating nonadjacent edges may be selected, and the two states capture those choices.
- **Root sentinel:** `edges[0]` is not a real edge and is deliberately excluded from adjacency construction.
- **One-node tree:** The root has no children and the returned maximum is zero.
