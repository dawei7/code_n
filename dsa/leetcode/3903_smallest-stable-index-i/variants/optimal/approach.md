## General

**Separate the two range aggregates**

At index $i$, the required prefix maximum depends only on positions at or before $i$, while the suffix minimum depends on positions at or after $i$. Recomputing both ranges independently for every candidate repeats most comparisons. Instead, prepare the information coming from the right once.

Create an array `suffix_minimum` such that `suffix_minimum[i]` equals the minimum of `nums[i..n - 1]`. Its final entry is `nums[n - 1]`; moving from right to left, each preceding entry is the smaller of `nums[i]` and `suffix_minimum[i + 1]`. This recurrence is exact because the suffix at $i$ consists of `nums[i]` followed by the suffix at $i+1$.

**Scan candidates in the order required by the answer**

Move from left to right while maintaining `prefix_maximum`, the maximum value seen so far. At index $i$, this running value is exactly the maximum of `nums[0..i]`, and the precomputed entry is exactly the minimum of `nums[i..n - 1]`. Their difference is therefore the defined instability score. Return immediately when it is at most `k`.

Because indices are tested in increasing order, the first accepted candidate is necessarily the smallest stable index. If the scan ends without returning, every index has been checked against its exact score and `-1` is correct.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Building the suffix minima and scanning the prefix each take $O(N)$ time, for $O(N)$ total time.

The suffix-minimum array contains $N$ integers and all other state is constant, so the auxiliary space is $O(N)$.

## Alternatives and edge cases

- **Simulate each definition literally:** Computing `max(nums[0..i])` and `min(nums[i..n - 1])` from scratch is correct but takes $O(N^2)$ time because the ranges heavily overlap.
- **Prefix maxima plus suffix minima:** Storing both arrays is also linear but uses two $O(N)$ arrays when the prefix maximum can be maintained in one variable.
- **Check only adjacent values:** The score depends on extrema anywhere in the complete prefix and suffix, so local neighbors cannot determine stability.
- **Binary-search the answer:** Instability scores need not be monotone as the index moves right, because the prefix maximum and suffix minimum can change at different positions.
- **Threshold equality:** A score equal to `k` is stable because the condition is less than or equal to the threshold.
- **Single element:** Its prefix maximum and suffix minimum are the same value, so its score is zero and index `0` is always stable.
- **All equal values:** Every score is zero; since `k` is non-negative, the smallest answer is immediately `0`.
- **No stable index:** A decreasing array can keep the same large prefix-to-suffix gap at every position, requiring `-1`.
- **Large values:** The score remains within the stated integer range, but implementations should subtract using the language's normal safe integer width.
