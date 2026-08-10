## General

**Rewrite road importance as city contributions**

Every road contributes the assigned value of each of its two endpoints. If city `c` has degree `d_c`, its assigned value appears once in the total for each incident road, so its complete contribution is

$$
d_c \cdot value_c.
$$

Therefore, total road importance can be rewritten as

$$
\sum_{c=0}^{n-1} d_c value_c.
$$

Once degrees are known, the identities of individual roads no longer matter to the assignment optimization.

**Count every road endpoint**

`deg = [0] * n` creates one degree counter per city. For each bidirectional road `[a,b]`, both `deg[a]` and `deg[b]` increase.

This counts each road twice across the array, once for each endpoint, which is exactly what the importance formula needs: a road's sum contains two city values.

Cities without roads retain degree zero.

**Pair large values with large degrees**

The available assigned values are exactly one through `n`. Sorting `deg` in ascending order and pairing it with `1,2,\ldots,n` gives the highest values to the highest degrees.

An exchange argument proves optimality. Suppose `d_a \le d_b` but values satisfy `v_a > v_b`. Their current contribution is `d_a v_a+d_b v_b`. Swapping values changes it by

$$
(d_a v_b+d_b v_a)-(d_a v_a+d_b v_b)
=
(d_b-d_a)(v_a-v_b)
\ge 0.
$$

Thus, removing an inverted assignment never decreases total importance. Repeated exchanges lead to sorted degrees paired with sorted values.

**Compute the optimal dot product**

`enumerate(deg, 1)` yields assigned values `i` from one through `n` beside ascending degrees `v`. The generator contributes `i * v` for each city role, and `sum` returns their dot product.

The actual city names need not be reconstructed because the requested result is only the maximum total. If degrees tie, swapping their assigned values leaves the dot product unchanged, so any city-level assignment within a tie is optimal.

**Trace a small degree sequence**

If degrees after sorting are `[0,1,1,3]`, the values one through four give total

`0*1 + 1*2 + 1*3 + 3*4 = 17`.

Giving value four to either degree-one city instead of the degree-three city would reduce the total, because that large value would be repeated across fewer roads.

**Why the rewritten total matches roads exactly**

Expanding the degree dot product adds `value_c` once per incident road at every city. Grouping those terms by road produces `value_a+value_b` for each road `[a,b]`, exactly its defined importance. No term is missing or extra.

The exchange proof then establishes that the sorted pairing maximizes this identical total over all one-to-one value assignments.

## Complexity detail

Let `r` be the number of roads. Degree counting takes `O(r)` time. Sorting `n` degrees takes `O(n\log n)`, and the final sum takes `O(n)`. Total time is `O(r+n\log n)`.

The degree array uses `O(n)` space. Python's sort may also use `O(n)` temporary memory, leaving the same asymptotic bound. The roads list is read but not changed.

The total can exceed 32-bit range; Python integers are safe, while fixed-width implementations should use 64-bit arithmetic.

## Alternatives and edge cases

- **Sort city indices by degree:** It can construct an explicit assignment, but sorting the degree values alone is sufficient for the maximum total.
- **Priority queue:** Repeatedly pairing largest degrees and values works but is more complex than one sort.
- **Try all assignments:** There are `n!` possibilities and the exchange argument makes enumeration unnecessary.
- **Use road endpoints during scoring:** After degrees are counted, the dot-product identity already incorporates every road.
- **Isolated city:** Degree zero receives one of the smallest values because its value contributes nothing.
- **All degrees equal:** Every assignment produces the same total.
- **Tied degrees:** Their assigned values may be swapped without changing importance.
- **Sparse graph:** Runtime includes only the actual `r` roads, not all possible city pairs.
- **No duplicate roads:** Degree increments correspond directly to distinct incident roads.
- **Bidirectional road:** Both endpoints contribute once; direction does not matter.
- **Large answer:** Use wide integer arithmetic outside Python.
- **Input preservation:** `roads` is unchanged; only the derived degree list is sorted.
- **City labels:** Numeric city identifiers do not influence importance, so they disappear after degree counting.
- **Disconnected graph:** Connectivity is not required; every component contributes through its own city degrees, and the global sorted assignment remains optimal.
- **One high-degree hub:** The exchange proof guarantees that it receives value `n`.
- **Road contribution counted twice in degrees:** This is intentional because road importance contains one value from each of its two endpoints.
- **Generator evaluation:** `sum` consumes products lazily, so no second length-`n` contribution list is allocated.
- **Ascending versus descending:** Ascending degrees paired with ascending values is equivalent to descending degrees paired with descending values.
- **Constraint on unique values:** `enumerate(..., 1)` supplies every value from one through `n` exactly once.
- **Graph shape:** Stars, chains, cycles, and disconnected components need no separate cases because only degree multiplicity affects the rewritten objective.
