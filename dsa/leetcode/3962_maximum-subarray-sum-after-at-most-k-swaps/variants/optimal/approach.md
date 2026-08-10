## General

The final answer may use any nonempty contiguous subarray and at most `k` arbitrary swaps. A useful way to separate these choices is to first fix the subarray that will be measured after the swaps. Call its positions the **inside**, and call every other position the **outside**.

For this fixed boundary, swapping two inside positions merely permutes values whose entire sum is already included. Swapping two outside positions does not affect the selected sum at all. Only a swap with one endpoint inside and one endpoint outside can change the candidate sum.

If an inside value `a` is exchanged with an outside value `b`, the subarray sum changes by

$$
b-a.
$$

The swap is useful exactly when `b>a`. Therefore, for a fixed subarray, the best plan is conceptually simple:

1. order the inside values from smallest to largest;
2. order the outside values from largest to smallest;
3. pair them in that order;
4. use at most `k` pairs, stopping before a pair whose outside value is not strictly larger.

The `t`-th selected inside value is the `t`-th smallest inside value, and its partner is the `t`-th largest outside value. This exchange argument is important: if a plan removes some larger inside value while leaving a smaller one, replacing the removed value with the smaller one cannot reduce the gain. Similarly, choosing a smaller outside value while a larger one is available cannot improve the plan. Thus an optimal set of `t` cross-boundary swaps always uses the `t` smallest inside values and `t` largest outside values.

If their sums are `S_{\text{in-small}}` and `S_{\text{out-large}}`, the fixed subarray's best attainable value is

$$
\text{currentSum}
-S_{\text{in-small}}
+S_{\text{out-large}}.
$$

The main difficulty is evaluating those order statistics quickly for every one of the `O(n^2)` possible subarrays.

**Coordinate compression**

The source creates `values = sorted(set(nums))`. This is the increasing list of the `M` distinct array values. The dictionary `ranks` maps each original value to its zero-based position in that list.

Compression preserves all comparisons and equalities: a lower rank means a smaller value, and equal values share a rank. It lets the algorithm store count and sum information in arrays of length `M` even when the input values are negative or far apart.

The array `global_frequency` counts how many times each compressed value occurs in the entire array. Its cumulative version, `global_prefix`, tells how many global elements have value at most a given rank.

**Fenwick trees store both multiplicity and sum**

The source builds two Fenwick trees over the complete array:

- `total_count_tree` stores how many values occupy each rank;
- `total_sum_tree` stores the sum of the actual values at those ranks.

For each new left endpoint, it also creates corresponding `inside_count_tree` and `inside_sum_tree` structures, initially empty. As the right endpoint advances, the newly included value is added to both inside trees and to `current_sum`.

A count tree makes it possible to locate the rank containing the `t`-th smallest item, including duplicate values. A parallel sum tree then gives the sum of all fully selected smaller ranks. If only some copies at the boundary rank are required, their contribution is the remaining count multiplied by the value at that rank.

The source performs this selection through Fenwick binary lifting. Starting with no selected prefix, it tries powers of two from large to small. It skips a Fenwick block only when adding the whole block would leave the cumulative count strictly below the requested count. At the end, `index` identifies the compressed value containing the requested order statistic. The expression

```python
selected_sum + (requested_count - selected_count) * values[index]
```

adds exactly the needed number of duplicate boundary values.

This mechanism finds the sum of several smallest items in `O(\log M)` time; it does not enumerate or sort the current subarray.

**Counting only strictly profitable swaps**

The algorithm must know how many paired swaps have positive gain. It avoids a separate binary search over the two changing multisets by precomputing a global pivot for every possible outside size.

Let `q` be the current `outside_size`. For `1 \le q < n`, `pivot[q]` is the rank of the `q`-th smallest value in the complete array, counting duplicates. Let that pivot value be `v`. The stored `prefix_at_pivot[q]` is the number of global elements whose value is at most `v`.

For the current subarray, define:

