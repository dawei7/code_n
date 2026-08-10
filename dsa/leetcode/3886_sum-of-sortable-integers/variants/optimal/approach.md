## General

**Rotations cannot move values between blocks**

For a candidate divisor `k`, the array is partitioned into fixed consecutive blocks of length `k`. A rotation changes order inside one block but preserves that block's multiset.

To make the entire array non-decreasing, two independent conditions must hold:

1. values belonging to earlier blocks must not exceed values belonging to later blocks;
2. each individual block's circular order must admit a non-decreasing rotation.

The source tests both conditions for every divisor of `N`.

**Precompute whether a cut separates globally ordered values**

Consider a cut before index `c`. Every value on the left stays in blocks before every value on the right. For a globally non-decreasing final array, it is necessary that

$$
\max(\texttt{nums}[0:c])
\le
\min(\texttt{nums}[c:N]).
$$

Rotations cannot repair a violation because the offending left value can never cross into a later block and the smaller right value can never move earlier.

The source builds `suffix_minimum[c]`, the minimum from `c` through the end, by scanning right to left. A rolling `prefix_maximum` holds the maximum strictly before each cut.

It sets `good_cut[c]` to the comparison above, then updates the prefix maximum with `nums[c]` for the next cut. The update order is important: `nums[c]` belongs to the right side of cut `c`.

For block length `k`, only cuts `k,2k,\ldots,N-k` are actual block boundaries. If any corresponding `good_cut` is false, `k` is immediately rejected.

**Why boundary checks are sufficient between blocks**

Suppose every block is internally rotated into non-decreasing order and every block boundary is good.

At a boundary `c`, every value before `c` is at most every value at or after `c`. In particular, the final value of the previous sorted block is at most the first value of the next sorted block. Thus concatenating all sorted blocks is globally non-decreasing.

The checks are therefore both necessary and sufficient for cross-block order.

**Characterize when a block can be rotated into sorted order**

Treat one block as a cycle. Count strict descents around the cycle, including the wrap edge from its last element back to its first:

$$
\#\{i:a_i>a_{(i+1)\bmod k}\}.
$$

A cyclic rotation can make the linear block non-decreasing exactly when this count is at most one.

If a sorted rotation exists, all internal edges of that linear order are non-descending. The only circular edge that may descend is the wrap from the sorted maximum back to the sorted minimum, so the original cycle has at most one descent.

Conversely, if the cycle has exactly one descent, cut immediately after that descent. Starting the rotation there makes every remaining adjacent edge non-descending. If it has zero descents, following all circular inequalities forces every value to be equal, and any rotation is sorted. More than one descent cannot be hidden by choosing a single rotation cut.

**How the source counts circular descents**

For a block starting at `start`, `previous` begins as its last element. The loop then visits its first through last elements.

The first comparison checks the wrap edge from last to first. Later comparisons check every ordinary internal edge. Whenever `previous>current`, `descents` increases.

The source rejects the candidate as soon as a block exceeds one descent. Strict comparison correctly allows equal adjacent values in a non-decreasing sequence.

**Enumerate only divisors**

Equal block length `k` is legal only when `k` divides `N`. The divisor loop checks candidates through `\sqrt N` and adds both `candidate` and its paired divisor `N/candidate`, avoiding duplication for a perfect square.

Order does not matter because the function sums all successful divisor values.

For each candidate:

- reject bad block boundaries;
- scan every block's circular descents;
- add `k` if all checks pass.

**Examples**

For `[3,1,2]`, divisor one fails cross-block cuts because the fixed singleton order is not sorted. Divisor three has one block whose circular edges have one descent, from three to one. Rotating after it yields `[1,2,3]`, so only three contributes.

For `[7,6,5]`, the length-three cycle has descents seven-to-six and six-to-five, exceeding one. Neither divisor succeeds.

If the whole array is already non-decreasing, every block boundary is good. Each block has at most the single wrap descent, so every divisor is sortable and their sum is returned.

## Complexity detail

Suffix minima and good-cut preprocessing take `O(N)` time and `O(N)` space. Divisor enumeration takes `O(\sqrt N)` time and stores `D` divisors.

For a divisor `k`, boundary testing examines `O(N/k)` cuts, while circular block scans visit all `N` elements once. This is `O(N)` per divisor. Across `D` divisors, total time is `O(ND)`, matching the manifest.

Arrays `suffix_minimum` and `good_cut` use `O(N)` space; the divisor list uses `O(D)\le O(N)`. Total auxiliary space is `O(N)`, also matching the manifest.

## Alternatives and edge cases

- **Try every `k` from one through `N`:** Most do not divide `N` and cannot form equal blocks. Divisor enumeration avoids unnecessary candidates.
- **Enumerate every rotation combination:** A candidate with many blocks has exponentially many combinations. The one-descent characterization tests each block independently.
- **Sort each block's values:** This checks its target order but not whether that target is a cyclic rotation of the original order. Circular descents capture exactly that constraint.
- **Check only blocks, not boundaries:** Individually sortable blocks may still contain values in incompatible global ranges.
- **Check only adjacent block endpoints before rotation:** Endpoints change under rotation. Prefix-maximum versus suffix-minimum checks complete block multisets.
- **Block length one:** Every block is trivially rotatable; `k=1` succeeds exactly when the original array is already globally sorted.
- **Block length `N`:** There are no inter-block cuts; success depends only on the whole cycle having at most one descent.
- **All equal values:** Every circular descent count is zero and every divisor succeeds.
- **Duplicate values:** Equal edges are not descents, consistent with non-decreasing order.
- **Perfect-square length:** The divisor enumeration avoids adding the square root twice.
- **Single-element array:** Its only divisor one succeeds, so the answer is one.
- **No sortable divisor:** The accumulator remains zero.
- **No actual mutation:** The method proves rotations exist but never constructs the rotated array, which is sufficient because only the sum of valid `k` values is requested.
