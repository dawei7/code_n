## General

**Start with indices that are already in conflict**

Call index `i` conflicting when `nums1[i]==nums2[i]`. Its current value violates the final requirement, so that index must participate in the rearrangement. Merely swapping other positions cannot change the value stored there.

The first scan collects three pieces of information:

- `same` is the number of mandatory conflicting indices;
- `ans` is the sum of their indices;
- `cnt[v]` is how many mandatory indices contain conflict value `v`.

The index sum is the unavoidable base cost. Every mandatory index must be an endpoint of at least one swap, and each time an index participates its index contributes to the operation cost.

The remaining question is whether the values at these mandatory positions can be rearranged so none returns to a position that forbids the same value.

**Why one value can make the selected set impossible**

Within the mandatory set, every position that currently contains value `v` also has `nums2[i]=v`, so those positions cannot receive `v` in the final arrangement. All copies of `v` must be placed into selected positions whose forbidden value is different.

If `v` occurs $f$ times among `s` selected indices, there are only $s-f$ positions that do not forbid `v`. Placement is possible only if

$$
f\le s-f,
$$

or equivalently $2f\le s$.

At most one value can violate this inequality. Two different values cannot each occur more than half of the same set. The loop over `cnt.items()` therefore looks for a single dominant value `lead` with `v*2>same`.

If no value is dominant, the mandatory multiset is balanced enough to permute its values away from their forbidden equal positions. The base index sum is then sufficient.

**Measure the exact deficit**

Suppose dominant value `lead` appears $f$ times among `same=s` mandatory indices. The code sets

`m = 2*f-s`.

This is the number of additional selected indices needed if each added index increases the set size without adding another `lead` value. After adding $h$ such helpers, the condition becomes

$$
2f\le s+h.
$$

The smallest integer $h$ satisfying it is exactly $2f-s=m$.

Thus `m` is not an arbitrary counter: it is the shortage of safe destinations for the dominant copies.

**What makes an outside index a safe helper**

The second scan considers indices that were not mandatory, so `a!=b` already holds there. A helper is accepted only when

`a != lead and b != lead`.

The first condition means adding its `nums1` value does not increase the number of selected `lead` copies. The second means its destination is available to receive a `lead` value, because `nums2[i]` does not forbid `lead`.

Together, one helper increases the selected-set size and supplies one new safe destination, reducing the deficit by exactly one. The code adds its index to `ans` and decrements `m`.

An index with `a==lead` would add another dominant copy as well as a position, making the imbalance no better. An index with `b==lead` cannot receive the dominant value, so it does not provide the missing destination. Such indices are correctly skipped.

**Why scanning in index order minimizes added cost**

The loop enumerates indices from zero upward and takes the first `m` eligible helpers. Every helper contributes its index to the total cost, and all eligible helpers reduce the deficit by the same one unit. Therefore, choosing the smallest eligible indices minimizes the additional sum.

The mandatory indices cannot be exchanged for cheaper choices because every one of them begins invalid and must be fixed. Greediness applies only to the optional helpers.

If the scan finds fewer than `m` safe helpers, the dominant copies have too few allowable destinations in the entire array. No sequence of swaps can overcome that counting obstruction, so returning `-1` is correct.

**Why balance is sufficient**

Once the selected positions contain no value more than half the set and the dominant value has enough positions that do not forbid it, their `nums1` values can be cyclically arranged among compatible positions so that each selected destination receives a value different from its `nums2` value. The standard rearrangement pairs the most frequent requirements against positions forbidding other values, then fills the remainder.

The selected-index cost lemma for this operation states that such a feasible rearrangement can be scheduled with minimum total cost equal to the sum of the selected indices; index zero can serve as a zero-cost temporary pivot if a cycle decomposition needs one. The algorithm therefore accumulates each mandatory or chosen helper index exactly once in `ans` rather than constructing the swaps explicitly.

Unselected indices already satisfy `nums1[i]!=nums2[i]` and remain unchanged.

**Trace the dominant-value sample**

For `nums1=[2,2,2,1,3]` and `nums2=[1,2,2,3,3]`, mandatory conflicts occur at indices 1, 2, and 4 with values 2, 2, and 3. Their index sum is $1+2+4=7$, `same=3`, and value 2 occurs twice.

The deficit is $2\cdot2-3=1$, with `lead=2`. Index 0 is already unequal but has `a=2`, so it cannot reduce the dominance. Index 3 has `a=1` and `b=3`, both different from 2, so it is the cheapest safe helper. Adding its cost gives $7+3=10$ and reduces the deficit to zero.

**No actual mutation is needed**

The function proves and prices the existence of a suitable swap sequence; it does not need to construct that sequence or modify either input array.

## Complexity detail

Let $n$ be the common array length. The first zipped scan is $O(n)$. Iterating through the counter is $O(u)$ for at most $u\le n$ distinct conflict values. The helper scan is another $O(n)$. Expected total time is $O(n)$ because Python counter operations are expected $O(1)$.

The counter can contain up to $O(n)$ distinct values, so auxiliary space is $O(n)$. All other variables use constant space.

The answer is a sum of indices and can be $O(n^2)$, so fixed-width implementations should use 64-bit arithmetic. Python integers grow automatically.

## Alternatives and edge cases

- **Explicit swap construction:** It is unnecessary for the requested minimum cost and introduces difficult cycle bookkeeping.
- **No initial conflicts:** `same=0`, `ans=0`, no dominant value exists, and zero is returned.
- **Balanced mandatory set:** No helper indices are needed even when several values repeat.
- **Unique dominant value:** Only one value can exceed half of the selected set.
- **Helper with `nums1[i]==lead`:** It adds another dominant copy and does not reduce the deficit.
- **Helper with `nums2[i]==lead`:** It cannot serve as a destination for a dominant copy.
- **Cheapest helpers:** Ascending enumeration minimizes their index sum.
- **Insufficient helpers:** A remaining positive `m` proves impossibility and produces `-1`.
- **Index zero:** Its participation has zero cost and is naturally preferred when eligible.
- **Inputs remain unchanged:** The method computes feasibility and cost without executing swaps.
