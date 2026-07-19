## General
**Store only nonzero coordinates**

During construction, scan the dense vector once and create a map from index to value only when the value is nonzero. A zero never contributes to any dot product, so omitting it loses no information relevant to this operation.

**Probe with the smaller sparse map**

For the dot product, iterate over whichever vector has fewer stored entries. For each `(index, value)`, look up the other vector's value at that index, using zero when the index is absent, and add the product. Every nonzero contribution is included because it must be present in both maps. An index stored in only one map contributes zero, exactly as in the dense formula.

The map intersection is therefore evaluated without materializing a dense result or visiting coordinates that are zero in both vectors. Keeping the representation inside each `SparseVector` also allows the same constructed object to participate efficiently in multiple dot products.

## Complexity detail
Constructing both maps scans $N$ coordinates per vector, which is $O(N)$ overall. The dot product iterates over the smaller map and performs expected constant-time lookups, adding $O(\min(K_1,K_2))$ time. The combined app operation is $O(N+\min(K_1,K_2))$.

The two maps store $K_1+K_2$ entries. The dot-product method itself uses only constant extra space beyond those representations.

## Alternatives and edge cases
- **Sorted index-value pairs:** store nonzeros in index order and intersect the two lists with two pointers in $O(K_1+K_2)$ time. This avoids hash lookup assumptions and can be preferable when vectors are reused.
- **Dense coordinate scan:** multiply corresponding entries with `zip`. It takes $O(N)$ per dot product and ignores the benefit of reusing sparse representations, though it is still linear and correct.
- **Pairwise sparse matching:** compare every nonzero entry of one vector with every nonzero entry of the other. It is correct but can take $O(K_1K_2)$ time.
- **All-zero vector:** its sparse map is empty and every dot product with it is zero.
- **Disjoint supports:** when the nonzero index sets do not intersect, the result is zero.
- **One shared nonzero:** only that coordinate contributes, regardless of other nonzeros unique to either vector.
- **Dense vectors:** every coordinate is stored, so the sparse method naturally degrades to linear work.
- **Equal dimensions:** corresponding indices are well-defined because both vectors have the same length.
