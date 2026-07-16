# Max Dot Product of Two Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1458 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) |

## Problem Description
### Goal

You are given two integer arrays, `nums1` and `nums2`. Choose a non-empty
subsequence from each array so that the two chosen subsequences have the same
length. A subsequence may delete any number of elements while preserving the
relative order of those that remain; selected positions do not need to be
contiguous.

If the selected subsequences are
$[x_1,x_2,\ldots,x_t]$ and $[y_1,y_2,\ldots,y_t]$, their dot product is

$$
\sum_{r=1}^{t} x_r y_r.
$$

Return the maximum dot product obtainable under these rules. At least one pair
must be selected, so returning zero by choosing two empty subsequences is not
allowed. This matters when every possible paired product is negative.

### Function Contract
**Inputs**

- `nums1`: an integer array of length $m$, where $1 \le m \le 500$.
- `nums2`: an integer array of length $n$, where $1 \le n \le 500$.
- Every value in either array lies in $[-1000,1000]$.

**Return value**

Return the greatest integer dot product of two non-empty, equal-length
subsequences, one drawn from each input while retaining each array's original
order.

### Examples
**Example 1**

- Input: `nums1 = [2,1,-2,5], nums2 = [3,0,-6]`
- Output: `18`
- Explanation: Pair subsequences `[2,-2]` and `[3,-6]`, producing
  $2\cdot3+(-2)\cdot(-6)=18$.

**Example 2**

- Input: `nums1 = [3,-2], nums2 = [2,-6,7]`
- Output: `21`
- Explanation: The one-element subsequences `[3]` and `[7]` produce the
  maximum.

**Example 3**

- Input: `nums1 = [-1,-1], nums2 = [1,1]`
- Output: `-1`
- Explanation: Every pair is negative, but the subsequences must be non-empty.

### Required Complexity
- **Time:** $O(mn)$
- **Space:** $O(\min(m,n))$

<details>
<summary>Approach</summary>

#### General

**Represent the best answer for every pair of prefixes**

For prefixes `nums1[:i]` and `nums2[:j]`, let the current DP value be the
maximum dot product of two non-empty equal-length subsequences contained in
those prefixes. At the pair of final elements
`nums1[i - 1]` and `nums2[j - 1]`, an optimal prefix solution has three
structural possibilities:

1. it skips the final element of the first prefix;
2. it skips the final element of the second prefix; or
3. it pairs those two final elements.

The first two possibilities come from the neighboring prefix states. Their
maximum also covers skipping both elements, so no separate fourth transition
is needed.

**Start or extend a subsequence without permitting emptiness**

Let `product = nums1[i - 1] * nums2[j - 1]`. If the final elements are
paired, that product may start a new one-pair solution. It may instead extend
the best solution for the two prefixes ending before both elements. Extending
a negative prior total would only make the new result smaller, so the paired
transition is
`product + max(0, previous[j - 1])`.

Including `product` directly is what enforces a non-empty answer. Border
states are negative infinity rather than zero: zero is not treated as an
already valid empty solution that could incorrectly defeat every negative
product. The complete transition takes the maximum of the paired choice,
skipping from the first array, and skipping from the second array.

**Compress the prefix table to two rows**

Row `i` depends only on row `i - 1` and the already computed entry to its
left. Retain `previous` for the completed prior row and build `current`
left to right. After the row is complete, replace `previous` with
`current`. Make the shorter input the column dimension so each row contains
$O(\min(m,n))$ entries.

For correctness, consider an optimal pair of subsequences in the two current
prefixes. If it omits either final element, one of the skip states contains it.
If it uses both, removing that final pair leaves either no selected pair or a
valid solution in the diagonal prefixes, exactly matching the start-or-extend
transition. Conversely, every transition preserves order, equal length, and
non-emptiness. The DP therefore includes every legal optimum and constructs
only legal candidates, so its final cell is the required maximum.

#### Complexity detail

There are $mn$ prefix pairs, and each transition performs constant work, giving
$O(mn)$ time. Only two rows are retained. By orienting the shorter array as the
column dimension, those rows use $O(\min(m,n))$ auxiliary space.

#### Alternatives and edge cases

- **Full two-dimensional DP:** The same recurrence in an $(m+1)\times(n+1)$
  table is straightforward and remains $O(mn)$ time, but uses $O(mn)$ space.
- **Enumerate subsequences:** Generating choices and pairing equal-length
  results is exponential and repeats the same prefix decisions extensively.
- **Recompute compatible predecessors:** For every potential final pair,
  scanning all earlier index pairs is correct but can take
  $O(m^2n^2)$ time; prefix DP summarizes those predecessors once.
- **All paired products negative:** The answer is the least negative legal
  product, never the empty-choice value zero.
- **Zeros present:** Selecting a zero can legitimately produce zero and may
  beat every negative product.
- **One-element input:** Only one element from that array can be selected, so
  the best compatible single pair is returned.
- **Different input lengths:** Chosen subsequences must have equal length, but
  unused elements in either original array are allowed.
- **Order conflict:** Large values cannot be paired together if their indices
  would reverse the order in one of the two subsequences.
- **Extreme values:** Individual products can reach $10^6$ in magnitude; use
  ordinary integer arithmetic without replacing negative states by zero.

</details>
