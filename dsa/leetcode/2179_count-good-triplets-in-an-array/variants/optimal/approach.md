## General

**Turn agreement between permutations into increasing positions**

Store the position of every value in `nums2`, then replace each value visited
in `nums1` conceptually by that stored position. Because both inputs are
permutations, a triplet keeps its order in both arrays exactly when its three
mapped positions form a strictly increasing subsequence.

**Count every mapped position as the middle**

Suppose the current value is at index $i$ in `nums1` and maps to position $p$
in `nums2`. A good triplet using it as the middle needs an earlier mapped
position smaller than $p$ and a later mapped position larger than $p$.

A Fenwick tree over positions of `nums2` records the mapped positions already
seen. Its prefix query gives the number $L$ of earlier positions smaller than
$p$. Of the $i$ earlier values, $i-L$ map above $p$. There are $n-1-p$
positions above $p$ altogether, so

$$
R=(n-1-p)-(i-L)
$$

of them belong to values not yet visited in `nums1`. The current value
therefore contributes $LR$ triplets. After adding that contribution, insert
$p$ into the tree.

Every good triplet has exactly one middle value. Its first value is included
in $L$ and its third in $R$ when that middle is processed, so it is counted
once. Conversely, each pair selected by those two counts is earlier and
smaller on the left and later and larger on the right, which makes the
resulting triplet increasing in both permutations.

## Complexity detail

Building the position map takes $O(n)$ time. Each of the $n$ values performs
one Fenwick prefix query and one update, each in $O(\log n)$ time, for
$O(n\log n)$ total time. The position map and Fenwick tree both contain
$O(n)$ entries, so the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Two Fenwick trees:** Precompute smaller values on the left and larger
  values on the right in separate passes. This has the same bounds but stores
  an additional count array; the one-pass identity derives the right count
  from totals instead.
- **Merge-sort counting:** Divide-and-conquer can count the required smaller
  and larger relationships in $O(n\log n)$ time, but coordinating both sides
  is less direct than rank queries.
- **Scan both sides for every middle:** Directly count qualifying left and
  right positions for each index. It is correct and easy to verify, but takes
  $O(n^2)$ time.
- Identical permutations make every choice of three values good, yielding
  $\binom{n}{3}$.
- Reversing one permutation relative to the other yields no increasing
  triplet.
- The answer can exceed 32-bit range when $n$ is large, so implementations
  must use an integer type capable of holding $\binom{10^5}{3}$.
