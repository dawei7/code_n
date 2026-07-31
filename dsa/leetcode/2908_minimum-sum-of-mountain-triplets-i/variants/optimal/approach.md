## General

**View each middle index as the peak.** For a fixed $j$, a valid left endpoint may be any earlier index whose value is smaller than `nums[j]`, and a valid right endpoint may be any later index with the same strict relation. Because the objective is a minimum sum, only the smallest value on each side can ever be useful for that peak.

**Precompute the right-side choices.** Build `suffix_minimum` from right to left so that `suffix_minimum[j + 1]` is the smallest value strictly after $j$. During a left-to-right scan, maintain `prefix_minimum` as the smallest value strictly before $j$. This supplies both best side values in constant time for every possible middle index.

When both minima are strictly smaller than `nums[j]`, their indices lie on the correct sides by construction, so the three values form a mountain triplet. They also give the minimum sum among all triplets with peak $j$: replacing either minimum by any other compatible side value cannot lower the sum. Every mountain triplet has exactly one middle index considered by the scan, so the least candidate over all peaks is the global answer. If no peak passes both strict comparisons, no mountain triplet exists.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Constructing suffix minima and scanning the candidate peaks each take $O(n)$ time, for $O(n)$ total time. The suffix-minimum array stores $n$ values, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Scan both sides for every peak:** Finding the minimum compatible value on each side with nested scans uses $O(n^2)$ time and $O(1)$ auxiliary space. It is acceptable for this small constraint but repeats work.
- **Enumerate every triplet:** Testing all index triples takes $O(n^3)$ time and obscures the fact that each side can be minimized independently once the peak is fixed.
- **Equal values:** Both side comparisons are strict. A side value equal to the peak cannot participate.
- **Nonconsecutive indices:** The three selected positions only need increasing indices; intervening elements are irrelevant.
- **Minimum length:** With exactly three elements, there is only one possible index triplet.
- **No peak with two smaller sides:** Return `-1`; an increasing or decreasing pair alone is insufficient.

