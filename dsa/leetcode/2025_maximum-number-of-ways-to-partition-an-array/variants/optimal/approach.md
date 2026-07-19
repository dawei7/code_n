## General
**Encode each pivot by its balance**

For a pivot with left sum $L$ and right sum $R$, define its balance as
$D = L - R$. The pivot is valid exactly when $D = 0$. Compute every original
balance and count them; the count of zero already covers the option of making
no change.

**Derive how one replacement changes a balance**

Suppose index `i` changes by `delta = k - nums[i]`. For a pivot at or before
`i`, the changed value lies on the right, so the new balance is
$D - \text{delta}$ and becomes zero when $D = \text{delta}$. For a pivot after
`i`, the value lies on the left, so the new balance is
$D + \text{delta}$ and becomes zero when $D = -\text{delta}$.

**Sweep the possible changed index**

Maintain two frequency maps. The left map contains balances for pivots at or
before the current index; the right map contains balances for pivots after it.
For each possible replacement, its valid-pivot count is therefore
`left[delta] + right[-delta]`. Before advancing to the next index, transfer the
crossed pivot from the right map to the left map.

Each pivot is always stored on the side that matches whether the current
replacement lies to its right or left. The two lookup equations are exactly
the conditions that make its adjusted balance zero. Thus every candidate
replacement counts all and only its valid pivots, while the initial zero count
represents leaving the array unchanged. Taking the maximum covers every
allowed choice.

## Complexity detail
Computing the $N - 1$ balances, sweeping $N$ replacement positions, and
transferring each balance once take $O(N)$ expected time with hash maps. At
most $N - 1$ distinct balances are stored, so the space usage is $O(N)$.

## Alternatives and edge cases
- **Recompute every replacement:** Trying each index and rescanning all pivots
  is direct but takes $O(N^2)$ time.
- **Sorted balances:** Balanced search trees can replace hash maps, yielding
  $O(N\log N)$ time with deterministic lookup bounds.
- Leaving the array unchanged may be strictly better than every replacement.
- Replacing a value already equal to `k` has `delta = 0` and preserves every
  original balance.
- Pivots never occur before index `0` or after the final element; there are
  exactly $N - 1$ candidates.
- Negative values and totals require ordinary integer sums, not absolute
  differences.
