## General

Removing a prefix of length `k` leaves exactly the suffix `nums[k:]`. Minimizing the removed length is therefore equivalent to finding the longest suffix that is already strictly increasing: its starting index is the answer.

The last element by itself is strictly increasing, so begin there. Move the suffix boundary left while the newly included adjacent pair satisfies `nums[suffix_start - 1] < nums[suffix_start]`. Each successful move preserves strict increase throughout the enlarged suffix. Stop at the first pair that is equal or decreasing, or return `0` if the scan reaches the beginning.

The suffix beginning at the returned boundary is strictly increasing because every one of its adjacent pairs was checked successfully. If the boundary is greater than zero, the scan stopped because `nums[suffix_start - 1] >= nums[suffix_start]`. Any shorter removed prefix would retain both members of that violating pair, so its remaining array could not be strictly increasing. Thus the boundary is feasible and no smaller prefix length is feasible.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The backward scan inspects each adjacent pair at most once, so it takes $O(N)$ time. It stores only the suffix boundary and uses $O(1)$ auxiliary space.

The benchmark defines size as $N$ and joins two increasing runs with one equal adjacent pair at the midpoint. The backward scan traverses the entire second run before stopping at that equality, so it performs linear work. A slower method that tests prefix lengths from zero upward repeatedly scans to the same midpoint violation for every shorter candidate, taking $O(N^2)$ time.

## Alternatives and edge cases

- **Forward last-violation scan:** The answer is one position after the last index `j` satisfying `nums[j] >= nums[j + 1]`; recording that position in a forward pass also takes $O(N)$ time and $O(1)$ space.
- **Test every prefix length:** Checking each remaining suffix independently follows the definition but repeats comparisons and can require $O(N^2)$ time.
- **Sort the remaining values:** Sorting changes their order and does not model prefix removal; the suffix must retain its original sequence.
- **Already strictly increasing:** Every adjacent comparison succeeds, the scan reaches index `0`, and the empty prefix is optimal.
- **Single element:** A one-element array is strictly increasing, so the answer is `0`.
- **Equal neighbors:** Equality is a violation because the required order is strictly increasing, not non-decreasing.
- **Strictly decreasing input:** Only the final element forms an increasing suffix, so the answer is $N-1$.
- **Several violations:** Only the rightmost violation determines the longest increasing suffix; all earlier violations lie inside the removed prefix.
- **Extreme values:** Comparisons remain valid at both numeric bounds; no arithmetic on the values is required.
