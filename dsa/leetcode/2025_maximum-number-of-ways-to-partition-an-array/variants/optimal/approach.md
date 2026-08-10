## General

**Express every pivot with a prefix sum**

Let `s[j]` be the sum of `nums[0]` through `nums[j]`, and let `total = s[-1]`. A pivot `p` lies between indices `p-1` and `p`, so its original left-side sum is `s[p-1]` and its right-side sum is `total - s[p-1]`.

The two sides are equal precisely when

$$
s[p-1]=\textit{total}-s[p-1],
$$

or equivalently when

$$
s[p-1]=\frac{\textit{total}}{2}.
$$

This converts the partition question into counting prefix-sum values. Only `s[0]` through `s[n-2]` represent legal pivots; `s[n-1]` is the whole-array sum and would correspond to an illegal pivot after the array.

**Build the original prefix sums and right-side counts**

The source fills array `s` in one pass. During the same loop, it increments `right[s[i - 1]]` for every `i` from one through `n-1`. Therefore `right` initially contains exactly the prefix sums for all legal pivots, including duplicate sums with their full multiplicity.

Before considering any change, the code checks whether `total` is even. If it is, `right[total // 2]` is the number of partitions already having equal sides. This is a valid candidate because changing an element is optional.

The parity check is essential. When `total` is odd, no integer prefix sum can equal half of it.

**Sweep the possible changed index**

The second pass considers changing each array element `nums[i]` to `k`. Define

$$
d=k-\texttt{nums}[i].
$$

After this replacement, the new total is `total + d`. The effect on a pivot depends on whether index `i` lies to the right or left of that pivot.

The maps `left` and `right` divide legal pivot prefix sums around the currently considered index:

- Before processing index `i`, `left` counts `s[0]` through `s[i-1]`. These correspond to pivots `p <= i`, where the changed element is on the right side.
- At that same moment, `right` counts `s[i]` through `s[n-2]`. These correspond to pivots `p > i`, where the changed element is on the left side.

This placement is why the count is calculated before `s[i]` is moved from `right` to `left`.

**Pivots whose left side does not change**

For a pivot `p <= i`, element `i` belongs to the right partition. Its stored left prefix `s[p-1]` is unchanged, while the whole-array total increases by `d`.

The new equality condition is

$$
2s[p-1]=\textit{total}+d.
$$

Thus these pivots are counted by

`left[(total + d) // 2]`

when `total + d` is even.

**Pivots whose left side does change**

For a pivot `p > i`, the changed element lies inside the left partition. Its new left sum is `s[p-1] + d`, and the new right sum is `total + d - (s[p-1] + d)`.

Equating them gives

$$
2(s[p-1]+d)=\textit{total}+d,
$$

which simplifies to

$$
2s[p-1]=\textit{total}-d.
$$

Therefore the applicable pivots in `right` are counted by

`right[(total - d) // 2]`.

The source first verifies that `total + d` is even. Since `total + d` and `total - d` differ by `2d`, they always have the same parity, so one check is sufficient for both target halves.

**Move one prefix across the boundary**

After evaluating the replacement at index `i`, the code executes `left[v] += 1` and `right[v] -= 1`, where `v = s[i]`. This prepares the maps for index `i+1`.

At `i=n-1`, `s[n-1]` is not a legal pivot and was never initially added to `right`. Its post-calculation map updates cannot influence another iteration because the loop is finished. During every meaningful iteration, however, the maps contain exactly the legal pivots on their stated sides.

**Trace a small example**

For `nums = [2,-1,2]`, the prefix sums are `[2,1,3]` and the legal pivot sums are two and one. The original total is three, so there is no unchanged equal partition.

When considering changing index zero to `k=3`, `d=1` and the new total is four. `left` is empty because no pivot is before or at index zero. Every legal pivot is in `right` and needs original prefix `(3-1)/2=1`. That value occurs once, at the pivot after index one. Changing the first element produces `[3,-1,2]`, whose sides at that pivot sum to two. The candidate count is one.

**Why the maximum is correct**

For a fixed changed index, every legal pivot belongs to exactly one of the two map groups. The algebra derives the necessary and sufficient old prefix value for each group, so their two frequency lookups count all and only balanced pivots after that change.

The sweep evaluates every possible changed index, and the initial candidate covers making no change. Taking the largest count therefore covers every action permitted by “at most one” replacement and returns the global optimum.

## Complexity detail

Let $N$ be the length of `nums`. Building prefix sums and the initial `right` counts takes $O(N)$ time. The replacement sweep also has $N$ iterations. Each dictionary lookup or update is expected $O(1)$, so total expected time is $O(N)$.

Array `s` stores $N$ prefix sums. Across `left` and `right`, there can be $O(N)$ distinct sum keys; repeated prefixes change counts rather than the asymptotic number of entries. Auxiliary space is $O(N)$. The source does not modify `nums`.

## Alternatives and edge cases

- **Try every replacement and rescan every pivot:** This direct method costs $O(N^2)$ and is too slow for $N=10^5$.
- **Recompute changed prefix sums:** Explicitly rebuilding them for each index repeats information; the two frequency maps encode the same effect algebraically.
- **No replacement:** The initial `ans` calculation preserves the possibility that the original array is already best.
- **Replacement by the same value:** Then `d=0`, and the two map lookups together recover the unchanged pivot count.
- **Odd new total:** No integer split can have equal sums, so that replacement contributes zero.
- **Negative values and totals:** Prefix maps and Python integer division after the evenness check work correctly for negative integers.
- **Duplicate prefix sums:** They represent different pivot indices and must be counted separately; dictionary frequencies preserve them.
- **Pivot immediately before the changed index:** It belongs to `left` because the changed element is on the pivot's right side.
- **Pivot immediately after the changed index:** It belongs to `right` because the changed element is on the pivot's left side.
- **Changing the first element:** `left` is initially empty, so all pivots use the changed-left-side formula.
- **Changing the last element:** All legal pivots are in `left`, so all use the unchanged-left-side formula.
- **Whole-array prefix:** `s[n-1]` never represents a legal pivot; its final bookkeeping update is harmless.
- **Large sums:** Python integers avoid overflow even though cumulative sums can exceed the range of an individual input value.
