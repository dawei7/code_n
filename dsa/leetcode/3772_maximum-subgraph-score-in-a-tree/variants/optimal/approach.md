## General

Replace each good node by weight $+1$ and each bad node by weight $-1$. Root the tree arbitrarily at node 0. For a node `u`, define `down[u]` as the maximum score of a connected selection that contains `u` and uses only nodes in `u`'s rooted subtree.

The selection must contain `u` itself. For each child `v`, it may either omit that entire branch or attach the best connected selection represented by `down[v]`. A non-positive child contribution never helps, giving

$$
\texttt{down[u]}=w_u+\sum_{v\text{ child of }u}\max(0,\texttt{down[v]}).
$$

A reverse traversal computes these values bottom-up. They solve the problem for the root, but another node may also benefit from the part of the tree above it. Reroot the result in a forward traversal. For a parent `u` and child `v`, remove `v`'s positive contribution from `answer[u]`; what remains is the best connected contribution available through the parent side:

$$
P_{u\to v}=\texttt{answer[u]}-\max(0,\texttt{down[v]}).
$$

The child includes that side exactly when it is positive, so

$$
\texttt{answer[v]}=\texttt{down[v]}+\max(0,P_{u\to v}).
$$

Cutting any edge incident to a required node separates the tree into independent branches. A connected subgraph containing that node can take from a branch only through its adjacent endpoint, and the recurrences take precisely the best positive contribution from every branch. The bottom-up pass handles child branches; the reroot pass supplies the one parent-side branch. Thus every `answer[u]` is both attainable and at least as large as any connected subgraph containing `u`.

## Complexity detail

Let $N$ be the number of nodes. Building the adjacency list and each of the two tree traversals takes $O(N)$ time because a tree has $N-1$ edges. The adjacency list, parent/order arrays, and two score arrays use $O(N)$ space.

## Alternatives and edge cases

- **Recompute a rooted DP for every node:** Rooting the tree separately at each required node is correct but repeats linear work and costs $O(N^2)$ time.
- **Recursive rerooting:** Two depth-first searches express the same recurrences compactly, but an iterative order avoids call-stack overflow on a path of length $10^5$.
- **All bad nodes:** Every additional node lowers the score, so selecting only the required node gives `-1` everywhere.
- **All good nodes:** The whole tree is optimal for every node, producing score `n` at every position.
- **Zero contribution:** A branch with total contribution zero may be included or omitted without changing the maximum.
- **Required bad node:** The subgraph must retain that node, but positive neighboring branches can more than offset its `-1` weight.
- **Non-unique optimum:** Several connected subgraphs can achieve the same maximum; only the score is returned.
