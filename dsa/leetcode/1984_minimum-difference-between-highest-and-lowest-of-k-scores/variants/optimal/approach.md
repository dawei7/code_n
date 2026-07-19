## General
**Sort scores to expose their rank order**

Sort the scores into non-decreasing order. For any selection of `k` students,
only its smallest and largest scores determine its spread. In sorted order,
those two extremes delimit an interval containing every score ranked between
them.

**Why an optimum is a consecutive window**

Suppose a chosen set skips a score lying between its selected minimum and
maximum. Replacing an extreme selected score with such an interior score cannot
increase the spread. Repeating this exchange yields `k` consecutive sorted
positions whose spread is no larger. Therefore at least one optimal selection
appears as a contiguous sorted window of length `k`.

**Scan every fixed-width window**

For each possible starting index `i`, the window ends at `i + k - 1`, and its
spread is computed as
`ordered[i + k - 1] - ordered[i]`. Take the minimum over all such windows.
This examines every form an optimal selection needs to take, so the smallest
recorded spread is globally optimal.

## Complexity detail
Sorting $N$ scores costs $O(N\log N)$ time. The subsequent scan examines
$N-k+1$ windows in $O(N)$ time, so sorting dominates. Keeping a separate sorted
copy uses $O(N)$ space. An in-place sort may reduce explicit array storage, but
the sorting implementation can still require auxiliary memory.

## Alternatives and edge cases
- **Enumerate all selections:** Checking every group of `k` positions is
  correct but can require $\binom{N}{k}$ selections.
- **Enumerate all pairs when `k = 2`:** Comparing every score pair takes
  $O(N^2)$ time, while sorting reveals that only adjacent scores matter.
- **Repeatedly extract minima:** Selecting successive ranks without a full sort
  can be made correct, but a naive repeated scan also incurs quadratic work.
- When `k = 1`, every one-score selection has spread `0`.
- When `k = N`, every score is forced, so the answer is the overall maximum
  minus the overall minimum.
- Duplicate scores can produce answer `0` whenever at least `k` equal values
  occur.
- Input order has no effect on the result because students may be selected from
  arbitrary positions.
