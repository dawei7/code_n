## General
**A monotone capped sum**

For a candidate cap $v$, define the mutated sum as the sum of `min(element, v)` over the array. This function never decreases as $v$ increases: raising the cap can only preserve or increase each contribution. Therefore binary search can find the smallest cap whose mutated sum is at least `target`.

Search the inclusive value range from 0 through $M$. For a midpoint, compute its capped sum in one array scan. If that sum is below the target, every smaller cap is also below it, so move the lower boundary above the midpoint. Otherwise retain the midpoint as a possible first cap reaching or exceeding the target.

When the search ends at cap `high`, the best answer must be either `high` or `high - 1`. All smaller caps have sums no closer from below than `high - 1`, and all larger caps have sums no closer from above than `high`. Evaluate both sums explicitly and choose the lower cap when their absolute differences tie.

If the target exceeds the unmodified array sum, the search reaches $M$; increasing the cap beyond $M$ cannot change the array, so returning $M$ is the smallest value producing that closest sum.

## Complexity detail
Each capped-sum evaluation takes $O(n)$ time, and binary search performs $O(\log M)$ evaluations, for $O(n \log M)$ total time. The search keeps only scalar boundaries and sums, using $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every cap:** Testing every integer from 0 through $M$ is correct but takes $O(nM)$ time.
- **Sort and consume a prefix:** Efficient sorting enables a prefix-sum derivation in $O(n \log n)$ time and $O(n)$ space, but modifies or copies the input; using selection sort instead degrades this route to $O(n^2)$.
- **Tie between adjacent caps:** Compare both sides of the binary-search crossing and explicitly prefer the smaller cap.
- **Target above the original sum:** Return $M$, the smallest cap that leaves every element unchanged.
- **Answer zero:** A very small target can make cap 0 tie with cap 1; the tie rule then permits 0 even though input values are positive.
- **Answer absent from `arr`:** The optimal cap may lie strictly between two input values.
