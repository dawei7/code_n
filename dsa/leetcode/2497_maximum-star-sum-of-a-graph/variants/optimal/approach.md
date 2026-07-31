## General

**Only positive neighbors can help.** The center is mandatory, but every incident edge is optional because the star may contain at most `k` edges. Adding a neighbor with a negative value strictly lowers the sum, and adding a zero never improves it. For a fixed center, an optimal star therefore chooses the largest positive values among its neighbors, taking no more than `k` of them.

**Retain only the useful local choices.** Create one min-heap per node. When processing an undirected edge `[u, v]`, `vals[v]` is a neighbor candidate for center `u`, and `vals[u]` is a candidate for center `v`. Insert a candidate only when it is positive. If a heap grows beyond `k`, remove its smallest entry. After every insertion, the heap for a node contains the largest `k` positive values seen among that node's processed neighbors: a new value is retained exactly when it belongs among those best choices.

Once all edges have been processed, evaluate each node as a center by adding its own value to the sum of its retained heap. The local argument above proves this is the best legal star for that center. Taking the maximum over all centers then covers every possible star, including a center with no selected edge when its heap is empty.

## Complexity detail

Let $n = \lvert\texttt{vals}\rvert$ and $m = \lvert\texttt{edges}\rvert$. Each edge generates at most two heap updates, each costing $O(\log(k+1))$ because a heap never contains more than `k` retained entries. Initializing and evaluating all centers adds $O(n)$ work, so total time is $O(n + m\log(k+1))$. The heaps contain at most two retained entries per edge overall, plus one list per node, giving $O(n+m)$ auxiliary space.

## Alternatives and edge cases

- **Sort every adjacency list:** Collecting all positive neighbor values and sorting each list is simpler, but costs up to $O(n + m\log n)$ time and stores every candidate even when `k` is small.
- **Scan all edges per center:** Rebuilding each node's neighbor list by examining every edge takes $O(nm)$ time on sparse benchmark graphs.
- **Zero allowed edges:** When `k = 0`, every candidate is just its center value, so the answer is `max(vals)`.
- **All neighbor values non-positive:** Ignore them all; selecting fewer than `k` edges is allowed.
- **Negative center:** A negative center may still win if enough positive neighbors outweigh it, but it may also be worse than a positive node taken alone.
- **Disconnected or isolated nodes:** Every node is evaluated independently as a possible center, regardless of graph connectivity.
