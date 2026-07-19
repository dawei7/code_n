## General
**Reserve the cheapest piles for Bob**

Exactly $G$ piles go to each participant. Bob's pile only needs to be no larger than the two piles paired with it, so assigning him any large pile wastes value that could instead support your score. An exchange makes this precise: if Bob receives a pile larger than some pile assigned to Alice or you in another group, swapping those piles preserves the required order in a suitable regrouping and cannot reduce your total. Therefore an optimal arrangement can give Bob the smallest $G$ piles.

**Pair the remaining piles from largest to smallest**

The largest $2G$ piles remain for Alice and you. Sort them and pair adjacent values from the high end. In each pair Alice must take the larger value and you receive the smaller one. Pairing a very large pile with a much smaller eligible pile would only lower your gain; exchanging partners so nearby ranks are paired raises or preserves the smaller values awarded to you.

Thus, in the full ascending order, skip the smallest third, then take every other value beginning at index $G$. Equivalently, working downward, skip the current largest pile for Alice, take the next one for yourself, and repeat $G$ times. The unused smallest piles are assigned to Bob, one per pair.

## Complexity detail
Sorting $N$ pile values takes $O(N\log N)$ time. Summing every other value in the upper two-thirds takes $O(N)$ additional time, so sorting dominates.

The implementation uses a separate sorted list, requiring $O(N)$ auxiliary space. An in-place sort can reduce language-dependent auxiliary storage, but the canonical implementation preserves its input and states the explicit copied-list bound.

## Alternatives and edge cases
- **In-place sorting:** mutate `piles` and use the same rank selection. This avoids the explicit copy but changes the caller's array and still depends on the language's sorting workspace.
- **Repeated extrema extraction:** repeatedly remove the largest for Alice, the next-largest for you, and the smallest for Bob. It is correct but array searches and removals make it quadratic.
- **Counting sort:** pile values are at most $10^4$, so a frequency table can select ranks in $O(N+10^4)$ time. It is asymptotically faster for this bounded value domain but more specialized.
- **Single group:** with three piles, you necessarily receive the median.
- **Duplicate sizes:** equal values may be assigned to either player without changing the total; rank multiplicities remain valid.
- **All piles equal:** every one of your $G$ piles has the common value.
- **Large outliers:** Alice consumes one pile from each upper pair, preventing you from simply taking the globally largest $G$ piles.
