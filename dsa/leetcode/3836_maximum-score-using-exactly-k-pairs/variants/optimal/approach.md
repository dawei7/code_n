## General

**Use prefixes because both index sequences must increase**

The chosen indices in `nums1` and `nums2` must each be strictly increasing. Once a pair `(i,j)` is chosen, every earlier pair must come from prefixes ending before `i` and `j`.

This order structure suggests a two-prefix dynamic program.

Define

$$
f[i][j][p]
$$

as the maximum score obtainable by choosing exactly `p` ordered pairs using only the first `i` values of `nums1` and the first `j` values of `nums2`.

The prefix lengths use one-based DP coordinates:

- the newest available first-array value is `nums1[i - 1]`;
- the newest available second-array value is `nums2[j - 1]`.

The desired result is `f[n][m][K]`.

**Represent impossible exact-count states with negative infinity**

Before examining values, choosing zero pairs from two empty prefixes has score zero:

`f[0][0][0] = 0`.

Every other state begins at `-inf`. This means “impossible,” not merely “a poor score.”

The distinction matters because input values may be negative. A legal score can be negative, and exactly `K` pairs must be selected. Initializing impossible positive-count states to zero would let the DP pretend it selected fewer pairs whenever all legal products are unfavorable.

Adding a finite product to negative infinity remains negative infinity, so an impossible predecessor cannot create a fake valid state.

**Option one: leave the newest nums1 element unused**

If `i > 0`, any selection using the first `i - 1` elements of `nums1` is also valid when the prefix is expanded to `i`. It simply ignores `nums1[i - 1]`.

The source applies:

`f[i][j][p] = max(f[i][j][p], f[i - 1][j][p])`.

This transition preserves the exact pair count and score.

**Option two: leave the newest nums2 element unused**

Similarly, if `j > 0`:

`f[i][j][p] = max(f[i][j][p], f[i][j - 1][p])`.

This expands the second prefix while ignoring `nums2[j - 1]`.

Both skip transitions are needed because an optimal ordered matching may omit arbitrary elements from either array.

**Option three: pair the two newest values**

When `i > 0`, `j > 0`, and `p > 0`, the DP may use `nums1[i - 1]` and `nums2[j - 1]` as the final chosen pair.

Every earlier pair must use indices smaller in both arrays, so it comes from `f[i - 1][j - 1][p - 1]`. The transition is:

`f[i - 1][j - 1][p - 1] + nums1[i - 1] * nums2[j - 1]`.

This adds exactly one pair and preserves both strict index orders.

The source takes the maximum of this candidate and the two skip possibilities.

**Why these three cases cover every legal selection**

Consider an optimal selection represented by state `f[i][j][p]`.

If it does not use `nums1[i - 1]`, it belongs to the first skip case.

Otherwise, if it does not use `nums2[j - 1]`, it belongs to the second skip case. This includes a solution where the newest first-array value is paired with an earlier second-array value: the last second-array value is unused, so the solution already appears in `f[i][j - 1][p]`.

If it uses both newest values, strict increasing order forces them to pair with each other as the final pair. Pairing one newest value with an earlier counterpart while also using the other newest value elsewhere would violate order or require another later counterpart that does not exist. Removing the final pair leaves a legal `p - 1`-pair selection from the two shorter prefixes, which is the third case.

Every optimal selection falls into at least one case, and every transition constructs a legal selection. Taking their maximum gives the exact state value.

**Loop order makes every predecessor ready**

The source loops `i` from 0 through `n`, `j` from 0 through `m`, and `p` from 0 through `K`.

`f[i - 1][j][p]` lies in a completed earlier `i` layer. `f[i][j - 1][p]` lies at an earlier `j` in the current layer. `f[i - 1][j - 1][p - 1]` is also already complete.

Therefore every transition reads finalized predecessor values. The exact-count dimension does not require a special order because the pairing predecessor also lies in smaller prefix dimensions.

**Trace why negative products cannot be skipped when K requires them**

For `nums1 = [-3,-2]`, `nums2 = [1,2]`, and `K = 2`, both pairs are forced by the lengths and ordering:

$$
(-3)(1)+(-2)(2)=-3-4=-7.
$$

The DP returns -7. The zero-pair base cannot leak into `p = 2` because only the pairing transition increases `p`, and impossible states remain negative infinity.

For the second example, pairing -2 with -3 produces a positive 6, and pairing 5 with 4 later produces 20. Their prefix order is valid, so the DP builds total 26.

**The source is a full table, not the rolling DP described by the manifest**

The manifest summary says “rolling exact-count prefix DP,” and its space bound is `O(K min(N,M))`. The executable source allocates:

`f = [[[-inf] * (K + 1) for _ in range(m + 1)] for _ in range(n + 1)]`.

All $(N+1)(M+1)(K+1)$ states coexist. No dimension is rolled or discarded. The algorithmic recurrence is correct, but the faithful source-space bound is $O(NMK)$.

A rolling implementation could keep only the previous and current `i` layers and, after choosing the shorter array as the `j` dimension, attain the manifest's smaller space. That optimization is not present here.

## Complexity detail

There are $(N+1)(M+1)(K+1)$ DP states. Each state performs at most three constant-time transitions and comparisons. Total time is $O(NMK)$.

The complete three-dimensional list stores every state, so exact auxiliary space is $O(NMK)$. This contradicts the manifest's $O(K\min(N,M))$ claim for the protected source.

Under maximum dimensions 100, the table contains a little over one million scalar entries plus Python list overhead. It is within the intended scale but materially larger than a rolling version.

All finite scores are integers. `-inf` is a floating sentinel, but it remains only in impossible states; the guaranteed-valid final state is produced from integer arithmetic and has an integer value.

## Alternatives and edge cases

- **Rolling two prefix layers:** Keep only `i - 1` and `i` while retaining the `j` and pair-count dimensions. This reduces space to $O(MK)$, or $O(K\min(N,M))$ after swapping arrays.
- **Top-down memoization:** Recursively choose skips or a pair and memoize `(i,j,p)`. It has the same $O(NMK)$ state bound but adds recursion overhead and depth concerns.
- **Enumerate index combinations:** Choosing all $K$-subsets from both arrays and pairing them in order is combinatorial and becomes infeasible quickly.
- **Exactly K, not at most K:** Negative infinity prevents the DP from preferring fewer pairs when all remaining products are negative.
- **K equals one:** The recurrence finds the maximum product over any one ordered index pair.
- **K equals min(N,M):** One array may have every index selected, while the other can still skip values if it is longer.
- **Negative times negative:** Such a product is positive and may be highly valuable; no sign-based greedy rule is safe.
- **Zero values:** Pairing with zero may be necessary to reach exactly `K` pairs, and the DP handles that naturally.
- **Strict index order:** The pair transition moves from both shorter prefixes, guaranteeing every earlier index is smaller in both arrays.
- **Impossible intermediate states:** They remain `-inf` and cannot beat any finite candidate.
- **Large products and sums:** Python integers represent products up to $10^{12}$ and accumulated scores exactly.
