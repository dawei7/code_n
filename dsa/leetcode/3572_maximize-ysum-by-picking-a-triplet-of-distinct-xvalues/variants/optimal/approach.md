## General

For any fixed value $p$ in `x`, a valid triplet can use at most one index whose `x` value equals $p$. If it uses that group at all, choosing anything except the group's largest corresponding `y` can only decrease the sum without helping distinctness. Therefore, collapse every `x` group to its maximum `y` representative.

After this reduction, every retained value belongs to a different `x`, so the problem becomes choosing the three largest representatives. Maintain three variables in descending order while scanning the dictionary values. Each new representative is inserted into its proper position among those three, discarding anything smaller.

If fewer than three groups exist, no valid triplet can be formed. Otherwise, the three retained maxima are feasible because their groups are distinct, and no other triplet can have a larger sum: replacing any selected group representative by a lower value is never beneficial, and the three globally largest representatives dominate every other choice.

## Complexity detail

Let $n$ be the common array length and $u$ the number of distinct `x` values. Building the maximum-per-group dictionary takes expected $O(n)$ time under standard hash-table behavior. Scanning its $u$ values and maintaining three maxima takes $O(u)$ time, so total expected time is $O(n)$. The dictionary uses $O(u)$ space; the top-three state is constant-sized.

The benchmark uses $u=n=S$ with distinct `x` values in descending order. The accepted hash reduction and constant-size selection remain linear. The calibrated comparison-based alternative explicitly sorts the pairs and then the group maxima, adding a logarithmic factor.

## Alternatives and edge cases

- **Sort pairs by `x`:** Consecutive equal groups are easy to reduce after sorting, but comparison sorting costs $O(n\log n)$ rather than expected linear time.
- **Heap of every representative:** A size-three heap is linear because its capacity is constant; a heap containing all $u$ representatives uses unnecessary $O(u\log u)$ work.
- **Fewer than three distinct `x` values:** Return `-1` regardless of how many indices exist.
- **Repeated `x` with larger later `y`:** The stored group maximum must be updated; the earlier representative is then irrelevant.
- **Exactly three groups:** Their three maxima are forced and should all be summed.
- **More than three groups:** Only the three largest group maxima matter, not group frequency or original index order.
- **Positive bounds:** Zero is a safe sentinel below every legal `y` value when maintaining the top three.
