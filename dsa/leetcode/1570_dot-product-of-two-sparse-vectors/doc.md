# Dot Product of Two Sparse Vectors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1570 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, Design |
| Official Link | [LeetCode](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/) |

## Problem Description
### Goal

Design a `SparseVector` from a dense integer array while retaining an efficient representation of its nonzero entries. Two vectors used together always have the same dimension.

The method `dotProduct(vec)` must return the sum of the products of values at matching indices. Most values may be zero, so the multiplication stage should take advantage of sparsity instead of examining every coordinate again.

### Function Contract
**Inputs**

- `nums1`: The dense values of the first vector of dimension $N$.
- `nums2`: The dense values of the second vector with the same dimension $N$.
- Every value is an integer from `0` through `100`. Let $K_1$ and $K_2$ be the numbers of nonzero entries in `nums1` and `nums2` respectively.

The native interface constructs `SparseVector(nums1)` and `SparseVector(nums2)`, then calls `first.dotProduct(second)`. The app-local adapter receives `nums1` and `nums2` directly and performs the same construction and operation.

**Return value**

Return

$$
\sum_{i=0}^{N-1} \texttt{nums1[i]}\,\texttt{nums2[i]}.
$$

### Examples
**Example 1**

- Input: `nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]`
- Output: `8`

**Example 2**

- Input: `nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]`
- Output: `0`

**Example 3**

- Input: `nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]`
- Output: `6`

### Required Complexity

- **Time:** $O(N + \min(K_1,K_2))$
- **Space:** $O(K_1+K_2)$

<details>
<summary>Approach</summary>

#### General

**Store only nonzero coordinates**

During construction, scan the dense vector once and create a map from index to value only when the value is nonzero. A zero never contributes to any dot product, so omitting it loses no information relevant to this operation.

**Probe with the smaller sparse map**

For the dot product, iterate over whichever vector has fewer stored entries. For each `(index, value)`, look up the other vector's value at that index, using zero when the index is absent, and add the product. Every nonzero contribution is included because it must be present in both maps. An index stored in only one map contributes zero, exactly as in the dense formula.

The map intersection is therefore evaluated without materializing a dense result or visiting coordinates that are zero in both vectors. Keeping the representation inside each `SparseVector` also allows the same constructed object to participate efficiently in multiple dot products.

#### Complexity detail

Constructing both maps scans $N$ coordinates per vector, which is $O(N)$ overall. The dot product iterates over the smaller map and performs expected constant-time lookups, adding $O(\min(K_1,K_2))$ time. The combined app operation is $O(N+\min(K_1,K_2))$.

The two maps store $K_1+K_2$ entries. The dot-product method itself uses only constant extra space beyond those representations.

#### Alternatives and edge cases

- **Sorted index-value pairs:** store nonzeros in index order and intersect the two lists with two pointers in $O(K_1+K_2)$ time. This avoids hash lookup assumptions and can be preferable when vectors are reused.
- **Dense coordinate scan:** multiply corresponding entries with `zip`. It takes $O(N)$ per dot product and ignores the benefit of reusing sparse representations, though it is still linear and correct.
- **Pairwise sparse matching:** compare every nonzero entry of one vector with every nonzero entry of the other. It is correct but can take $O(K_1K_2)$ time.
- **All-zero vector:** its sparse map is empty and every dot product with it is zero.
- **Disjoint supports:** when the nonzero index sets do not intersect, the result is zero.
- **One shared nonzero:** only that coordinate contributes, regardless of other nonzeros unique to either vector.
- **Dense vectors:** every coordinate is stored, so the sparse method naturally degrades to linear work.
- **Equal dimensions:** corresponding indices are well-defined because both vectors have the same length.

</details>
