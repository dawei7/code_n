## General

Although a move may jump to any index, the strictly increasing values place all indices on a line. Any direct jump cost equals the sum of the adjacent value gaps crossed by that jump. Replacing a jump with adjacent moves can only make it cheaper, because every adjacent move always has its ordinary gap cost available and may instead receive the special cost 1.

Therefore a minimum route can be evaluated as a sum of directed adjacent-edge costs. The source precomputes one prefix sum for moving right and another for moving left, then answers each query by subtraction.

**Adjacent value gaps**

For edge between indices $i-1$ and $i$, define

$$
d_i=\texttt{nums}[i]-\texttt{nums}[i-1].
$$

Strict increase guarantees $d_i>0$. A normal move across this edge in either direction costs $d_i$.

The special closest-neighbor move may reduce one direction to cost 1. Because closest choice belongs to the departure index, the cost from $i-1$ to $i$ can differ from the cost from $i$ to $i-1$.

**Cost of moving right across one edge**

Consider departure index $i-1$ and destination $i$.

If $i-1=0$, the departure has only one adjacent neighbor, so index $i$ is automatically closest and the cost is 1.

For an interior departure, compare:

- left gap $d_{i-1}=\texttt{nums}[i-1]-\texttt{nums}[i-2]$;
- right gap $d_i=\texttt{nums}[i]-\texttt{nums}[i-1]$.

The right neighbor is closest only when

$$
d_i<d_{i-1}.
$$

If the gaps tie, the problem chooses the smaller index, which is the left neighbor, so moving right does not receive the special cost.

The source's `c1` is:

$$
c_i^{\rightarrow}
=
\begin{cases}
d_i,&i>1\text{ and }d_{i-1}\le d_i,\\
1,&\text{otherwise}.
\end{cases}
$$

The first branch means the left neighbor is closer or wins the tie, so the best rightward edge move is the ordinary gap cost. The second means the right neighbor is uniquely closest, or the departure is the left endpoint.

**Cost of moving left across one edge**

Now depart from index $i$ toward $i-1$.

If $i=n-1$, the departure is the right endpoint and has only the left neighbor, so cost is 1.

At an interior index $i$, compare left gap $d_i$ with right gap $d_{i+1}$. The left neighbor is closest when

$$
d_i\le d_{i+1}.
$$

Equality chooses the smaller index $i-1$, so unlike the rightward case, the tie does receive the special cost.

The source's `c2` is:

$$
c_i^{\leftarrow}
=
\begin{cases}
d_i,&i<n-1\text{ and }d_i>d_{i+1},\\
1,&\text{otherwise}.
\end{cases}
$$

This exactly encodes the asymmetric tie rule.

**Why arbitrary jumps are unnecessary**

Suppose a route includes a normal jump from index $a$ to a larger index $b$. Its cost is

$$
\texttt{nums}[b]-\texttt{nums}[a]
=
\sum_{i=a+1}^{b}d_i.
$$

Traversing the same interval one adjacent edge at a time costs at most that sum because each directed adjacent edge costs either its gap $d_i$ or the cheaper special cost 1. The same argument holds for a jump to the left.

After replacing all arbitrary jumps, the problem becomes shortest path on a directed line with positive edge costs.

Any path from $l<r$ that backtracks crosses some adjacent edge in both directions before eventually crossing it toward the destination again. Removing that positive-cost excursion cannot hurt reachability and strictly reduces cost. Hence an optimal path moves monotonically right through each edge once. For $l>r$, it moves monotonically left.

There is no need for Dijkstra's algorithm per query.

**Directional prefix sums**

`s1[i]` stores the cost to move monotonically right from index 0 to index $i$:

$$
\texttt{s1}[i]
=
\sum_{t=1}^{i}c_t^{\rightarrow}.
$$

Thus for $l<r$:

$$
\operatorname{cost}(l,r)
=
\texttt{s1}[r]-\texttt{s1}[l].
$$

`s2[i]` stores the sum of leftward edge costs for edge indices 1 through $i$:

$$
\texttt{s2}[i]
=
\sum_{t=1}^{i}c_t^{\leftarrow}.
$$

Moving from $l$ down to $r<l$ crosses edge indices $l,l-1,\ldots,r+1$, so:

$$
\operatorname{cost}(l,r)
=
\texttt{s2}[l]-\texttt{s2}[r].
$$

When $l=r$, the source uses the second expression and subtracts an entry from itself, returning zero.

**Example**

For `nums = [-5,-2,3]`, the gaps are 3 and 5.

- Rightward edge $0\to1$ is closest from endpoint 0, costing 1.
- From index 1, the left gap 3 is smaller than right gap 5, so $1\to2$ costs the ordinary 5.
- Leftward from endpoint 2 to 1 costs 1.
- From index 1, left is closest, so $1\to0$ also costs 1.

Thus query $0\to2$ costs $1+5=6$, while $2\to0$ costs $1+1=2$.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and $Q=\lvert\texttt{queries}\rvert$.

The preprocessing loop computes two directed edge costs and two prefix entries for each of the $N-1$ adjacent edges, costing

$$
O(N)
$$

time.

Each query uses one comparison and one prefix subtraction, so all queries cost $O(Q)$.

Total time is

$$
O(N+Q).
$$

The two prefix arrays each contain $N$ integers, using

$$
O(N)
$$

auxiliary space. The answer array uses $O(Q)$ required output space.

No graph is explicitly built, and neither input array is modified.

## Alternatives and edge cases

- **Dijkstra per query:** Model every allowed move explicitly, but the complete direct-jump graph is dense and repeated shortest-path searches are unnecessary on the ordered line.
- **Use only absolute differences:** This misses closest-neighbor moves whose cost 1 is cheaper than the adjacent gap.
- **One undirected edge cost:** Incorrect because closest status belongs to the departure index; the two directions may have different costs.
- **Tie at an interior index:** The smaller adjacent index wins, making a left move special and a right move ordinary.
- **Left endpoint:** Its only neighbor is closest, so the first rightward edge costs 1.
- **Right endpoint:** Its only neighbor is closest, so the last leftward edge costs 1.
- **Adjacent gap equal to one:** Normal and special moves both cost 1, so either interpretation yields the same edge weight.
- **Same query endpoints:** No movement is needed, and prefix subtraction returns zero.
- **Negative values:** Strict ordering keeps every adjacent gap positive; absolute move costs depend on differences, not signs.
- **Direct long jump:** Its cost decomposes into adjacent gaps and can always be matched or improved by adjacent traversal.
- **Input preservation:** The source only reads `nums` and `queries` while constructing separate prefixes and output.
