## General

**Reverse the viewpoint of each directed edge**

The array entry `edges[i] = j` means source node `i` points to target node `j`. The edge score belongs to the target and receives the *source label* `i` as a contribution.

Therefore, while scanning source indices, the update is:

```python
cnt[j] += i
```

It is not `cnt[i] += j`. The latter would add outgoing destinations to sources and calculate a different quantity.

Every node has exactly one outgoing edge, so every source index contributes exactly once to exactly one score. A target may have zero, one, or many incoming sources. Nodes with no incoming edges retain score zero.

**Maintain scores and the best node together**

`cnt` is a length-$n$ list initialized to zero. After processing sources `0` through `i`, `cnt[v]` equals the sum of labels among those processed sources whose edge points to `v`.

`ans` is initialized to node `0`. Before any edge is processed, all scores are zero, and node zero is the smallest index among the tied maximum scores. Thus, `ans = 0` is the correct initial tie-aware winner.

After adding source `i` to target `j`, only one score changes: `cnt[j]`. Every other score remains exactly as it was. If the previous `ans` was the correct winner before the update, the new winner can only remain `ans` or become `j`.

The solution performs exactly that comparison:

```python
if cnt[ans] < cnt[j] or (cnt[ans] == cnt[j] and j < ans):
    ans = j
```

Target `j` replaces the current answer when it has a strictly larger score. If scores tie, it replaces only when its index is smaller.

**Why an online winner remains valid**

It might initially seem safer to finish all scores and then scan for the maximum. The online update is equally correct because each iteration modifies only `j`.

Maintain the invariant that `ans` is the smallest-index node having the maximum score among the current partial scores. Before an update, all unchanged nodes are already no better than `ans` under score-first, index-second ordering. After increasing `cnt[j]`, only `j` might overtake or tie `ans`. The condition compares those exact possibilities and picks the correct one. Thus, the invariant remains true after every source.

At the end, partial scores are full edge scores, so `ans` is the required final node.

**Trace the tie example**

For `edges = [2, 0, 0, 2]`:

- Source `0` contributes zero to node `2`. All scores remain zero, so node `0` stays the smallest tied winner.
- Source `1` contributes one to node `0`. Node `0` leads with score one.
- Source `2` contributes two to node `0`. Its score becomes three.
- Source `3` contributes three to node `2`. Node `2` also reaches score three.

The final comparison sees equal scores but `2 < 0` is false, so node `0` remains. This implements the smallest-index tie rule without a separate final pass.

**The zero-label contribution**

Node labels themselves are contribution amounts. Source node `0` contributes zero to its target. The directed edge still exists, but it does not numerically increase that target's score. This is why a target with an incoming edge only from node zero can still have score zero and tie nodes with no incoming edges.

The initialization and tie logic handle that naturally.

**Why every final score is exact**

Fix a target node `v`. The loop visits every possible source `i` once. It adds `i` to `cnt[v]` exactly when `edges[i] == v` and never otherwise. After all sources, the accumulated value is therefore:

$$
\sum_{\{i:\ \texttt{edges}[i]=v\}} i,
$$

which is the definition of `v`'s edge score.

The maintained-winner invariant then guarantees that `ans` has the greatest of these exact totals and, among equal totals, the smallest index. The returned node satisfies both requested priorities.

**Why score magnitude requires more than intuition about indegree**

A node with more incoming edges does not necessarily have a higher score, because incoming source labels carry different weights. One edge from a large-index source can outweigh several edges from small sources. Accumulating source indices is essential; counting incoming edges would not solve the problem.

## Complexity detail

Let $n$ be the number of nodes. The loop processes all $n$ array entries exactly once and performs constant-time indexing, addition, and comparison. Time complexity is $O(n)$.

The `cnt` list contains $n$ integer scores, so auxiliary space is $O(n)$. The winner and loop variables use constant additional space.

The largest possible score is the sum of many labels, bounded by $n(n-1)/2$. Python integers handle this automatically. A fixed-width implementation should use a 64-bit integer for $n$ up to $10^5$.

## Alternatives and edge cases

- **Two-pass method:** First accumulate every score, then scan from index zero and keep the first maximum. It has the same $O(n)$ bounds and may be conceptually simpler, while the exact method combines the passes.
- **Dictionary of scores:** A hash map works, but every target lies in the dense range `0` through `n - 1`, so a list is faster and simpler.
- **Count indegrees:** This is incorrect because the score sums source labels rather than the number of sources.
- **Target with no incoming edges:** Its score remains zero and it can win only if no node has a positive score, with smallest-index tie-breaking.
- **Incoming edge from node zero:** It contributes zero even though the edge exists.
- **Several nodes tie:** The comparison's second clause retains or selects the smallest index.
- **Current target equals `ans`:** Its score is updated in place; comparing it with itself makes no unnecessary change.
- **Repeated target values in `edges`:** Each source label is added independently to that target's running total.
- **Exactly one outgoing edge per source:** The enumeration accounts for every source once and needs no missing-edge branch.
- **Large accumulated sums:** Use sufficiently wide arithmetic outside Python.
