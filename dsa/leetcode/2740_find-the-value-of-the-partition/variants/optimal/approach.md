## General

**The partition value is a distance between two input values**

For any valid partition, let:

- $a=\max(\texttt{nums1})$;
- $b=\min(\texttt{nums2})$.

Both $a$ and $b$ are elements taken from the original array, and the partition value is $\lvert a-b\rvert$.

Therefore no partition can achieve a value smaller than the smallest absolute difference between any two array elements. The remaining question is whether that global closest-pair gap can always be realized by a partition. It can.

**Sorting reveals the closest pair**

After sorting:

$$
v_0\le v_1\le\cdots\le v_{n-1},
$$

the minimum absolute difference between any two values occurs between adjacent elements.

If a nonadjacent pair $v_i,v_j$ with $i<j$ is chosen, its gap is the sum of adjacent nonnegative gaps from $i$ to $j$. None of those component gaps can exceed the whole sum, so at least one adjacent pair is no farther apart.

The expression `min(b - a for a, b in pairwise(nums))` computes the smallest adjacent gap. Since the list is sorted, `b-a` is already nonnegative and no absolute-value call is needed.

**Why the adjacent gap is attainable as a partition value**

Let adjacent sorted values `a` and `b` achieve the minimum gap.

Place all values at or below `a` into `nums1` and all values at or above `b` into `nums2`. Because `a` and `b` are adjacent in sorted order, there is no value strictly between them that creates an assignment problem.

Then `max(nums1)=a` and `min(nums2)=b`, so the partition value is `b-a`. Both arrays are nonempty because they contain the selected occurrences.

If duplicate values make `a=b`, place one occurrence in each partition. Distribute lower values to the first side and higher values to the second. Both extrema equal the duplicated value, producing value zero.

Thus the smallest adjacent gap is not merely a lower bound; a legal partition achieves it.

**Why original positions do not matter**

The partition divides elements into two arrays but imposes no requirement to preserve a contiguous prefix, original order, or equal sizes. Sorting is only an analytical and computational tool for comparing values. Any original occurrences can be assigned to the constructed sides.

This distinguishes the problem from array-cut tasks where a split index must preserve positions.

**Trace nums equal to 1, 3, 2, 4**

Sorting produces `[1,2,3,4]`. Every adjacent gap is one, so the minimum is one.

Choosing `nums1=[1,2]` and `nums2=[3,4]` gives extrema two and three and value one.

No partition can produce zero because all values are distinct in this example.

**Trace nums equal to 100, 1, 10**

Sorted order is `[1,10,100]`. Adjacent gaps are nine and ninety, so the result is nine.

One realizing partition is `nums1=[10]` and `nums2=[1,100]`. Although the second partition contains a value larger than ten, its minimum is one, so the value is $\lvert10-1\rvert=9$.

This example shows that the realizing partition need not be “all smaller values versus all larger values” in the same orientation. The general construction can also swap the roles of the two selected extrema because of the absolute value. What matters is that some legal grouping makes them the relevant maximum and minimum.

**A subtle orientation point**

For adjacent $a\le b$, the straightforward threshold construction makes $a$ the maximum of the first group and $b$ the minimum of the second. The second example's displayed partition instead uses ten as the first maximum and one as the second minimum. Both achieve the same global closest-pair distance.

The algorithm returns only the value, so it need not reconstruct either partition.

**Input mutation**

`nums.sort()` reorders the supplied list in place. The contract asks only for the minimum value, so preserving original order is unnecessary for this implementation.


Every partition value is the absolute difference between two original elements, so it is at least the global closest-pair difference. Sorting makes that closest-pair difference equal to the minimum adjacent gap. A partition can place the lower adjacent value as one side's maximum and the upper as the other side's minimum, achieving exactly that gap. The returned minimum adjacent difference is therefore both a lower bound and attainable, hence optimal.

## Complexity detail

Let $n$ be the array length. In-place sorting costs $O(n\log n)$ time. `pairwise(nums)` lazily produces $n-1$ adjacent pairs, and `min` scans them in $O(n)$ time. Sorting dominates, so total time is $O(n\log n)$.

Python's Timsort may use $O(n)$ temporary memory in the worst case, matching the manifest's conservative $O(n)$ space. The pairwise iterator and generator use $O(1)$ explicit state.

The input list itself is mutated rather than copied.

## Alternatives and edge cases

- **Check every pair:** Finds the closest values in $O(n^2)$ time but ignores the adjacent-after-sorting property.
- **Balanced tree insertion:** Can track predecessor and successor gaps in $O(n\log n)$ time without a full final sort, but is more complex.
- **Counting array:** Useful only when the numeric range is small; values here reach $10^9$.
- **Two elements:** They must be separated, and their absolute difference is the only adjacent gap.
- **Duplicate values:** Adjacent gap zero is attainable by placing different occurrences on opposite sides.
- **Already sorted input:** Timsort may run faster, while the asymptotic bound remains $O(n\log n)$.
- **Original order:** Irrelevant to partition membership, but the exact source destroys it through in-place sorting.
- **Unequal partition sizes:** Fully allowed; only nonemptiness matters.
- **Positive values:** The proof would also work for negative values because it depends only on sorted differences.
- **No partition construction:** The function correctly returns only the optimal value requested.
