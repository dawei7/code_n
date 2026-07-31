## General

Suppose the element originally at index $i$ becomes a fixed point with final index $v=\texttt{nums[i]}$. Exactly

$$
d=i-v
$$

earlier elements must have been deleted. Therefore $v\le i$ is necessary; discard every element with $v>i$.

Now consider two chosen fixed points with original indices $i<j$, values $v$ and $w$, and deletion counts $d=i-v$ and $e=j-w$.

- Their final positions must preserve order, so $v<w$.
- Deletions before a later retained element include all deletions before an earlier one, so $d\le e$.

These conditions are also sufficient. Before the first chosen point, delete exactly its $d$ required elements. Between two consecutive chosen points, delete $e-d$ elements. Because

$$
e-d=(j-i)-(w-v)
$$

and $w-v\ge1$, there are enough unchosen positions between $i$ and $j$ to perform those deletions. Thus every chain whose values strictly increase and whose deletion counts do not decrease can be realized by one deletion plan.

Represent each eligible element by the point `(d, v)`. Sort the points first by `d` and then by `v`. In this order the deletion count is automatically nondecreasing. Points with equal `d` are deliberately ordered by increasing `v`, because equal deletion counts are compatible—for example, fixed points already present without deletion all have `d == 0`.

The remaining task is the longest strictly increasing subsequence of the `v` coordinates. Strictness prevents two retained elements from claiming the same final index. Maintain `tails[k]` as the smallest possible final value of a chain of length `k + 1`. For each value, `bisect_left` finds the first tail greater than or equal to it: replacing that tail preserves future options, while appending extends the longest chain.

Every realizable collection appears as a strictly increasing subsequence after sorting, and every subsequence constructed this way satisfies the sufficient chain conditions. The LIS length is therefore exactly the maximum achievable number of fixed points.

## Complexity detail

Let $n$ be the length of `nums`. Constructing the eligible points takes $O(n)$ time, sorting takes $O(n\log n)$ time, and the binary-search LIS pass takes $O(n\log n)$ time. The total is $O(n\log n)$ time. The point list and LIS tails use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Quadratic chain dynamic programming:** After sorting the points, compare every earlier point to compute the longest compatible chain. This is direct but takes $O(n^2)$ time.
- **Fenwick tree over final indices:** Sort by deletion count and query the best chain ending at a smaller value. This also achieves $O(n\log n)$ time but needs a tree or coordinate domain instead of the compact tails array.
- **Elements with `nums[i] > i`:** Deletions only move an element left, so such an element can never reach its larger requested index and must be excluded.
- **Equal deletion counts:** Equality is valid; several unchanged fixed points may all have deletion count zero. Sorting equal counts by increasing value preserves these chains.
- **Equal values:** Two elements cannot both occupy the same final index, so the LIS comparison must be strict and must use `bisect_left`, not `bisect_right`.
- **No eligible point:** If every value exceeds its original index, the point list and tails remain empty and the answer is `0`.
- **Deleting zero elements:** Already-fixed indices are represented by points `(0, i)` and can all participate in the same increasing chain.
