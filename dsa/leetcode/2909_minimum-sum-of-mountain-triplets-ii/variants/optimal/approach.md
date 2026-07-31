## General

**Reduce each peak to two range minima.** Once an index $j$ is chosen as the middle, the best left endpoint is the minimum value among indices before $j$, and the best right endpoint is the minimum value among indices after $j$. If either minimum is not strictly smaller than `nums[j]`, then no endpoint on that side can make $j$ a valid peak.

**Reuse the side information.** Build `suffix_minimum` from right to left so `suffix_minimum[j + 1]` gives the best possible right value for peak $j$. Scan candidate peaks from left to right while maintaining `prefix_minimum`, the best value strictly before the current index. Each peak can then be validated and scored in constant time instead of rescanning either side.

Whenever both strict comparisons hold, the chosen indices have the required order because the minima come from disjoint prefix and suffix ranges. Their values give the least sum possible for that fixed peak. Conversely, any valid mountain triplet has a middle index visited by the scan, and replacing its endpoints with the corresponding range minima preserves validity while never increasing the sum. Therefore the minimum recorded candidate is globally optimal. If no candidate is recorded, no valid peak exists.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The suffix construction and peak scan are each linear, so the running time is $O(n)$. The suffix-minimum array stores $n$ values, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Scan both sides for every peak:** Directly finding compatible minima for each middle index uses $O(n^2)$ time. It avoids an auxiliary array but cannot scale to $n=10^5$.
- **Enumerate every triplet:** Checking all $\binom{n}{3}$ index triples takes $O(n^3)$ time and is far beyond the input limit.
- **Two full minimum arrays:** Storing both prefix and suffix minima is also $O(n)$ time and space, but the prefix side can be maintained in one variable.
- **Equal values:** A side value equal to the peak fails the required strict comparison.
- **Nonconsecutive indices:** Only the ordering $i<j<k$ matters; adjacency is not required.
- **Large values:** A valid sum can reach $3\cdot 10^8$, which fits ordinary Python integers without special handling.
- **No compatible peak:** Return `-1` even when smaller pairs exist; the result requires three indices.
