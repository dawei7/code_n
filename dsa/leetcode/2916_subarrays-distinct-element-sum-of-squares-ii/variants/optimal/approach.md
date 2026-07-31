## General

**Represent all subarrays ending at one position.** After processing index
`right`, associate each possible start `left` with the number $d_{left}$ of
distinct values in `nums[left:right + 1]`. The contribution of this right
endpoint is $\sum_{left=0}^{right} d_{left}^2$. Adding that quantity after every
right endpoint counts each non-empty subarray exactly once.

**Use the previous occurrence to identify one range change.** Suppose the new
value last appeared at position $p$, or let $p=-1$ if it has not appeared.
For starts at or before $p$, the old occurrence already made the value
distinct, so their counts do not change. For starts in $[p+1,\texttt{right}]$,
the new position introduces the value for the first time. Consequently, moving
to the next right endpoint is exactly a range increment by one.

**Maintain both first and second moments.** A lazy segment tree stores the sum
of all $d_{left}$ values and the sum of their squares in every node. If every
value in a node of length $m$ increases by $v$, then

$$
\sum (d+v)^2 = \sum d^2 + 2v\sum d + mv^2.
$$

This identity updates both aggregates without visiting individual starts.
After the last-occurrence range is incremented, the root's squared sum is
precisely the contribution for the current right endpoint. Lazy propagation
preserves the same transformation for descendants when a later partial update
needs them. Thus every root value is correct, and accumulating those root
values produces the required total.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each position performs one hash-table
lookup and one lazy segment-tree range update in $O(\log n)$ time, for
$O(n\log n)$ total time. The segment tree arrays and the last-position map
both use $O(n)$ auxiliary space. Arithmetic is reduced modulo $10^9+7$ after
each aggregate update.

## Alternatives and edge cases

- **Enumerate every subarray with a set:** Extending a set from each left endpoint is straightforward but takes $O(n^2)$ time in the worst case, which is too slow for $n=10^5$.
- **Recompute distinct counts independently:** Scanning each subarray from scratch repeats even more work and can require $O(n^3)$ time.
- **Binary indexed tree formulations:** Multiple Fenwick trees can encode the same range-update algebra, but coordinating the squared term is less direct than storing both moments in a lazy segment tree.
- **Repeated current value:** Only starts strictly after its previous position gain a new distinct value; including earlier starts would count that value twice.
- **All values equal:** Every non-empty subarray has score one, and each update affects only the newest start after the previous occurrence.
- **All values distinct:** Every update begins at zero, so a subarray's distinct count equals its length.
- **Modulo arithmetic:** The first moments, squared moments, and accumulated answer must all be reduced to keep intermediate aggregates bounded.

