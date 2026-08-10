## General

The source reconstructs denominations in increasing order. Before processing amount `a`, `ways[a]` is the number of combinations produced by all already recovered denominations smaller than `a`.

A new denomination equal to `a` can change the number of ways to form amount `a` by exactly one: the new combination consisting solely of coin `a`. This makes the decision forced.

**Initial coin-change state**

`ways[0]=1` represents the one way to make zero: choose no coins. Every positive amount initially has zero ways.

`denominations` begins empty and is naturally sorted because candidate amounts are visited from one through `n`.

**Forced decision at each amount**

Let `target=numWays[a-1]`.

If `ways[a]==target`, denomination `a` must be absent. Adding it would create one extra way for amount `a` and violate the target.

If `ways[a]+1==target`, denomination `a` must be present. Its single-coin combination accounts for exactly the missing one way.

If the difference is anything else, reconstruction is impossible. Denominations greater than `a` cannot help form amount `a`, and a unique denomination `a` can add neither zero when present nor more than one direct way at its own amount. The source returns an empty list.

**Why a coin a adds exactly one way at amount a**

All coin values are positive. A combination using new coin `a` and totaling `a` can contain exactly one such coin and no other positive coin. Therefore `[a]` is its only new combination at that amount.

Uniqueness of returned denominations prevents adding multiple coin types with the same value.

**Updating future amounts**

When `a` is recovered, the ascending loop:

`ways[total] += ways[total-a]`

for `total=a,...,n` is the standard unbounded coin-change transition.

Ascending order is essential. After updating `ways[a]`, a later total such as `2a` can reuse that updated value, representing two copies of coin `a`. Thus infinite supply is modeled.

Processing denominations in increasing order counts combinations rather than permutations. A multiset such as coins two and four is added once, not again for reversed selection order.

**Inductive correctness**

Before amount `a`, assume recovered denominations below `a` are the only set consistent with all earlier targets, and `ways` gives their combination counts.

Larger denominations cannot affect amounts through `a`. The comparison at `a` therefore uniquely determines whether coin `a` exists, or proves no solution. If it exists, the unbounded update correctly incorporates it into every future amount while leaving earlier amounts unchanged.

By induction, after the final amount, all target counts match the unique recovered denomination set. The returned list is sorted and unique.

**Why later validation is still necessary**

Adding a forced denomination changes many future counts. A future target may contradict those implied combinations, at which point the source returns empty. Matching early entries alone is not sufficient.

For example, an unexpectedly large target difference greater than one at its first disagreement cannot be repaired by that amount’s single possible denomination.

## Complexity detail

The outer loop visits `n` amounts. Every recovered denomination performs an update over at most `n` totals. In the worst case this is `O(n^2)` time.

`ways` has `n+1` entries and the result can contain `n` denominations, so auxiliary/result storage is `O(n)`.

## Alternatives and edge cases

- **Backtracking over denomination subsets:** There are `2^n` possible sets; the increasing forced-choice invariant avoids exponential search.
- **Generating functions:** Coin-change counts correspond to a product of reciprocal polynomials. Algebraic factor recovery is possible but far more complex than this coefficient-by-coefficient reconstruction.
- **Target equals current ways:** Coin `a` must be absent, not merely optional.
- **Target equals current plus one:** Coin `a` is forced.
- **Target below current ways:** Existing smaller coins already create too many combinations, so no later coin can remove them.
- **Target more than one above current:** Coin `a` can add only its singleton combination at amount `a`, so impossible.
- **Coin one:** If present, amount one target must be exactly one; its ascending update then creates repeated-one combinations for all future totals.
- **Zero target:** It is valid when recovered smaller coins cannot form that amount.
- **Infinite supply:** Ascending totals allow the new denomination to reuse itself.
- **Combination order:** Denomination-by-denomination updates avoid counting order permutations.
- **Maximum denomination n:** It affects only `ways[n]` within the observed range.
- **Unique sorted output:** Each amount is considered once in ascending order.
- **Large counts:** Python integers safely hold intermediate ways up to the provided targets and implied values.
- **Empty result ambiguity:** The source returns `[]` both for an impossible instance and for a valid empty denomination set; this matches the required return representation.
- **Why earlier targets stay fixed:** Adding denomination `a` cannot form any positive amount below `a`, so its ascending update begins exactly at `a`. Once an amount has been validated, every later recovery decision leaves that coefficient unchanged, which is the structural reason the greedy induction cannot invalidate its past conclusions.
