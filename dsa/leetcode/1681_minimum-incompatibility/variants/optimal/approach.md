## General

**Represent occurrences, not just values**

The array can contain duplicate values, and equal-valued occurrences may belong to different groups. A bitmask over indices preserves those distinct occurrences. With `n <= 16`, there are at most $2^n$ masks, which is small enough for subset dynamic programming.

Each of the `k` groups must contain

`m = n // k`

elements. A valid group mask therefore has exactly `m` set bits and no repeated value among those selected indices.

**Precompute the cost of every possible group**

`g[mask]` is initialized to `-1`, meaning that `mask` is not a valid group. The preprocessing loop ignores masks whose `bit_count()` is not `m`.

For a size-`m` mask, the source scans the selected indices. Set `s` records values already encountered. If selected value `x` is already in `s`, the group contains a duplicate and the loop stops. Otherwise it updates the minimum and maximum.

If `len(s) == m` after the scan, all selected values were distinct. The group incompatibility is `mx - mi`, stored in `g[mask]`.

Precomputing this table separates local group validity and cost from the later global partition decisions.

**Define the partition state**

`f[used]` is the minimum incompatibility sum for partitioning exactly the index occurrences whose bits are set in `used` into complete valid groups. Every value begins at infinity except `f[0] = 0`, because using no indices costs zero.

A transition chooses one new valid group `j` containing only unused indices. It updates

`f[used | j] = min(f[used | j], f[used] + g[j])`.

Since every valid `g[j]` has exactly `m` bits, reachable masks always contain a whole number of groups. When all `n` bits are set, exactly `k` groups have been formed.

**Why only one unused occurrence of each value is considered**

For a reachable `used`, the source builds `mask` by scanning unused indices and selecting only the first unused occurrence of every distinct value. Set `s` tracks which values have already contributed a representative.

At first this may look as though valid groups using a later duplicate are lost. They are not. Within the remaining multiset, two unused occurrences with the same value are interchangeable for the next group. If an optimal next group contains a later occurrence of value `x`, swapping it with the chosen representative changes neither the group’s values, its incompatibility, nor the multiset of values left for future groups. Only occurrence identities swap.

Therefore at least one optimal continuation exists whose next group uses only the chosen representatives. This symmetry reduction avoids enumerating many equivalent index choices while preserving the optimum.

If fewer than `m` distinct unused values exist, no valid next group can be formed, so the state is correctly abandoned.

**Enumerate all candidate groups among representatives**

Starting with `j = mask`, the update

`j = (j - 1) & mask`

visits every nonempty submask of `mask` exactly once. Most have the wrong size; `g[j] == -1` rejects them immediately. A submask with a nonnegative precomputed cost is a complete size-`m` group of distinct unused values.

Because `mask` contains only unused indices, `j` cannot overlap `used`. The bitwise OR therefore adds exactly one new group.

**Why the dynamic program finds the optimum**

Every DP transition appends a valid group, so every finite `f` value describes a legal partial partition and its exact accumulated cost.

Conversely, take an optimal partition of the values remaining at some reachable state. By the duplicate-symmetry argument, its next group can be represented using the one-per-value candidate mask. The submask enumeration will consider that group, and the remaining groups form the same problem at the updated state. Inductively, the DP can reproduce an optimal complete partition.

Taking the minimum over all transitions preserves the least cost for each used mask. Therefore `f[-1]` is the minimum total incompatibility when a partition exists. If it remains infinity, no legal partition can cover all occurrences and the source returns `-1`.

## Complexity detail

There are $2^n$ masks in both `g` and `f`. Group preprocessing can inspect up to `n` indices for a mask, giving an $O(n2^n)$ upper bound.

Across DP states, submask enumeration has the standard $O(3^n)$ worst-case bound: each index can conceptually be already used, selected in the candidate submask, or unused outside it. The $O(n)$ representative-mask construction per state is dominated by $O(3^n)$. Total time is $O(3^n)$.

The `g` and `f` arrays use $O(2^n)$ space. Temporary sets hold at most `n` distinct values, so total auxiliary space remains $O(2^n)$.

## Alternatives and edge cases

- **Backtracking with sorted groups:** Assign occurrences recursively while pruning duplicate group states. It can work for `n <= 16` but has a less predictable worst case than mask DP.
- **Frequency impossibility check:** If any value occurs more than `k` times, pigeonhole reasoning makes a valid partition impossible. The exact source does not check early; its DP eventually returns `-1`.
- **Enumerate every size-`m` group at every state:** Correct but repeats validity work. Precomputed `g` makes transitions constant-time after choosing a submask.
- **`k == n`:** Then `m == 1`, every occurrence forms a singleton group with incompatibility zero, so the answer is zero.
- **`k == 1`:** The only group uses every index; it is valid only if all values are distinct.
- **Duplicate values across groups:** This is allowed and is why occurrences use separate bits.
- **Duplicate values within a group:** `g` leaves that mask at `-1`, preventing the transition.
- **Interchangeable duplicates:** Selecting only one unused occurrence per value is safe because the objective depends on values, not original indices.
- **Unreachable state:** An infinite `f[used]` is skipped because it does not represent any legal partial partition.
- **No enough distinct values remaining:** The state cannot form another valid group and is correctly skipped.
- **Minimum and maximum initialization:** Input values are at most `n <= 16`, so initial `mi = 20` and `mx = 0` safely bracket every selected value.
- **Returned `-1`:** Infinity at the all-used mask proves no sequence of valid group transitions covers the array.
