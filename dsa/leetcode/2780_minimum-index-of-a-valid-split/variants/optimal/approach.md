## General

A value that is dominant in both sides of a split must also be dominant in the complete array: adding the two strict inequalities for its left and right counts gives more than half of the total length. Because the contract guarantees exactly one dominant value in `nums`, every valid split must use that value.

Use Boyer-Moore majority voting to identify it. Maintain a candidate and a balance. Equal values add one vote and different values cancel one vote; whenever the balance reaches zero, the next value starts a new candidate. Since a strict majority exists, it cannot be completely cancelled and is the final candidate.

Count the candidate's total occurrences. Then scan possible split indices from left to right while maintaining its prefix count `left`. At index `i`, the left length is `i + 1`, the right length is `n - i - 1`, and the right count is `total - left`. The split is valid exactly when

$$
2\,\texttt{left} > i+1
\quad\text{and}\quad
2(\texttt{total}-\texttt{left}) > n-i-1.
$$

Return immediately when both inequalities hold. The scan order makes this the minimum valid index. If the scan ends, no valid split exists.

**Why checking only the global dominant value is sufficient**

Each non-empty array can have at most one value occurring more than half its length. If some value dominates both split parts, summing its occurrences shows that it dominates their concatenation. It must therefore be the unique dominant value already found for `nums`. No other candidate needs to be tested.

## Complexity detail

Boyer-Moore voting, the total-frequency count, and the split scan each take $O(n)$ time. The algorithm stores only the candidate, balances, counts, lengths, and loop index, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Frequency map:** Counting every value also identifies the dominant element in $O(n)$ time, but requires $O(n)$ additional space in the worst case.
- **Sorting:** The middle sorted value is the dominant candidate, but sorting costs $O(n\log n)$ time and may mutate the input.
- **Recount each side:** Computing fresh frequencies for every split is correct but takes $O(n^2)$ time.
- **Single element:** No index satisfies $i < n-1$, so the answer is `-1` even though the lone value is dominant.
- **Strict majority:** A count equal to exactly half a part's length is not dominant; both comparisons must use `>`, not `>=`.
- **Minimum index:** Return at the first valid split rather than continuing to search.
- **All values equal:** When $n \ge 2$, splitting after index `0` is immediately valid.

