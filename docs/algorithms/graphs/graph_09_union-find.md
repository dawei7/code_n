# Union-Find (Disjoint Set Union, DSU)

| | |
|---|---|
| **ID** | `graph_09` |
| **Category** | graphs |
| **Complexity (required)** | O(n) |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **Wikipedia** | [Disjoint-set data structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) |

## Problem statement

Maintain a partition of `n` elements into disjoint sets
under two operations:
- `find(x)` — return the **representative** (root) of the
  set containing `x`.
- `union(x, y)` — merge the sets containing `x` and `y`.

Both operations should be fast (close to O(1) amortized).
Useful for: connectivity queries, Kruskal's MST, network
components, image processing, etc.

**Input:** a stream of union + find queries on `n` elements.
**Output:** for each find, the representative of `x`'s set;
for each union, the merged set's new representative.

**Example:**

Initial: each element in its own set.
```
union(0, 1)     -> {0, 1}, {2}, {3}, {4}
union(2, 3)     -> {0, 1}, {2, 3}, {4}
find(0)         -> 0   (or 1, depending on impl)
find(2)         -> 2   (or 3)
union(1, 3)     -> {0, 1, 2, 3}, {4}
find(0)         -> 0   (or 1, 2, 3 — all the same set)
```

## When to use it

- Asked in some form at every interview. Often as part of
  Kruskal's MST or as a "**count connected components**"
  sub-problem.
- Foundation for **Kruskal's algorithm**, **offline
  connectivity queries**, and the **Percolation** problem.

## Approach

Two classic optimizations:

**Path compression** (in `find`): after finding the root of
`x`, set `parent[x] = root`. Flattens the tree.
**Union by rank/size**: always attach the smaller tree under
the root of the larger one.

With both, the amortized cost per operation is
**O(α(n))** (inverse Ackermann, < 5 for any practical `n`).

**Path compression** (recursive):
```
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])    # compress
    return parent[x]
```

**Union by rank:**
```
def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry: return
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1
```

**Union by size** (alternative; same complexity):
```
def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry: return
    if size[rx] < size[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    size[rx] += size[ry]
```

## Algorithm (pseudocode)

```
class DSU:
    parent = [0, 1, 2, ..., n-1]
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = self.find(parent[x])
        return parent[x]

    def union(x, y):
        rx = self.find(x); ry = self.find(y)
        if rx == ry: return False
        if rank[rx] < rank[ry]: rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]: rank[rx] += 1
        return True
```

The `union` returns `True` if a merge happened, `False` if
`x` and `y` were already in the same set (useful for
cycle detection).

## Walk-through

`n = 5`. Operations: `union(0,1)`, `union(1,2)`, `find(0)`,
`union(3,4)`, `union(2,4)`, `find(0)`, `find(3)`.

Initial: `parent = [0, 1, 2, 3, 4]`, `rank = [0, 0, 0, 0, 0]`.

| Op | Action | parent after | rank after |
|---|---|---|---|
| `union(0, 1)` | r=0, r=1, rank[0]==rank[1], parent[1]=0, rank[0]=1 | `[0, 0, 2, 3, 4]` | `[1, 0, 0, 0, 0]` |
| `union(1, 2)` | r=find(1)=0, r=2, rank[0]=1 > rank[2]=0, parent[2]=0 | `[0, 0, 0, 3, 4]` | same |
| `find(0)` | parent[0]=0, return 0 | unchanged | same |
| `union(3, 4)` | r=3, r=4, rank[3]==rank[4], parent[4]=3, rank[3]=1 | `[0, 0, 0, 3, 3]` | `[1, 0, 0, 1, 0]` |
| `union(2, 4)` | r=find(2)=0, r=find(4)=3, rank[0]==rank[3], parent[3]=0, rank[0]=2 | `[0, 0, 0, 0, 3]` | `[2, 0, 0, 1, 0]` |
| `find(0)` | return 0 | unchanged | same |
| `find(3)` | parent[3]=0, return 0 (with path compression) | unchanged | same |

All elements {0, 1, 2, 3, 4} are now in one set with root 0. ✓

## Complexity

| | Time (amortized) | Space |
|---|---|---|
| **Best** | O(α(n)) per op | O(n) |
| **Average** | O(α(n)) per op | O(n) |
| **Worst** | O(α(n)) per op | O(n) |

`α(n)` is the inverse Ackermann function — for all
practical `n` (n < 10^600), `α(n) ≤ 5`. So DSU is
"effectively O(1) per operation".

Without the optimizations: O(n) per `find` in the worst
case (degenerate tree).

## Variants & optimizations

- **Union by size** — alternative to rank; slightly
  simpler, same complexity.
- **Weighted union** — when the elements have weights, the
  "smaller" is the lower weight. Used in Kruskal's for
  "minimize total edge weight".
- **Persistent DSU** — versioned history of unions; uses a
  persistent segment tree. O(log n) per op.
- **DSU with rollback** — undo the most recent union. O(log n)
  per op with the half-edge trick.
- **DSU on trees** (small-to-large) — efficient subtree
  queries on trees. O(n log n) preprocessing, O(1) query.

## Real-world applications

- **Kruskal's MST** — sort edges by weight, add to the MST
  if their endpoints are in different DSU sets.
- **Network connectivity** — "is computer A in the same
  subnet as computer B?" → DSU query.
- **Image processing** — connected-component labeling
  (flood fill is essentially DSU on a grid).
- **Percolation theory** — does water reach from the top to
  the bottom of a random porous medium? Modeled as DSU.
- **Least Common Ancestor** (offline) — Tarjan's algorithm
  uses DSU.
- **Social network "friend of friend"** — keep merging
  friendship groups, query "are X and Y in the same group?".

## Related algorithms in cOde(n)

- **[graph_08 — Kruskal's MST](graph_08_kruskals-mst.md)** —
  DSU's most famous application. (d=6/10, r=8/10)
- **[graph_10 — Prim's MST](graph_10_prims-mst.md)** — the
  alternative MST algorithm (no DSU). (d=6/10, r=8/10)
- **[graph_11 — Cycle Detection](graph_11_cycle-detection.md)** —
  DSU detects cycles in O(V + E). (d=4/10, r=8/10)
- **[graph_12 — Bipartite Check](graph_12_bipartite-check.md)** —
  can also be done with DSU (alternate coloring).
  (d=4/10, r=8/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