- `L` as the number of inside values strictly less than `v`;
- `T` as the number of inside values less than or equal to `v`;
- `H` as the number of outside values strictly greater than `v`.

The source obtains `L` by querying the inside count tree before the pivot rank. It obtains `T` by adding `inside_frequency[position]`, the number of inside copies exactly equal to the pivot. The global count at most the pivot is known, so

$$
H
=q-\bigl(\text{global values at most }v-\text{inside values at most }v\bigr)
=q-\text{prefixAtPivot}[q]+T.
$$

This is the second expression inside the source's `max`.

The number of strictly profitable ordered pairs is

$$
\max(L,H).
$$

To see why, consider the two sides of the pivot.

- If `L \ge H`, every outside value above `v` can be paired with a smaller inside value first. The remaining inside values below `v` can then be paired with available outside values at least `v`, and those pairs are still strict improvements. Thus all `L` low inside values are profitable.
- If `H>L`, pair all inside values below `v` first. The remaining outside values above `v` can be paired with available inside values at most `v`, so all `H` high outside values are profitable.
- After `\max(L,H)` such pairs, any additional inside candidate is at least `v` while any additional outside candidate is at most `v`. The next gain is therefore nonpositive.

The choice of `v` as the global `q`-th order statistic guarantees that the necessary partners exist in both cases. It also handles duplicate pivot values correctly. Equal values produce zero gain and are deliberately excluded from the profitable count.

The exact source computes

```python
profitable = max(
    inside_before,
    outside_size - prefix_at_pivot[outside_size] + inside_through,
)
swaps = min(k, profitable)
```

so it never uses more than `k` swaps and never spends a swap on a zero or negative improvement.

**Computing the exchanged sums**

When `swaps > 0`, the first Fenwick selection obtains `inside_smallest_sum`, the sum of exactly that many smallest inside values.

For the outside, the source uses the difference between the total trees and the inside trees. At every Fenwick block,

```python
total_count_tree[next_index] - inside_count_tree[next_index]
```

is the number of outside values in that block, and the analogous sum-tree difference is their total value.

Instead of directly selecting the largest `swaps` outside values, it selects the smallest `outside_size - swaps` outside values. Subtracting their sum from the complete outside sum leaves exactly the desired largest values:

$$
S_{\text{out-large}}
=
\bigl(\text{totalSum}-\text{currentSum}\bigr)
-S_{\text{out-small}}.
$$

When every outside value is selected, `outside_size - swaps` is zero and the smaller-complement sum is correctly set to zero.

The candidate is then increased by

$$
S_{\text{out-large}}-S_{\text{in-small}}.
$$

The nested `left` and `right` loops examine every nonempty subarray, and `answer` retains the largest candidate. Because the optimization for each fixed boundary is exact, taking the maximum across all boundaries yields the required global answer.

**Why swaps can be viewed independently**

The selected inside and outside positions are all distinct because the algorithm chooses multisets of equal cardinality and pairs their members once. Arbitrary-index swaps allow each chosen outside value to replace one chosen inside value. The order of those swaps does not matter to the final multiset inside the boundary.

The algorithm is optimizing the subarray in the final array, so it is legitimate to fix the final boundary first and ask which original values can be moved across it. Every final configuration using cross-boundary swaps corresponds to removing the same number of inside values and inserting the same number of outside values.

## Complexity detail

Let `n` be the array length and `M` the number of distinct values, with `M \le n`.

Creating the sorted distinct list costs `O(n\log n)` time in the worst case. Building ranks, global frequencies, global prefixes, and the pivot tables costs `O(n+M)` after sorting. Inserting all values into the two total Fenwick trees costs `O(n\log M)`.

There are `O(n^2)` subarrays. Extending one right endpoint performs one inside Fenwick update in `O(\log M)`. When swaps are profitable, it performs up to two Fenwick order-statistic selections, each `O(\log M)`. The pivot-related prefix query is also `O(\log M)`. Therefore every subarray costs at most `O(\log M)`, giving

