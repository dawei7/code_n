## General

**Choose a center, then choose only helpful neighbors**

A star consists of one center and at most `k` of its adjacent nodes. The center is always present, so its value must be included even when negative. Neighbor participation is optional because the limit is “at most” `k` rather than “exactly” `k`.

For a fixed center, a neighbor with a negative value can only decrease the star sum. A zero-valued neighbor leaves the sum unchanged and is never needed to improve it. Therefore, an optimal star uses only positive neighbors, selecting up to the `k` largest positive values adjacent to its center.

The problem can consequently be solved independently for every possible center.

**Build lists of positive neighbor values**

The graph is undirected. For each edge `[a,b]`:

- if `vals[b]>0`, append `vals[b]` to `g[a]` because node `b` is a useful candidate neighbor for center `a`;
- if `vals[a]>0`, append `vals[a]` to `g[b]` for the reverse center-neighbor relationship.

The conditions depend on the neighbor's value, not the center's. A negative-valued node can still be a center, and it may become the best center if its positive neighbors compensate for it. Its negative value merely means it should not be included as an optional neighbor of another center.

Both edge directions are considered even though only positive endpoint values are stored. If both endpoints are positive, each endpoint appears in the other's list. If only one is positive, it appears only as a candidate for the other center.

`defaultdict(list)` makes an absent center behave as if it had an empty neighbor list.

**Sort each center's candidates from best to worst**

Every stored list `bs` is sorted in descending order. Then `g[i][:k]` contains exactly the first `k` entries, or the whole list if it has fewer than `k`.

Because every stored value is positive, taking more entries until the limit is reached always increases the sum. Thus the best choice for center `i` is:

$$
\texttt{vals}[i]
+
\text{sum of its largest }\min(k,p_i)\text{ positive neighbor values},
$$

where $p_i$ is its number of positive neighbors.

An exchange argument proves the top-choice rule. Suppose a selected neighbor has value $x$ while an unselected eligible neighbor has a larger value $y$. Replacing $x$ with $y$ preserves the edge limit and increases the star sum by $y-x$. Therefore, no optimal selection can omit a larger positive value in favor of a smaller one.

**Evaluate every node as the center**

The final generator enumerates `vals`. For node `i` with center value `v`, it computes

`v + sum(g[i][:k])`.

`max` returns the greatest center-specific optimum. Every valid star has one center, so it is included in exactly one of these center cases. Within that case, the sorted prefix is at least as good as its neighbor subset. Conversely, the selected prefix consists only of actual neighbors and contains at most `k` nodes, so it constructs a valid star.

These two facts show that the largest evaluated value is precisely the global maximum star sum.

**Why a star with zero edges is covered**

If `k=0`, every slice `[:0]` is empty and contributes zero, so the candidate for each center is just `vals[i]`. The result becomes the maximum individual node value.

The same happens for a center with no positive neighbors, even when `k>0`. This correctly models a star containing only its center.

**Trace the main sample**

For center 3, the adjacent nodes have values 2, 10, $-10$, and $-20$. Only 2 and 10 are stored. After descending sort, both are selected when `k=2`. Adding center value 4 gives $4+10+2=16$.

Negative neighbors are not used merely to fill two slots, because the rule allows fewer than two edges.

**Follow the actual implementation, not the heap summary**

The manifest summary describes maintaining a size-`k` min-heap. The stored Optimal solution does not do that. It accumulates all positive neighbor values and fully sorts every list. Both strategies select the same values, but their detailed runtime behavior differs and the explanation must match the executed source.

## Complexity detail

Let $n$ be the number of nodes and $m$ the number of edges. Graph construction processes each edge once and stores at most two positive-neighbor entries, using $O(n+m)$ time and $O(n+m)$ space including dictionary lists.

If center `i` stores $d_i^+$ positive neighbor values, sorting costs $O(d_i^+\log d_i^+)$. Summed over all centers, this is at most $O(m\log m)$ in the worst case. Evaluating slices and sums can inspect up to $\min(k,d_i^+)$ entries per center, for $O(n+m)$ total across stored entries. The overall exact bound is $O(n+m\log m)$, commonly simplified to $O(n+m\log m)$.

The manifest's $O(m\log(k+1))$ bound belongs to a bounded-heap implementation, not to these full sorts.

## Alternatives and edge cases

- **Size-`k` min-heaps:** Keep only the best `k` positive neighbors per center for $O(m\log(k+1))$ time; this matches the manifest summary but not the exact source.
- **Select then partition:** A linear-time selection algorithm can avoid fully sorting large neighbor lists, though it is more complex.
- **Negative center:** It must still be included, but sufficiently valuable positive neighbors may make its star optimal.
- **Negative neighbor:** Never include it because using fewer than `k` edges is allowed.
- **Zero neighbor:** It cannot improve the sum and may safely be omitted.
- **`k=0`:** Choose the maximum single node.
- **Isolated node:** Its only possible star contains itself.
- **Fewer than `k` positive neighbors:** Use all available positive ones.
- **Multiple edges:** The constraints describe graph edges; the algorithm assumes each edge represents one neighbor relationship.
- **Manifest mismatch:** Complexity analysis must account for sorting complete lists in the protected implementation.
