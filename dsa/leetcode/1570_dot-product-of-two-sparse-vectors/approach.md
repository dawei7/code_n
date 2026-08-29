## General

**Store only coordinates that can contribute**

In a dot product, any coordinate containing zero in either vector contributes zero.

The constructor builds dictionary `self.d` with entries only for truthy values:

`{i: v for i, v in enumerate(nums) if v}`.

Under the nonnegative input constraint, `if v` means exactly `v != 0`. Each stored key is the original index and each value is the nonzero vector entry there.

This representation preserves all information relevant to multiplication while omitting potentially many zeros.

**Construction scans the dense input once**

The input still arrives as an ordinary list, so constructing a sparse vector must inspect every position at least once.

`enumerate` supplies both index and value. Nonzero entries are inserted into the dictionary; zero entries require no stored record.

If a vector has `K` nonzero entries, its dictionary contains exactly `K` key-value pairs.

**Iterate over the smaller sparse dictionary**

For the dot product, local variables `a` and `b` initially reference the two dictionaries.

If `b` contains fewer entries than `a`, the source swaps these local references. Afterward, `a` is always the dictionary with no more nonzero coordinates.

The generator iterates `a.items()`. For each nonzero coordinate `i` with value `v`, it asks `b.get(i, 0)` for the other vector's value at the same index.

When that index is absent from `b`, the other value is implicitly zero and the product contributes zero. When present, the product `v * b[i]` is the correct coordinate contribution.

**Why only the intersection matters**

The mathematical dot product is:

$$
\sum_{i=0}^{N-1} x_i y_i.
$$

If `i` is not a stored key in one dictionary, that vector has zero at `i` and the term vanishes.

Only indices in the intersection of the two key sets can contribute. Iterating the smaller dictionary and probing the other considers every intersection index while doing no loop work for zeros in the smaller vector.

It may still generate a zero product for a key absent from `b`, but dictionary lookup handles that in expected constant time.

**Tracing the first example**

Vector one stores indices zero, three, and four with values one, two, and three.

Vector two stores indices one and three with values three and four.

The smaller dictionary has two entries. Index one is absent from vector one and contributes zero. Index three is present with value two, contributing `4 * 2 = 8`.

`sum` returns eight without visiting coordinates two or other explicit zeros.

**Zero vectors**

If either vector contains only zeros, its dictionary is empty.

The size comparison makes the empty dictionary `a` when necessary. Iterating it produces no terms, and Python's `sum` of an empty generator is zero.

No special branch is required.

**Why swapping a and b is safe**

`a` and `b` are local references. Swapping them does not modify either `SparseVector` object or its dictionary.

Multiplication is commutative, so iterating coordinates from either vector yields the same dot product. Choosing the smaller one only reduces work.

**Expected hash-table behavior**

`dict.get` performs expected $O(1)$ key lookup. Keys are bounded integer indices, a standard efficient dictionary use.

The result generator is lazy: products are passed to `sum` one at a time, so no list of contributions is allocated.


For every key iterated from `a`, the code multiplies its exact stored value by the exact corresponding value from `b`, or zero when that coordinate is absent.

All coordinates outside `a` either hold zero in `a`'s vector or belong only to the other vector, so their mathematical terms are zero. Every nonzero intersection coordinate is present in `a` and is processed exactly once.

The generated sum therefore equals the full dense dot product.

**Why the sparse representation helps**

Once construction is complete, dot-product time depends on the smaller nonzero count rather than full vector length.

This is especially useful when both vectors are long but one has very few nonzero entries. The constructor cost is paid once, while the object may participate in later dot products.

## Complexity detail

Let $N$ be common dense length and $K_1,K_2$ be the nonzero counts.

Constructing both sparse vectors requires $O(N)$ time per original input scan, or $O(N)$ when discussing equal-length construction together up to a constant factor. It stores $O(K_1+K_2)$ entries.

One dot product iterates $\min(K_1,K_2)$ entries with expected constant dictionary lookup, taking expected $O(\min(K_1,K_2))$ time and $O(1)$ additional space.

The manifest's combined $O(N+\min(K_1,K_2))$ time and $O(K_1+K_2)$ storage summarize construction plus one product.

## Alternatives and edge cases

- **Store the dense arrays:** Dot product is simple but always costs $O(N)$ even when almost all entries are zero.
- **Sorted index-value pairs:** Use two pointers in $O(K_1+K_2)$ time without hash assumptions.
- **Iterate the larger dictionary:** It remains correct but can perform unnecessary lookups; the source swaps to the smaller one.
- **Both vectors zero:** The empty generator sums to zero.
- **One vector zero:** Iterating the empty smaller dictionary returns zero immediately.
- **Disjoint nonzero indices:** Every lookup defaults to zero and the result is zero.
- **One shared index:** Exactly one nonzero product contributes.
- **Falsy filtering:** Input values are nonnegative integers, so only numeric zero is omitted.
- **Equal vector lengths:** They guarantee that matching dictionary indices refer to corresponding coordinates.
- **Dictionary get default:** Missing keys correctly represent implicit zeros.
- **Repeated dot products:** Sparse construction can be reused across calls.
- **Generator expression:** Contributions are not materialized in another list.
- **Integer arithmetic:** Products and sums are exact in Python without overflow.
