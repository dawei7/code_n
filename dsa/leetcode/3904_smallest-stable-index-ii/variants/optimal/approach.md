## General

**Precompute the information that comes from the right**

Evaluating the definition independently at every index would repeatedly scan almost the same prefixes and suffixes. That quadratic work is too expensive when the array contains up to $10^5$ elements. The suffix contribution can instead be prepared in one right-to-left pass.

Build `suffix_minimum` so that `suffix_minimum[i]` is the minimum value in `nums[i..n - 1]`. The final entry equals `nums[n - 1]`. For every earlier position, the relevant suffix consists of `nums[i]` followed by the suffix beginning at $i+1$, so its minimum is the smaller of `nums[i]` and `suffix_minimum[i + 1]`.

**Test candidates from smallest to largest**

Scan the array from left to right while maintaining `prefix_maximum`, the greatest value observed through the current index. At index $i$, this running value is exactly the maximum of `nums[0..i]`, and `suffix_minimum[i]` is exactly the minimum of `nums[i..n - 1]`. Their difference is therefore the defined instability score.

Return as soon as that score is at most `k`. Because the scan visits indices in ascending order, this first match is necessarily the smallest stable index. Reaching the end proves that every exact score exceeds `k`, so returning `-1` is correct.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The right-to-left suffix pass and the left-to-right candidate scan each take $O(N)$ time, so the total time is $O(N)$.

The suffix-minimum array stores $N$ integers. Apart from it, the algorithm uses constant state, giving $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Recompute both ranges for every index:** This directly implements the definition and produces correct scores, but its overlapping scans require $O(N^2)$ time.
- **Store prefix maxima too:** Two prepared arrays also give $O(N)$ time, but the prefix maximum only needs one running variable, so the second array is unnecessary.
- **Inspect only nearby elements:** A prefix maximum or suffix minimum can occur far from $i$; adjacent values do not determine the score.
- **Binary-search the first valid index:** The score sequence is not guaranteed to be monotone because the prefix maximum and suffix minimum can change at unrelated positions.
- **Inclusive ranges:** `nums[i]` belongs to both the prefix and suffix; excluding it from either range changes the contract.
- **Threshold equality:** A score exactly equal to `k` is stable because the comparison is inclusive.
- **Single element:** Both extrema equal the only value, so the score is zero and index `0` is stable.
- **No stable index:** A decreasing array can preserve one prefix-to-suffix gap at every position, making `-1` necessary.
- **Large inputs:** The $10^5$ length limit is the reason repeated range scans are not viable, while values and differences fit comfortably in standard wide integer types.
