## General

A row’s strength is the number of soldiers, represented by ones. The input provides an important ordering guarantee: within every row, all ones appear before all zeros. That structure allows a boundary search instead of an ordinary sum, although the exact source makes a reversed copy before using Python’s binary-search helper.

The method separates the problem into two phases. It first computes one strength per row, then sorts row indices by those strengths and returns the first `k` indices.

**Understand the reversed-row boundary**

An original row has the form `[1, 1, ..., 1, 0, 0, ..., 0]`. Python’s `bisect_right` expects an ascending sequence, but this original order is descending. The slice `row[::-1]` reverses it into
`[0, 0, ..., 0, 1, 1, ..., 1]`, which is ascending.

On that reversed sequence, `bisect_right(..., 0)` returns the position immediately after the last zero. Because all zeros occur first, that position equals the number of civilians in the row. If the row length is `n`, then

$$
\text{soldiers} = n - \text{civilians}.
$$

That is why the comprehension stores `n - bisect_right(row[::-1], 0)`.

Consider three boundary cases:

- Reversing an all-one row leaves all ones. The insertion point to the right of zero is zero, so the strength is `n - 0 = n`.
- Reversing an all-zero row leaves all zeros. The insertion point is `n`, so the strength is zero.
- If a row contains two ones followed by three zeros, the reversal contains three zeros followed by two ones. The insertion point is three, and `5 - 3` gives two soldiers.

The computation is performed for every row, producing `ans[i]` as the strength of row `i`. Despite its name, `ans` is working data rather than the final returned index list.

**Sort indices instead of losing their identities**

`idx = list(range(m))` creates `[0, 1, ..., m - 1]`. These values are the row identities the problem wants returned. The call `idx.sort(key=lambda i: ans[i])` orders each index by the stored soldier count of its row.

Only the strength appears in the key. The required secondary rule says that when two rows have equal strength, the smaller row index is weaker. Python’s list sort is stable: elements with equal keys remain in their original relative order. Since `idx` begins in ascending numerical order, tied rows remain ordered by ascending index automatically.

For example, if the strengths are `[2, 4, 1, 2, 5]`, sorting the indices by those values gives `[2, 0, 3, 1, 4]`. Rows zero and three both have strength two, and zero stays first because the initial index list placed it first.

Finally, `idx[:k]` takes exactly the first `k` indices from weakest to strongest. The constraint `1 <= k <= m` guarantees that the requested slice is available.

Every returned index is among the globally first `k` rows under the two-level order. The primary ordering is valid because sorting uses exact soldier counts. The secondary ordering is valid because stable sorting preserves the initially ascending indices within each equal-count group. Taking a prefix therefore returns precisely the required rows in the required order.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns.

The binary search itself takes $O(\log n)$ comparisons for one row. However, the exact expression first evaluates `row[::-1]`, and constructing that reversed list copies all $n$ elements. Therefore, one strength computation costs $O(n + \log n) = O(n)$ time, and all rows cost $O(mn)$ time. This is an important difference from a custom boundary search performed directly on the original row.

Sorting the $m$ indices by their strengths costs $O(m \log m)$ time. Creating the final slice costs $O(k)$. The exact total is

$$
O(mn + m\log m),
$$

not $O(m\log n + m\log m)$ for this particular slicing implementation.

`ans` and `idx` each contain $m$ integers. Python’s sort can use $O(m)$ temporary storage. During one comprehension iteration, `row[::-1]` temporarily holds $n$ values; that temporary is discarded before the next row’s reversal. The peak auxiliary space is therefore $O(m + n)$, plus the $O(k)$ returned slice. If the output is counted and `k <= m`, the same $O(m + n)$ bound remains.

## Alternatives and edge cases

- **Direct binary search on the original row:** Search for the first zero while treating ones as the left region and zeros as the right region. This avoids reversing the row and achieves the manifest-style $O(m\log n + m\log m)$ time with $O(m)$ working space.
- **Linear row sum:** Because entries are binary, `sum(row)` directly gives the strength in $O(n)$ time per row. It matches the exact slicing implementation’s $O(mn)$ row-processing bound and is simpler, though it ignores the sorted-row opportunity.
- **Tuple sorting:** Build `(strength, index)` pairs and sort them. Tuple ordering makes the tie-breaker explicit and does not rely on sort stability, at the cost of storing pairs instead of separate arrays.
- **Max-heap of size `k`:** Retain only the weakest `k` candidates. With direct binary search this can reduce ordering work to $O(m\log k)$ and working storage to $O(k)$, which helps when `k` is much smaller than `m`.
- **Vertical scan:** Examine columns from left to right and record rows at their first zero. This emits non-full rows in weakness order but needs extra handling for all-one rows.
- **Equal strengths:** Stability is essential in the exact code. An unstable sort using only `ans[i]` would not guarantee smaller indices first.
- **All-zero row:** Its reversed insertion point is `n`, so its strength is zero and it belongs at the weak end.
- **All-one row:** Its insertion point after zero is zero, so its strength is `n` and it belongs at the strong end.
- **All rows tied:** The sorted index list stays `[0, 1, ..., m - 1]`, and the first `k` indices are returned.
- **`k == m`:** The slice returns every row in complete weakest-to-strongest order.
- **Broken row-order guarantee:** If a row interleaves ones and zeros, binary search on the reversal no longer counts zeros reliably. The method depends on soldiers preceding civilians.
- **Input preservation:** Reversal through slicing creates temporary lists and does not mutate the rows or matrix.
