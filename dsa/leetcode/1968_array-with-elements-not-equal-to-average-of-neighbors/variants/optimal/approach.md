## General

**Create alternating low and high values**

After sorting, split the distinct values into a lower half and an upper half. Let

`m = (n + 1) // 2`,

so the lower half is `nums[0:m]` and the upper half is `nums[m:n]`. The lower half has the same number of values as the upper half when $n$ is even and one extra when $n$ is odd.

The solution alternates one lower value and one upper value:

`nums[0], nums[m], nums[1], nums[m + 1], ...`.

If $n$ is odd, the last unpaired lower value is appended at the end.

Because all input values are distinct and the list is sorted, every upper-half value is strictly greater than every lower-half value.

**Why every internal high value is safe**

An upper-half value in the alternating result is surrounded by lower-half values, except when it is at an endpoint. Both neighbors are strictly smaller than it. The average of two numbers smaller than $h$ is also smaller than $h$:

$$
\frac{a+b}{2}<h.
$$

Therefore an internal high value cannot equal its neighbors' average.

**Why every internal low value is safe**

An internal lower-half value is surrounded by upper-half values. Both neighbors are strictly greater than it, so their average is strictly greater:

$$
\frac{a+b}{2}>\ell.
$$

It also cannot equal the average.

Endpoints have only one neighbor and are not constrained by the problem. Thus the alternating low-high structure satisfies every required internal index.

**Trace odd and even lengths**

For sorted `[1,2,3,4,5]`, `m=3`. The output is `[1,4,2,5,3]`. High values four and five are local peaks between low values; internal low value two is a valley between highs. The final low three is an endpoint.

For sorted `[1,2,3,4]`, `m=2` and the output is `[1,3,2,4]`. Three is above both neighbors and two is below both neighbors.

The output need not match the examples because any valid rearrangement is accepted.

**Why distinctness matters**

Strict separation between halves is the heart of the proof. If duplicates were allowed across the split, an upper value might equal a lower neighbor, and local peak/valley inequalities would no longer be strict. The contract guarantees distinct integers, so the simple split is sufficient.

**Why the loop emits every value exactly once**

The loop index `i` ranges through all $m$ lower positions and appends `nums[i]` once. It appends upper position `i + m` only when that index is below $n$. These upper indices cover $m$ through $n-1$ exactly once. The two index ranges are disjoint and together cover the sorted array, so the result is a true rearrangement with no omissions or duplicates.

**Input mutation**

`nums.sort()` sorts the caller's list in place. The returned arrangement is a separate `ans` list, but the original list object remains sorted afterward. This side effect is part of the exact implementation.

**A useful way to see the proof**

The algorithm never needs to compare an element with the numerical average itself. Instead, it gives every constrained position a stronger property: it is either strictly smaller than both neighbors or strictly larger than both neighbors. Equality with their average is then impossible automatically. This stronger local zigzag condition is easier to construct and reason about than testing averages one by one. Sorting supplies a clean boundary between the two groups, and alternating the groups turns that global boundary into the required local inequalities.

## Complexity detail

Let $N$ be the number of elements.

Sorting dominates at $O(N\log N)$ time. The alternating construction visits each value once and costs $O(N)$, so total time is $O(N\log N)$.

The answer list uses $O(N)$ space. Python's sort may also use $O(N)$ temporary memory in the worst case. Scalar indices use constant space.

The construction itself is linear after sorting.

## Alternatives and edge cases

- **Swap adjacent pairs after sorting:** A different local-peak construction can also work, but its proof must handle endpoints and parity carefully.
- **Random shuffling until valid:** It has no deterministic runtime guarantee and repeatedly checks the same condition.
- **Sort then interleave halves in another order:** Starting with high instead of low also works if strict alternation and half separation are maintained.
- **Odd length:** The lower half has one extra value, which becomes the final unconstrained endpoint.
- **Even length:** Every lower value pairs with one upper value.
- **Minimum allowed length three:** The result has one internal value that is strictly a peak or valley.
- **Large value gaps:** Actual distances do not matter; only strict less-than and greater-than relations are used.
- **Distinct values:** They guarantee strict half separation and prevent an average equality through equal neighbors.
- **No arithmetic in code:** The method enforces inequalities structurally and never computes a potentially floating-point average.
- **Input side effect:** The exact source sorts `nums` in place before returning a separate arrangement.
- **Any valid output:** There is no requirement to preserve relative order or choose a lexicographically smallest rearrangement.