$$
O(n^2\log M)=O(n^2\log n)
$$

total time.

For every left endpoint, the source allocates and zero-initializes three arrays of length `M`: the inside count tree, inside sum tree, and direct inside frequency array. Across all left endpoints this initialization costs `O(nM)` total time, which is at most `O(n^2)` and is dominated by `O(n^2\log n)`.

At any moment, the global arrays, the two total Fenwick trees, the current inside arrays, the rank map, and the pivot arrays together occupy `O(n+M)=O(n)` auxiliary space. A new set of inside arrays replaces the previous left endpoint's set; the algorithm does not retain `O(n)` structures for all left endpoints simultaneously.

The source never sorts or rewrites `nums` itself. It builds new compressed and tree structures, so the input list's order and contents are not mutated.

## Alternatives and edge cases

- **Re-sort inside and outside for every subarray:** The fixed-boundary greedy rule could be implemented by materializing both sides and sorting them each time, but doing so repeats substantial work and pushes the running time well beyond the required quadratic-logarithmic approach.

- **Enumerate swap sequences:** Exploring actual index-pair sequences branches explosively and treats different operation orders as different even when they produce the same inside multiset. Choosing removed and inserted order statistics captures exactly what affects the sum.

- **Use heaps for each fixed left endpoint:** Two heaps can expose extremes, but deletions, duplicate management, and reconstructing the outside complement for every moving right endpoint are delicate. The paired count-and-sum Fenwick trees support both multiplicity and prefix sums uniformly.

- **Pair values in a different order:** For a fixed number of swaps, removing anything other than the smallest inside values or importing anything other than the largest outside values cannot improve the gain. The sorted extreme pairing is justified by a direct exchange argument.

- **Use exactly `k` swaps:** The contract permits at most `k`. Equal or worse exchanges should be omitted, so the source caps by the number of strictly profitable pairs rather than forcing all available operations.

- **Zero swaps:** When `k=0`, `swaps` remains zero for every subarray. The algorithm then compares ordinary subarray sums and correctly reduces to the maximum-subarray-sum problem, albeit within its general `O(n^2\log n)` framework.

- **The whole array as the subarray:** Then `outside_size=0`, no cross-boundary swap is possible, and the candidate is simply the total array sum. The pivot table is not accessed for size zero.

- **A one-element subarray:** It is included because every right loop starts at `right=left`. Up to `k` larger outside values may replace that single inside value, but the profitable count can never exceed the one available inside position.

- **All values negative:** The selected subarray must remain nonempty, so the correct answer may be negative. The very small initial sentinel is replaced by the first enumerated candidate; the algorithm never introduces an empty-subarray value of zero.

- **All values equal:** Every possible cross-boundary exchange has zero gain. The strict pivot calculation produces no profitable swaps, and the best result comes from an unchanged nonempty subarray, normally the whole array when the repeated value is nonnegative or one element when it is negative.

- **Duplicate values at the pivot:** The direct `inside_frequency` array distinguishes values strictly before the pivot from values through the pivot. This prevents equal-value swaps from being misclassified as improvements.

- **`k` larger than either side:** The profitable count is inherently bounded by the number of usable inside and outside positions. Taking `min(k, profitable)` therefore never requests more order statistics than either multiset contains.

- **Outside complement selection of size zero:** If every outside item is among the selected largest items, there are no unselected small outside values. The explicit zero branch avoids asking the Fenwick tree for a zeroth order statistic.

- **Negative coordinates:** Compression depends only on sorted order, so negative, zero, and positive input values are all handled by the same ranks and sum trees.

- **Fenwick boundary condition:** Binary lifting skips a block only while its cumulative count remains strictly less than the requested count. Using `<=` instead would step past the rank containing the final required copy and would break duplicate handling.

- **Potential simpler methods for special `k`:** Kadane's algorithm is sufficient only for `k=0`. When swaps are allowed, the value of a boundary depends on outside order statistics, so ordinary maximum-subarray state alone does not contain enough information.
