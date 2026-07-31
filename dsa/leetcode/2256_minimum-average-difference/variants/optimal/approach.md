## General

**Replace repeated range sums with one evolving boundary**

The two averages at an index depend only on the sum before the split and the
sum after it. Compute the whole-array sum once. While scanning left to right,
add the current value to `prefix`; the suffix sum is then `total - prefix`.
This gives both range sums in constant time per index without storing a prefix
array.

Divide `prefix` by `index + 1`. For the suffix, divide by the remaining element
count when it is positive, and use zero at the final index. These integer
divisions exactly implement the required downward rounding because every
quantity is nonnegative.

Track the smallest difference and its index. Update them only for a strictly
smaller difference. Since indices are visited in increasing order, declining
to update on equality preserves the earliest index automatically.

Before evaluating index $i$, `prefix` equals the sum through $i$, while
`total - prefix` equals the sum strictly after $i$. Therefore the computed
difference is exactly the definition for that split. The scan evaluates every
candidate and retains the smallest index among all minimum values, so its final
index is the required answer.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The initial total and the index scan each
take $O(n)$ time, giving $O(n)$ total time. Only sums, counters, and the current
best pair are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Recompute both sums at every split:** This is straightforward and correct but requires $O(n^2)$ time.
- **Prefix-sum array:** Stored prefix sums also give $O(n)$ time, but consume $O(n)$ auxiliary space when two scalar sums suffice.
- **Floating-point averages:** Fractions are not part of the definition and can change comparisons; use integer division.
- **Single element:** The right side is empty, its average is zero, and index `0` is the only answer.
- **Final index:** Avoid division by zero and use the defined empty-side average of zero.
- **Tied differences:** Keep the first index by updating only on a strict improvement.
- **All zeros or equal values:** Many indices may tie, so the answer is the smallest one.
- **Large values:** The total can reach $10^{10}$ and requires a sufficiently wide integer type outside Python.
