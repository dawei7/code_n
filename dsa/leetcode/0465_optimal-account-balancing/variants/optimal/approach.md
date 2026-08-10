## General

The original transaction graph contains more detail than settlement needs. If one person paid several people and received money from others, only that person's final net balance matters. Any settlement that makes every net balance zero resolves all original obligations, regardless of which historical edge created them.

The exact solution first compresses all transactions into nonzero account balances, then uses subset dynamic programming to partition those accounts into zero-sum groups. A zero-sum group of `q` people can be settled in at most `q - 1` transactions. Splitting accounts into more independent zero-sum groups can lower the total, so the DP searches every such partition.

**Build net balances**

For transaction `[f, t, x]`, person `f` gave away `x` and receives balance change `-x`; person `t` received it and gets `+x`. The dictionary updates are therefore

`g[f] -= x` and `g[t] += x`.

The sign convention could be reversed as long as it were used consistently. What matters is that every transaction adds opposite amounts, so the sum of all balances remains zero.

People whose final balance is zero require no settlement and are removed. `nums` contains only the `k` nonzero balances. Person identifiers are no longer needed because settlement cost depends on amounts, not labels.

**Represent groups by masks**

With `k = len(nums)`, a mask from `0` through `2^k - 1` represents a subset of outstanding accounts. Bit `j` is set when `nums[j]` belongs to the subset.

`f[mask]` is the minimum number of transactions needed to settle exactly that subset as a collection of independent zero-sum groups. It begins at infinity because most arbitrary subsets do not sum to zero and cannot be settled internally. The empty subset needs no transactions, so `f[0] = 0`.

For every nonempty mask, the code scans all balances and computes its sum. Only a zero-sum subset receives a finite result. This is necessary: if a subset's balances do not total zero, money must cross between it and its complement, so it is not a self-contained settlement group.

**Why a zero-sum group needs at most `q - 1` transfers**

Take a zero-sum group with `q` nonzero balances. Repeatedly choose one debtor and one creditor and transfer the smaller remaining absolute amount between them. Every transfer clears at least one person's balance. After at most `q - 1` transfers, all but possibly one balance are zero; the last is automatically zero because the group's sum is zero.

Thus a mask with `q = mask.bit_count()` accounts has the valid baseline

$$
q-1
$$

transactions. This treats the whole subset as one group. It may not be minimal because the subset might split into several smaller zero-sum groups.

**Enumerate every proper submask**

For a zero-sum mask `i`, the code begins with

`j = (i - 1) & i`

and repeatedly applies

`j = (j - 1) & i`.

This standard bit trick visits every nonempty proper submask `j` of `i` exactly once. The complement within `i` is `i ^ j`, because all bits of `j` are also bits of `i`.

The recurrence tries

$$
f[i]=\min\bigl(f[i],\ f[j]+f[i\mathbin{\char94}j]\bigr).
$$

If either part is not internally zero-sum, its DP value remains infinity and cannot improve the answer. If both are finite, combining their independent settlements yields a valid settlement of `i`. Since `i` itself sums to zero, one zero-sum part automatically implies its complement also sums to zero.

**Why the recurrence finds the true minimum**

Any valid optimal settlement can be viewed as connected components in a graph whose vertices are accounts and whose edges are new transactions. Money never needs to cross between components, so each component's original net balances sum to zero. A component with `q` vertices needs at least `q - 1` transaction edges to be connected and can be settled with that many.

Therefore an optimal answer corresponds to partitioning the outstanding accounts into zero-sum groups and summing `group size - 1` over them.

The DP includes the one-group baseline for every zero-sum mask. It also tries every way to divide that mask into two submasks, and previously computed values already contain every further recursive partition of those parts. Thus every zero-sum partition is considered. Conversely, every finite combination made by the recurrence consists only of valid zero-sum groups, so it never invents an impossible settlement. Taking the minimum gives exactly the optimal transaction count.

The full mask is guaranteed to sum to zero because every original transfer contributed equal and opposite balance changes. Therefore `f[-1]`, the last DP entry, is always finite and is the required answer.

**Trace the first example**

Transactions `[0,1,10]` and `[2,0,5]` create balances `0: -5`, `1: +10`, and `2: -5`. No proper nonempty subset sums to zero. The full three-person mask has zero sum and uses its baseline `3 - 1 = 2`, so two settlement transactions are necessary.

In the second example, netting collapses all history to person `0: -4`, person `1: +4`, and person `2: 0`. The zero account is removed, leaving two opposite balances. Their full mask costs `2 - 1 = 1` transaction.

## Complexity detail

Let $n$ be the number of input transactions, $p$ the number of distinct people, and $k$ the number of nonzero balances.

Netting takes expected $O(n)$ time and $O(p)$ dictionary space. Computing a balance sum by scanning all `k` values for every mask costs $O(k2^k)$ time.

Across all masks, enumerating all submasks has total complexity $O(3^k)$: for each account, a term in a mask/submask pair can be outside the mask, inside the mask but outside the submask, or inside both. The overall time is therefore $O(n+k2^k+3^k)=O(n+3^k)$.

The DP array contains $2^k$ entries, while balances and the account map use $O(k+p)$ space. Total auxiliary space is $O(p+2^k)$.

This differs from the current manifest, which describes symmetry-pruned backtracking with $O(n+k!)$ time and $O(p+k^2)$ space. The exact optimal source is subset DP, so the bounds above are the faithful ones.

## Alternatives and edge cases

- **Settle the first outstanding balance by backtracking:** Pair it with each opposite-sign balance, recurse, and backtrack. Strong pruning works well for small `k`, but it is a different algorithm from the exact subset DP.
- **Greedily match largest debtor and creditor:** It produces a valid settlement but can miss a partition with fewer total transactions.
- **Keep original transaction edges:** Historical relationships do not constrain new settlement transfers; net balances are the sufficient state.
- **All balances cancel individually:** After netting, `nums` is empty, `f` contains only `f[0] = 0`, and the answer is zero.
- **Zero-balance people:** They are excluded because they need no transaction and would only enlarge the exponential state space.
- **One nonzero balance:** This cannot occur after correct netting because all balances sum to zero.
- **Repeated balance amounts:** Masks distinguish people by position even when amounts match; different groupings are still considered.
- **Full-mask feasibility:** Equal-and-opposite transaction updates guarantee its sum is zero.
- **Subset enumeration duplication:** Both `j` and its complement are visited, so partitions may be evaluated twice. This affects constants but not correctness or the $O(3^k)$ bound.
- **Manifest mismatch:** The approach intentionally explains the executable subset DP rather than the unrelated backtracking summary.
