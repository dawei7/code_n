## General

**Free reordering removes all positional constraints**

Within either array, any two positions can be swapped for free. Repeating free swaps can realize any permutation of that array. Therefore original indices do not matter for the final feasibility or paid cost; only the frequency of each value in each array matters.

Let `A_x` be the count of value `x` in `nums1` and `B_x` its count in `nums2`. If the final arrays are identical, they must contain the same count `T_x` of every value. Paid cross-array swaps preserve the combined number of copies, so

$$
2T_x=A_x+B_x.
$$

Thus the only possible target frequency is

$$
T_x=\frac{A_x+B_x}{2}.
$$

This immediately gives the feasibility condition: `A_x+B_x` must be even for every value. If any combined frequency is odd, it cannot be divided equally between two identical arrays.

**Cancel copies already balanced between the arrays**

The source begins with `cnt2 = Counter(nums2)` and an empty `cnt1`. It then scans `nums1`.

For a value `x`:

- if `cnt2[x]` is positive, one copy from `nums1` is matched with one copy from `nums2`, and the source decrements `cnt2[x]`;
- otherwise, `nums2` has no unmatched copy of `x` left, so this copy is an excess on the `nums1` side and `cnt1[x]` is incremented.

After every element of `nums1` is processed,

$$
\texttt{cnt1}[x]=\max(A_x-B_x,0)
$$

and

$$
\texttt{cnt2}[x]=\max(B_x-A_x,0).
$$

The counters no longer represent complete frequencies. They represent directional imbalance after all common copies have been canceled.

For example, if `nums1` contains five copies of `x` and `nums2` contains one, one pair is canceled, `cnt1[x]=4`, and `cnt2[x]=0`. The final equal split needs three copies on each side, so two of the four residual copies must move from the first array to the second.

**Why every residual count must be even**

For any value,

$$
A_x+B_x\equiv A_x-B_x\pmod2.
$$

Therefore the combined frequency is even exactly when the nonzero directional difference is even. The source checks every residual in both counters. If any `v` is odd, it returns minus one.

Zero entries that remain in `cnt2` are harmless because zero is even. Values absent from one counter have their positive residual in the other counter, where they are checked.

This parity test is sufficient as well as necessary. When every total can be halved, assigning `T_x` copies to each array gives a valid equal-frequency target for every value. The arrays have equal length, so those per-value target counts sum to the correct size.

**How one paid swap fixes two directional surpluses**

Suppose `A_x>B_x`. The first array has

$$
\frac{A_x-B_x}{2}
$$

copies of `x` that must move to the second array. The division by two is important: the raw difference counts how far apart the two arrays are, and transferring one copy reduces that difference by two—one side loses it while the other gains it.

Similarly, for a value `y` with `B_y>A_y`, some copies must move from `nums2` to `nums1`.

A paid operation exchanges one value at a shared index. Free reordering allows the algorithm to place any chosen excess `x` from `nums1` opposite any chosen excess `y` from `nums2`. Swapping them performs both required transfers at cost one.

The number of copies that must leave `nums1` is

$$
R=\sum_{x:A_x>B_x}\frac{A_x-B_x}{2}.
$$

Because both arrays have the same length, their total positive and negative frequency imbalances balance. Exactly `R` copies also need to leave `nums2`. Pairing one surplus from each side therefore completes all transfers in `R` paid swaps.

**Minimum-cost lower bound and construction**

Every copy that must leave `nums1` requires participation in a cross-array swap; free swaps never move a value between arrays. One paid swap can move at most one such copy out of `nums1`. Therefore any solution costs at least `R`.

The surplus-pairing construction above uses exactly `R` paid swaps, attaining that lower bound. Afterward both arrays have the target frequency `T_x` for every value. Their orders may differ, but free within-array swaps can permute one or both arrays into identical order at no additional cost.

The source computes `R` as

`ans += v // 2`

over the values in `cnt1`. It does not also sum `cnt2` because that would count both sides of each paid exchange and double the answer.

**Examples**

For `nums1=[10,20]` and `nums2=[20,10]`, cancellation removes both values completely. There is no imbalance, so `ans=0`. A free reorder is enough.

For `nums1=[10,10]` and `nums2=[20,20]`, the residual counters contain two tens on the first side and two twenties on the second. Both counts are even. The first array must send `2/2=1` ten, and the second simultaneously sends one twenty. One paid swap is both necessary and sufficient.

For `nums1=[10,20]` and `nums2=[30,40]`, every value has combined count one. Residual counts are odd, so no equal split exists and the method returns minus one.

The exact source requires `Counter` from `collections`.

## Complexity detail

Let `N` be each array length and `U` the number of distinct values across both arrays. Constructing `cnt2` and scanning `nums1` take expected `O(N)` time. Iterating through the two counters takes `O(U)` time, and `U\le2N`, so total expected time is `O(N)`.

The two counters store at most `O(U)` keys, giving `O(U)` auxiliary space. This matches the manifest. The stated value domain also bounds `U` by `8\cdot10^4`, but it can still grow with `N`, so `O(U)` is the informative bound.

All counter and arithmetic operations are constant-time in the customary model. The answer is at most `N`, and Python integers easily hold it.

## Alternatives and edge cases

- **Compare sorted arrays only:** If sorting makes the arrays equal, cost zero. Otherwise sorting alone cannot determine how many cross-array transfers are needed unless frequency differences are then analyzed.
- **Build full frequency counters for both arrays:** Compute `A_x-B_x` directly for every key. This is equally correct and perhaps more algebraic; cancellation during the scan stores only unmatched copies.
- **Simulate indices and swaps:** Free permutations make particular indices irrelevant. Searching positional swap sequences adds unnecessary state and can become exponential.
- **Check only total multiset size:** Both arrays already have equal length, but each individual value's combined count must be even. A globally even number of elements is not enough.
- **Odd residual:** It makes equality impossible because half of the combined frequency would not be an integer.
- **Sum both surplus counters:** This doubles the paid cost. One exchange handles one outgoing surplus on each side simultaneously.
- **Already equal multisets:** All residuals are zero and the result is zero even if element orders differ.
- **Identical arrays:** They are a special zero-cost case handled by the same cancellation logic.
- **One value dominates one side:** A large even residual contributes half its size to the answer; each paid swap reduces the inter-array difference for that value by two.
- **Free operations before and after paid swaps:** They allow arbitrary surplus values to be aligned at a shared index and allow final equal multisets to be arranged identically.
- **Counter zero entries:** Decrementing matched counts may leave stored zeros. They neither affect parity nor the answer.
- **Hash-table complexity:** Counter operations are expected constant time. A fixed array indexed by values could give deterministic linear behavior under the bounded value domain.
- **Source mutation:** The method changes only its counters. Both input arrays remain untouched.
