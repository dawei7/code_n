## General

**Interpret every restriction as an upper-bound cone**

If position `j` has upper bound $B_j$, the adjacent-difference limits imply

$$
a[i]\le B_j+\sum_{t=\min(i,j)}^{\max(i,j)-1}\texttt{diff}[t].
$$

The value can rise by at most each crossed edge limit. Position zero is an additional anchor with exact value—and therefore upper bound—zero.

The tightest possible upper bound at position `i` is the minimum cone value supplied by every anchor. The source computes these minima without comparing every position to every restriction.

**Initialize explicit anchors**

`bounds` begins with a very large sentinel at every position. `bounds[0]=0` installs the required starting value.

Each restriction applies `min(bounds[index],maximum)`. Indices are unique under the contract, but using `min` safely expresses that restrictions are upper bounds.

**Propagate left-side anchors forward**

For indices one through `n-1`:

`bounds[i] = min(bounds[i], bounds[i-1]+diff[i-1])`.

After this pass, `bounds[i]` is the tightest bound reaching `i` from any anchor at or to its left. The previous position has already combined all such anchors; crossing the next edge adds its allowed difference.

The anchor at zero guarantees every position becomes finite even if no explicit restriction lies before it.

For example, if the first two edge limits are three and five, the zero anchor alone gives provisional bounds zero, three, and eight. A tighter restriction farther right is not visible yet; that is the purpose of the reverse pass.

**Propagate right-side anchors backward**

The reverse pass applies

`bounds[i] = min(bounds[i], bounds[i+1]+diff[i])`.

Now each position also receives the tightest cone from every anchor to its right. A restriction cannot influence a position on the opposite side until this pass carries it backward.

After both passes, `bounds[i]` equals the minimum bound induced by all anchors.

The passes work because the domain is a line. Every anchor-to-position path approaches from exactly one direction, so it is summarized either by the forward or backward recurrence. A branching graph would require a general shortest-path propagation instead.

**Why the bound array itself is feasible**

The forward pass guarantees

$$
\texttt{bounds}[i]\le\texttt{bounds}[i-1]+\texttt{diff}[i-1].
$$

The backward pass guarantees the reverse inequality

$$
\texttt{bounds}[i-1]\le\texttt{bounds}[i]+\texttt{diff}[i-1].
$$

Together they imply the absolute adjacent difference is within the limit. Anchor zero remains zero because all other propagated values are nonnegative, and every restriction is respected by the minimum operation.

All bounds are nonnegative: anchors are nonnegative and propagation only adds positive edge limits. Therefore choosing `a=bounds` is a valid sequence.

**Why no valid sequence can exceed it**

Every valid sequence must remain below every anchor cone by repeatedly applying the adjacent-difference inequality along the unique line path. Hence `a[i]<=bounds[i]` for each position.

Since the complete `bounds` array is itself feasible, each upper bound can be attained simultaneously. Its maximum is both an upper limit for every valid sequence and achieved by this constructed sequence. Returning `max(bounds)` is exact.

This simultaneous attainability is crucial. Taking independent per-position upper bounds would not be enough if they violated adjacent differences, but the two directional inequalities show the envelope fits together as one legal sequence.

For the second example, the zero anchor limits early growth, the restriction at index three lowers nearby positions, and the backward/forward cones meet. After index three, the sequence may rise through successive edge limits to reach 12 at the final position.

The huge sentinel `10**30` is safely above every reachable legal bound under the constraints. It represents “no anchor seen yet” and disappears from all positions after zero's forward propagation.

## Complexity detail

Initializing the array costs $O(N)$, installing $R$ restrictions costs $O(R)$, and each directional pass costs $O(N)$. Total time is $O(N+R)$.

`bounds` stores $N$ integers, so auxiliary space is $O(N)$. The requested sequence is not separately constructed because `bounds` already serves as its achievable maximal envelope.

## Alternatives and edge cases

- **Compare every restriction with every position:** This costs $O(NR)$; two line sweeps combine all cones.
- **Forward pass only:** It misses restrictions located to the right of a position.
- **Backward pass only:** It misses the required zero anchor's influence to the right.
- **Propagate with the wrong edge:** Between `i` and `i+1`, the limit is `diff[i]`.
- **Treat restrictions as exact values:** They are upper bounds; the optimal envelope may place a position lower.
- **Ignore downward changes:** The absolute-difference rule constrains both directions, which the two inequalities enforce.
- **Restriction looser than propagated bound:** `min` leaves the tighter existing cone unchanged.
- **Maximum at an unrestricted position:** Intersecting cones can peak between or beyond restrictions.
- **Nonnegative requirement:** All computed bounds remain nonnegative from nonnegative anchors and positive additions.
- **Position zero:** Its exact value remains zero.
- **Input preservation:** Restrictions and differences are read only.
- **Large sentinel:** It is an initialization device, not a candidate returned after propagation.
- **Line structure:** Two sweeps are sufficient because every influence travels uniquely left or right.
